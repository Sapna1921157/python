from elasticsearch import Elasticsearch

# Initialize the Elasticsearch client
es = Elasticsearch(
    ["http://localhost:9200"],  # Replace with your Elasticsearch host
)

# Verify the connection
if es.ping():
    print("Connected to Elasticsearch!")
else:
    print("Could not connect to Elasticsearch.")
