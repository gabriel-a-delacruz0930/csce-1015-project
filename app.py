from datetime import datetime

def create_task(text: str):
    return {"text": text, "done": False, "created_at": datetime.utcnow().isoformat()}
