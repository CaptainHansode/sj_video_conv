# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'probe_result_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 810)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_textEdit = QTextEdit(Dialog)
        self.result_textEdit.setObjectName(u"result_textEdit")

        self.verticalLayout.addWidget(self.result_textEdit)

        self.close_bt = QPushButton(Dialog)
        self.close_bt.setObjectName(u"close_bt")

        self.verticalLayout.addWidget(self.close_bt)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.close_bt.setText(QCoreApplication.translate("Dialog", u"\u9589\u3058\u308b", None))
    # retranslateUi

