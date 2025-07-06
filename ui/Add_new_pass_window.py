# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add_new_pass_window.ui'
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

class Ui_Add_new_pass_window(object):
    def setupUi(self, Add_new_pass_window):
        if not Add_new_pass_window.objectName():
            Add_new_pass_window.setObjectName(u"Add_new_pass_window")
        Add_new_pass_window.resize(600, 440)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Add_new_pass_window.sizePolicy().hasHeightForWidth())
        Add_new_pass_window.setSizePolicy(sizePolicy)
        Add_new_pass_window.setMinimumSize(QSize(600, 440))
        Add_new_pass_window.setMaximumSize(QSize(900, 440))
        Add_new_pass_window.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        icon = QIcon()
        icon.addFile(u":/icons/icon_main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Add_new_pass_window.setWindowIcon(icon)
        Add_new_pass_window.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(141, 69, 195, 255), stop:0.427447 rgba(101, 121, 192, 235), stop:1 rgba(215, 139, 225, 255));\n"
"font-family: Microsoft YaHei UI")
        self.verticalLayout = QVBoxLayout(Add_new_pass_window)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.label_4 = QLabel(Add_new_pass_window)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 20pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(-1, 10, -1, 10)
        self.label_2 = QLabel(Add_new_pass_window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.Login_lineEdit = QLineEdit(Add_new_pass_window)
        self.Login_lineEdit.setObjectName(u"Login_lineEdit")
        self.Login_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 14pt \"Microsoft YaHei UI\";\n"
"color:white;")

        self.gridLayout.addWidget(self.Login_lineEdit, 1, 1, 1, 1)

        self.label_3 = QLabel(Add_new_pass_window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.Password_lineEdit = QLineEdit(Add_new_pass_window)
        self.Password_lineEdit.setObjectName(u"Password_lineEdit")
        self.Password_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 14pt \"Microsoft YaHei UI\";\n"
"color:white;")

        self.gridLayout.addWidget(self.Password_lineEdit, 2, 1, 1, 1)

        self.label = QLabel(Add_new_pass_window)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.Alias_lineEdit = QLineEdit(Add_new_pass_window)
        self.Alias_lineEdit.setObjectName(u"Alias_lineEdit")
        self.Alias_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 14pt \"Microsoft YaHei UI\";\n"
"color:white;")

        self.gridLayout.addWidget(self.Alias_lineEdit, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label_5 = QLabel(Add_new_pass_window)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"height:40px;\n"
"color:white;\n"
"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Add_new_pass_window)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:none;\n"
"height:40px;" "\n border: 5px solid white;")
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(1)

        self.horizontalLayout.addWidget(self.frame)

        self.Generator_Button = QPushButton(Add_new_pass_window)
        self.Generator_Button.setObjectName(u"Generator_Button")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.Generator_Button.setFont(font)
        self.Generator_Button.setStyleSheet(u"QPushButton{\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/wand_stars_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Generator_Button.setIcon(icon1)
        self.Generator_Button.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.Generator_Button)

        self.frame_2 = QFrame(Add_new_pass_window)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:none;\n"
"height:40px;" "\n border: 5px solid white;")
        self.frame_2.setFrameShape(QFrame.Shape.HLine)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Save_Button = QPushButton(Add_new_pass_window)
        self.Save_Button.setObjectName(u"Save_Button")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.Save_Button.setFont(font1)
        self.Save_Button.setStyleSheet(u"QPushButton{\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/save_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Save_Button.setIcon(icon2)
        self.Save_Button.setIconSize(QSize(26, 26))

        self.horizontalLayout_2.addWidget(self.Save_Button)

        self.Cancel_Button = QPushButton(Add_new_pass_window)
        self.Cancel_Button.setObjectName(u"Cancel_Button")
        self.Cancel_Button.setFont(font1)
        self.Cancel_Button.setStyleSheet(u"QPushButton{\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/close_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Cancel_Button.setIcon(icon3)
        self.Cancel_Button.setIconSize(QSize(26, 26))

        self.horizontalLayout_2.addWidget(self.Cancel_Button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Add_new_pass_window)

        QMetaObject.connectSlotsByName(Add_new_pass_window)
    # setupUi

    def retranslateUi(self, Add_new_pass_window):
        Add_new_pass_window.setWindowTitle(QCoreApplication.translate("Add_new_pass_window", u"Add new password", None))
        self.label_4.setText(QCoreApplication.translate("Add_new_pass_window", u"Add new password entry", None))
        self.label_2.setText(QCoreApplication.translate("Add_new_pass_window", u"Login / email:", None))
        self.label_3.setText(QCoreApplication.translate("Add_new_pass_window", u"Password:", None))
        self.label.setText(QCoreApplication.translate("Add_new_pass_window", u"Alias for entry:", None))
        self.label_5.setText(QCoreApplication.translate("Add_new_pass_window", u"<html><head/><body><p>You can also use password generator to make a strong one</p></body></html>", None))
        self.Generator_Button.setText(QCoreApplication.translate("Add_new_pass_window", u"Generator", None))
        self.Save_Button.setText(QCoreApplication.translate("Add_new_pass_window", u"Save new entry", None))
        self.Cancel_Button.setText(QCoreApplication.translate("Add_new_pass_window", u"Cancel", None))
    # retranslateUi

