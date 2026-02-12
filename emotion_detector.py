import cv2
import numpy as np

class EmotionDetector:
    def __init__(self):
        # Load Haar cascade for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detect_emotion(self, frame):
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces) > 0:
            # Simple heuristic: if faces are detected, assume positive emotion score
            # In a real implementation, use a trained model
            positive_score = 0.5 + np.random.uniform(0, 0.5)  # Random score between 0.5 and 1.0
            return positive_score, {'detected_faces': len(faces)}
        return 0, {}

    def get_emotion_score(self, frames):
        scores = []
        for frame in frames:
            score, _ = self.detect_emotion(frame)
            scores.append(score)
        return np.mean(scores) if scores else 0
