# Email Phishing Detector

## About the Project

Email Phishing Detector is a Python-based cybersecurity project that uses machine learning to identify potentially malicious phishing emails.

The system analyzes email content, subject lines, sender information, URLs, and other header patterns to classify an email as **Phishing** or **Not Phishing**. It also provides a confidence score for each prediction.

---

## Main Features

* Email text and header analysis
* Subject and URL feature extraction
* Machine learning-based classification
* Phishing and legitimate email detection
* Confidence score for predictions
* NLP-based text analysis
* Command-line interface
* Supports Windows and Linux

---

## Technologies Used

* **Python** – Core development
* **Machine Learning** – Email classification
* **NLP** – Text analysis
* **Random Forest / SVM** – Classification
* **Email Parsing** – Header and content extraction
* **Pandas** – Dataset processing

---

## Project Structure

```text
email-phish-detector/
│
├── src/
│   └── train.py
│
├── sample_data/
│   └── sample_emails.csv
│
├── models/
│
├── docs/
│   └── architecture.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

```text
Email Input (.eml)
        ↓
Text & Header Extraction
        ↓
Feature Engineering
        ↓
Machine Learning Model
        ↓
Phishing / Not Phishing
        ↓
Confidence Score
```

The system extracts useful information from the email and processes it into features that can be analyzed by the trained machine learning model.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Utkarshshukla4/email_phish_detector.git
cd email_phish_detector
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Windows:

```bash
pip install -r requirements.txt
```

Linux/macOS:

```bash
python3 -m pip install -r requirements.txt
```

---

## Running the Project

### Windows

```bash
python src/train.py
```

### Linux/macOS

```bash
python3 src/train.py
```

The script trains the machine learning model using the available dataset and performs email phishing detection.

---

## Input Example

Provide an email message or subject line as input to the application.

Example:

```text
Subject: Urgent: Verify Your Account

Your account has been temporarily restricted.
Click the following link to verify your account.
```

---

## Output Example

```text
Prediction: Phishing Email
Confidence: 95%
```

---

## Security Application

The project helps identify common phishing indicators such as suspicious wording, malicious links, and unusual email patterns.

It can be used as a learning project for understanding how machine learning and NLP can support email security.

---

## Note

For better accuracy and real-world use, replace `sample_data/sample_emails.csv` with a larger and properly labeled phishing email dataset.

---

## Future Improvements

* Add a web-based interface
* Analyze complete `.eml` files automatically
* Improve detection using larger datasets
* Add URL reputation checking
* Integrate threat intelligence APIs
* Add email attachment analysis

---

## Author

**Utkarsh Shukla**

Cybersecurity Project | Python | Machine Learning | Phishing Detection
