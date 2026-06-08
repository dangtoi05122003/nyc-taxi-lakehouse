import attr

@attr.s(kw_only=True, auto_attribs=True)
class BaseDagConfig:
    dag_id: str
    dag_type: str
    schedule_interval: str
    max_active_runs: int
    catchup: bool
    owner: str
    retries: int
    retry_delay: int
    start_date: str
    is_paused_upon_creation: bool