import os
from glob import glob

class BaseGenerator:
    def __init__(self, path):
        self.path = path
    def load_config_path(self):
        return glob(os.path.join(self.path, "*.yml"))