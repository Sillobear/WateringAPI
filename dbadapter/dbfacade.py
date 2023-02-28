from models import measurement as ms
from dbadapter import dbConfig

database = dbConfig.get_database()
measurements = database["measurements"]

def saveMeasurement(newMeasurement: ms.new_measurement) -> None:
    measurement = ms.measurement(newMeasurement.sensor_id, newMeasurement.moisture)
    data = {
        "sensor_id" : measurement.sensor_id,
        "moisture" : measurement.moisture,
        "datetime" : measurement.datetime
    }
    measurements.insert_one(data)