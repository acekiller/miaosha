from .task_meta import TaskMeta


class TmallTask(metaclass=TaskMeta):
    def __init__(self, account: str, password: str, qr_login: bool):
        self.account = account
        self.password = password
        self.qr_login = qr_login
        self.key = f"tmall_{account}"


def get_tmall_task(account: str, password: str, qr_login: bool) -> TaskMeta:
    return TmallTask(account, password, qr_login)