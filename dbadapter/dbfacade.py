import datetime

from models import measurement as ms
from dbadapter import dbConfig

database = dbConfig.get_database()
measurements = database["moistures"]

def saveMeasurement(newMeasurement: ms.new_measurement) -> None:
    measurement = ms.measurement(newMeasurement.sensor_id, newMeasurement.moisture)
    data = {
      "metadata": { "sensorId": newMeasurement.sensor_id, "type": "moisture" },
      "timestamp":datetime.datetime.now(),
      "moisture": newMeasurement.moisture
    }
    measurements.insert_one(data)