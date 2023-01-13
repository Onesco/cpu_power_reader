from typing import Union
from fastapi import FastAPI
from utils.utilities import Util
from utils.cpu_power import get_process_power

app = FastAPI()


@app.get('/powers/')
def read_powers():
    sleep = 10
    cpu_power = get_process_power(sleep);
    util = Util(cpu_power)

    cpu_power = util.cpu_power
    cpu_percent = util.cpu_percent
    running_process_power = util.get_running_process_power(limit=100, page_num=1)

    return {
       "cpu_power": cpu_power,
        "cpu_percent": cpu_percent,
        "running_process_power": running_process_power
    }
