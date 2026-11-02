"""Detect emotions with the IBM Watson NLP Emotion Predict API."""

import requests


EMOTION_KEYS = ("anger", "disgust", "fear", "joy", "sadness")
API_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"


def _empty_result():
    """Return the standard result for invalid input or an unavailable API."""
    return {**dict.fromkeys(EMOTION_KEYS), "dominant_emotion": None}


def emotion_detector(text_to_analyse):
    """Return emotion scores and the dominant emotion for the supplied text."""
    if not isinstance(text_to_analyse, str) or not text_to_analyse.strip():
        return _empty_result()

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    payload = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(
            API_URL, json=payload, headers=headers, timeout=30
        )
        if response.status_code == 400:
            return _empty_result()
        response.raise_for_status()
        emotions = response.json()["emotionPredictions"][0]["emotion"]
        scores = {key: emotions[key] for key in EMOTION_KEYS}
    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
        return _empty_result()

    scores["dominant_emotion"] = max(EMOTION_KEYS, key=scores.get)
    return scores
