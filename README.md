# AI-Based Interview Emotion & Confidence Analyzer

An intelligent web application that analyzes candidate soft skills during interviews by detecting facial emotions and voice confidence, providing objective performance scores and improvement tips.

## Features

- **Facial Emotion Detection**: Uses OpenCV to detect faces and analyze emotional expressions
- **Voice Confidence Analysis**: Transcribes audio and analyzes sentiment, fluency, and filler words
- **Performance Scoring**: Generates overall scores based on emotion and voice metrics
- **Improvement Tips**: Provides personalized suggestions for better interview performance
- **Modern UI**: Beautiful gradient interface with Streamlit

## Tech Stack

- **Frontend**: Streamlit
- **Computer Vision**: OpenCV
- **Speech Recognition**: SpeechRecognition
- **NLP**: TextBlob, NLTK
- **Programming Language**: Python

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/divya-chowdary42/AI-Based-Interview-Emotion-Confidence-Analyzer.git
   cd AI-Based-Interview-Emotion-Confidence-Analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open your browser to `http://localhost:8501`

## Usage

1. Upload a video file (MP4, AVI, MOV) for emotion analysis
2. Upload an audio file (WAV, MP3, FLAC) for voice confidence analysis
3. Click "Analyze" to get results
4. View your emotion score, voice confidence score, overall performance, and improvement tips

## Requirements

- Python 3.7+
- Webcam access (for live analysis, if implemented)
- Microphone access (for live analysis, if implemented)

## Contributing

Feel free to fork this repository and submit pull requests with improvements!

## License

This project is open-source and available under the MIT License.
