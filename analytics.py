from turtle import color
from click import option
from matplotlib import pyplot
import streamlit as st
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from  matplotlib.ticker import FuncFormatter
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
pd.options.plotting.backend = "plotly"


#label_attr_dict_obs = {'HOLSTEIN':'HOLSTEIN','BRUNE SUISSE':'BRUNE SUISSE','BRUNE AL':'BRUNE AL','CROISEE':'CROISEE','FLECKVIEH':'FLECKVIEH'}



#importer la base données sur laquelle on va effectuer les analyses
def imprt_data():
    st.caption('importation des données:')
    #sheet_inp = st.text_input('Donner le nom de la feuille ')
    datafile = st.file_uploader("Upload file", type='xlsx')
    if datafile is not None:
        df = pd.read_excel(datafile)
        #data_frame_excel = pd.read_excel(df,index_col=None,na_values=['NA'])
        #dataframe = df.astype(str)
        #st.write(dataframe)
        analys_data(df)



#fonction pour faire les analyses
#@st.cache(suppress_st_warning=True)
def analys_data(df):
    zone = df['ZONE']
    up = df['Nom UP']
    race = df['RACE']
    obs = df['OBSERVATION']

    #get list of unque Observations
    ListObs = obs.unique().tolist()
    #get list of unique zones
    ListZone = zone.unique().tolist()
    ListZone_na = zone.dropna().unique().tolist()

    #group and count observations par zone 
    obs_zone = df.groupby(['OBSERVATION','ZONE'])['ZONE'].count()
    #get list of unique races
    ListRace = race.unique().tolist()
    #group and count race par zone 
    race_zone = df.groupby(['RACE','ZONE'])['RACE'].count().unstack(fill_value=0).stack()
    rz_tidy = df.groupby(['RACE','ZONE']).count().reset_index()
    #zone_race = df.groupby(['RACE','ZONE'])['RACE'].count()
    #print(race_zone)

    count_obs = df['OBSERVATION'].value_counts()

    count_race = race.value_counts()

    st.write('you can now start analyzing your data!')

    #Display data differently : only head, tail or display whole thing
    st.write('Apercu des données : ')
    display_header = st.checkbox('Afficher l en-tête')
    if display_header:
        st.dataframe(df.head())

    display_tail = st.checkbox('Afficher le pied de page')
    if display_tail:
        st.dataframe(df.tail())

    display_all = st.checkbox('Afficher toutes les données')
    if display_all:
        st.dataframe(df)

    #---- funnel plot -----#
    col1 , col2 = st.columns(2)
    if "fun" not in st.session_state:
        st.session_state.vis_obs='OK'
    choose_inp = st.multiselect('selectionnez les observations à visualiser',options=ListObs,default=["OK","DECES"],key="fun")
    fig2 = px.funnel(df , x=count_obs[choose_inp],y=choose_inp)
    st.plotly_chart(fig2)
    #---- pie chart -----#
    fig3 = px.pie(df, values=count_obs, names=ListObs, color_discrete_sequence=px.colors.sequential.RdBu, width=700, height=900)
    fig3.update_traces(textposition='inside')
    fig3.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    st.plotly_chart(fig3)

    #graphs related to visualization of data obs/zone
    

    #def callback():
        #st.session_state.butt_click = True    

    viz_obs = st.checkbox('Visualization: OBSERVATION/ZONE',key="butt_click")

    if (viz_obs):
        select_obs = st.selectbox('Quel Observation voulez-vouz visualiser?',ListObs,key='vis_obs')
        fig4 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
        fig4.add_trace(go.Pie(labels=ListZone, values=obs_zone[select_obs], name="distribution observations"),1, 1)
        fig4.update_traces(hole=.4, hoverinfo="label+percent+name")
        fig4.update_layout(title_text="Observation/zone",annotations=[dict(text=select_obs, align= 'center', font_size=10, showarrow=False)])
        st.plotly_chart(fig4)

        
    #----- graphs related to visualization of data race/zone 
    viz_race = st.checkbox('Visualization: RACE/ZONE')
    if viz_race:
        #----- donut pie -------#
        select_race = st.selectbox('Quel RACE voulez-vouz visualiser?',ListRace)
        fig5 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
        fig5.add_trace(go.Pie(labels=ListZone, values=race_zone[select_race], name="distribution observations"),1, 1)
        fig5.update_traces(hole=.4, hoverinfo="label+percent+name",textposition='inside')
        fig5.update_layout(title_text="race/zone",uniformtext_minsize=12, uniformtext_mode='hide',annotations=[dict(text=select_race, align= 'center', font_size=10, showarrow=False)])
        st.plotly_chart(fig5)

        #---------- scatter data ---------#
        col1,col2 = st.columns(2)
        #with col1:
           #r =st.selectbox('RACE',ListRace)
        fig8 = px.scatter(race_zone ,x=ListZone_na ,y=race_zone[select_race],title=select_race)
        st.plotly_chart(fig8)
    

    #--------  Empirical Cumulative Distribution ---------#
    #fig6 = px.ecdf(df, x='ZONE')
    #fig7 =px.ecdf(df, x='RACE')
    #st.plotly_chart(fig7)

    #sample = np.hstack((race_zone,ListRace))
    fig, ax = plt.subplots()
    ax.hist(race_zone, bins=50)
    #st.pyplot(fig)
  
    





    

