# crm/cron.py
from datetime import datetime

# Add these imports for GraphQL check
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def log_crm_heartbeat():
    """
    Logs a heartbeat message every 5 minutes to confirm CRM app health.
    Also optionally queries the GraphQL hello field to verify endpoint.
    """
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{timestamp} CRM is alive\n")
    
    # Optional GraphQL check
    transport = RequestsHTTPTransport(
        url="http://127.0.0.1:8000/graphql/",  # adjust if different
        verify=True,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)
    query = gql("""
    query {
        hello
    }
    """)
    try:
        response = client.execute(query)
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(f"GraphQL hello response: {response}\n")
    except Exception as e:
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(f"GraphQL query failed: {e}\n")