import streamlit as st
import numpy as np

from tensorflow.keras.models import load_model
from PIL import Image

#Load the pre-trained model
classifier_model = load_model('/app/fitness_project/model')

#Define the categories to match the output of the pre-trained model
classifier_dictionary = {
    0:'Glasses',
    1:'Jeans',
    2:'Shoes'
}

#Function to pre-process the input image to match the expected input of the pre-trained model, then predict the class
def prediction(img):
    """
    Preprocess the single image to match the dimensions of the expected input, and the predicts the class label
    Args:
        img: Uploaded single image
    """
    img = Image.open(img)
    img = img.resize((90, 120))
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    indx = classifier_model.predict(img, verbose=0).argmax()

    return classifier_dictionary[indx]

# Set page title
st.set_page_config(page_title="Image Classifier")

# Add title to app
st.title("Image Classifier App!")

# Define function to upload image
def upload_image():
    """
    Sets a button to upload the image then apply the prediction function to it
    """
    #Button
    uploaded_file = st.file_uploader("Choose an image file of Glasses, Jeans or Shoes", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        #Preprocess, Predict
        classifier_label = prediction(uploaded_file)
        st.markdown(f"<h3 style='text-align: center;'>{classifier_label}!</h3>", unsafe_allow_html=True)
        #Display the uploaded image
        st.image(uploaded_file, caption=f"{classifier_label}", use_column_width=True)
    else:
        st.warning("Please upload an image file of Glasses, Jeans or Shoes.")

# Display upload widget
upload_image()
