# coding: utf-8
import time
import datetime as dt
from model import Model
import numpy as np

def convert_unix_time(datetime_obj):
    return int(time.mktime(datetime_obj.timetuple()))

def get_random_data(count=50):
    current_time = convert_unix_time(dt.datetime.now())
    
    return [Model(
        current_time - np.random.randint(0, 365 * 24 * 60 * 60 * 10),
        np.random.randint(30, 700) / 10.0,
        np.random.randint(0, 1),
        np.random.randint(0, 360),
        np.random.randint(0, 90)
    ) for _ in range(count)]