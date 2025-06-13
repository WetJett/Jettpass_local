# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Message_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import ui.icons

class Ui_Info_message(object):
    def setupUi(self, Info_message):
        if not Info_message.objectName():
            Info_message.setObjectName(u"Info_message")
        Info_message.resize(400, 250)
        Info_message.setMinimumSize(QSize(400, 250))
        Info_message.setMaximumSize(QSize(400, 250))
        icon = QIcon()
        icon.addFile(u":/icons/icon_main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Info_message.setWindowIcon(icon)
        Info_message.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(141, 69, 195, 255), stop:0.427447 rgba(101, 121, 192, 235), stop:1 rgba(215, 139, 225, 255));\n"
"font-family: Microsoft YaHei UI")
        self.verticalLayout = QVBoxLayout(Info_message)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Error_type_label = QLabel(Info_message)
        self.Error_type_label.setObjectName(u"Error_type_label")
        self.Error_type_label.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.Error_type_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Error_type_label)

        self.Message_label = QLabel(Info_message)
        self.Message_label.setObjectName(u"Message_label")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.Message_label.setFont(font)
        self.Message_label.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.Message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Message_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.frame = QFrame(Info_message)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:none;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.Ok_Button = QPushButton(Info_message)
        self.Ok_Button.setObjectName(u"Ok_Button")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.Ok_Button.setFont(font1)
        self.Ok_Button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,90);\n"
"}")
        self.Ok_Button.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.Ok_Button)

        self.frame_2 = QFrame(Info_message)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:none;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Info_message)

        QMetaObject.connectSlotsByName(Info_message)
    # setupUi

    def retranslateUi(self, Info_message):
        Info_message.setWindowTitle(QCoreApplication.translate("Info_message", u"Info", None))
        self.Error_type_label.setText(QCoreApplication.translate("Info_message", u"TextLabel", None))
        self.Message_label.setText(QCoreApplication.translate("Info_message", u"TextLabel", None))
        self.Ok_Button.setText(QCoreApplication.translate("Info_message", u"OK", None))
    # retranslateUi

