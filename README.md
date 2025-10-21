# Phishing Email Detection Tool

Simple project demonstrating heuristic + ML based phishing email detection.

## Setup
1. Create virtualenv and install requirements.
2. Train the model: `python src/train.py`
3. Classify an email:
   `python src/classify_email.py --subject "..." --body "..." --from_email "..."`

## Notes
Replace `data/sample_emails.csv` with a larger labeled dataset for production use.
