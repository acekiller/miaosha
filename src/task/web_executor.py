from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .task_config import TaskWebExectorConfig

class WebExecutor:
    def __init__(self, web_executor_config: TaskWebExectorConfig) -> None:
        self.web_executor_config = web_executor_config
        options = Options()
        options.binary_location = web_executor_config.chrome_path
        self.driver = webdriver.Chrome(options=options, service=Service(driver_path))

    def has(self, by: By, element_key: str) -> bool:
        try :
            _ = self.driver.find_element(by, element_key)
            return True
        except Exception:
            return False
        
    def _wait_load(self):
        self.driver.execute_script("return document.readyState").equals("complete")
        
    def load(self, url: str):
        self.driver.get(url)
        self._wait_load()

    def wait_to(self, url: str):
        WebDriverWait(self.driver, 10, 0.01).until(EC.url_to_be(url=url))
        self._wait_load()

    def current_url(self) -> str:
        return self.driver.current_url

    def find(self, by: By, element_key: str) -> (WebElement, bool):
        try :
            element = self.driver.find_element(by, element_key)
            return (element, True)
        except Exception:
            return (None, False)
        
    def find_list(self, by: By, element_key: str) -> (list[WebElement], bool):
        try :
            elements = self.driver.find_element(by, element_key)
            return (elements, True)
        except Exception:
            return (None, False)

    def execute(self, by: By, element_key: str) -> (WebElement, bool):
        try :
            element = self.driver.find_element(by, element_key).click()
            self._wait_load()
            return (element, True)
        except Exception:
            return (None, False)
        
    def fill(self, by: By, element_key: str, value: str) -> (WebElement, bool):
        try :
            element = self.driver.find_element(by, element_key).send_keys(value)
            self._wait_load()
            return (element, True)
        except Exception:
            return (None, False)
        

    def wait(self, by: By, element_key: str, exec_click: bool = False, timeout: int = 10, poll_frequency: int = 0.5) -> (WebElement, bool):
        try :
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located((by, element_key)))
            if exec_click:
                element.click()
                self._wait_load()
            return (element, True)
        except Exception:
            return (None, False)