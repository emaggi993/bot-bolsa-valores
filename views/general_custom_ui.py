from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsDropShadowEffect

class GeneralCustomUi():
    def __init__(self, ui):
        self.ui = ui
        self.remove_defaul_title_bar()
        self.ui.top_bar_frame.mouseMoveEvent = self.move_window
        self.set_windows_shadow()
        self.set_title_bar_buttons_actions()

    def remove_defaul_title_bar(self):
        self.ui.setAttribute(Qt.WA_TranslucentBackground, True ) 
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
    
    def mouse_press_event(self, event):
        self.drag_pos = event.globalPos()
    
    def move_window(self, event):
        if event.buttons()== Qt.LeftButton:
            self.ui.move(self.ui.pos() + event.globalPos() - self.drag_pos)
            self.drag_pos = event.globalPos()

    def set_windows_shadow(self):
        shadow = QGraphicsDropShadowEffect(self.ui)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor("#000000")
        self.ui.background_frame.setGraphicsEffect(shadow)

    def maximize_window(self):
        self.ui.showMaximized()
        self.ui.maximize_button.setVisible(False)
        self.ui.shadow_layout.setContentsMargins(0,0,0,0)
    def restore_window(self):
        self.ui.showNormal()
        self.ui.maximize_button.setVisible(True)
        self.ui.shadow_layout.setContentsMargins(10,10,10,10)
    
    def set_title_bar_buttons_actions(self):
        self.ui.maximize_button.clicked.connect(self.maximize_window)
        self.ui.restore_button.clicked.connect(self.restore_window)
        self.ui.close_button.clicked.connect(self.ui.close)
        self.ui.minimize_button.clicked.connect(self.ui.showMinimized)