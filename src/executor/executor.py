from src.task import TaskMeta

class Executor:
    def __init__(self, key: str, task: TaskMeta):
        self.task = task

    def execute(self):
        if not self.task.has_login():
            self.task.login()

        print("开始执行订单任务")
        self.task.execute_order_task()

    def login(self):
        self.task.login()