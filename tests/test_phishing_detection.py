import unittest
from src.feature_extraction import extract_features
from src.model_training import train_model
from src.phishing_detection import detect_phishing

class TestPhishingDetection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.texts = [
            'This is a legitimate email.',
            'Free money!!! Click here to claim your prize.',
            'Your account has been compromised. Update your password.',
            'Meeting schedule for next week.',
            'Congratulations! You won a lottery. Click to claim.'
        ]
        cls.labels = [0, 1, 1, 0, 1]
        cls.X_train_tfidf, cls.X_test_tfidf, cls.vectorizer = extract_features(cls.texts, cls.texts)
        cls.model = train_model(cls.X_train_tfidf, cls.labels)

    def test_detect_phishing(self):
        test_emails = [
            "Free money!!! Click here to claim your prize.",
            "Please update your bank information.",
            "This is a legitimate email for meeting schedule."
        ]
        results = [detect_phishing(email, self.vectorizer, self.model) for email in test_emails]
        expected_results = ['Phishing', 'Phishing', 'Legitimate']
        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()
