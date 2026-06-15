from catalog.schema import Schema

class Zones(Schema):
    def __init__(self, config_path, format):
        super().__init__(config_path, format)
if __name__ == "__main__":
    app = Zones("/opt/airflow/config/schema/zones.yml", 'CSV')
    app.create_all_tables()