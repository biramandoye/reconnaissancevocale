import streamlit as st
#import cv2
import numpy as np
from gtts import gTTS
#from pygame import mixer
import speech_recognition as sr


# Fonction de détection des visages
#def detect_faces(image, scaleFactor, minNeighbors):
    # ... (code précédent)

# Fonction de transcription de la parole
def transcribe_speech(audio_file, recognition_language="en-US"):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        transcribed_text = recognizer.recognize_google(audio_data, language=recognition_language)
        return transcribed_text
    except sr.UnknownValueError:
        return "Erreur : Impossible de transcrire la parole. Aucun discours détecté."
    except sr.RequestError as e:
        return f"Erreur lors de la requête à l'API de reconnaissance vocale : {e}"

# Fonction principale
def main():
    st.title("Application de transcription de la parole")

    # ... (code précédent)

    # Ajouter une nouvelle option pour choisir l'API de reconnaissance vocale
    speech_api = st.selectbox("Choisissez l'API de reconnaissance vocale", ["Google", "Microsoft", "IBM", "Wit.ai"])

    # Ajouter une fonctionnalité pour choisir la langue de reconnaissance vocale
    recognition_language = st.selectbox("Choisissez la langue de reconnaissance vocale", ["en-US", "fr-FR", "es-ES"])

    # Ajouter une fonctionnalité pour suspendre et reprendre la reconnaissance vocale
    is_recognition_paused = st.checkbox("Suspendre la reconnaissance vocale")

    # ... (code précédent)

    # Ajouter une fonctionnalité pour transcrire la parole
    if st.button("Transcrire la parole"):
        # ... (code précédent)

        with st.spinner("Enregistrement de la parole..."):
            transcribed_text = transcribe_speech("audio.wav", recognition_language)

        st.success("Transcription réussie!")
        st.write(f"Texte transcrit : {transcribed_text}")

        # Ajouter une fonctionnalité pour enregistrer le texte transcrit dans un fichier
        save_text_button = st.button("Enregistrer le texte transcrit")
        if save_text_button:
            with open("transcribed_text.txt", "w") as file:
                file.write(transcribed_text)
            st.success("Texte transcrit enregistré avec succès!")

    # ... (code précédent)

# Appeler la fonction principale
if __name__ == "__main__":
    main()
