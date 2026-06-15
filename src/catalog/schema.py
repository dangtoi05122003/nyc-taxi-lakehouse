from client.trino_client import TrinoClient
from utils import load_yaml

class Schema:
    def __init__(self, config_path, format):
        self.config = load_yaml(config_path)
        self.client = TrinoClient()
        self.format = format
    def create_all_tables(self):
        for table_name, table_config in self.config["tables"].items():
            self.client.create_table(tablename=table_name,columns=table_config['columns'], partition_by=table_config['partition_by'], path=self.config['path']['source'], format=self.format)