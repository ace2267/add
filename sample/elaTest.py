import elasticsearch as es
import json
import pprint
import pandas as pd

es_client = es.Elasticsearch("192.168.1.253:9200")
# doc = es_client.get(index = 'logs-endpoint-monster-2019.04.10', doc_type = 'doc', id = 'kSjCB2oBtKCy25KIiFQS')
# doc = es_client.get(index = 'nwsession-fin-2019.04.08', doc_type = 'doc', id = 'rehk_2kBtKCy25KIzVEA')
# print(json.dumps(doc, indent = 2))


docs = es_client.search(index = 'nwsession-fin-*', body = {'query': {'range': {'@timestamp': {'gte' : '2019-04-08T00:00:00', 'lte' : '2019-04-08T23:59:59'} }}})

from pandasticsearch import Select
pandas_df = Select.from_dict(docs).to_pandas()
print(pandas_df.describe())


pandas_df.dtypes

# print(pandas_df.head(2))

# print(pandas_df)
# print(json.dumps(docs, indent = 2))



# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(doc)
# print(doc['_source']['event_timestamp'])
# docArr = doc.replace("","\")
# print(doc)

# print(type(doc))
# dict = json.loads(doc)
# print(dict)

# docs = es_client.search(index = 'nwsession-2019.02.20', body = {'query': {'match': {'file_attributes': '38'}}})

# print(json.dumps(docs, indent = 2))

