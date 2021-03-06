import pymongo
from loguru import logger


class SeriesCollectionMongo:

    def __init__(self, dbname: str, name_collection: str, host='localhost', port=27017):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.name_collection = name_collection
        self.client = pymongo.MongoClient(self.host, self.port)
        self.db = self.client[self.dbname]
        self.collection = self.db[self.name_collection]

    def insert_document(self, data: dict, multiple=False):
        if multiple:
            return self.collection.insert_many(data).insert_ids
        return self.collection.insert_one(data).inserted_id

    def find_document(self, elements: dict, multiple=False):
        if multiple:
            data = self.collection.find(elements)
            return [doc for doc in data]
        return self.collection.find_one(elements)

    def update_document(self, query_elements: dict, new_values: dict, multiple=False):
        if multiple:
            return self.collection.update_many(query_elements, {'$set': new_values}, upsert=False).modified_count
        return self.collection.update_one(query_elements, {'$set': new_values}, upsert=False).modified_count

    def delete_document(self, query: dict, multiple=False):
        if multiple:
            return self.collection.delete_many(query).deleted_count
        return self.collection.delete_one(query).deleted_count

    def delete_key_document(self, query_element: dict, keys: list, multiple=False):
        keys = {key: True for key in keys}
        if multiple:
            return self.collection.update_many(query_element, {'$unset': keys}).modified_count
        return self.collection.update_one(query_element, {'$unset': keys}).modified_count

    def create_text_index(self, fields):
        return self.collection.create_index([(fields, 'text')])


if __name__ == '__main__':
    collection = SeriesCollectionMongo('tutorial', 'user')
    collection.update_document({}, {'age': 25, 'description': 'Hello World'}, multiple=True)
