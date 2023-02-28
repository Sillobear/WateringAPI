from pydantic import BaseModel
from datetime import datetime

class new_measurement(BaseModel):
    sensor_id: int
    moisture: float

class measurement():
    def __init__(self, sensor_id, moisture) -> None:
        self.sensor_id = sensor_id
        self.moisture = moisture
        self.datetime = datetime.now()
