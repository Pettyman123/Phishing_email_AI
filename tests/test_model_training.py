import unittest
import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_preprocessing import preprocess_text
from src.feature_extraction import extract_features
from src.model_training import train_model, evaluate_model

class TestModelTraining(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.DataFrame({
            'text': [
                'This is a legitimate email.',
                'Free money!!! Click here to claim your prize.',
                'Your account has been compromised. Update your password.',
                'Meeting schedule for next week.',
                'Congratulations! You won a lottery. Click to claim.'
            ],
            'label': [0, 1, 1, 0, 1]
        })
        cls.df['text'] = preprocess_text(cls.df['text'])
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(cls.df['text'], cls.df['label'], test_size=0.2, random_state=42)
        cls.X_train_tfidf, cls.X_test_tfidf, cls.vectorizer = extract_features(cls.X_train, cls.X_test)
        cls.model = train_model(cls.X_train_tfidf, cls.y_train)

    def test_train_model(self):
        self.assertIsNotNone(self.model)

    def test_evaluate_model(self):
        try:
            evaluate_model(self.model, self.X_test_tfidf, self.y_test)
        except Exception as e:
            self.fail(f"evaluate_model() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()

