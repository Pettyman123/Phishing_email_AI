import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_preprocessing import preprocess_text, load_data
from src.feature_extraction import extract_features
from src.model_training import train_model, evaluate_model
from src.phishing_detection import detect_phishing

# Load and inspect data
data_filepath = 'data/emails.csv'
df = load_data(data_filepath)

# Print columns to check
print("Columns in the dataset:", df.columns)

# Check and rename columns if necessary
if 'text' not in df.columns or 'label' not in df.columns:
    raise ValueError("Dataset columns 'text' and 'label' not found or named differently.")

# Preprocess the text
df['text'] = preprocess_text(df['text'])

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Extract features
X_train_tfidf, X_test_tfidf, vectorizer = extract_features(X_train, X_test)

# Train model
model = train_model(X_train_tfidf, y_train)

# Evaluate model
evaluate_model(model, X_test_tfidf, y_test)

# Example phishing detection on new email
new_email = "Subject: Congratulations! You've won a prize. Click here to claim."
result = detect_phishing(new_email, vectorizer, model)
print(f"The email is classified as: {result}")

