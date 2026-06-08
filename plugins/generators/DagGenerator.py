from generators.base import BaseGenerator
from utils import load_yaml
from models.Base import BaseDagConfig
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta, datetime
from abc import ABC, abstractmethod

class Generators(BaseGenerator, ABC):
    def __init__(self, path, layer):
        super().__init__(path)
        self.layer = layer
    def load_dags(self, global_session):
        for path in self.load_config_path():
            data = (load_yaml(path)).get('general')
            defaults = data.get("default_args")
            for config in data.get("dag_configs"):
                tasks = config.get("tasks")
                conf = BaseDagConfig(**{**defaults, **{k:v for k, v in config.items() if k != "tasks"}})
                global_session[conf.dag_id] = self.create_airflow_dag(conf, tasks)
    def create_airflow_dag(self, conf, tasks):
        dag = DAG(
            dag_id = conf.dag_id,
            default_args = {
                'owner': conf.owner,
                'retries': conf.retries,
                'retry_delay': timedelta(minutes=conf.retry_delay)
            },
            schedule_interval = conf.schedule_interval,
            start_date = datetime.strptime(conf.start_date, '%Y-%m-%d'),
            catchup = conf.catchup,
            max_active_runs = conf.max_active_runs,
            is_paused_upon_creation = conf.is_paused_upon_creation,
            tags = [self.layer, conf.dag_type]
        )
        with dag:
            for task in tasks:
                BashOperator(task_id = task["task_id"], bash_command = self.get_bash_command(task))
    @abstractmethod
    def get_bash_command(self, task):
        pass