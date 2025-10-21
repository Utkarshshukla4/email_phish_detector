# src/train.py
import pandas as pd
import joblib
import os
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from features import feature_vector

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample_emails.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    X = []
    for _, row in df.iterrows():
        fv = feature_vector(row['subject'] if not pd.isna(row['subject']) else "",
                            row['body'] if not pd.isna(row['body']) else "",
                            row['from_email'] if not pd.isna(row['from_email']) else "")
        X.append(fv)
    y = df['label'].astype(int).values
    return X, y

def train_and_save():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    vec = DictVectorizer(sparse=False)
    clf = LogisticRegression(max_iter=1000)
    pipe = Pipeline([
        ("vec", vec),
        ("clf", clf)
    ])
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    probs = pipe.predict_proba(X_test)[:,1]
    print("Classification report:\n", classification_report(y_test, preds))
    try:
        print("ROC AUC:", roc_auc_score(y_test, probs))
    except Exception:
        pass
    joblib.dump(pipe, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")

if __name__ == "__main__":
    train_and_save()
