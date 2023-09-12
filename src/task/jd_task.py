from .task_meta import TaskMeta


class JdTask(metaclass=TaskMeta):
    def __init__(self, account: str, password: str, qr_login: bool):
        self.account = account
        self.password = password
        self.qr_login = qr_login
        self.key = f"jd_{account}"


def get_jd_task(account: str, password: str, qr_login: bool) -> TaskMeta:
    return JdTask(account, password, qr_login)