from datetime import datetime
from dateutil import relativedelta
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {'response': 'OK'}

@app.get("/diff/")
async def get_diff():
    date_one = datetime(2006, 7, 28)
    date_two = datetime.now()

    diff = relativedelta.relativedelta(date_two, date_one)

    return {'years': diff.years, 'months': diff.months, 'days': diff.days}