from selenium.webdriver.remote.webelement import WebElement
from .web_executor import WebExecutor
from datetime import datetime, timedelta, UTC
import pytz

class TaskMeta(type):
    def __init__(self, web_executor: WebExecutor):
        # 自定义类的初始化逻辑
        self.web_executor = web_executor
        super().__init__()


    "是否已经登录"
    def has_login(self):
        pass

    "是否已经选择商品"
    def has_selected_goods(self):
        pass

    "获取购物车商品"
    def get_cart_goods(self):
        pass

    "登录账户"
    def login(self):
        pass

    "选中商品"
    def select_goods(self, element: WebElement):
        pass

    "清理购物车"
    def clear_cart(self):
        pass

    "执行订单任务"
    def execute_order_task(self):
        pass

    def wait_to(self, exec_time: datetime):
        e_time = exec_time + timedelta(milliseconds=-100)
        while True:
            now = datetime.now(UTC)
            if now >= e_time:
                break
        







