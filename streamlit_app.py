import streamlit as st
import speech_recognition as sr

# create a speech recognizer object
r = sr.Recognizer()

# define a function to transcribe audio
def transcribe_audio(audio_file):
    # read the audio data
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    # transcribe the audio using Google Speech Recognition
    try:
        transcript = r.recognize_google(audio)
    except sr.UnknownValueError:
        transcript = "Could not understand audio"
    except sr.RequestError as e:
        transcript = f"Could not request results from Google Speech Recognition service; {e}"

    return transcript

# create a Streamlit app
def app():
    # add a button to record audio
    if st.button("Record Audio"):
        # record audio using Streamlit's builtin recorder
        with st.audio("audio.wav", format="wav"):
            audio_file = st.recorder()
        # transcribe the audio and display the transcript
        transcript = transcribe_audio(audio_file)
        st.write("Transcript:")
        st.write(transcript)

# run the app
if __name__ == "__main__":
    app()
