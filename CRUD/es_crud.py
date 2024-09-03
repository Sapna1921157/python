from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Create an index if it doesn't exist
if not es.indices.exists(index="mahadev"):
    es.indices.create(index="mahadev")

if es.exists(index="mahadev", id="k3dRtpEBmAs3vJMLVBZ8"):
    response = es.get(index="mahadev", id="k3dRtpEBmAs3vJMLVBZ8")
    print(response['_source'])
else:
    print("Document not found!")



# # Index a new document
# # doc = {
# #     "title": "Elasticsearch in Python",
# #     "content": "Learning to use Elasticsearch with Python.",
# #     "tags": ["elasticsearch", "python"],
# #     "published": True
# # }
# # es.index(index="mahadev", id=1, document=doc)



# Update the document
update_doc = {
     "doc": {
        "age": 31,        # Update the age to 31
        "city": "Boston"  # Update the city to Boston
    }
}
updated = es.update(index="mahadev", id="h3dRtpEBmAs3vJMLVBZ8", body=update_doc)
print("Updated data",updated)
print(response['_source'])




# Search for documents
print("\nSearching for documents with 'Elasticsearch' in content:")
query = {
    "query": {
        "bool": {
            "must": [
                {"match": {"age": "31"}},
                {"match": {"city": "boston"}}
            ]
        }
    }
}
response = es.search(index="mahadev", body=query)
for hit in response['hits']['hits']:
    print(hit['_source'])

# # # Delete the document
# # es.delete(index="mahadev", id=1)

# # # Delete the index (optional)
# # es.indices.delete(index="mahadev")
