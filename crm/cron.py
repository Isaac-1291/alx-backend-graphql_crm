# crm/cron.py
from datetime import datetime

def log_crm_heartbeat():
    """
    Logs a heartbeat message every 5 minutes to confirm CRM app health.
    """
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{timestamp} CRM is alive\n")