# coding: utf-8

import uuid

class Model:
    def __init__(self, unix_time, quality, sensor_label, meta_1, meta_2):
        self.id = uuid.uuid4().hex
        
        self.unix_time = unix_time
        self.quality = quality
        self.sensor_label = sensor_label
        self.meta_1 = meta_1
        self.meta_2 = meta_2