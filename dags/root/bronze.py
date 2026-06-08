import os
from generators.bronze import BronzeGenerators

CONFIG_PATH = os.getenv("AIRFLOW_BRONZE_PATH")

generator = BronzeGenerators(path =CONFIG_PATH, layer = 'bronze')
generator.load_dags(globals())