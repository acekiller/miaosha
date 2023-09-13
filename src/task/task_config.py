from datetime import datetime, timedelta
from enum import Enum, unique

import sys
if sys.platform == "darwin":
    default_chrome_path = "resources/116/Chrome.app/Contents/MacOS/Google Chrome"
    default_chrome_drive_path = "resources/116/chromedriver"
else:
    default_chrome_path = None
    default_chrome_drive_path = None

config_dict = {
        'jd': {
            "name": "京东",
            "web_site": "https://www.jd.com",
            "cart_url": "https://cart.jd.com/cart_index",
        },
        "tmall": {
            "name": "天猫",
            "web_site": "https://www.tmall.com",
            "cart_url": "https://cart.tmall.com/cart.htm",
        },
    }

@unique
class PlatformType(Enum):
    JD = "jd"
    TMALL = "tmall"
    
    def web_site(self):
        return config_dict.get(self.value).get("web_site")

    def cart_url(self):
        return config_dict.get(self.value).get("cart_url")

    def platform_flag(self) -> str:
        return self.value
        

class TaskWebExectorConfig:
    def __init__(self, chrome_path: str = default_chrome_path, driver_path: str = default_chrome_drive_path):
        self.chrome_path = chrome_path
        self.driver_path = driver_path
        

class GoodsConfig:
    def __init__(self, url: str, exec_time: datetime = None, add_when_exec: bool = False, clean_other_goods: bool = False):
        "商品链接"
        self.url = url
        "执行时间"
        self.exec_time = exec_time
        "执行时添加购物车还是直接添加购物车"
        self.add_when_exec = add_when_exec
        "是否需要清理其他商品"
        self.clean_other_goods = clean_other_goods

        self.goods_items = []

class TaskConfig:
    def __init__(self, platform: PlatformType, web_executor_config: TaskWebExectorConfig, account: str, password: str, qr_login: bool):
        self.account = account
        self.password = password
        self.key = f"{platform.platform_flag()}_{account}"
        self.qr_login = qr_login
        self.platform = platform
        self._web_executor_config = web_executor_config
        self.goods_item_changed = None

    def addGoods_item(self, goods: GoodsConfig):
        self.goods_items.append(goods)
        if self.goods_item_changed:
            self.goods_item_changed()

    def addGoods_items(self, goods_list: list[GoodsConfig]):
        self.goods_items.extend(goods_list)
        if self.goods_item_changed:
            self.goods_item_changed()

    def get_goods_items(self):
        return self.goods_items

    def get_web_executor_config(self):
        return self._web_executor_config
    
    def next_execute_goods_items(self) -> (list[GoodsConfig], datetime):
        goods_items = [GoodsConfig(url="https://item.jd.com/569064.html")]
        return(goods_items, datetime.now() + timedelta(seconds=20))
        # return (self.goods_items, self.goods_items[0].exec_time)
        # return (self.goods_items, self.goos_items[0].exec_time)

    