#!/usr/bin/env python3
import datetime
import logging
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Configure logging
log_file = "/tmp/order_reminders_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

def main():
    # Setup GraphQL client
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=False,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # GraphQL query for orders within last 7 days
    query = gql("""
        query GetRecentOrders($date: DateTime!){
          orders(orderDate_Gte: $date) {
            id
            customer {
              email
            }
          }
        }
    """)

    # Calculate 7 days ago
    seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).isoformat()

    # Execute query
    result = client.execute(query, variable_values={"date": seven_days_ago})

    # Log orders
    for order in result.get("orders", []):
        order_id = order["id"]
        email = order["customer"]["email"]
        logging.info(f"Reminder: Order {order_id}, Customer Email: {email}")

    print("Order reminders processed!")

if __name__ == "__main__":
    main()