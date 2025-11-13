# SmartSpam: ML-Powered Email Spam Detector
# Author: UMARxAI (https://github.com/UMARxAI)
# Adapted from: shukur-alom/Spam_mail_detector_using_ML
# Purpose: Portfolio project for ML-based spam detection | November 2025
import pickle

# Load the trained vectorizer for email preprocessing
count_vectorizer = pickle.load(open('count_vector_email.pickle', 'rb'))

# Load the trained spam email detection model
spam_mail = pickle.load(open('spam_email_detector.pickle', 'rb'))

# Get user input and transform it for the model
tra = count_vectorizer.transform([input("Enter email content: ")])

# Predict if the email is spam (0) or not spam (1)
ans = spam_mail.predict(tra)

if ans == 0:
    print("It's spam Mail. Be careful.")
else:
    print("It's not spam Mail :) ")


