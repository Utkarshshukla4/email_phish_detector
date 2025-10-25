## Contact

Utkarsh Shukla

Email- utqrshkumar07@gmail.com

 GitHub- https://github.com/Utkarshshukla4



##  Overview
This project detects phishing emails using a trained machine learning model that analyzes subject lines, URLs, and header patterns.  
It’s lightweight, easy to run, and ideal for securing personal or enterprise email systems.


##  Features
- Email text and header feature extraction  
- Machine learning classification (phish / not phish)  
- Confidence scoring for each result  
- Works on Windows and Linux  
- Easy-to-use CLI interface  



##  Architecture

[Email Input (.eml)] 
      ↓
[Text + Header Extractor]
      ↓
[Feature Engineering]
      ↓
[ML Model (Random Forest / SVM)]



## Project Structure
email-phish-detector/
├── src/
├── sample_data/
├── models/
├── docs/
│   └── architecture.png
├── requirements.txt
├── README.md
└── .gitignore

   
## Steps
Clone this repository.

Create a virtual environment.

Install dependencies.


## For First Installation
git clone https://github.com/Utkarshshukla4/email-phish-detector.git

cd email-phish-detector

## Create Environment 
Windows:

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt


Linux / macOS:

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


## Running the Project
Windows:-
python src/train.py

Linux / macOS:-
python3 src/train.py


## Input Example

Paste an email message or subject line in the input box.

## Output Example
Prediction: Phishing Email  
Confidence: 95%

## Note
Replace data/sample_emails.csv with a larger labeled dataset for production use.

## Summary

This project helps identify phishing attempts by examining textual features and suspicious words in email bodies.
