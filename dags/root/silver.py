import os
from generators.silver import SilverGenerators

CONFIG_PATH = os.getenv("AIRFLOW_SILVER_PATH")

generator = SilverGenerators(path =CONFIG_PATH, layer = 'bronze')
generator.load_dags(globals())