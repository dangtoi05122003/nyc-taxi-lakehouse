import os
from generators.schema import SchemaGenerators

CONFIG_PATH = os.getenv("AIRFLOW_SCHEMA_PATH")

generator = SchemaGenerators(path =CONFIG_PATH, layer = 'schema')
generator.load_dags(globals())