# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sign_up_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import ui.icons

class Ui_Sign_up_window(object):
    def setupUi(self, Sign_up_window):
        if not Sign_up_window.objectName():
            Sign_up_window.setObjectName(u"Sign_up_window")
        Sign_up_window.resize(500, 330)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Sign_up_window.sizePolicy().hasHeightForWidth())
        Sign_up_window.setSizePolicy(sizePolicy)
        Sign_up_window.setMinimumSize(QSize(500, 330))
        Sign_up_window.setMaximumSize(QSize(800, 332))
        icon = QIcon()
        icon.addFile(u":/icons/icon_main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Sign_up_window.setWindowIcon(icon)
        Sign_up_window.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(141, 69, 195, 255), stop:0.427447 rgba(101, 121, 192, 235), stop:1 rgba(215, 139, 225, 255));\n"
"font-family: Microsoft YaHei UI")
        self.verticalLayout = QVBoxLayout(Sign_up_window)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.label_4 = QLabel(Sign_up_window)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font: 700 20pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(-1, 10, -1, 10)
        self.label = QLabel(Sign_up_window)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.Retype_password_lineEdit = QLineEdit(Sign_up_window)
        self.Retype_password_lineEdit.setObjectName(u"Retype_password_lineEdit")
        self.Retype_password_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.Retype_password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.Retype_password_lineEdit, 2, 1, 1, 1)

        self.label_3 = QLabel(Sign_up_window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.Password_lineEdit = QLineEdit(Sign_up_window)
        self.Password_lineEdit.setObjectName(u"Password_lineEdit")
        self.Password_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.Password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.Password_lineEdit, 1, 1, 1, 1)

        self.label_2 = QLabel(Sign_up_window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.Login_lineEdit = QLineEdit(Sign_up_window)
        self.Login_lineEdit.setObjectName(u"Login_lineEdit")
        self.Login_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")

        self.gridLayout.addWidget(self.Login_lineEdit, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton = QPushButton(Sign_up_window)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,90);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/person_add_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(26, 26))

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Sign_up_window)

        QMetaObject.connectSlotsByName(Sign_up_window)
    # setupUi

    def retranslateUi(self, Sign_up_window):
        Sign_up_window.setWindowTitle(QCoreApplication.translate("Sign_up_window", u"Sign up", None))
        self.label_4.setText(QCoreApplication.translate("Sign_up_window", u"Almost there!", None))
        self.label.setText(QCoreApplication.translate("Sign_up_window", u"Login:", None))
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("Sign_up_window", u"<html><head/><body><p>font: 700 14pt &quot;Microsoft YaHei UI&quot;;</p><p>background-color: none;</p><p>color:white;</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("Sign_up_window", u"Retype password:", None))
        self.label_2.setText(QCoreApplication.translate("Sign_up_window", u"Password:", None))
        self.pushButton.setText(QCoreApplication.translate("Sign_up_window", u" Sign up", None))
    # retranslateUi

