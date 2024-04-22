import os
import streamlit as st
from lyzr import QABot
import shutil
from PIL import Image


st.set_page_config(
    page_title="Lyzr Planning Genius",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png",
)

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Lyzr Planning Genius📖")
st.markdown("### Welcome to the Lyzr Planning Genius!")

def remove_existing_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)


data_directory = "data"
os.makedirs(data_directory, exist_ok=True)
remove_existing_files(data_directory)

uploaded_file = st.sidebar.file_uploader("Choose PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded PDF file to the data directory
    file_path = os.path.join(data_directory, uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.getvalue())
    # Display the path of the stored file
    st.success(f"File successfully saved")


def get_all_files(directory):
    # List to store all file paths
    file_paths = []

    # Walk through the directory tree
    for root, dirs, files in os.walk(data_directory):
        for file in files:
            # Join the root path with the file name to get the absolute path
            file_path = os.path.join(root, file)
            # Append the file path to the list
            file_paths.append(file_path)

    return file_paths


def book_qabot(filepath):
    with st.spinner("Generating Embeddings...."):
        qa_bot = QABot.pdf_qa(
            input_files=[file_path],
        )
    return qa_bot


paths = get_all_files(data_directory)
question = st.text_input("What are you planning?")
if st.button("Plan"):
    for path in paths:
        qa = book_qabot(path)
        with st.spinner("Retrieving Answer...."):
            response = qa.query(question)
        st.markdown(response.response)