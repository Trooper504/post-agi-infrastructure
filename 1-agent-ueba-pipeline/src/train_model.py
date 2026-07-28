import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
import os

def train_ueba_model():
    print("Loading synthetic agent logs...")
    data_path = os.path.join("1-agent-ueba-pipeline", "tests", "synthetic_agent_logs.json")
    
    try:
        df = pd.read_json(data_path)
    except FileNotFoundError:
        print(f"Error: Could not find {data_path}. Run generate_logs.py first.")
        return

    # 1. Feature Engineering
    # We isolate the behavior metrics: what did it do, where, how fast, and how heavy?
    features = df[['action', 'target_system', 'latency_ms', 'token_usage']]
    
    # Convert categorical text data (like "fetch_crm_record") into a binary matrix so the math works
    print("Encoding categorical features...")
    X = pd.get_dummies(features)

    # 2. Train the Isolation Forest
    # We set contamination to 0.02 because we know our anomaly rate is roughly 2%
    print("Training the Isolation Forest model...")
    model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
    model.fit(X)

    # 3. Predict and Evaluate
    # The model returns -1 for outliers/anomalies and 1 for normal behavior
    df['prediction'] = model.predict(X)
    
    # Map the -1/1 output back to our 1/0 anomaly_flag format for easy grading
    df['predicted_anomaly'] = df['prediction'].apply(lambda x: 1 if x == -1 else 0)

    print("\n=== Model Evaluation ===")
    print("How well did the unsupervised model find the hidden rogue agents?\n")
    
    # Compare the model's blind guesses against the actual injected anomalies
    print(classification_report(df['anomaly_flag'], df['predicted_anomaly'], 
                                target_names=["Normal Agent", "Rogue Agent"]))

if __name__ == "__main__":
    train_ueba_model()