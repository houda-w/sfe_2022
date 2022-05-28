import io
import os

import streamlit as st

from pathlib import Path
from zipfile import ZipFile


def get_all_file_paths(directory_path):
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory_path):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

#@st.cache(suppress_st_warning=True)
def zip_folder():
    #x = st.slider("Slider for interactivity", 0, 100, 55)
    #st.write(x)

    zip_buffer = io.BytesIO()

    generate_zip_file_clicked = st.button("Generate ZIP file")

    if generate_zip_file_clicked:
        # path to folder which needs to be zipped
        directory_path = Path("OUTPUT")

        # calling function to get all file paths in the directory
        file_paths = get_all_file_paths(directory_path)

        # printing the list of all files to be zipped
        #print('Les fichiers qui seront zipper:')
        #for file_name in file_paths:
         #   st.write(file_name)

        # writing files to a zipfile
        with ZipFile(zip_buffer, 'w') as zip_file:
            # writing each file one by one
            for file in file_paths:
                zip_file.write(file)
        st.download_button("Download ZIP file!", zip_buffer, "TOT_PV.zip")
        #print('All files zipped successfully!')

        

