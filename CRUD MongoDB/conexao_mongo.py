from pymongo import MongoClient

def conectar():

    client = MongoClient(
        "mongodb://professor:professor@54.152.107.141:27017/?authSource=admin"
    )

    return client["universidade_nosql"]