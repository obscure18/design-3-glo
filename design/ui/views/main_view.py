from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QMainWindow
from design.ui.views.generated.ui_main_view import Ui_main_window
from design.ui.models.main_model import MainModel
from design.ui.controllers.main_controller import MainController


class MainView(QMainWindow):
    def __init__(self, model: MainModel, controller: MainController):
        super().__init__()
        self.controller = controller
        self.model = model

        self.timer = QTimer(self)
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.setup_connections()
        self.model.subscribe_update_function(self.start_timer)
        self.model.subscribe_update_function(self.update_console_log)

    def add_tab(self, tab_widget, tab_title):
        self.ui.tab_widget.addTab(tab_widget, tab_title)

    def add_painting(self, paint_widget):
        self.ui.painting_layout.addWidget(paint_widget)

    @pyqtSlot()
    def start_new_cycle(self):
        if not self.model.start_new_cycle:
            self.controller.start_new_cycle()

    @pyqtSlot()
    def find_robot(self):
        if not self.model.find_robot_flag:
            self.controller.find_robot()

    @pyqtSlot()
    def update_lcd(self):
        if self.model.timer_is_on:
            self.controller.update_time()
            self.ui.chrono_lcd.display(self.model.time)

    def setup_connections(self):
        self.ui.start_btn.clicked.connect(self.on_start)
        self.ui.pause_btn.clicked.connect(self.on_pause)
        self.ui.stop_btn.clicked.connect(self.on_stop)
        self.timer.timeout.connect(self.update_lcd)
        self.ui.new_cycle_btn.clicked.connect(self.start_new_cycle)
        self.ui.find_robot_btn.clicked.connect(self.find_robot)

    @pyqtSlot()
    def on_start(self):
        self.controller.activate_timer()
        self.timer.start(1000)

    @pyqtSlot()
    def on_stop(self):
        self.controller.deactivate_timer()
        self.controller.reset_timer()
        self.timer.stop()

    @pyqtSlot()
    def on_pause(self):
        self.controller.deactivate_timer()
        self.timer.stop()

    def start_timer(self):
        if not self.timer.isActive() and self.model.timer_is_on:
            self.timer.start(1000)

    def update_console_log(self):
        self.ui.console_log_textEdit.setPlainText(self.model.log_messages)
