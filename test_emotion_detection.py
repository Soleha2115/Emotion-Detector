"""Unit tests for the emotion_detection module."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test that each supported emotion can be detected."""

    def test_joy(self):
        """Detect joy as the dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Detect anger as the dominant emotion."""
        result = emotion_detector("I am really mad at you")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Detect disgust as the dominant emotion."""
        result = emotion_detector("I feel disgusted just thinking about it")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Detect sadness as the dominant emotion."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Detect fear as the dominant emotion."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
