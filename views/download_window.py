# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dowload_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class DownloadWindow(object):
    def setupUi(self, DowloadWindow):
        if not DowloadWindow.objectName():
            DowloadWindow.setObjectName(u"DowloadWindow")
        DowloadWindow.resize(1014, 443)
        DowloadWindow.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(DowloadWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(DowloadWindow)
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
        self.frame_2 = QFrame(self.action_bar_frame_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(190, 20, 481, 131))
        self.frame_2.setStyleSheet(u"background-color: #fff;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"\n"
"color: rgb(80, 30, 83)")

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.FechaDesde = QDateEdit(self.frame)
        self.FechaDesde.setObjectName(u"FechaDesde")
        self.FechaDesde.setStyleSheet(u"background-color: rgb(227, 227, 227)")
        self.FechaDesde.setCalendarPopup(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.FechaDesde)

        self.FechaHasta = QDateEdit(self.frame)
        self.FechaHasta.setObjectName(u"FechaHasta")
        self.FechaHasta.setStyleSheet(u"background-color: rgb(227, 227, 227)")
        self.FechaHasta.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.FechaHasta)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)


        self.verticalLayout_4.addWidget(self.frame)

        self.botones = QFrame(self.action_bar_frame_2)
        self.botones.setObjectName(u"botones")
        self.botones.setGeometry(QRect(180, 180, 491, 91))
        self.botones.setFrameShape(QFrame.StyledPanel)
        self.botones.setFrameShadow(QFrame.Raised)
        self.BTNIniciar = QPushButton(self.botones)
        self.BTNIniciar.setObjectName(u"BTNIniciar")
        self.BTNIniciar.setGeometry(QRect(9, 22, 471, 31))
        self.BTNIniciar.setStyleSheet(u"background-color: rgb(80, 27, 85);\n"
"color: rgb(251, 186, 0);")
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

        self.PBEstado = QProgressBar(self.progress)
        self.PBEstado.setObjectName(u"PBEstado")
        self.PBEstado.setValue(0)

        self.horizontalLayout_3.addWidget(self.PBEstado)


        self.horizontalLayout_2.addWidget(self.progress)


        self.verticalLayout_2.addWidget(self.action_bar_frame_2)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(DowloadWindow)

        QMetaObject.connectSlotsByName(DowloadWindow)
    # setupUi

    def retranslateUi(self, DowloadWindow):
        DowloadWindow.setWindowTitle(QCoreApplication.translate("DowloadWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("DowloadWindow", u"Bot-Bolsa de Valores de Asunci\u00f3n", None))
        self.minimize_button.setText(QCoreApplication.translate("DowloadWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("DowloadWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("DowloadWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("DowloadWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("DowloadWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Selecciona rango de fecha para descargar los registros disponibles</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("DowloadWindow", u"Desde:", None))
        self.label_2.setText(QCoreApplication.translate("DowloadWindow", u"Hasta", None))
        self.BTNIniciar.setText(QCoreApplication.translate("DowloadWindow", u"Iniciar", None))
        self.LabelError.setText("")
    # retranslateUi

