# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'union_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class UnionWindow(object):
    def setupUi(self, UnionWindow):
        if not UnionWindow.objectName():
            UnionWindow.setObjectName(u"UnionWindow")
        UnionWindow.resize(1014, 443)
        UnionWindow.setStyleSheet(u"border-radius: 5px;")
        self.verticalLayout = QVBoxLayout(UnionWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(UnionWindow)
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
        self.action_bar_frame_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(80, 27, 85);\n"
"color: rgb(251, 186, 0);\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(118, 40, 127, 255);\n"
"color: rgb(251, 186, 0);\n"
"}")
        self.action_bar_frame_2.setFrameShape(QFrame.StyledPanel)
        self.action_bar_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.action_bar_frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_datos = QFrame(self.action_bar_frame_2)
        self.frame_datos.setObjectName(u"frame_datos")
        self.frame_datos.setMinimumSize(QSize(0, 200))
        self.frame_datos.setMaximumSize(QSize(16777215, 300))
        self.frame_datos.setStyleSheet(u"background-color: #fff;")
        self.frame_datos.setFrameShape(QFrame.StyledPanel)
        self.frame_datos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_datos)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_datos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"\n"
"color: rgb(80, 30, 83)")

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.frame = QFrame(self.frame_datos)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(80, 27, 85);\n"
"color: rgb(251, 186, 0);\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(118, 40, 127, 255);\n"
"color: rgb(251, 186, 0);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.LESeleccionarCarpeta = QLineEdit(self.frame)
        self.LESeleccionarCarpeta.setObjectName(u"LESeleccionarCarpeta")
        self.LESeleccionarCarpeta.setMinimumSize(QSize(800, 25))
        self.LESeleccionarCarpeta.setStyleSheet(u"background-color: rgb(229, 229, 229);")

        self.horizontalLayout_4.addWidget(self.LESeleccionarCarpeta)

        self.BTNSeleccionar = QPushButton(self.frame)
        self.BTNSeleccionar.setObjectName(u"BTNSeleccionar")
        self.BTNSeleccionar.setMinimumSize(QSize(200, 25))
        self.BTNSeleccionar.setMaximumSize(QSize(200, 16777215))
        self.BTNSeleccionar.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.BTNSeleccionar)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_fecha = QFrame(self.frame_datos)
        self.frame_fecha.setObjectName(u"frame_fecha")
        self.frame_fecha.setMinimumSize(QSize(0, 90))
        self.frame_fecha.setMaximumSize(QSize(16777215, 90))
        self.frame_fecha.setStyleSheet(u"QDateEdit{\n"
"background-color: rgb(229, 229, 229);\n"
"}")
        self.frame_fecha.setFrameShape(QFrame.StyledPanel)
        self.frame_fecha.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_fecha)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_fecha)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(400, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_fecha)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(400, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.dateEdit_2 = QDateEdit(self.frame_fecha)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMaximumSize(QSize(400, 16777215))
        self.dateEdit_2.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit_2, 1, 1, 1, 1)

        self.fecha_desde = QDateEdit(self.frame_fecha)
        self.fecha_desde.setObjectName(u"fecha_desde")
        self.fecha_desde.setMaximumSize(QSize(400, 16777215))
        self.fecha_desde.setCalendarPopup(True)

        self.gridLayout.addWidget(self.fecha_desde, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_fecha)

        self.frame_observacion = QFrame(self.frame_datos)
        self.frame_observacion.setObjectName(u"frame_observacion")
        self.frame_observacion.setMinimumSize(QSize(0, 35))
        self.frame_observacion.setMaximumSize(QSize(16777215, 35))
        self.frame_observacion.setStyleSheet(u"\n"
"background-color: rgb(230, 229, 255);\n"
"color: rgb(0, 0, 0);")
        self.frame_observacion.setFrameShape(QFrame.StyledPanel)
        self.frame_observacion.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_observacion)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.frame_observacion)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_8.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_observacion)


        self.verticalLayout_6.addWidget(self.frame_datos)

        self.botones = QFrame(self.action_bar_frame_2)
        self.botones.setObjectName(u"botones")
        self.botones.setMinimumSize(QSize(0, 45))
        self.botones.setMaximumSize(QSize(16777215, 45))
        self.botones.setCursor(QCursor(Qt.PointingHandCursor))
        self.botones.setStyleSheet(u"")
        self.botones.setFrameShape(QFrame.StyledPanel)
        self.botones.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.botones)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.BTNIniciar = QPushButton(self.botones)
        self.BTNIniciar.setObjectName(u"BTNIniciar")
        self.BTNIniciar.setMinimumSize(QSize(0, 35))
        self.BTNIniciar.setMaximumSize(QSize(16777215, 35))
        self.BTNIniciar.setCursor(QCursor(Qt.PointingHandCursor))
        self.BTNIniciar.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.BTNIniciar)


        self.verticalLayout_6.addWidget(self.botones)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.footer = QFrame(self.action_bar_frame_2)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(0, 45))
        self.footer.setMaximumSize(QSize(16777215, 45))
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.error = QFrame(self.footer)
        self.error.setObjectName(u"error")
        self.error.setMinimumSize(QSize(800, 30))
        self.error.setMaximumSize(QSize(16777215, 30))
        self.error.setFrameShape(QFrame.StyledPanel)
        self.error.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.error)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.LabelError = QLabel(self.error)
        self.LabelError.setObjectName(u"LabelError")
        self.LabelError.setMinimumSize(QSize(0, 20))

        self.verticalLayout_5.addWidget(self.LabelError)


        self.horizontalLayout_2.addWidget(self.error)

        self.progress = QFrame(self.footer)
        self.progress.setObjectName(u"progress")
        self.progress.setMinimumSize(QSize(0, 30))
        self.progress.setMaximumSize(QSize(16777215, 30))
        self.progress.setFrameShape(QFrame.StyledPanel)
        self.progress.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.progress)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.PBEstado = QProgressBar(self.progress)
        self.PBEstado.setObjectName(u"PBEstado")
        self.PBEstado.setMinimumSize(QSize(0, 20))
        self.PBEstado.setMaximumSize(QSize(16777215, 20))
        self.PBEstado.setValue(0)

        self.horizontalLayout_3.addWidget(self.PBEstado)


        self.horizontalLayout_2.addWidget(self.progress)


        self.verticalLayout_6.addWidget(self.footer)


        self.verticalLayout_2.addWidget(self.action_bar_frame_2)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(UnionWindow)

        QMetaObject.connectSlotsByName(UnionWindow)
    # setupUi

    def retranslateUi(self, UnionWindow):
        UnionWindow.setWindowTitle(QCoreApplication.translate("UnionWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("UnionWindow", u"Bot-Bolsa de Valores de Asunci\u00f3n", None))
        self.minimize_button.setText(QCoreApplication.translate("UnionWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("UnionWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("UnionWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("UnionWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("UnionWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Seleccionar carpeta con archivos de la Bolsa de Valores</span></p></body></html>", None))
        self.LESeleccionarCarpeta.setPlaceholderText(QCoreApplication.translate("UnionWindow", u"Seleccionar carperta", None))
        self.BTNSeleccionar.setText(QCoreApplication.translate("UnionWindow", u"Seleccionar", None))
        self.label.setText(QCoreApplication.translate("UnionWindow", u"Desde", None))
        self.label_2.setText(QCoreApplication.translate("UnionWindow", u"Hasta", None))
        self.label_4.setText(QCoreApplication.translate("UnionWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">Tener en cuenta los d\u00edas en la fecha de inicio (desde), en la fecha final (hasta) puede superar al la \u00faltima fecha en la carpeta</span></p></body></html>", None))
        self.BTNIniciar.setText(QCoreApplication.translate("UnionWindow", u"Iniciar", None))
        self.LabelError.setText("")
    # retranslateUi

