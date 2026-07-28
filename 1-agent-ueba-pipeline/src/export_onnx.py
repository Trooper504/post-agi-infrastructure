import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import os

def export_model():
    # 1. Load Data and Retrain
    print("Loading data and training model...")
    data_path = os.path.join("1-agent-ueba-pipeline", "tests", "synthetic_agent_logs.json")
    df = pd.read_json(data_path)
    
    features = df[['action', 'target_system', 'latency_ms', 'token_usage']]
    # ONNX requires strict typing. We force float32 here for compatibility.
    X = pd.get_dummies(features).astype(np.float32) 
    
    model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
    model.fit(X)

    # 2. Define the Graph Inputs
    print("Compiling scikit-learn model to ONNX graph...")
    initial_type = [('input_features', FloatTensorType([None, X.shape[1]]))]
    
    # Update target_opset to include the main domain:
    onnx_model = convert_sklearn(model, initial_types=initial_type, target_opset={'': 15, 'ai.onnx.ml': 3})

    # 3. Serialize and Save
    model_dir = os.path.join("1-agent-ueba-pipeline", "models")
    os.makedirs(model_dir, exist_ok=True)
    
    model_path = os.path.join(model_dir, "ueba_agent_model.onnx")
    with open(model_path, "wb") as f:
        f.write(onnx_model.SerializeToString())
        
    print(f"Success! Independent ONNX model saved to: {model_path}")

if __name__ == "__main__":
    export_model()