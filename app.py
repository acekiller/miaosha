import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction, QMouseEvent
from src.executor import Executor
from src.task import get_jd_task

class AppMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initUI()

    def _initUI(self):
        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('关闭应用')
        exitAct.triggered.connect(QApplication.instance().quit)

        self.statusBar()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('新增菜单')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 800, 700)
        self.setWindowTitle('电商秒单')

        self.setMouseTracking(True)

        self.show()

    def mouseMoveEvent(self, e: QMouseEvent):
        x = int(e.position().x())
        y = int(e.position().y())
        print(x, y)
        return super().mouseMoveEvent(e)

    
def init_executor():
    jd_task = get_jd_task("jd_account", "jd_password", qr_login=False)
    executor = Executor(key=jd_task.key(), task=jd_task)
    executor.execute()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppMain()

    init_executor()

    sys.exit(app.exec())
