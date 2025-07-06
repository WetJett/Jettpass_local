# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'View_Edit_entry_window.ui'
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

class Ui_View_Edit_entry_window(object):
    def setupUi(self, View_Edit_entry_window):
        if not View_Edit_entry_window.objectName():
            View_Edit_entry_window.setObjectName(u"View_Edit_entry_window")
        View_Edit_entry_window.resize(510, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(View_Edit_entry_window.sizePolicy().hasHeightForWidth())
        View_Edit_entry_window.setSizePolicy(sizePolicy)
        View_Edit_entry_window.setMinimumSize(QSize(510, 350))
        View_Edit_entry_window.setMaximumSize(QSize(900, 350))
        icon = QIcon()
        icon.addFile(u":/icons/icon_main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        View_Edit_entry_window.setWindowIcon(icon)
        View_Edit_entry_window.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(141, 69, 195, 255), stop:0.427447 rgba(101, 121, 192, 235), stop:1 rgba(215, 139, 225, 255));\n"
"font-family: Microsoft YaHei UI")
        self.verticalLayout = QVBoxLayout(View_Edit_entry_window)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.label_3 = QLabel(View_Edit_entry_window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 20pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(View_Edit_entry_window)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.Login_lineEdit = QLineEdit(View_Edit_entry_window)
        self.Login_lineEdit.setObjectName(u"Login_lineEdit")
        self.Login_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 14pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.Login_lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.Login_lineEdit, 0, 1, 1, 1)

        self.Login_copy_Button = QPushButton(View_Edit_entry_window)
        self.Login_copy_Button.setObjectName(u"Login_copy_Button")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(14)
        font.setBold(True)
        self.Login_copy_Button.setFont(font)
        self.Login_copy_Button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"width:30px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,90);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/content_copy_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Login_copy_Button.setIcon(icon1)
        self.Login_copy_Button.setIconSize(QSize(26, 26))

        self.gridLayout.addWidget(self.Login_copy_Button, 0, 2, 1, 1)

        self.label_2 = QLabel(View_Edit_entry_window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.Password_lineEdit = QLineEdit(View_Edit_entry_window)
        self.Password_lineEdit.setObjectName(u"Password_lineEdit")
        self.Password_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 14pt \"Microsoft YaHei UI\";\n"
"color:white;")
        self.Password_lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.Password_lineEdit, 1, 1, 1, 1)

        self.Password_copy_Button = QPushButton(View_Edit_entry_window)
        self.Password_copy_Button.setObjectName(u"Password_copy_Button")
        self.Password_copy_Button.setFont(font)
        self.Password_copy_Button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"width:30px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,90);\n"
"}")
        self.Password_copy_Button.setIcon(icon1)
        self.Password_copy_Button.setIconSize(QSize(26, 26))

        self.gridLayout.addWidget(self.Password_copy_Button, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Edit_Button = QPushButton(View_Edit_entry_window)
        self.Edit_Button.setObjectName(u"Edit_Button")
        self.Edit_Button.setFont(font)
        self.Edit_Button.setStyleSheet(u"QPushButton{\n"
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
        self.Edit_Button.setIcon(icon2)
        self.Edit_Button.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.Edit_Button)

        self.Save_Button = QPushButton(View_Edit_entry_window)
        self.Save_Button.setObjectName(u"Save_Button")
        self.Save_Button.setFont(font)
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/save_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Save_Button.setIcon(icon3)
        self.Save_Button.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.Save_Button)

        self.Delete_Button = QPushButton(View_Edit_entry_window)
        self.Delete_Button.setObjectName(u"Delete_Button")
        self.Delete_Button.setFont(font)
        self.Delete_Button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 2px solid rgba(255,0,0,60);\n"
"border-radius: 4px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,0,0,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,0,0,90);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/delete_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Delete_Button.setIcon(icon4)
        self.Delete_Button.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.Delete_Button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(View_Edit_entry_window)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:none;" "\n border: 5px solid white;")
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame)

        self.Back_Button = QPushButton(View_Edit_entry_window)
        self.Back_Button.setObjectName(u"Back_Button")
        self.Back_Button.setFont(font)
        self.Back_Button.setStyleSheet(u"QPushButton{\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/close_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Back_Button.setIcon(icon5)
        self.Back_Button.setIconSize(QSize(26, 26))

        self.horizontalLayout_2.addWidget(self.Back_Button)

        self.frame_2 = QFrame(View_Edit_entry_window)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:none;" "\n border: 5px solid white;")
        self.frame_2.setFrameShape(QFrame.Shape.HLine)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(View_Edit_entry_window)

        QMetaObject.connectSlotsByName(View_Edit_entry_window)
    # setupUi

    def retranslateUi(self, View_Edit_entry_window):
        View_Edit_entry_window.setWindowTitle(QCoreApplication.translate("View_Edit_entry_window", u"View/edit entry", None))
        self.label_3.setText(QCoreApplication.translate("View_Edit_entry_window", u"View / Edit password entry", None))
        self.label.setText(QCoreApplication.translate("View_Edit_entry_window", u"Login/email:", None))
        self.Login_lineEdit.setInputMask("")
        self.Login_copy_Button.setText("")
        self.label_2.setText(QCoreApplication.translate("View_Edit_entry_window", u"Password:", None))
        self.Password_copy_Button.setText("")
        self.Edit_Button.setText(QCoreApplication.translate("View_Edit_entry_window", u"Edit", None))
        self.Save_Button.setText(QCoreApplication.translate("View_Edit_entry_window", u"Save", None))
        self.Delete_Button.setText(QCoreApplication.translate("View_Edit_entry_window", u"Delete ", None))
        self.Back_Button.setText(QCoreApplication.translate("View_Edit_entry_window", u"Back", None))
    # retranslateUi

