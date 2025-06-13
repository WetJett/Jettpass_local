# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_win.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import ui.icons

class Ui_Jettpass(object):
    def setupUi(self, Jettpass):
        if not Jettpass.objectName():
            Jettpass.setObjectName(u"Jettpass")
        Jettpass.resize(800, 600)
        Jettpass.setMinimumSize(QSize(750, 530))
        Jettpass.setBaseSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/icons/icon_main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Jettpass.setWindowIcon(icon)
        Jettpass.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(141, 69, 195, 255), stop:0.427447 rgba(101, 121, 192, 235), stop:1 rgba(215, 139, 225, 255));\n"
"font-family: Microsoft YaHei UI")
        self.centralwidget = QWidget(Jettpass)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.search_LineEdit = QLineEdit(self.centralwidget)
        self.search_LineEdit.setObjectName(u"search_LineEdit")
        self.search_LineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")

        self.verticalLayout_3.addWidget(self.search_LineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.listView.setFont(font)
        self.listView.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 7px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")

        self.horizontalLayout_2.addWidget(self.listView)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Add_pass_button = QPushButton(self.centralwidget)
        self.Add_pass_button.setObjectName(u"Add_pass_button")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.Add_pass_button.setFont(font1)
        self.Add_pass_button.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u":/icons/add_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Add_pass_button.setIcon(icon1)
        self.Add_pass_button.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.Add_pass_button)

        self.Change_m_pass_button = QPushButton(self.centralwidget)
        self.Change_m_pass_button.setObjectName(u"Change_m_pass_button")
        self.Change_m_pass_button.setFont(font1)
        self.Change_m_pass_button.setStyleSheet(u"QPushButton{\n"
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
        icon2.addFile(u":/icons/edit_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Change_m_pass_button.setIcon(icon2)
        self.Change_m_pass_button.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.Change_m_pass_button)

        self.Pass_gen_button = QPushButton(self.centralwidget)
        self.Pass_gen_button.setObjectName(u"Pass_gen_button")
        self.Pass_gen_button.setFont(font1)
        self.Pass_gen_button.setStyleSheet(u"QPushButton{\n"
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
        icon3.addFile(u":/icons/key_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Pass_gen_button.setIcon(icon3)
        self.Pass_gen_button.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.Pass_gen_button)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:none")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.Log_out_button = QPushButton(self.centralwidget)
        self.Log_out_button.setObjectName(u"Log_out_button")
        self.Log_out_button.setFont(font1)
        self.Log_out_button.setStyleSheet(u"QPushButton{\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/logout_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Log_out_button.setIcon(icon4)
        self.Log_out_button.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.Log_out_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        Jettpass.setCentralWidget(self.centralwidget)

        self.retranslateUi(Jettpass)

        QMetaObject.connectSlotsByName(Jettpass)
    # setupUi

    def retranslateUi(self, Jettpass):
        Jettpass.setWindowTitle(QCoreApplication.translate("Jettpass", u"Jettpass", None))
        self.search_LineEdit.setPlaceholderText(QCoreApplication.translate("Jettpass", u"Type alias here to search...", None))
        self.Add_pass_button.setText(QCoreApplication.translate("Jettpass", u"Add new password", None))
        self.Change_m_pass_button.setText(QCoreApplication.translate("Jettpass", u"Change master password ", None))
        self.Pass_gen_button.setText(QCoreApplication.translate("Jettpass", u"Password gererator", None))
        self.Log_out_button.setText(QCoreApplication.translate("Jettpass", u"Log out", None))
    # retranslateUi

