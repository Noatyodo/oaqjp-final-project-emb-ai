from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        # Test case for joy result
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant emotion'], 'joy')
        # Test case for anger result
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant emotion'], 'anger')
        # Test case for disgust result
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant emotion'], 'disgust')
        # Test case for sadness result
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant emotion'], 'sadness')
        #test case for fear result
        result_5 = emotion_detector('I am really afraid that this will happen 	')
        self.assertEqual(result_5['dominant emotion'], 'fear')   

unittest.main() 
