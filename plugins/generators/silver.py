from generators.DagGenerator import Generators

class SilverGenerators(Generators):
    def __init__(self, path, layer):
        super().__init__(path, layer)
    def get_bash_command(self, task):
        return f"docker exec nyc-spark spark-submit {task['script_path']}"