import streamlit as st
import time


def initialize():
    """
    This function initializes the Streamlit application and sets up the user interface.

    It includes the following components:
    - Title of the application
    - File uploader for image files (jpg, png)
    - Select box for character selection
    - Select box for emotion selection
    - Submit button to start processing
    - Audio player with stop button
    """

    # Set the title of the application
    st.title("Image Narration Application")

    # Create a file uploader for image files
    uploaded_file = st.file_uploader(
        "Choose an image...",
        type=["jpg", "png"],
        accept_multiple_files=False,
    )

    # If a file is uploaded, check its size and display it if it's within the limit
    if uploaded_file is not None:
        if uploaded_file.size <= 10 * 1024 * 1024:  # file size limit 10MB
            st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        else:
            st.error(
                "The file size should not exceed 10MB"
            )  # Display an error if the file is too large

    # Create a select box for character selection
    character_list = ["harrypotter", "captain jack sparrow", "james bond", "batman"]
    character = st.selectbox("Select a character", character_list)

    # Create a select box for emotion selection
    emotion_list = ["angry", "happy", "sad"]
    emotion = st.selectbox("Select an emotion", emotion_list)

    # Create a submit button to start processing
    if st.button("Submit"):
        st.write("Processing...")  # Display a processing message
        time.sleep(2)  # wait for 2 seconds
        st.audio("audio_file.mp3")  # play some audio

        # Create a stop button to stop the audio
        if st.button("Stop Audio"):
            st.stop()  # stop the audio
