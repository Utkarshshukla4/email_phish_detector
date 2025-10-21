# src/classify_email.py
import joblib
import os
from features import feature_vector, count_urls
import sys
import argparse

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model not found. Run train.py first.")
    return joblib.load(MODEL_PATH)

def rule_checks(subject, body, from_email):
    reasons = []
    text = f"{subject} {body}".lower()
    if 'bank' in text and 'http' in text and 'verify' in text:
        reasons.append("contains bank + verify + link (common phishing pattern)")
    if count_urls(text) >= 2:
        reasons.append("multiple URLs")
    if any(w in text for w in ["urgent", "immediately", "asap"]):
        reasons.append("urgent language")
    # Add sender-check heuristic (very naive)
    if from_email and ("support" in from_email.split('@')[0] and "@" in from_email):
        reasons.append("sender uses 'support' - verify domain")
    return reasons

def classify(subject, body, from_email):
    model = load_model()
    fv = feature_vector(subject, body, from_email)
    prob = model.predict_proba([fv])[0][1]
    rules = rule_checks(subject, body, from_email)
    # combine: if prob > 0.5 or rules non-empty => phishing
    phishing = prob > 0.5 or len(rules) > 0
    return phishing, prob, rules

def main():
    parser = argparse.ArgumentParser(description="Classify an email as phishing or not")
    parser.add_argument("--subject", default="", help="Email subject")
    parser.add_argument("--body", default="", help="Email body")
    parser.add_argument("--from_email", default="", help="From email address")
    args = parser.parse_args()
    phishing, prob, rules = classify(args.subject, args.body, args.from_email)
    print(f"Phishing probability (model): {prob:.3f}")
    print("Rule triggered reasons:", rules if rules else "none")
    print("Final decision:", "PHISHING" if phishing else "LEGITIMATE")

if __name__ == "__main__":
    main()
