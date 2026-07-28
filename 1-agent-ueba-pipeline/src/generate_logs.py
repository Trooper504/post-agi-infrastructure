import os
import json
import random
from datetime import datetime, timedelta

def generate_normal_event(agent_id, current_time):
    return {
        "timestamp": current_time.isoformat(),
        "agent_id": agent_id,
        "action": random.choice(["fetch_crm_record", "send_email", "summarize_document", "query_database"]),
        "target_system": random.choice(["salesforce_api", "exchange_server", "internal_wiki"]),
        "latency_ms": random.randint(150, 900),
        "token_usage": random.randint(50, 800),
        "status_code": 200,
        "anomaly_flag": 0
    }

def generate_rogue_event(agent_id, current_time):
    # Simulates an agent hit by a prompt injection, data exfiltration, or infinite loop
    return {
        "timestamp": current_time.isoformat(),
        "agent_id": agent_id,
        "action": random.choice(["mass_data_export", "system_shell_exec", "unauthorized_lateral_movement"]),
        "target_system": random.choice(["root_filesystem", "external_untrusted_api", "auth_server"]),
        # Anomalously fast (stuck in a loop) or very slow (heavy exfiltration)
        "latency_ms": random.choice([random.randint(10, 50), random.randint(3000, 8000)]),
        # Massive token spike from injected payloads
        "token_usage": random.randint(5000, 16000), 
        "status_code": random.choice([200, 401, 403, 500]),
        "anomaly_flag": 1
    }

def build_dataset(total_events=10000, anomaly_rate=0.03):
    logs = []
    start_time = datetime.now()
    agent_pool = [f"agent_svc_{i}" for i in range(1, 6)]

    for i in range(total_events):
        current_time = start_time + timedelta(seconds=i * random.uniform(0.5, 3.0))
        agent = random.choice(agent_pool)

        if random.random() < anomaly_rate:
            logs.append(generate_rogue_event(agent, current_time))
        else:
            logs.append(generate_normal_event(agent, current_time))

    return logs

if __name__ == "__main__":
    print("Generating synthetic agent execution logs...")
    dataset = build_dataset(total_events=50000, anomaly_rate=0.02)
    
    output_dir = "1-agent-ueba-pipeline/tests"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "synthetic_agent_logs.json")
    with open(output_path, "w") as f:
        json.dump(dataset, f, indent=2)
        
    print(f"Successfully generated {len(dataset)} logs at {output_path}")