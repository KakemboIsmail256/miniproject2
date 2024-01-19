import unittest
from your_library import detect_danger_in_voice

class TestVoiceAnalysis(unittest.TestCase):
    def test_danger_detection_when_danger_detected(self):
        # Test case for detecting danger in the person's voice when danger is detected
        audio_file = "path_to_audio_file_with_danger.wav"
        result = detect_danger_in_voice(audio_file)
        self.assertEqual(result, "Danger detected in the person's voice")

    def test_danger_detection_when_no_danger_detected(self):
        # Test case for detecting danger in the person's voice when no danger is detected
        audio_file = "path_to_audio_file_without_danger.wav"
        result = detect_danger_in_voice(audio_file)
        self.assertEqual(result, "No danger detected in the person's voice")

if __name__ == '__main__':
    unittest.main()
