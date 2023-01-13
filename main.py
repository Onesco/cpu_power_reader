from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.utilities import Util
from utils.cpu_power import get_process_power

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_headers = ["*"],
    allow_methods = ["*"],
)


@app.get('/powers/')
def read_powers(sleep: int = 2, limit: int = 100, page_num= 1):
    cpu_power = get_process_power(sleep);
    util = Util(cpu_power)
    cpu_power = util.cpu_power
    cpu_percent = util.cpu_percent
    running_process_power = util.get_running_process_power(limit, page_num)

    return {
       "cpu_power": cpu_power,
        "cpu_percent": cpu_percent,
        "running_process_power": running_process_power
    }
