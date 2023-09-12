
from .task_meta import TaskMeta
from .web_executor import WebExecutor
from .task_config import TaskConfig, GoodsConfig
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class JdTask(metaclass=TaskMeta):
    def __init__(self, task_config: TaskConfig):
        self.task_config = task_config
        we = WebExecutor(web_executor_config=task_config.get_web_executor_config())
        super.__init__(web_executor=we)

    "是否已经登录"
    def has_login(self):
        return self.web_executor.has(By.CLASS_NAME, "nickname")

    "是否已经选择商品"
    def has_selected_goods(self):
        pass

    "获取购物车商品"
    def get_cart_goods(self):
        pass

    "登录账户"
    def login(self):
        self.web_executor.load(self.task_config.platform.web_site())
        pre_url = self.web_executor.current_url
        self.web_executor.execute(By.LINK_TEXT, "你好，请登录")
        if self.task_config.qr_login:
            self.web_executor.execute(By.LINK_TEXT, "扫码登录")
        else:
            self.web_executor.execute(By.LINK_TEXT, "账户登录")
            self.web_executor.fill(By.ID, "loginname", self.task_config.account)
            self.web_executor.fill(By.ID, "nloginpwd", self.task_config.password)
            self.web_executor.execute(By.ID, "loginsubmit")
        self.web_executor.wait_to(pre_url)
        with self.wait(By.CLASS_NAME, "nickname") as (element, is_login):
            if is_login:
                print("登录成功")


    "选中商品"
    def select_goods(self, element: WebElement):
        pass

    "清理购物车"
    def clear_cart(self):
        pass


    def add_goods_items(self, goods_items: list[GoodsConfig]):
        pass

    def add_goods_item(self, goods: GoodsConfig):
        pass

    "执行订单任务"
    def execute_order_task(self):
        (goods_items, exec_time) = self.task_config.next_execute_goods_items()
        # for goods in goods_items:
        #     pass
        
        self.wait_to(exec_time)
        self.add_goods_items(goods_items)
        self.web_executor.load(self.task_config.platform.cart_url())
        if self.web_executor.has(By.CLASS_NAME, "cart-empty"):
            print("购物车没有商品")
            return
        
        while True:
            (element, success) = self.web_executor.execute(By.CLASS_NAME, "common-submit-btn")
            if success:
                break
            else:
                continue

        while True:
            (element, success) = self.web_executor.execute(By.CLASS_NAME, "order-submit")
            if success:
                break
            else:
                continue


def get_jd_task(account: str, password: str, qr_login: bool) -> TaskMeta:
    return JdTask(account, password, qr_login)