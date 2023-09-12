from datetime import datetime

class GoodsConfig:
    def __init__(self, url: str, exec_time: datetime, add_when_exec: bool = False, clearn_other_goods: bool = False):
        "商品链接"
        self.url = url
        "执行时间"
        self.exec_time = exec_time
        "执行时添加购物车还是直接添加购物车"
        self.add_when_exec = add_when_exec
        "是否需要清理其他商品"
        self.clearn_other_goods = clearn_other_goods

class TaskConfig:
    def __init__(self, key: str):
        pass
