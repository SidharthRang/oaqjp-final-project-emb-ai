from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        tests = [
            {"statement":"I am glad this happened","emotion": "joy"},
            {"statement":"I am really mad about this","emotion": "anger"},
            {"statement":"I feel disgusted just hearing about this","emotion": "disgust"},
            {"statement":"I am so sad about this","emotion": "sadness"},
            {"statement":"I am really afraid that this will happen","emotion": "fear"}
        ]
        for test in tests:
            result = emotion_detector(test["statement"])
            dominant_emotion = result['dominant_emotion']
            self.assertEqual(dominant_emotion, test["emotion"])
    
unittest.main()
