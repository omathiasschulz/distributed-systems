class ControllerPessoa:

    collection = None

    def __init__(self, collection):
        self.collection = collection

    def get(self):
        return str(self.collection.find()[0])

    def getOne(self, id):
        return str(self.collection.find_one({'_id': id}))

    def insertOne(self, jsonData):
        return self.collection.insert_one(jsonData).inserted_id

    def updateOne(self, id, jsonData):
        self.collection.update_one({'_id': id}, {'$set': jsonData})

    def deleteOne(self, id):
        self.collection.delete_one({'_id': id})