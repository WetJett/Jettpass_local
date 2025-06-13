# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'M_pass_change_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import ui.icons

class Ui_Change_m_pass_window(object):
    def setupUi(self, Change_m_pass_window):
        if not Change_m_pass_window.objectName():
            Change_m_pass_window.setObjectName(u"Change_m_pass_window")
        Change_m_pass_window.resize(600, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Change_m_pass_window.sizePolicy().hasHeightForWidth())
        Change_m_pass_window.setSizePolicy(sizePolicy)
        Change_m_pass_window.setMinimumSize(QSize(600, 360))
        Change_m_pass_window.setMaximumSize(QSize(16777215, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icon_main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Change_m_pass_window.setWindowIcon(icon)
        Change_m_pass_window.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(141, 69, 195, 255), stop:0.427447 rgba(101, 121, 192, 235), stop:1 rgba(215, 139, 225, 255));\n"
"font-family: Microsoft YaHei UI")
        self.verticalLayout = QVBoxLayout(Change_m_pass_window)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 15, 30, 30)
        self.label_4 = QLabel(Change_m_pass_window)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setStyleSheet(u"font: 700 18pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.Old_pass_lineEdit = QLineEdit(Change_m_pass_window)
        self.Old_pass_lineEdit.setObjectName(u"Old_pass_lineEdit")
        self.Old_pass_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.Old_pass_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.Old_pass_lineEdit, 0, 1, 1, 1)

        self.New_pass_ret_lineEdit = QLineEdit(Change_m_pass_window)
        self.New_pass_ret_lineEdit.setObjectName(u"New_pass_ret_lineEdit")
        self.New_pass_ret_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.New_pass_ret_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.New_pass_ret_lineEdit, 2, 1, 1, 1)

        self.label_2 = QLabel(Change_m_pass_window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.New_pass_lineEdit = QLineEdit(Change_m_pass_window)
        self.New_pass_lineEdit.setObjectName(u"New_pass_lineEdit")
        self.New_pass_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 12pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.New_pass_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.New_pass_lineEdit, 1, 1, 1, 1)

        self.label_3 = QLabel(Change_m_pass_window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(Change_m_pass_window)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Change_button = QPushButton(Change_m_pass_window)
        self.Change_button.setObjectName(u"Change_button")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(14)
        font.setBold(True)
        self.Change_button.setFont(font)
        self.Change_button.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u":/icons/edit_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Change_button.setIcon(icon1)
        self.Change_button.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.Change_button)

        self.Cancel_button = QPushButton(Change_m_pass_window)
        self.Cancel_button.setObjectName(u"Cancel_button")
        self.Cancel_button.setFont(font)
        self.Cancel_button.setStyleSheet(u"QPushButton{\n"
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
        icon2.addFile(u":/icons/close_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Cancel_button.setIcon(icon2)
        self.Cancel_button.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.Cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Change_m_pass_window)

        QMetaObject.connectSlotsByName(Change_m_pass_window)
    # setupUi

    def retranslateUi(self, Change_m_pass_window):
        Change_m_pass_window.setWindowTitle(QCoreApplication.translate("Change_m_pass_window", u"Change master password", None))
        self.label_4.setText(QCoreApplication.translate("Change_m_pass_window", u"Changing master password for account", None))
        self.Old_pass_lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("Change_m_pass_window", u"New password:", None))
        self.label_3.setText(QCoreApplication.translate("Change_m_pass_window", u"Retype new password:", None))
        self.label.setText(QCoreApplication.translate("Change_m_pass_window", u"Old password:", None))
        self.Change_button.setText(QCoreApplication.translate("Change_m_pass_window", u"Change", None))
        self.Cancel_button.setText(QCoreApplication.translate("Change_m_pass_window", u"Cancel", None))
    # retranslateUi

