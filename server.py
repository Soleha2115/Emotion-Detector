"""Flask web server for the Emotion Detector application."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector")
def sent_detector():
    """Analyze query text and return its emotion scores as a readable string."""
    text_to_analyse = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyse)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again.", 400

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the main emotion analysis page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
