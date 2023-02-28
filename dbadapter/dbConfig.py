from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://sbranden:3Rc5zdaUNtr33HOw@wateringdb.udefj6u.mongodb.net/?retryWrites=true&w=majority"

def get_database():
    client = MongoClient(CONNECTION_STRING)
    return client['wateringdb']

if __name__ == "__main__":
    # Get the database
    dbname = get_database()