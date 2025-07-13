# coding: utf-8

import uuid

class SetModel:
    def __init__(self, score=0, models=[]):
        self.score = score
        self.models = models
    
    def calc_score(self, time_weight=1.0, quality_weight=1.0, sensor_label_weight=1.0, meta_weight=1.0):
        if not self.models:
            return 0

class Model:
    def __init__(self, unix_time, quality, sensor_label, meta_1, meta_2):
        self.id = uuid.uuid4().hex
        
        self.unix_time = unix_time
        self.quality = quality
        self.sensor_label = sensor_label
        self.meta_1 = meta_1
        self.meta_2 = meta_2