# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sj_video_conv_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(443, 984)
        icon = QIcon()
        icon.addFile(u"images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(24, 24))
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAbout_FFMpeg = QAction(MainWindow)
        self.actionAbout_FFMpeg.setObjectName(u"actionAbout_FFMpeg")
        self.action_about_ffmpeg = QAction(MainWindow)
        self.action_about_ffmpeg.setObjectName(u"action_about_ffmpeg")
        self.action_about_me = QAction(MainWindow)
        self.action_about_me.setObjectName(u"action_about_me")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.groupBox_4 = QGroupBox(self.splitter)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font = QFont()
        font.setFamily(u"Yu Gothic UI")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 12, 9, 9)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.list_item_explorer_bt = QPushButton(self.groupBox_4)
        self.list_item_explorer_bt.setObjectName(u"list_item_explorer_bt")
        self.list_item_explorer_bt.setMinimumSize(QSize(0, 0))
        self.list_item_explorer_bt.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.list_item_explorer_bt)

        self.del_sel_bt = QPushButton(self.groupBox_4)
        self.del_sel_bt.setObjectName(u"del_sel_bt")
        self.del_sel_bt.setMinimumSize(QSize(0, 0))
        self.del_sel_bt.setMaximumSize(QSize(32, 32))
        self.del_sel_bt.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.del_sel_bt)

        self.del_all_bt = QPushButton(self.groupBox_4)
        self.del_all_bt.setObjectName(u"del_all_bt")
        self.del_all_bt.setMinimumSize(QSize(0, 0))
        self.del_all_bt.setMaximumSize(QSize(32, 32))
        self.del_all_bt.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.del_all_bt)

        self.move_down_item_bt = QPushButton(self.groupBox_4)
        self.move_down_item_bt.setObjectName(u"move_down_item_bt")
        self.move_down_item_bt.setMinimumSize(QSize(0, 0))
        self.move_down_item_bt.setMaximumSize(QSize(32, 32))
        self.move_down_item_bt.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.move_down_item_bt)

        self.move_up_item_bt = QPushButton(self.groupBox_4)
        self.move_up_item_bt.setObjectName(u"move_up_item_bt")
        self.move_up_item_bt.setMinimumSize(QSize(0, 0))
        self.move_up_item_bt.setMaximumSize(QSize(32, 32))
        self.move_up_item_bt.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.move_up_item_bt)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, -1, -1, 6)
        self.filter_le = QLineEdit(self.groupBox_4)
        self.filter_le.setObjectName(u"filter_le")

        self.horizontalLayout_23.addWidget(self.filter_le)

        self.del_filter_bt = QPushButton(self.groupBox_4)
        self.del_filter_bt.setObjectName(u"del_filter_bt")
        self.del_filter_bt.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_23.addWidget(self.del_filter_bt)


        self.verticalLayout_4.addLayout(self.horizontalLayout_23)

        self.video_table = QTableWidget(self.groupBox_4)
        if (self.video_table.columnCount() < 2):
            self.video_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.video_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.video_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.video_table.setObjectName(u"video_table")
        self.video_table.setEnabled(True)
        self.video_table.setAutoScroll(False)
        self.video_table.horizontalHeader().setCascadingSectionResizes(False)
        self.video_table.horizontalHeader().setStretchLastSection(True)
        self.video_table.verticalHeader().setVisible(False)

        self.verticalLayout_4.addWidget(self.video_table)

        self.file_list_view = QListView(self.groupBox_4)
        self.file_list_view.setObjectName(u"file_list_view")

        self.verticalLayout_4.addWidget(self.file_list_view)

        self.video_list = QListWidget(self.groupBox_4)
        self.video_list.setObjectName(u"video_list")
        self.video_list.setMaximumSize(QSize(16777215, 64))
        self.video_list.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.video_list)

        self.probe_bt = QPushButton(self.groupBox_4)
        self.probe_bt.setObjectName(u"probe_bt")

        self.verticalLayout_4.addWidget(self.probe_bt)

        self.splitter.addWidget(self.groupBox_4)
        self.overall_op_groupBox = QGroupBox(self.splitter)
        self.overall_op_groupBox.setObjectName(u"overall_op_groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overall_op_groupBox.sizePolicy().hasHeightForWidth())
        self.overall_op_groupBox.setSizePolicy(sizePolicy)
        self.overall_op_groupBox.setMinimumSize(QSize(0, 0))
        self.overall_op_groupBox.setMaximumSize(QSize(16777215, 230))
        self.overall_op_groupBox.setFont(font)
        self.overall_op_groupBox.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.overall_op_groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 12, 9, 9)
        self.resize_checkBox = QCheckBox(self.overall_op_groupBox)
        self.resize_checkBox.setObjectName(u"resize_checkBox")
        self.resize_checkBox.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_8.addWidget(self.resize_checkBox)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.size_template_c_Label = QLabel(self.overall_op_groupBox)
        self.size_template_c_Label.setObjectName(u"size_template_c_Label")
        self.size_template_c_Label.setEnabled(False)
        self.size_template_c_Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.size_template_c_Label)

        self.size_template_comboBox = QComboBox(self.overall_op_groupBox)
        self.size_template_comboBox.addItem("")
        self.size_template_comboBox.addItem("")
        self.size_template_comboBox.addItem("")
        self.size_template_comboBox.addItem("")
        self.size_template_comboBox.addItem("")
        self.size_template_comboBox.addItem("")
        self.size_template_comboBox.addItem("")
        self.size_template_comboBox.addItem("")
        self.size_template_comboBox.addItem("")
        self.size_template_comboBox.setObjectName(u"size_template_comboBox")
        self.size_template_comboBox.setEnabled(False)

        self.horizontalLayout_17.addWidget(self.size_template_comboBox)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.resolution_x_label = QLabel(self.overall_op_groupBox)
        self.resolution_x_label.setObjectName(u"resolution_x_label")
        self.resolution_x_label.setEnabled(False)
        self.resolution_x_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.resolution_x_label)

        self.resolution_x_sp = QSpinBox(self.overall_op_groupBox)
        self.resolution_x_sp.setObjectName(u"resolution_x_sp")
        self.resolution_x_sp.setEnabled(False)
        self.resolution_x_sp.setMinimum(360)
        self.resolution_x_sp.setMaximum(12800)
        self.resolution_x_sp.setValue(1280)

        self.horizontalLayout_9.addWidget(self.resolution_x_sp)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.resolution_y_label = QLabel(self.overall_op_groupBox)
        self.resolution_y_label.setObjectName(u"resolution_y_label")
        self.resolution_y_label.setEnabled(False)
        self.resolution_y_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.resolution_y_label)

        self.resolution_y_sp = QSpinBox(self.overall_op_groupBox)
        self.resolution_y_sp.setObjectName(u"resolution_y_sp")
        self.resolution_y_sp.setEnabled(False)
        self.resolution_y_sp.setMinimum(360)
        self.resolution_y_sp.setMaximum(12800)
        self.resolution_y_sp.setValue(720)

        self.horizontalLayout_8.addWidget(self.resolution_y_sp)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.overall_op_groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.tm_st_sp = QDoubleSpinBox(self.overall_op_groupBox)
        self.tm_st_sp.setObjectName(u"tm_st_sp")
        self.tm_st_sp.setDecimals(3)
        self.tm_st_sp.setMaximum(460800.000000000000000)
        self.tm_st_sp.setSingleStep(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.tm_st_sp)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(self.overall_op_groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.tm_ed_sp = QDoubleSpinBox(self.overall_op_groupBox)
        self.tm_ed_sp.setObjectName(u"tm_ed_sp")
        self.tm_ed_sp.setDecimals(3)
        self.tm_ed_sp.setMaximum(460800.000000000000000)
        self.tm_ed_sp.setSingleStep(0.100000000000000)

        self.horizontalLayout_7.addWidget(self.tm_ed_sp)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_22)

        self.splitter.addWidget(self.overall_op_groupBox)
        self.groupBox_3 = QGroupBox(self.splitter)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setMaximumSize(QSize(16777215, 100))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.specific_dir_checkBox = QCheckBox(self.groupBox_3)
        self.specific_dir_checkBox.setObjectName(u"specific_dir_checkBox")

        self.gridLayout.addWidget(self.specific_dir_checkBox, 0, 0, 1, 1)

        self.save_path_le = QLineEdit(self.groupBox_3)
        self.save_path_le.setObjectName(u"save_path_le")
        self.save_path_le.setEnabled(False)
        self.save_path_le.setStyleSheet(u"")

        self.gridLayout.addWidget(self.save_path_le, 0, 1, 1, 1)

        self.save_path_bt = QToolButton(self.groupBox_3)
        self.save_path_bt.setObjectName(u"save_path_bt")
        self.save_path_bt.setEnabled(False)
        self.save_path_bt.setMinimumSize(QSize(32, 32))
        self.save_path_bt.setMaximumSize(QSize(16777215, 16777215))
        self.save_path_bt.setBaseSize(QSize(0, 32))
        self.save_path_bt.setStyleSheet(u"")

        self.gridLayout.addWidget(self.save_path_bt, 0, 2, 1, 1)

        self.explorer_bt = QPushButton(self.groupBox_3)
        self.explorer_bt.setObjectName(u"explorer_bt")
        self.explorer_bt.setEnabled(False)
        self.explorer_bt.setMinimumSize(QSize(32, 32))
        self.explorer_bt.setMaximumSize(QSize(32, 16777215))
        self.explorer_bt.setStyleSheet(u"")
        self.explorer_bt.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.explorer_bt, 0, 3, 1, 1)

        self.overwrite_file_checkBox = QCheckBox(self.groupBox_3)
        self.overwrite_file_checkBox.setObjectName(u"overwrite_file_checkBox")
        self.overwrite_file_checkBox.setEnabled(False)
        self.overwrite_file_checkBox.setChecked(True)

        self.gridLayout.addWidget(self.overwrite_file_checkBox, 1, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_3)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMaximumSize(QSize(16777215, 240))
        font1 = QFont()
        font1.setFamily(u"Yu Gothic UI")
        font1.setPointSize(9)
        self.tabWidget.setFont(font1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mp4_groupBox = QGroupBox(self.tab)
        self.mp4_groupBox.setObjectName(u"mp4_groupBox")
        self.mp4_groupBox.setFont(font1)
        self.mp4_groupBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.mp4_groupBox)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.label_8 = QLabel(self.mp4_groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.mp4_codec_comboBox = QComboBox(self.mp4_groupBox)
        self.mp4_codec_comboBox.addItem("")
        self.mp4_codec_comboBox.addItem("")
        self.mp4_codec_comboBox.setObjectName(u"mp4_codec_comboBox")

        self.horizontalLayout_4.addWidget(self.mp4_codec_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(self.mp4_groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.mp4_pixformat_comboBox = QComboBox(self.mp4_groupBox)
        self.mp4_pixformat_comboBox.addItem("")
        self.mp4_pixformat_comboBox.addItem("")
        self.mp4_pixformat_comboBox.addItem("")
        self.mp4_pixformat_comboBox.addItem("")
        self.mp4_pixformat_comboBox.addItem("")
        self.mp4_pixformat_comboBox.setObjectName(u"mp4_pixformat_comboBox")

        self.horizontalLayout_5.addWidget(self.mp4_pixformat_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_7 = QLabel(self.mp4_groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.mp4_acodec_comboBox = QComboBox(self.mp4_groupBox)
        self.mp4_acodec_comboBox.addItem("")
        self.mp4_acodec_comboBox.addItem("")
        self.mp4_acodec_comboBox.addItem("")
        self.mp4_acodec_comboBox.addItem("")
        self.mp4_acodec_comboBox.setObjectName(u"mp4_acodec_comboBox")

        self.horizontalLayout.addWidget(self.mp4_acodec_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, -1, 0)
        self.label_18 = QLabel(self.mp4_groupBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_18)

        self.mp4_playbackspeed_sp = QDoubleSpinBox(self.mp4_groupBox)
        self.mp4_playbackspeed_sp.setObjectName(u"mp4_playbackspeed_sp")
        self.mp4_playbackspeed_sp.setDecimals(1)
        self.mp4_playbackspeed_sp.setMinimum(0.100000000000000)
        self.mp4_playbackspeed_sp.setMaximum(64.000000000000000)
        self.mp4_playbackspeed_sp.setSingleStep(0.100000000000000)
        self.mp4_playbackspeed_sp.setValue(1.000000000000000)

        self.horizontalLayout_20.addWidget(self.mp4_playbackspeed_sp)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.label_9 = QLabel(self.mp4_groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.mp4_compression_sp = QSpinBox(self.mp4_groupBox)
        self.mp4_compression_sp.setObjectName(u"mp4_compression_sp")
        self.mp4_compression_sp.setMaximum(48)

        self.horizontalLayout_6.addWidget(self.mp4_compression_sp)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.convert_mp4_bt = QPushButton(self.mp4_groupBox)
        self.convert_mp4_bt.setObjectName(u"convert_mp4_bt")
        self.convert_mp4_bt.setMinimumSize(QSize(0, 36))
        font2 = QFont()
        font2.setFamily(u"Yu Gothic UI")
        font2.setPointSize(10)
        self.convert_mp4_bt.setFont(font2)
        self.convert_mp4_bt.setStyleSheet(u"")
        self.convert_mp4_bt.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.convert_mp4_bt)


        self.verticalLayout_7.addWidget(self.mp4_groupBox)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.avi_groupBox = QGroupBox(self.tab_2)
        self.avi_groupBox.setObjectName(u"avi_groupBox")
        self.verticalLayout_9 = QVBoxLayout(self.avi_groupBox)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.label_10 = QLabel(self.avi_groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.avi_codec_comboBox = QComboBox(self.avi_groupBox)
        self.avi_codec_comboBox.addItem("")
        self.avi_codec_comboBox.addItem("")
        self.avi_codec_comboBox.setObjectName(u"avi_codec_comboBox")

        self.horizontalLayout_10.addWidget(self.avi_codec_comboBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.label_6 = QLabel(self.avi_groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_6)

        self.avi_pixformat_comboBox = QComboBox(self.avi_groupBox)
        self.avi_pixformat_comboBox.addItem("")
        self.avi_pixformat_comboBox.addItem("")
        self.avi_pixformat_comboBox.addItem("")
        self.avi_pixformat_comboBox.addItem("")
        self.avi_pixformat_comboBox.addItem("")
        self.avi_pixformat_comboBox.setObjectName(u"avi_pixformat_comboBox")

        self.horizontalLayout_11.addWidget(self.avi_pixformat_comboBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.label_11 = QLabel(self.avi_groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_11)

        self.avi_acodec_comboBox = QComboBox(self.avi_groupBox)
        self.avi_acodec_comboBox.addItem("")
        self.avi_acodec_comboBox.addItem("")
        self.avi_acodec_comboBox.addItem("")
        self.avi_acodec_comboBox.setObjectName(u"avi_acodec_comboBox")

        self.horizontalLayout_12.addWidget(self.avi_acodec_comboBox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.label_17 = QLabel(self.avi_groupBox)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_17)

        self.mjepg_compression_sp = QSpinBox(self.avi_groupBox)
        self.mjepg_compression_sp.setObjectName(u"mjepg_compression_sp")
        self.mjepg_compression_sp.setMaximum(32)

        self.horizontalLayout_18.addWidget(self.mjepg_compression_sp)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.convert_avi_bt = QPushButton(self.avi_groupBox)
        self.convert_avi_bt.setObjectName(u"convert_avi_bt")
        self.convert_avi_bt.setMinimumSize(QSize(0, 36))
        self.convert_avi_bt.setFont(font2)
        self.convert_avi_bt.setStyleSheet(u"")
        self.convert_avi_bt.setIconSize(QSize(24, 24))

        self.verticalLayout_9.addWidget(self.convert_avi_bt)


        self.verticalLayout_6.addWidget(self.avi_groupBox)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_2 = QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.png_groupBox = QGroupBox(self.tab_4)
        self.png_groupBox.setObjectName(u"png_groupBox")
        self.verticalLayout_12 = QVBoxLayout(self.png_groupBox)
        self.verticalLayout_12.setSpacing(4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(6, 6, 6, 6)
        self.png_autofps_checkBox = QCheckBox(self.png_groupBox)
        self.png_autofps_checkBox.setObjectName(u"png_autofps_checkBox")
        self.png_autofps_checkBox.setLayoutDirection(Qt.RightToLeft)
        self.png_autofps_checkBox.setChecked(True)

        self.verticalLayout_12.addWidget(self.png_autofps_checkBox)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.png_fps_lb = QLabel(self.png_groupBox)
        self.png_fps_lb.setObjectName(u"png_fps_lb")
        self.png_fps_lb.setEnabled(False)
        self.png_fps_lb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.png_fps_lb)

        self.png_fps_spinBox = QSpinBox(self.png_groupBox)
        self.png_fps_spinBox.setObjectName(u"png_fps_spinBox")
        self.png_fps_spinBox.setEnabled(False)
        self.png_fps_spinBox.setMinimum(4)
        self.png_fps_spinBox.setMaximum(60)
        self.png_fps_spinBox.setValue(30)

        self.horizontalLayout_16.addWidget(self.png_fps_spinBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.label_19 = QLabel(self.png_groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_19)

        self.frame_by_frame_format_comboBox = QComboBox(self.png_groupBox)
        self.frame_by_frame_format_comboBox.addItem("")
        self.frame_by_frame_format_comboBox.addItem("")
        self.frame_by_frame_format_comboBox.addItem("")
        self.frame_by_frame_format_comboBox.addItem("")
        self.frame_by_frame_format_comboBox.setObjectName(u"frame_by_frame_format_comboBox")

        self.horizontalLayout_21.addWidget(self.frame_by_frame_format_comboBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)

        self.convert_frame_by_frame_bt = QPushButton(self.png_groupBox)
        self.convert_frame_by_frame_bt.setObjectName(u"convert_frame_by_frame_bt")
        self.convert_frame_by_frame_bt.setMinimumSize(QSize(0, 36))
        self.convert_frame_by_frame_bt.setFont(font2)
        self.convert_frame_by_frame_bt.setStyleSheet(u"")
        self.convert_frame_by_frame_bt.setIconSize(QSize(24, 24))

        self.verticalLayout_12.addWidget(self.convert_frame_by_frame_bt)


        self.verticalLayout_2.addWidget(self.png_groupBox)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gif_groupBox = QGroupBox(self.tab_3)
        self.gif_groupBox.setObjectName(u"gif_groupBox")
        self.verticalLayout_11 = QVBoxLayout(self.gif_groupBox)
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.gif_autofps_checkBox = QCheckBox(self.gif_groupBox)
        self.gif_autofps_checkBox.setObjectName(u"gif_autofps_checkBox")
        self.gif_autofps_checkBox.setLayoutDirection(Qt.RightToLeft)
        self.gif_autofps_checkBox.setChecked(True)

        self.verticalLayout_11.addWidget(self.gif_autofps_checkBox)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.gif_fps_lb = QLabel(self.gif_groupBox)
        self.gif_fps_lb.setObjectName(u"gif_fps_lb")
        self.gif_fps_lb.setEnabled(False)
        self.gif_fps_lb.setLayoutDirection(Qt.LeftToRight)
        self.gif_fps_lb.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.gif_fps_lb)

        self.gif_fps_spinBox = QSpinBox(self.gif_groupBox)
        self.gif_fps_spinBox.setObjectName(u"gif_fps_spinBox")
        self.gif_fps_spinBox.setEnabled(False)
        self.gif_fps_spinBox.setLayoutDirection(Qt.LeftToRight)
        self.gif_fps_spinBox.setMinimum(4)
        self.gif_fps_spinBox.setMaximum(60)
        self.gif_fps_spinBox.setValue(30)

        self.horizontalLayout_15.addWidget(self.gif_fps_spinBox)


        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.convert_gifanim_bt = QPushButton(self.gif_groupBox)
        self.convert_gifanim_bt.setObjectName(u"convert_gifanim_bt")
        self.convert_gifanim_bt.setMinimumSize(QSize(0, 36))
        self.convert_gifanim_bt.setFont(font2)
        self.convert_gifanim_bt.setStyleSheet(u"")
        self.convert_gifanim_bt.setIconSize(QSize(24, 24))

        self.verticalLayout_11.addWidget(self.convert_gifanim_bt)


        self.verticalLayout_5.addWidget(self.gif_groupBox)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_10 = QVBoxLayout(self.tab_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.wav_groupBox = QGroupBox(self.tab_5)
        self.wav_groupBox.setObjectName(u"wav_groupBox")
        self.verticalLayout_13 = QVBoxLayout(self.wav_groupBox)
        self.verticalLayout_13.setSpacing(4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.label_13 = QLabel(self.wav_groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_13)

        self.wav_acodec_comboBox = QComboBox(self.wav_groupBox)
        self.wav_acodec_comboBox.addItem("")
        self.wav_acodec_comboBox.addItem("")
        self.wav_acodec_comboBox.addItem("")
        self.wav_acodec_comboBox.addItem("")
        self.wav_acodec_comboBox.setObjectName(u"wav_acodec_comboBox")

        self.horizontalLayout_14.addWidget(self.wav_acodec_comboBox)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, -1, 0)
        self.label_12 = QLabel(self.wav_groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.wav_samprate_comboBox = QComboBox(self.wav_groupBox)
        self.wav_samprate_comboBox.addItem("")
        self.wav_samprate_comboBox.addItem("")
        self.wav_samprate_comboBox.addItem("")
        self.wav_samprate_comboBox.addItem("")
        self.wav_samprate_comboBox.addItem("")
        self.wav_samprate_comboBox.setObjectName(u"wav_samprate_comboBox")

        self.horizontalLayout_13.addWidget(self.wav_samprate_comboBox)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.label_16 = QLabel(self.wav_groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_16)

        self.mp3_bitrate_comboBox = QComboBox(self.wav_groupBox)
        self.mp3_bitrate_comboBox.addItem("")
        self.mp3_bitrate_comboBox.addItem("")
        self.mp3_bitrate_comboBox.addItem("")
        self.mp3_bitrate_comboBox.addItem("")
        self.mp3_bitrate_comboBox.setObjectName(u"mp3_bitrate_comboBox")

        self.horizontalLayout_19.addWidget(self.mp3_bitrate_comboBox)


        self.verticalLayout_13.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)

        self.convert_wav_bt = QPushButton(self.wav_groupBox)
        self.convert_wav_bt.setObjectName(u"convert_wav_bt")
        self.convert_wav_bt.setMinimumSize(QSize(0, 36))
        self.convert_wav_bt.setFont(font2)
        self.convert_wav_bt.setStyleSheet(u"")
        self.convert_wav_bt.setIconSize(QSize(24, 24))

        self.verticalLayout_13.addWidget(self.convert_wav_bt)


        self.verticalLayout_10.addWidget(self.wav_groupBox)

        self.tabWidget.addTab(self.tab_5, "")
        self.splitter.addWidget(self.tabWidget)

        self.verticalLayout_3.addWidget(self.splitter)

        self.info_lb = QLabel(self.centralwidget)
        self.info_lb.setObjectName(u"info_lb")
        self.info_lb.setFont(font)

        self.verticalLayout_3.addWidget(self.info_lb)

        self.prog_bar = QProgressBar(self.centralwidget)
        self.prog_bar.setObjectName(u"prog_bar")
        self.prog_bar.setMinimumSize(QSize(0, 16))
        self.prog_bar.setMaximumSize(QSize(16777215, 10))
        self.prog_bar.setFont(font)
        self.prog_bar.setValue(0)
        self.prog_bar.setTextVisible(True)

        self.verticalLayout_3.addWidget(self.prog_bar)

        self.ffmeg_lb = QLabel(self.centralwidget)
        self.ffmeg_lb.setObjectName(u"ffmeg_lb")
        self.ffmeg_lb.setFont(font)
        self.ffmeg_lb.setStyleSheet(u"color:rgb(166, 166, 166);")

        self.verticalLayout_3.addWidget(self.ffmeg_lb)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 443, 22))
        self.menuAbout = QMenu(self.menuBar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.action_about_me)
        self.menuAbout.addAction(self.action_about_ffmpeg)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.mp3_bitrate_comboBox.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionAbout_FFMpeg.setText(QCoreApplication.translate("MainWindow", u"About FFMpeg", None))
        self.action_about_ffmpeg.setText(QCoreApplication.translate("MainWindow", u"About FFMpeg", None))
        self.action_about_me.setText(QCoreApplication.translate("MainWindow", u"About Video Conv", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u30d5\u30a1\u30a4\u30eb\u3092\u30c9\u30e9\u30c3\u30b0&\u30c9\u30ed\u30c3\u30d7", None))
        self.list_item_explorer_bt.setText("")
        self.del_sel_bt.setText("")
        self.del_all_bt.setText("")
        self.move_down_item_bt.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.move_up_item_bt.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
#if QT_CONFIG(whatsthis)
        self.filter_le.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u30d5\u30a3\u30eb\u30bf\u30fc", None))
#endif // QT_CONFIG(whatsthis)
        self.filter_le.setInputMask("")
        self.filter_le.setText("")
        self.filter_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u30d5\u30a3\u30eb\u30bf\u30fc", None))
        self.del_filter_bt.setText("")
        ___qtablewidgetitem = self.video_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u30d5\u30a1\u30a4\u30eb\u540d", None));
        ___qtablewidgetitem1 = self.video_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u30d1\u30b9", None));
        self.probe_bt.setText(QCoreApplication.translate("MainWindow", u"\u9078\u629e\u306e\u8a73\u7d30", None))
        self.overall_op_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u30aa\u30d7\u30b7\u30e7\u30f3", None))
        self.resize_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u30b5\u30a4\u30ba\u3092\u5909\u66f4", None))
        self.size_template_c_Label.setText(QCoreApplication.translate("MainWindow", u"\u30b5\u30a4\u30ba\u30d7\u30ea\u30bb\u30c3\u30c8", None))
        self.size_template_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"HD 1280x720", None))
        self.size_template_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"WXGA++ 1600x900", None))
        self.size_template_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"FHD 1920x1080", None))
        self.size_template_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"WQHD 2560x1440", None))
        self.size_template_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"4K 3840x2160", None))
        self.size_template_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"8K 7680x4320", None))
        self.size_template_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"1024x576", None))
        self.size_template_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"768x432", None))
        self.size_template_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"640x360", None))

        self.resolution_x_label.setText(QCoreApplication.translate("MainWindow", u"Width(X)", None))
        self.resolution_x_sp.setSuffix("")
        self.resolution_y_label.setText(QCoreApplication.translate("MainWindow", u"Height(Y)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u30b9\u30bf\u30fc\u30c8\u30c8\u30ea\u30e0", None))
        self.tm_st_sp.setSuffix(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u30a8\u30f3\u30c9\u30c8\u30ea\u30e0", None))
        self.tm_ed_sp.setSuffix(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u51fa\u529b\u30d5\u30a9\u30eb\u30c0", None))
        self.specific_dir_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u30d5\u30a9\u30eb\u30c0\u3092\u6307\u5b9a", None))
        self.save_path_bt.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.explorer_bt.setText("")
        self.overwrite_file_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u66f8\u304d", None))
        self.mp4_groupBox.setTitle("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u52d5\u753b\u30b3\u30fc\u30c7\u30c3\u30af", None))
        self.mp4_codec_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"libx264", None))
        self.mp4_codec_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"libx265", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u30ab\u30e9\u30fc\u30b9\u30da\u30fc\u30b9", None))
        self.mp4_pixformat_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"yuv420p", None))
        self.mp4_pixformat_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"yuyv422", None))
        self.mp4_pixformat_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"yuvj420p", None))
        self.mp4_pixformat_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"yuvj422p", None))
        self.mp4_pixformat_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"yuvj444p", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u30aa\u30fc\u30c7\u30a3\u30aa\u30b3\u30fc\u30c7\u30c3\u30af", None))
        self.mp4_acodec_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"aac", None))
        self.mp4_acodec_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"flac", None))
        self.mp4_acodec_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"ac3", None))
        self.mp4_acodec_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"libmp3lame", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u518d\u751f\u901f\u5ea6", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5727\u7e2e\u7387", None))
        self.convert_mp4_bt.setText(QCoreApplication.translate("MainWindow", u"MP4\u306b\u5909\u63db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"MP4", None))
        self.avi_groupBox.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u52d5\u753b\u30b3\u30fc\u30c7\u30c3\u30af", None))
        self.avi_codec_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"rawvideo", None))
        self.avi_codec_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"mjpeg", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u30ab\u30e9\u30fc\u30b9\u30da\u30fc\u30b9", None))
        self.avi_pixformat_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"yuv420p", None))
        self.avi_pixformat_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"yuyv422", None))
        self.avi_pixformat_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"yuvj420p", None))
        self.avi_pixformat_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"yuvj422p", None))
        self.avi_pixformat_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"yuvj444p", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u30aa\u30fc\u30c7\u30a3\u30aa\u30b3\u30fc\u30c7\u30c3\u30af", None))
        self.avi_acodec_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"pcm_s16le", None))
        self.avi_acodec_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"pcm_s24le", None))
        self.avi_acodec_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"pcm_s32le", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"mjpeg\u306e\u5727\u7e2e\u7387", None))
        self.convert_avi_bt.setText(QCoreApplication.translate("MainWindow", u"AVI\u306b\u5909\u63db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"AVI", None))
        self.png_groupBox.setTitle("")
        self.png_autofps_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u30d5\u30ec\u30fc\u30e0\u30ec\u30fc\u30c8\u3092\u81ea\u52d5\u7684\u306b\u5224\u5b9a\u3059\u308b", None))
        self.png_fps_lb.setText(QCoreApplication.translate("MainWindow", u"\u30d5\u30ec\u30fc\u30e0\u30ec\u30fc\u30c8 (FPS)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u30d5\u30a9\u30fc\u30de\u30c3\u30c8", None))
        self.frame_by_frame_format_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"png", None))
        self.frame_by_frame_format_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"jpg", None))
        self.frame_by_frame_format_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"tga", None))
        self.frame_by_frame_format_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"tif", None))

        self.convert_frame_by_frame_bt.setText(QCoreApplication.translate("MainWindow", u"\u9023\u756a\u306b\u5909\u63db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u9023\u756a", None))
        self.gif_groupBox.setTitle("")
        self.gif_autofps_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u30d5\u30ec\u30fc\u30e0\u30ec\u30fc\u30c8\u3092\u81ea\u52d5\u7684\u306b\u5224\u5b9a\u3059\u308b", None))
        self.gif_fps_lb.setText(QCoreApplication.translate("MainWindow", u"\u30d5\u30ec\u30fc\u30e0\u30ec\u30fc\u30c8 (FPS)", None))
        self.convert_gifanim_bt.setText(QCoreApplication.translate("MainWindow", u"GIF\u30a2\u30cb\u30e1\u306b\u5909\u63db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"GIF\u30a2\u30cb\u30e1", None))
        self.wav_groupBox.setTitle("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u30aa\u30fc\u30c7\u30a3\u30aa\u30b3\u30fc\u30c7\u30c3\u30af", None))
        self.wav_acodec_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"pcm_s16le", None))
        self.wav_acodec_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"pcm_s24le", None))
        self.wav_acodec_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"pcm_s32le", None))
        self.wav_acodec_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"libmp3lame", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u30b5\u30f3\u30d7\u30ea\u30f3\u30b0\u30ec\u30fc\u30c8", None))
        self.wav_samprate_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"44100", None))
        self.wav_samprate_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"48000", None))
        self.wav_samprate_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"168000", None))
        self.wav_samprate_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"192000", None))
        self.wav_samprate_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"256000", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u30d3\u30c3\u30c8\u30ec\u30fc\u30c8(MP3\u306e\u307f)", None))
        self.mp3_bitrate_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"128K", None))
        self.mp3_bitrate_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"160K", None))
        self.mp3_bitrate_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"256K", None))
        self.mp3_bitrate_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"320K", None))

        self.convert_wav_bt.setText(QCoreApplication.translate("MainWindow", u"WAVE or MP3\u306b\u5909\u63db", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"WAV/MP3", None))
        self.info_lb.setText(QCoreApplication.translate("MainWindow", u"Info:", None))
        self.ffmeg_lb.setText(QCoreApplication.translate("MainWindow", u"Powerd by FFMPEG. www.ffmpeg.org", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

