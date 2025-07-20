import json
import os

class Policyholder:
    def __init__(self, holder_id, name, active=True):
        self.holder_id = holder_id
        self.name = name
        self.active = active

    def suspend(self):
        self.active = False

    def reactivate(self):
        self.active = True

    def to_dict(self):
        return {"holder_id": self.holder_id, "name": self.name, "active": self.active}
