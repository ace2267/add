# index - tablespace
#  type -table
# doc -row
# 필드 - 컬럼
# 맵핑- 스키마

from elasticsearch import Elasticsearch, exceptions

class Elas:
    def __init__(self):
        self.esnode = None

    def ElasticServSetting(self):
        try:
            self.esnode = Elasticsearch(hosts="192.168.1.253", port="9200")
        except exceptions.ConnectionError as e:
            print (e)
        else:
            settings= {
                "settings": {
                    "number_of_shards": 3
                },
                "mappings": {
                    "doc": {
                        "properties": {
                            "numb" : {"type": "integer"},
                            "name" : {"type": "text"}
                        }
                    }
                }
            }
            # create index
            self.esnode.indices.create(index="indx190128", ignore=400, body=settings)


def main():
    node = Elas() # 객체 생성
    node.ElasticServSetting()l
if __name__ == "__main__":
    main()
