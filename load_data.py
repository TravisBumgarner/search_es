import csv
from elasticsearch import Elasticsearch

es = Elasticsearch()

def load_data(index, doc_type, file):
    es.indices.create(index=index, ignore=400)

    with open(file) as f:
        reader = csv.DictReader(f)

        headers = ["street", "city", "zip", "state", "beds", "sq__ft", "sale_date"]


        for line in reader:
            street, city, zip, state, beds, sq__ft, sale_date = line.values()

            data = {
                "street": street,
                "city": city,
                "zip": zip,
                "state": state,
                "beds": int(beds),
                "sq__ft": int(sq__ft),
                "sale_date": sale_date
            }

            es.index(index="housing4", doc_type="house", body=data)

load_data('housing4', 'house', './housing.csv')

# LatD", "LatM", "LatS", "NS", "LonD", "LonM", "LonS", "EW", "City", "State"


