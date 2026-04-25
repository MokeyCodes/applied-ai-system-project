import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def log_run(question, result, validation):
    timestamp = datetime.now().isoformat()
    payload = {
        "timestamp": timestamp,
        "question": question,
        "answer": result["answer"],
        "sources": result["sources"],
        "validation": validation,
    }

    filename = LOG_DIR / f"run_{timestamp.replace(':', '-')}.json"
    filename.write_text(json.dumps(payload, indent=2), encoding="utf-8")