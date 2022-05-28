import streamlit as st
import db_tryout

html_temp = """
    <h2 style="color:#4E944F;font-family:American Typewriter;text-align:left;font-size:30px;text-shadow: -1px 0 #F4FCD9">Office Régional de la mise en valeur agricole </h2>
    """  

st.set_page_config(page_title='ORMVA-SM G-PV')

col1, col2= st.columns([1,5])
with col2:
    st.write("")
    st.write("")
    st.markdown(html_temp.format('white','white'),unsafe_allow_html=True)
with col1:
    st.image('logo_ormva2.png', width=100)





db_tryout.change_choice()



