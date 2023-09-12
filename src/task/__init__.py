from .task_meta import TaskMeta
from .task_config import TaskConfig, GoodsConfig

from .jd_task import get_jd_task
from .tmall_task import get_tmall_task

__all__ = [
    "TaskMeta",
    "TaskConfig",
    "GoodsConfig",
    "get_jd_task",
    "get_tmall_task",
]
