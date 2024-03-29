# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

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
        self.background_frame.setStyleSheet(u"background-color: rgb(233, 232, 238)")
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
        self.top_bar_frame.setStyleSheet(u"background-color: rgb(80, 27, 85)")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title_label = QLabel(self.top_bar_frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"color: rgb(251, 186, 0)")

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
        self.botones = QFrame(self.action_bar_frame_2)
        self.botones.setObjectName(u"botones")
        self.botones.setGeometry(QRect(270, 40, 300, 161))
        self.botones.setMinimumSize(QSize(300, 0))
        self.botones.setFrameShape(QFrame.StyledPanel)
        self.botones.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.botones)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.BTNDescarga = QPushButton(self.botones)
        self.BTNDescarga.setObjectName(u"BTNDescarga")
        self.BTNDescarga.setMinimumSize(QSize(0, 30))
        self.BTNDescarga.setStyleSheet(u"background-color: rgb(80, 27, 85);\n"
"color: rgb(251, 186, 0);")

        self.verticalLayout_4.addWidget(self.BTNDescarga)

        self.BTNUnir = QPushButton(self.botones)
        self.BTNUnir.setObjectName(u"BTNUnir")
        self.BTNUnir.setMinimumSize(QSize(0, 30))
        self.BTNUnir.setStyleSheet(u"background-color: rgb(80, 27, 85);\n"
"color: rgb(251, 186, 0);")

        self.verticalLayout_4.addWidget(self.BTNUnir)

        self.BTNConfiguracion = QPushButton(self.botones)
        self.BTNConfiguracion.setObjectName(u"BTNConfiguracion")
        self.BTNConfiguracion.setMinimumSize(QSize(0, 30))
        self.BTNConfiguracion.setStyleSheet(u"background-color: rgb(80, 27, 85);\n"
"color: rgb(251, 186, 0);")

        self.verticalLayout_4.addWidget(self.BTNConfiguracion)

        self.footer = QFrame(self.action_bar_frame_2)
        self.footer.setObjectName(u"footer")
        self.footer.setGeometry(QRect(-1, 280, 961, 61))
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.error = QFrame(self.footer)
        self.error.setObjectName(u"error")
        self.error.setMinimumSize(QSize(800, 0))
        self.error.setFrameShape(QFrame.StyledPanel)
        self.error.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.error)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.LabelError = QLabel(self.error)
        self.LabelError.setObjectName(u"LabelError")

        self.verticalLayout_5.addWidget(self.LabelError)


        self.horizontalLayout_2.addWidget(self.error)

        self.progress = QFrame(self.footer)
        self.progress.setObjectName(u"progress")
        self.progress.setFrameShape(QFrame.StyledPanel)
        self.progress.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.progress)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addWidget(self.progress)


        self.verticalLayout_2.addWidget(self.action_bar_frame_2)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Bot-Bolsa de Valores de Asunci\u00f3n", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.BTNDescarga.setText(QCoreApplication.translate("MainWindow", u"Descargar archivos", None))
        self.BTNUnir.setText(QCoreApplication.translate("MainWindow", u"Unir archivos", None))
        self.BTNConfiguracion.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.LabelError.setText("")
    # retranslateUi

