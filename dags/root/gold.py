import os
from generators.gold import GoldGenerators

CONFIG_PATH = os.getenv("AIRFLOW_GOLD_PATH")

generator = GoldGenerators(path =CONFIG_PATH, layer = 'gold')
generator.load_dags(globals())