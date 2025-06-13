# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Warning_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import ui.icons

class Ui_Warning_window(object):
    def setupUi(self, Warning_window):
        if not Warning_window.objectName():
            Warning_window.setObjectName(u"Warning_window")
        Warning_window.resize(400, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Warning_window.sizePolicy().hasHeightForWidth())
        Warning_window.setSizePolicy(sizePolicy)
        Warning_window.setMinimumSize(QSize(400, 250))
        icon = QIcon()
        icon.addFile(u":/icons/icon_main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Warning_window.setWindowIcon(icon)
        Warning_window.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(141, 69, 195, 255), stop:0.427447 rgba(101, 121, 192, 235), stop:1 rgba(215, 139, 225, 255));\n"
"font-family: Microsoft YaHei UI")
        self.verticalLayout = QVBoxLayout(Warning_window)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.Warning_label = QLabel(Warning_window)
        self.Warning_label.setObjectName(u"Warning_label")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.Warning_label.setFont(font)
        self.Warning_label.setStyleSheet(u"font: 700 20pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.Warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Warning_label)

        self.Message_label = QLabel(Warning_window)
        self.Message_label.setObjectName(u"Message_label")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.Message_label.setFont(font1)
        self.Message_label.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.Message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Message_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.Message_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.Ok_Button = QPushButton(Warning_window)
        self.Ok_Button.setObjectName(u"Ok_Button")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.Ok_Button.setFont(font2)
        self.Ok_Button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgba(255,0,0,30);\n"
"border: 1px solid rgba(255,0,0,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,0,0,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,0,0,90);\n"
"}")
        self.Ok_Button.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.Ok_Button)

        self.Cancel_Button = QPushButton(Warning_window)
        self.Cancel_Button.setObjectName(u"Cancel_Button")
        self.Cancel_Button.setFont(font2)
        self.Cancel_Button.setStyleSheet(u"QPushButton{\n"
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
        self.Cancel_Button.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.Cancel_Button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Warning_window)

        QMetaObject.connectSlotsByName(Warning_window)
    # setupUi

    def retranslateUi(self, Warning_window):
        Warning_window.setWindowTitle(QCoreApplication.translate("Warning_window", u"WARNING", None))
        self.Warning_label.setText(QCoreApplication.translate("Warning_window", u"WARNING", None))
        self.Message_label.setText(QCoreApplication.translate("Warning_window", u"TextLabel", None))
        self.Ok_Button.setText(QCoreApplication.translate("Warning_window", u"OK", None))
        self.Cancel_Button.setText(QCoreApplication.translate("Warning_window", u"Cancel", None))
    # retranslateUi

