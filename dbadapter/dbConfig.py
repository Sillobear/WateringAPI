from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://api:pymongo@clusteriot.w0cvdaq.mongodb.net/?retryWrites=true&w=majority"

def get_database():
    client = MongoClient(CONNECTION_STRING)
    return client['sensor_db']

if __name__ == "__main__":
    # Get the database
    dbname = get_database()