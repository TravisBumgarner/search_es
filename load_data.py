import csv
from elasticsearch import Elasticsearch

es = Elasticsearch()

def load_data(index, doc_type, file):
    es.indices.create(index=index, ignore=400)

    with open(file) as f:
        reader = csv.DictReader(f)

        headers = next(reader)
        print(headers)

        for line in reader:
            es.index(index=index, doc_type=doc_type, body=line)
            print(line)
load_data('people2', 'person', './us-500.csv')

# "LatD", "LatM", "LatS", "NS", "LonD", "LonM", "LonS", "EW", "City", "State"