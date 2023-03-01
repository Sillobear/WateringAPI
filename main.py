from fastapi import FastAPI
from models import measurement
from dbadapter import dbfacade

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello":"World"}


@app.post("/new/")
async def create_item(measurement: measurement.new_measurement):
    dbfacade.saveMeasurement(measurement)
    return measurement