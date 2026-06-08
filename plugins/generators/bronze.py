from generators.DagGenerator import Generators

class BronzeGenerators(Generators):
    def __init__(self, path, layer):
        super().__init__(path, layer)
    def get_bash_command(self, task):
        return f"cd /opt/airflow && python {task['script_path']}"