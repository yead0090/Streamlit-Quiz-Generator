import streamlit as st 
from api_calling import note_generator,audio_transcription,quiz_generator
from PIL import Image
import re

st.title("Note Summary and Quiz generator")
st.markdown("Upload up to 3 images to generate Note summary and quizzes")
st.divider()

with st.sidebar:
    st.header("controls")

    #image
    images=st.file_uploader(
        "upload the photos of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )


    pil_images=[]
    for img in images:
       pil_image=Image.open(img)
       pil_images.append(pil_image)

    if images:
        if len(images)>3:
            st.error("upload at max 3 images")
        else:
         st.subheader("uploaded images")
         col=st.columns(len(images))
         
         
         for i,img in enumerate(images):
            with col[i]:
               st.image(img)

    #difficulty
    selected_option=st.selectbox(
       "Enter the difficulty of your quiz",
       ["Easy","Medium","Hard"],
       index=None
    )

    

    pressed=st.button("click the button to initiate AI",type="primary")

if pressed:
   if not images:
     st.error("You must upload images")
   if not selected_option:
      st.error("You must select a difficulty")

   if images and selected_option:
        #note
        with st.container(border=True):
            st.subheader("Your note") 
            #this portion will be replaced by api call
            with st.spinner("AI is writing for you"):
              generated_notes=note_generator(pil_images)
              st.markdown(generated_notes)


        #audio
        with st.container(border=True):
            st.subheader("Audio Transcription") 
            #this portion will be replaced by api call
            with st.spinner("AI is generating audio transcript for you"):
             #cleaning text
             clean_text=re.sub(r'[#,*,-,`]',' ',generated_notes)
             audio_transcript=audio_transcription(clean_text)
             st.audio(audio_transcript)

        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz({selected_option}) Difficulty") 
            #this portion will be replaced by api call
            with st.spinner("Ai is generating the quizzes"):
                quizzes=quiz_generator(pil_images,selected_option)
                st.markdown(quizzes)
            


      
   
   


  
   
   
