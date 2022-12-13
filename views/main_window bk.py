# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1014, 443)
        MainWindow.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(MainWindow)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(107, 109, 109)")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_bar_frame = QFrame(self.content_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setMinimumSize(QSize(0, 39))
        self.top_bar_frame.setMaximumSize(QSize(16777215, 40))
        self.top_bar_frame.setStyleSheet(u"background-color: rgb(177, 177, 177)")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")

        self.horizontalLayout.addWidget(self.title_label)

        self.button_holder_frame = QFrame(self.top_bar_frame)
        self.button_holder_frame.setObjectName(u"button_holder_frame")
        self.button_holder_frame.setMinimumSize(QSize(0, 30))
        self.button_holder_frame.setMaximumSize(QSize(110, 16777215))
        self.button_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.button_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.button_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(10, 0, 22, 22))
        icon = QIcon()
        icon.addFile(u"./assets/icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.button_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(40, 0, 22, 22))
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.button_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(70, 0, 22, 22))
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon2)
        self.close_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.button_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(40, 0, 22, 22))
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon3)
        self.maximize_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.button_holder_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.top_bar_frame)

        self.action_bar_frame_2 = QFrame(self.content_frame)
        self.action_bar_frame_2.setObjectName(u"action_bar_frame_2")
        self.action_bar_frame_2.setMinimumSize(QSize(0, 39))
        self.action_bar_frame_2.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_2.setFrameShadow(QFrame.Raised)
        self.btn_agregar_nuevo_boletin = QPushButton(self.action_bar_frame_2)
        self.btn_agregar_nuevo_boletin.setObjectName(u"btn_agregar_nuevo_boletin")
        self.btn_agregar_nuevo_boletin.setGeometry(QRect(0, 0, 150, 30))
        font = QFont()
        font.setBold(True)
        self.btn_agregar_nuevo_boletin.setFont(font)
        self.btn_agregar_nuevo_boletin.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(204, 170, 28);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #ffc13b;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/excel icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agregar_nuevo_boletin.setIcon(icon4)
        self.btn_agregar_nuevo_boletin.setIconSize(QSize(20, 20))
        self.btn_rehacer_rango = QPushButton(self.action_bar_frame_2)
        self.btn_rehacer_rango.setObjectName(u"btn_rehacer_rango")
        self.btn_rehacer_rango.setGeometry(QRect(280, 0, 150, 30))
        self.btn_rehacer_rango.setFont(font)
        self.btn_rehacer_rango.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(204, 170, 28);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #ffc13b;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rehacer_rango.setIcon(icon5)
        self.btn_rehacer_rango.setIconSize(QSize(20, 20))
        self.btn_verificar_bancos = QPushButton(self.action_bar_frame_2)
        self.btn_verificar_bancos.setObjectName(u"btn_verificar_bancos")
        self.btn_verificar_bancos.setGeometry(QRect(510, 0, 191, 30))
        self.btn_verificar_bancos.setFont(font)
        self.btn_verificar_bancos.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(204, 170, 28);\n"
"color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: #ffc13b;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_verificar_bancos.setIcon(icon6)
        self.btn_verificar_bancos.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.action_bar_frame_2)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Proyectos", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_agregar_nuevo_boletin.setText(QCoreApplication.translate("MainWindow", u"Agregar Boletin", None))
        self.btn_rehacer_rango.setText(QCoreApplication.translate("MainWindow", u"Generar BD por fecha", None))
        self.btn_verificar_bancos.setText(QCoreApplication.translate("MainWindow", u"Verificar Integridad Bancos", None))
    # retranslateUi

