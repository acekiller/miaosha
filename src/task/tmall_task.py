from .task_meta import TaskMeta
from .web_executor import WebExecutor
from .task_config import TaskConfig, GoodsConfig
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from .task_config import TaskConfig, PlatformType, TaskWebExectorConfig


class TmallTask(metaclass=TaskMeta):
    def __init__(self, task_config: TaskConfig):
        self.task_config = task_config
        we = WebExecutor(web_executor_config=task_config.get_web_executor_config())
        self.web_executor = we
        self.web_executor.load(self.task_config.platform.web_site())
        # super.__init__(web_executor=we)

    def key(self):
        return self.task_config.key

    "是否已经登录"
    def has_login(self):
        return self.web_executor.has(By.CLASS_NAME, "sn-user-nick")

    "是否已经选择商品"
    def has_selected_goods(self):
        pass

    "获取购物车商品"
    def get_cart_goods(self):
        pass

    "登录账户"
    def login(self):
        pre_url = self.web_executor.current_url()
        self.web_executor.execute(By.LINK_TEXT, "请登录")
        if self.task_config.qr_login:
            if self.web_executor.has(By.CLASS_NAME, "icon-qrcode"):
                self.web_executor.execute(By.CLASS_NAME, "icon-qrcode")
        else:
            if self.web_executor.has(By.CLASS_NAME, "icon-password"):
                self.web_executor.execute(By.CLASS_NAME, "icon-password")
                self.web_executor.execute(By.CLASS_NAME, "password-login-tab-item")
            self.web_executor.fill(By.ID, "fm-login-id", self.task_config.account)
            self.web_executor.fill(By.ID, "fm-login-password", self.task_config.password)
            self.web_executor.execute(By.ID, "password-login")
        self.web_executor.wait_to(pre_url)
        print("账户登录成功")


    "选中商品"
    def select_goods(self, element: WebElement):
        pass

    "清理购物车"
    def clear_cart(self):
        pass


    def add_goods_items(self, goods_items: list[GoodsConfig]):
        for item in goods_items:
            self.add_goods_item(item)

    def add_goods_item(self, goods: GoodsConfig):
        self.web_executor.load(goods.url)
        self.web_executor.execute(By.ID, "InitCartUrl")

    "执行订单任务"
    def execute_order_task(self):
        (goods_items, exec_time) = self.task_config.next_execute_goods_items()
        wait_goods_items = []
        for item in goods_items:
            if not item.add_when_exec:
                self.add_goods_item(item)
            else:
                wait_goods_items.append(item)

        self.web_executor.load(self.task_config.platform.cart_url())
        TaskMeta.wait_to(exec_time)
        if wait_goods_items:
            self.add_goods_items(goods_items)
            self.web_executor.load(self.task_config.platform.cart_url())

        if self.web_executor.has(By.ID, "empty"):
            return

        while True:
            if self.web_executor.has(By.CLASS_NAME, "submit-btn-disabled"):
                continue
            success = self.web_executor.execute(By.ID, "J_Go")
            if success:
                break
            else:
                continue
        
        while True:
            success = self.web_executor.execute(By.LINK_TEXT, "提交订单")
            if success:
                break
            else:
                continue
        self.web_executor.wait(By.LINK_TEXT, "立即支付")


def get_tmall_task(account: str, password: str, qr_login: bool) -> TaskMeta:
    config = TaskConfig(PlatformType.TMALL, TaskWebExectorConfig(), account, password, qr_login)
    return TmallTask(config)