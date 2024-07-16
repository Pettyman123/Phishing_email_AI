
def detect_phishing(email_text, vectorizer, model):
	email_tfdif = vectorizer.transform([email_text])
	prediction = model.predict(email_tfdif)
	return 'Phishing' if prediction ==1 else 'Legitimate'

