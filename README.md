# Final Project

Emotion Detector uses the IBM Watson NLP Emotion Predict API to identify anger, disgust, fear, joy, and sadness in a text statement.

## Run locally

Install dependencies with `pip install -r requirements.txt`, then start the app with `python server.py`. Open `http://localhost:5000` in a browser.

The API endpoint is `/emotionDetector?textToAnalyze=...`. Blank input or an unavailable Watson response returns an invalid-text message.

Run the test suite with `python -m unittest`.