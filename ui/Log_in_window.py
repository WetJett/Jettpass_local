# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Log_in_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import ui.icons

class Ui_Log_in_window(object):
    def setupUi(self, Log_in_window):
        if not Log_in_window.objectName():
            Log_in_window.setObjectName(u"Log_in_window")
        Log_in_window.resize(450, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Log_in_window.sizePolicy().hasHeightForWidth())
        Log_in_window.setSizePolicy(sizePolicy)
        Log_in_window.setMinimumSize(QSize(450, 400))
        Log_in_window.setMaximumSize(QSize(800, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icon_main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Log_in_window.setWindowIcon(icon)
        Log_in_window.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(141, 69, 195, 255), stop:0.427447 rgba(101, 121, 192, 235), stop:1 rgba(215, 139, 225, 255));\n"
"font-family: Microsoft YaHei UI")
        self.verticalLayout = QVBoxLayout(Log_in_window)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 20, 30, 30)
        self.label = QLabel(Log_in_window)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 20pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(15, 20, 15, 20)
        self.Login_lineEdit = QLineEdit(Log_in_window)
        self.Login_lineEdit.setObjectName(u"Login_lineEdit")
        self.Login_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")

        self.gridLayout.addWidget(self.Login_lineEdit, 1, 1, 1, 1)

        self.Pass_promt_lbl = QLabel(Log_in_window)
        self.Pass_promt_lbl.setObjectName(u"Pass_promt_lbl")
        self.Pass_promt_lbl.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color: white;")
        self.Pass_promt_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.Pass_promt_lbl, 2, 0, 1, 1)

        self.Password_lineEdit = QLineEdit(Log_in_window)
        self.Password_lineEdit.setObjectName(u"Password_lineEdit")
        self.Password_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.Password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.Password_lineEdit, 2, 1, 1, 1)

        self.login_promt_lbl = QLabel(Log_in_window)
        self.login_promt_lbl.setObjectName(u"login_promt_lbl")
        self.login_promt_lbl.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.login_promt_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.login_promt_lbl, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.LogInButton = QPushButton(Log_in_window)
        self.LogInButton.setObjectName(u"LogInButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LogInButton.sizePolicy().hasHeightForWidth())
        self.LogInButton.setSizePolicy(sizePolicy1)
        self.LogInButton.setMinimumSize(QSize(200, 50))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(14)
        font.setBold(True)
        self.LogInButton.setFont(font)
        self.LogInButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.LogInButton.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,90);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/login_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LogInButton.setIcon(icon1)
        self.LogInButton.setIconSize(QSize(26, 26))

        self.verticalLayout.addWidget(self.LogInButton)

        self.frame = QFrame(Log_in_window)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;")

        self.horizontalLayout.addWidget(self.label_2)

        self.Sign_up_Button = QPushButton(self.frame)
        self.Sign_up_Button.setObjectName(u"Sign_up_Button")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.Sign_up_Button.setFont(font1)
        self.Sign_up_Button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,90);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/person_add_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Sign_up_Button.setIcon(icon2)
        self.Sign_up_Button.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.Sign_up_Button)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Log_in_window)

        QMetaObject.connectSlotsByName(Log_in_window)
    # setupUi

    def retranslateUi(self, Log_in_window):
        Log_in_window.setWindowTitle(QCoreApplication.translate("Log_in_window", u"Log in", None))
        self.label.setText(QCoreApplication.translate("Log_in_window", u"Hi!", None))
        self.Pass_promt_lbl.setText(QCoreApplication.translate("Log_in_window", u" Password:", None))
        self.login_promt_lbl.setText(QCoreApplication.translate("Log_in_window", u"Login:", None))
        self.LogInButton.setText(QCoreApplication.translate("Log_in_window", u"Log in", None))
        self.label_2.setText(QCoreApplication.translate("Log_in_window", u"Don't have an account?", None))
        self.Sign_up_Button.setText(QCoreApplication.translate("Log_in_window", u" Sign up", None))
    # retranslateUi

