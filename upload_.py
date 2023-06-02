import streamlit as st
import cv2 as cv
from pathlib import Path 
import streamlit as st

def upload(cname,k):
    st.title(f'Class {cname}')
    path=Path(f'Images/upload/{cname}')
    path.mkdir(exist_ok=True)
    uploaded_files=st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"],accept_multiple_files=True,key=str(k)+cname)
    if uploaded_files:
        for file in uploaded_files:
            img_=file.getvalue()
            with open(f'{path}/{file.name}','wb') as f:
                f.write(img_)

# About Teachable Machine
def display_info(n_classes):
            if n_classes<=1:
                st.text("""
            With Teachable Machine, you can train a model to recognize and classify different 
            inputs, such as images. The tool uses a technique called transfer learning, where a 
            pre-trained model is adapted to recognize new classes of data.
            
            Here's a general overview of how Teachable Machine works:

                1. Collection: You collect and label examples of different classes of data. 
                For example, if you're training an image classifier, you would provide images for 
                each category you want to recognize.

                2. Training: Teachable Machine uses your labeled examples to train a machine 
                learning model. It leverages a pre-existing neural network and fine-tunes it 
                using your data. The training is done in your web browser and doesn't require 
                any server-side processing.

                3. Testing: Once the model is trained, you can test it using new examples to see 
                how well it performs. Teachable Machine provides a live preview that shows the 
                model's predictions in real-time.

                4. Exporting: You can export the trained model in different formats, to use your 
                model.

            Teachable Machine can be used for various applications, such as creating custom 
            image classifiers, gesture recognition systems, or sound classifiers. It's a 
            beginner-friendly tool that provides a hands-on introduction to machine learning 
            concepts.
                """)