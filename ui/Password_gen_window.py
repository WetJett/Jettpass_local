# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Password_gen_window.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)
import ui.icons

class Ui_Pass_gen_window(object):
    def setupUi(self, Pass_gen_window):
        if not Pass_gen_window.objectName():
            Pass_gen_window.setObjectName(u"Pass_gen_window")
        Pass_gen_window.resize(500, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Pass_gen_window.sizePolicy().hasHeightForWidth())
        Pass_gen_window.setSizePolicy(sizePolicy)
        Pass_gen_window.setMinimumSize(QSize(500, 300))
        Pass_gen_window.setMaximumSize(QSize(700, 400))
        icon = QIcon()
        icon.addFile(u":/icons/icon_main.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Pass_gen_window.setWindowIcon(icon)
        Pass_gen_window.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(141, 69, 195, 255), stop:0.427447 rgba(101, 121, 192, 235), stop:1 rgba(215, 139, 225, 255));\n"
"font-family: Microsoft YaHei UI")
        self.verticalLayout = QVBoxLayout(Pass_gen_window)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.label = QLabel(Pass_gen_window)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 20pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 15, -1, -1)
        self.Password_lineEdit = QLineEdit(Pass_gen_window)
        self.Password_lineEdit.setObjectName(u"Password_lineEdit")
        self.Password_lineEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Password_lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"font: 700 14pt \"Microsoft YaHei UI\";\n"
"color:white;")

        self.horizontalLayout.addWidget(self.Password_lineEdit)

        self.Copy_Button = QPushButton(Pass_gen_window)
        self.Copy_Button.setObjectName(u"Copy_Button")
        self.Copy_Button.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"height: 30px;\n"
"width: 40px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,90);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/content_copy_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Copy_Button.setIcon(icon1)
        self.Copy_Button.setIconSize(QSize(26, 26))

        self.horizontalLayout.addWidget(self.Copy_Button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Pass_gen_window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"background-color: none;\n"
"color:white;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.frame = QFrame(Pass_gen_window)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: none;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame)

        self.Num_of_chars_Box = QSpinBox(Pass_gen_window)
        self.Num_of_chars_Box.setObjectName(u"Num_of_chars_Box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Num_of_chars_Box.sizePolicy().hasHeightForWidth())
        self.Num_of_chars_Box.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(12)
        font.setBold(True)
        self.Num_of_chars_Box.setFont(font)
        self.Num_of_chars_Box.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"border-radius: 4px;\n"
"\n"
"width: 25px;\n"
"height: 30px;\n"
"color:white;")
        self.Num_of_chars_Box.setMinimum(8)
        self.Num_of_chars_Box.setMaximum(50)
        self.Num_of_chars_Box.setValue(15)

        self.horizontalLayout_2.addWidget(self.Num_of_chars_Box)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.frame_2 = QFrame(Pass_gen_window)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: none;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Pass_gen_button = QPushButton(Pass_gen_window)
        self.Pass_gen_button.setObjectName(u"Pass_gen_button")
        self.Pass_gen_button.setFont(font)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/wand_stars_24dp_E3E3E3_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Pass_gen_button.setIcon(icon2)
        self.Pass_gen_button.setIconSize(QSize(26, 26))

        self.horizontalLayout_3.addWidget(self.Pass_gen_button)

        self.Back_to_main_button = QPushButton(Pass_gen_window)
        self.Back_to_main_button.setObjectName(u"Back_to_main_button")
        self.Back_to_main_button.setFont(font)
        self.Back_to_main_button.setStyleSheet(u"QPushButton{\n"
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
        self.Back_to_main_button.setIcon(icon3)
        self.Back_to_main_button.setIconSize(QSize(26, 26))

        self.horizontalLayout_3.addWidget(self.Back_to_main_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Pass_gen_window)

        QMetaObject.connectSlotsByName(Pass_gen_window)
    # setupUi

    def retranslateUi(self, Pass_gen_window):
        Pass_gen_window.setWindowTitle(QCoreApplication.translate("Pass_gen_window", u"Password generator", None))
        self.label.setText(QCoreApplication.translate("Pass_gen_window", u"Password generator", None))
        self.Password_lineEdit.setPlaceholderText(QCoreApplication.translate("Pass_gen_window", u"Password will appear here...", None))
        self.Copy_Button.setText("")
        self.label_2.setText(QCoreApplication.translate("Pass_gen_window", u"Number of characters:", None))
        self.Pass_gen_button.setText(QCoreApplication.translate("Pass_gen_window", u"Generate", None))
        self.Back_to_main_button.setText(QCoreApplication.translate("Pass_gen_window", u"Back", None))
    # retranslateUi

