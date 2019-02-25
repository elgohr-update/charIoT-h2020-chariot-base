# -*- coding: utf-8 -*-
from iotl import interpreter

class IoTLWrapper(object):
    
    def __init__(self, options):
        self.filepath = options['filepath']
        self.IoTState = interpreter.IoTState()

    def load(self):
        with open(self.filepath, 'r') as f:
            self.IoTState.parse(f.read())
        return True

    def isSensitive(self, sensor_id):
        return self.IoTState.params[sensor_id]['privacySensitive'] == 1

    def acl(self, sensor_id):
        return self.IoTState.acl[sensor_id] 