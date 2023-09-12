from src.task import TaskMeta

class Executor:
    def __init__(self, key: str, task: TaskMeta):
        self.task = task

    def execute(self):
        self._login()

    def _login(self):
        self.task.login()