import streamlit as st
import pyaudio
import speech_recognition as sr

def transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

def main():
    st.title("Speech to Text Transcription")
    with st.beta_container():
        st.write("Click the button below and start speaking!")
        button_pressed = st.button("Start Recording")
        if button_pressed:
            st.write("Recording...")
            text = transcribe_audio()
            st.write(f"You said: {text}")

if __name__ == "__main__":
    main()
