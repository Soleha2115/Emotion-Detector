"""Unit tests for the emotion_detection module."""

import unittest
from unittest.mock import Mock, patch

import requests

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test Watson response parsing and error handling."""

    def setUp(self):
        self.emotions = {
            "anger": 0.1,
            "disgust": 0.05,
            "fear": 0.04,
            "joy": 0.75,
            "sadness": 0.06,
        }
        self.response = Mock()
        self.response.status_code = 200
        self.response.json.return_value = {
            "emotionPredictions": [{"emotion": self.emotions}]
        }

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_returns_emotion_scores_and_dominant_emotion(self, post):
        """Return the scores and expected highest-scoring emotion."""
        post.return_value = self.response

        result = emotion_detector("I am glad this happened")

        self.assertEqual(result["dominant_emotion"], "joy")
        self.assertEqual(
            {key: result[key] for key in self.emotions}, self.emotions
        )
        post.assert_called_once()

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_text_does_not_call_api(self, post):
        """Reject blank text without making a network request."""
        result = emotion_detector("  \n")

        self.assertIsNone(result["dominant_emotion"])
        post.assert_not_called()

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request_returns_empty_result(self, post):
        """Return the empty result when the API rejects the request."""
        self.response.status_code = 400
        post.return_value = self.response

        result = emotion_detector("unrecognized input")

        self.assertIsNone(result["dominant_emotion"])

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_network_error_returns_empty_result(self, post):
        """Return the empty result when the API is unreachable."""
        post.side_effect = requests.RequestException("service unavailable")

        result = emotion_detector("I am worried")

        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
