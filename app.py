import streamlit as st
import cv2
import numpy as np
from emotion_detector import EmotionDetector
from voice_analyzer import VoiceAnalyzer
import tempfile
import os

def main():
    st.title("AI-Based Interview Emotion & Confidence Analyzer")

    st.sidebar.header("Instructions")
    st.sidebar.write("1. Upload a video file for emotion analysis.")
    st.sidebar.write("2. Upload an audio file for voice confidence analysis.")
    st.sidebar.write("3. Click 'Analyze' to get results.")

    emotion_detector = EmotionDetector()
    voice_analyzer = VoiceAnalyzer()

    video_file = st.file_uploader("Upload Video File", type=["mp4", "avi", "mov"])
    audio_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "flac"])

    if st.button("Analyze"):
        emotion_score = 0
        voice_score = 0
        voice_tips = []

        if video_file is not None:
            # Save video to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_video:
                tmp_video.write(video_file.read())
                tmp_video_path = tmp_video.name

            cap = cv2.VideoCapture(tmp_video_path)
            frames = []
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                frames.append(frame)
                if len(frames) > 30:  # Limit to 30 frames for speed
                    break
            cap.release()
            os.unlink(tmp_video_path)

            emotion_score = emotion_detector.get_emotion_score(frames)

        if audio_file is not None:
            # Save audio to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_audio:
                tmp_audio.write(audio_file.read())
                tmp_audio_path = tmp_audio.name

            transcript = voice_analyzer.transcribe_audio(tmp_audio_path)
            voice_score, voice_tips = voice_analyzer.analyze_confidence(transcript)
            os.unlink(tmp_audio_path)

        overall_score = (emotion_score + voice_score) / 2 * 100

        st.header("Results")
        st.write(f"Emotion Score: {emotion_score:.2f}")
        st.write(f"Voice Confidence Score: {voice_score:.2f}")
        st.write(f"Overall Performance Score: {overall_score:.2f}/100")

        st.header("Improvement Tips")
        tips = voice_tips
        if emotion_score < 0.5:
            tips.append("Smile more and show enthusiasm.")
        for tip in tips:
            st.write(f"- {tip}")

if __name__ == "__main__":
    main()
