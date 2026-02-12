import speech_recognition as sr
from textblob import TextBlob
import re

class VoiceAnalyzer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self, audio_file):
        try:
            with sr.AudioFile(audio_file) as source:
                audio = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio)
            return text
        except Exception as e:
            return f"Error transcribing audio: {str(e)}"

    def analyze_confidence(self, text):
        if not text or "Error" in text:
            return 0, ["Unable to analyze voice. Please ensure clear audio."]

        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity  # -1 to 1

        # Count positive words, fluency (sentence length)
        positive_words = ['confident', 'sure', 'excellent', 'great', 'good', 'yes', 'absolutely', 'amazing', 'fantastic', 'brilliant']
        word_count = len(re.findall(r'\b\w+\b', text))
        positive_count = sum(1 for word in positive_words if word in text.lower())

        # Analyze fluency: check for filler words
        filler_words = ['um', 'uh', 'like', 'you know', 'so', 'well']
        filler_count = sum(1 for word in filler_words if word in text.lower())

        # Simple confidence score: sentiment + positive words + fluency - fillers
        fluency_score = min(word_count / 50, 1)  # Normalize to 0-1
        filler_penalty = min(filler_count / 10, 0.5)  # Penalty for fillers
        confidence_score = (sentiment + 1) / 2 + positive_count / len(positive_words) + fluency_score - filler_penalty
        confidence_score = max(min(confidence_score / 3, 1), 0)  # Average, cap between 0-1

        tips = []
        if sentiment < 0:
            tips.append("Try to maintain a positive and enthusiastic tone.")
        if positive_count < 2:
            tips.append("Incorporate more positive affirmations like 'I'm confident' or 'That's great'.")
        if fluency_score < 0.5:
            tips.append("Practice speaking more fluently by preparing key points in advance.")
        if filler_count > 5:
            tips.append("Reduce filler words like 'um', 'uh', or 'like' to sound more polished.")
        if word_count < 20:
            tips.append("Provide more detailed responses to showcase your knowledge.")

        return confidence_score, tips
