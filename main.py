'''
Copyright (c) 1998-2024 SAKAIDEN and CaptainHansode
sakaiden@live.jp
http://sakaiden.com

Created by CaptainHansode
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import re
import subprocess
import os
import time
import webbrowser
import collections
import json
import datetime
import logging
import numpy as np
import importlib
import info
import sj_video_conv_ui
import probe_result_dialog
import config as cfg
from PySide2 import QtCore, QtGui, QtWidgets

importlib.reload(sj_video_conv_ui)
importlib.reload(cfg)


class SJVideoConvResultWindow(QtWidgets.QDialog, probe_result_dialog.Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(SJVideoConvResultWindow, self).__init__(*args, **kwargs)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setupUi(self)
        self.setWindowTitle("Probe Result")
        self._init_style()
        """Event"""
        self.close_bt.clicked.connect(self.closeEvent)

    def _init_style(self):
        style_file = 'style.qss'
        with open(style_file, 'r') as f:
            style = f.read()
        self.setStyleSheet(style)

    def closeEvent(self, event):
        self.hide()
        # self.deleteLater()


class SJVideoConv(QtWidgets.QMainWindow, sj_video_conv_ui.Ui_MainWindow):
    r"""UI Class
    """
    def __init__(self, *args, **kwargs):
        super(SJVideoConv, self).__init__(*args, **kwargs)
        """set up ui"""
        self.setupUi(self)
        self.tool_name = info.TOOL_NAME
        self.version = info.TOOL_VERSION
        self.auther = info.AUTHOR
        self.license = info.LICENSE
        self.setWindowTitle("{} {}".format(self.tool_name, self.version))
        self.setObjectName(self.tool_name)
        self.setAcceptDrops(True)

        self._init_config()
        self._init_style()
        self.setWindowFlags(QtCore.Qt.Window)
        self.msgbox = QtWidgets.QMessageBox(self)
        
        """logger"""
        self.logger = logging.getLogger(f"{info.BEST_BASE}.log")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:  # すでにハンドラーが追加されていない場合のみ追加
            fh = logging.FileHandler(f"{info.BEST_BASE}.log", encoding="utf-8")
            fh.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        self.get_exclusion_types = {
            # 古い形式など
            ".flv": True,
            ".webm": True,
            ".rmvb": True,
            ".mpg": True,
            ".mpeg": True,
            ".divx": True,
            ".mkv": True,
            ".3gp": True,
            # ".oma": True,

            # 音声形式
            ".wav": True,
            ".mp3": True,
            ".wma": True,

            # 標準的
            ".avi": True,
            ".mov": True,
            ".wmv": True,
            ".mp4": True
        }

        self.ffmpeg = "ffmpeg.exe"
        self.ffprobe = "ffprobe.exe"
        self.concat_path = "concat_list.txt"
        self.file_table = []

        """Ui set"""
        self.video_list.hide()
        self.move_up_item_bt.hide()
        self.move_down_item_bt.hide()
        self.file_list_view.hide()
        # self.explorer_bt.hide()  # 隠すだけにしておく
        self._init_icon()

        # hheader = QtWidgets.QHeaderView(QtCore.Qt.Orientation.Horizontal)
        # hheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # self.video_table.setHorizontalHeader(hheader)
        # 編集を禁止する
        self.video_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 自動ソートアリはあり
        self.video_table.setSortingEnabled(True)
        # self.video_table.horizontalHeader().sectionClicked.connect(self.on_header_clicked)
        self.sort_toggle = True  # オリジナルのソートの上下用

        """Events"""
        self.action_about_me.triggered.connect(self.about_me_clicked)
        self.action_about_ffmpeg.triggered.connect(self.about_ffmpeg_clicked)
        self.move_up_item_bt.clicked.connect(self.move_up_item)
        self.move_down_item_bt.clicked.connect(self.move_down_item)
        self.del_sel_bt.clicked.connect(self.del_item)
        self.del_all_bt.clicked.connect(self.clear_list)
        self.probe_bt.clicked.connect(self.probe_bt_clicked)

        self.save_path_bt.clicked.connect(self.save_path_bt_clicked)
        self.explorer_bt.clicked.connect(self.explorer_bt_clicked)
        self.list_item_explorer_bt.clicked.connect(self.list_item_explorer_bt_clicked)
        # self.same_directory_checkBox.stateChanged.connect(self.set_save_setting_wigdget)
        self.specific_dir_checkBox.stateChanged.connect(self.set_save_setting_wigdget)
        self.resize_checkBox.stateChanged.connect(self.set_resize_setting_wigdget)
        # self.specific_dir_checkBox
        self.png_autofps_checkBox.stateChanged.connect(self.set_autofps_checkBox_chaged)
        self.gif_autofps_checkBox.stateChanged.connect(self.set_autofps_checkBox_chaged)

        self.convert_mp4_bt.clicked.connect(lambda: self.run_convert("mp4"))
        self.convert_avi_bt.clicked.connect(lambda: self.run_convert("avi"))
        self.convert_gifanim_bt.clicked.connect(lambda: self.run_convert("gif"))
        self.convert_frame_by_frame_bt.clicked.connect(lambda: self.run_convert("fbyf"))
        self.convert_wav_bt.clicked.connect(lambda: self.run_convert("wav"))

        self.size_template_comboBox.currentIndexChanged.connect(self.size_template_comboBox_chaged)
        self.size_template_comboBox.currentIndexChanged.connect(self.size_template_comboBox_chaged)

        self._set_last_state()

    def _init_config(self):
        self.config_path = os.path.join(
            os.environ.get("APPDATA"),
            self.tool_name
            )
        self.def_config_name = "DefaultConfig.json"
        self.def_config = {
            "posx": 120,
            "posy": 120,
            "width": 300,
            "height": 200,
            "trim_st_sec": 0,
            "trim_ed_sec": 0,
            "resolution_x": 1280,
            "resolution_y": 720,
            "specific_dir": False,
            "overwrite_file": True,
            "mp4_compression_val": 0,
            # デフォルトはデスクトップで
            "save_path": os.path.join(
                os.environ.get("USERPROFILE"), "Desktop")
        }
        self.config = cfg.ToolConfig(
            self.config_path, self.def_config_name, self.def_config)

        # init config 値が無い場合に書き込む
        for i in self.def_config:
            val = self.config.data.get(i)
            if val is None:
                self.config.data[i] = self.def_config[i]

    def _check_license(self):
        r"""lic """
        result = False
        return result

    def _set_last_state(self):
        size = [self.config.data["width"], self.config.data["height"]]
        self.setGeometry(QtCore.QRect(
            self.config.data["posx"],
            self.config.data["posy"],
            size[0],
            size[1]))

        self.tm_st_sp.setValue(self.config.data["trim_st_sec"])
        self.tm_ed_sp.setValue(self.config.data["trim_ed_sec"])
        self.resolution_x_sp.setValue(self.config.data["resolution_x"])
        self.resolution_y_sp.setValue(self.config.data["resolution_y"])
        self.specific_dir_checkBox.setChecked(self.config.data["specific_dir"])
        self.overwrite_file_checkBox.setChecked(self.config.data["overwrite_file"])
        self.save_path_le.setText(self.config.data["save_path"])

        self.mp4_compression_sp.setValue(self.config.data["mp4_compression_val"])

    def _save_last_state(self):
        self.config.data["posx"] = self.x() + 8
        self.config.data["posy"] = self.y() + 30
        self.config.data["width"] = self.width()
        self.config.data["height"] = self.height()
        self.config.data["trim_st_sec"] = self.tm_st_sp.value()
        self.config.data["trim_ed_sec"] = self.tm_ed_sp.value()
        self.config.data["resolution_x"] = self.resolution_x_sp.value()
        self.config.data["resolution_y"] = self.resolution_y_sp.value()
        self.config.data["specific_dir"] = self.specific_dir_checkBox.isChecked()
        self.config.data["overwrite_file"] = self.overwrite_file_checkBox.isChecked()
        self.config.data["save_path"] = self.save_path_le.text()
        self.config.data["mp4_compression_val"] = self.mp4_compression_sp.value()
        self.config.save()

    def _init_style(self):
        # style_file = os.path.join(
        #                 os.path.dirname(__file__),
        #                 'style.qss'
        #                 )
        style_file = 'style.qss'
        with open(style_file, 'r') as f:
            style = f.read()
        self.setStyleSheet(style)

    def _init_icon(self):
        """アイコンの設定"""
        ico = QtGui.QIcon()
        ico.addPixmap(
            QtGui.QPixmap("images/filebrowser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.explorer_bt.setIcon(ico)
        self.explorer_bt.setIconSize(self.explorer_bt.size())
        self.list_item_explorer_bt.setIcon(ico)
        self.list_item_explorer_bt.setIconSize(self.list_item_explorer_bt.size())

        ico.addPixmap(
            QtGui.QPixmap("images/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_sel_bt.setIcon(ico)
        ico.addPixmap(
            QtGui.QPixmap("images/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_all_bt.setIcon(ico)

    def closeEvent(self, event):
        """close event override"""
        self._save_last_state()
        self.deleteLater()  # 閉じたら削除  

    def query_box(self, title="Query", msg=""):
        """クエリー"""
        ret = self.msgbox.information(
            self, title, msg, self.msgbox.Yes, self.msgbox.No)
        if ret:
            print("Yes Pressed")
        return ret

    def about_me_clicked(self):
        r"""menu help"""
        webbrowser.open(info.AUTHOR_EMAL)

    def about_ffmpeg_clicked(self):
        r"""menu help"""
        webbrowser.open("https://www.ffmpeg.org/")

    def set_save_setting_wigdget(self, state):
        self.save_path_le.setEnabled(state)
        self.save_path_bt.setEnabled(state)
        self.explorer_bt.setEnabled(state)
        self.overwrite_file_checkBox.setEnabled(state)
        # self.specific_dir_checkBox.setCheckState(state)

    def set_resize_setting_wigdget(self, state):
        self.resolution_x_label.setEnabled(state)
        self.resolution_y_label.setEnabled(state)
        self.resolution_x_sp.setEnabled(state)
        self.resolution_y_sp.setEnabled(state)
        self.size_template_comboBox.setEnabled(state)
        self.size_template_c_Label.setEnabled(state)

    def set_autofps_checkBox_chaged(self, state):
        self.gif_autofps_checkBox.setChecked(state)
        self.png_autofps_checkBox.setChecked(state)
        self.png_fps_lb.setEnabled(not state)
        self.gif_fps_spinBox.setEnabled(not state)
        self.gif_fps_lb.setEnabled(not state)
        self.png_fps_spinBox.setEnabled(not state)

    def size_template_comboBox_chaged(self):
        sel_tmp_name = self.size_template_comboBox.currentText()
        if sel_tmp_name == "HD 1280x720":
            self.resolution_x_sp.setValue(1280)
            self.resolution_y_sp.setValue(720)
        if sel_tmp_name == "WXGA++ 1600x900":
            self.resolution_x_sp.setValue(1600)
            self.resolution_y_sp.setValue(900)
        if sel_tmp_name == "FHD 1920x1080":
            self.resolution_x_sp.setValue(1920)
            self.resolution_y_sp.setValue(1080)
        if sel_tmp_name == "WQHD 2560x1440":
            self.resolution_x_sp.setValue(2560)
            self.resolution_y_sp.setValue(1440)
        if sel_tmp_name == "4K 3840x2160":
            self.resolution_x_sp.setValue(3840)
            self.resolution_y_sp.setValue(2160)
        if sel_tmp_name == "8K 7680x4320":
            self.resolution_x_sp.setValue(7680)
            self.resolution_y_sp.setValue(4320)
        if sel_tmp_name == "1024x576":
            self.resolution_x_sp.setValue(1024)
            self.resolution_y_sp.setValue(576)
        if sel_tmp_name == "768x432":
            self.resolution_x_sp.setValue(768)
            self.resolution_y_sp.setValue(432)
        if sel_tmp_name == "640x360":
            self.resolution_x_sp.setValue(640)
            self.resolution_y_sp.setValue(360)

    def dropEvent(self, event):
        """
        ドラッグされたオブジェクトの、ドロップ許可がおりた場合の処理
        """
        mimedata = event.mimeData()
        urllist = mimedata.urls()
        # 一度クリアした後、ドラッグしたファイルの一覧をListに追加する
        err_list = []
        for i in urllist:
            fpath = re.sub("^/", "", i.path())

            if os.path.isdir(fpath):
                continue

            if self.is_exclusion(fpath):
                err_list.append(os.path.basename(fpath))
                continue
            # self.video_list.addItem(fpath)

            root, ext = os.path.splitext(fpath)
            fname = os.path.basename(fpath)
            self.file_table.append(
                # [fname, os.path.dirname(root), ext.replace(".", "")])
                [fname, os.path.dirname(root)])

        if err_list:
            msg = "{}\n\nこのファイルはサポートされていません".format("\n".join(err_list))
            self.msgbox.setStyleSheet("QLabel {background-color: rgb(255, 35, 35);}")
            self.msgbox.information(self, "Info", msg)

        QtWidgets.QApplication.processEvents()
        # テーブルをアップデート
        self.update_table()

    def dragEnterEvent(self, event):
        """
        ドラッグされたオブジェクトを許可するかどうかを決める
        ドラッグされたオブジェクトが、ファイルなら許可する
        """
        mime = event.mimeData()

        if mime.hasUrls() is True:
            event.accept()
        else:
            event.ignore()

    def is_exclusion(self, file_path):
        r"""除外する場合はTrue"""
        if os.path.isdir(file_path):  # ディレクトリは拡張子チェック除外
            return False

        root, ext = os.path.splitext(file_path)
        ext = ext.lower()
        if ext in self.get_exclusion_types.keys():
            return False
        else:
            return True

    def on_explorer(self, file_path):
        r"""エクスプローラー"""
        if file_path == "":
            return None
        if os.path.exists(os.path.dirname(file_path)) is False:
            msg = u"{} フォルダがありません".format(os.path.dirname(file_path))
            self.statusbar.showMessage(msg)
            return None

        # ファイルがないならディレクトリパス
        if os.path.exists(file_path) is False:
            file_path = os.path.dirname(file_path)

        # ファイルかどうかを判断する
        if os.path.isfile(file_path):
            cmd = 'explorer /select,\"{}\"'.format(file_path.replace("/", "\\"))
        else:
            cmd = 'explorer \"{}\"'.format(file_path.replace("/", "\\"))
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        return None

    def save_file_path_dialog(
            self, titel="Select File", type_filter="", def_dir="C:\\"):
        r"""ファイル選択ダイアログ"""
        file_path = QtWidgets.QFileDialog.getSaveFileName(
            self,
            titel,
            dir=def_dir,
            filter=type_filter,
            options=QtWidgets.QFileDialog.DontUseNativeDialog
            )
        return file_path[0]

    def open_file_path_dialog(
            self, titel="Select File", type_filter="", def_dir="C:\\"):
        r"""ファイル選択ダイアログ"""
        file_path = QtWidgets.QFileDialog.getOpenFileName(
            self,
            titel,
            dir=def_dir,
            filter=type_filter,
            options=QtWidgets.QFileDialog.DontUseNativeDialog
            )
        return file_path[0]

    """以下主にコンフィグ設定側"""
    def open_dir_path_dialog(self, titel=u"出力ディレクトリを選択", def_dir="C:\\"):
        r"""フォルダ選択ダイアログ"""
        dir_path = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            titel,
            dir=def_dir,
            options=QtWidgets.QFileDialog.DontUseNativeDialog
            )
        return dir_path

    def save_path_bt_clicked(self):
        r"""cliecked"""
        ret = self.open_dir_path_dialog(def_dir=self.save_path_le.text())

        if ret == "":
            return None
        self.save_path_le.setText(ret)
        self.config.data["save_path"] = ret
        self.config.save()

    def explorer_bt_clicked(self):
        self.on_explorer(self.save_path_le.text())

    def update_table(self):
        if len(self.file_table) == 0:
            return None
        rowcnt = len(self.file_table)
        colcnt = len(self.file_table[0])
        # 一度オフにしないと空になってしまう
        self.video_table.setSortingEnabled(False)
        self.video_table.setRowCount(rowcnt)  # 行数を設定
        self.video_table.setColumnCount(colcnt)  # 列
        self.video_table.setHorizontalHeaderLabels([u"ファイル名", u"パス"])
        for i in range(rowcnt):
            for j in range(colcnt):
                item = QtWidgets.QTableWidgetItem(str(self.file_table[i][j]))
                self.video_table.setItem(i, j, item)
        self.video_table.setSortingEnabled(True)

        # コラムの大きさを設定
        header = self.video_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

    def on_header_clicked(self, logicalIndex):
        """ヘッダーをクリックした際のオリジナルのソート方法
        これであれば、moveupやmovedownしても問題ない
        """
        current_row = self.video_table.currentRow()
        if current_row == -1:
            return None

        if logicalIndex == 0:
            self.logger.info("Name Sort")
            print("Name Sort")
        # キーで回収してソートして与え直す
        sort_dct = {}
        for i in range(self.video_table.rowCount()):
            # クリックしたindexの場所のテキストをキーとして取得
            key_name = "{}_{:0=4}".format(
                self.video_table.item(i, logicalIndex).text(), i)
            sort_dct[key_name] = [
                self.video_table.item(i, 0).text(),
                self.video_table.item(i, 1).text()
                # self.video_table.item(i, 2).text()
            ]
        self.file_table = []  # リストは一回クリア
        for k, v in sorted(sort_dct.items()):
            self.file_table.append(v)

        if self.sort_toggle is True:  # ソートの上下用
            self.file_table.reverse()
            self.sort_toggle = False
        else:
            self.sort_toggle = True
        self.update_table()

    def list_item_explorer_bt_clicked(self):
        current_row = self.video_table.currentRow()
        if current_row == -1:
            return None
        fpath = os.path.join(
            self.video_table.item(current_row, 1).text(),
            self.video_table.item(current_row, 0).text()
            )
        self.on_explorer(fpath)

    def move_up_item(self):
        # Table
        current_row = self.video_table.currentRow()
        current_col = self.video_table.currentColumn()
        next_row = current_row - 1  # 次の行
        if current_row != -1:
            if current_row == 0:
                return None
            for i in range(self.video_table.columnCount()):
                # 上下のアイテムを入れ替え
                # ソート列が固定されてしまい、空になったりして上手く動かない
                # 自分で名前ソートや、パスソートをするべき
                # 自動のソートモードがonの場合は上下をDisableにするのがいい
                current_item = self.video_table.takeItem(current_row, i)
                next_item = self.video_table.takeItem(next_row, i)
                self.video_table.setItem(current_row, i, next_item)
                self.video_table.setItem(next_row, i, current_item)
            self.video_table.setCurrentCell(next_row, current_col)
            self.video_table.setFocus()
        return None

    def move_down_item(self):
        # Table
        current_row = self.video_table.currentRow()
        current_col = self.video_table.currentColumn()
        next_row = current_row + 1  # 次の行
        if current_row != -1:
            if current_row == self.video_table.rowCount() - 1:
                return None
            for i in range(self.video_table.columnCount()):
                # 上下のアイテムを入れ替え
                current_item = self.video_table.takeItem(current_row, i)
                next_item = self.video_table.takeItem(next_row, i)
                self.video_table.setItem(current_row, i, next_item)
                self.video_table.setItem(next_row, i, current_item)

            self.video_table.setCurrentCell(next_row, current_col)
            self.video_table.setFocus()
        return None

    def del_item(self):
        # テーブル版
        current_row = self.video_table.currentRow()
        if current_row == -1:
            return None

        # 取得した範囲のレンジを削除出来る
        del_rows = []
        for sel_renge in self.video_table.selectedRanges():
            # 上と下が同じならトップのみ
            if sel_renge.topRow() == sel_renge.bottomRow():
                del_rows.append(sel_renge.topRow())
                continue
            # topとボトムが離れてたら複数行選択
            for i in range(sel_renge.topRow(), sel_renge.bottomRow() + 1):
                del_rows.append(i)

        del_rows = list(set(del_rows))
        for i in sorted(del_rows, reverse=True):
            self.logger.info(i)
            self.video_table.removeRow(i)

        # テーブル作り直して入れる?
        self.file_table = []
        ext = ""
        for i in range(self.video_table.rowCount()):
            name = self.video_table.item(i, 0).text()
            path = self.video_table.item(i, 1).text()
            # ext = self.video_table.item(i, 2).text()
            self.file_table.append([name, path, ext])
        return None

    def clear_list(self):
        # self.video_list.clear()
        self.video_table.clear()
        self.file_table = []
        self.video_table.setColumnCount(2)  # 行数を設定
        self.video_table.setHorizontalHeaderLabels([u"ファイル名", u"パス"])

    def make_input_list(self):
        flist = []
        for i in range(self.video_list.count()):
            flist.append("file {}".format(self.video_list.item(i).text()))

        save_file = open(self.concat_path, 'w')
        save_file.writelines("\n".join(flist))
        save_file.close()

    def get_video_frame(self, video_file):
        cmd = "{} -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 -i \"{}\"".format(
                self.ffprobe,
                video_file
                )
        self.logger.info(cmd)
        print(cmd)
        cmd_ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        cmd_ret.wait()
        ret = 0
        for i in cmd_ret.stdout.readlines():
            rline = i.decode().replace('\r\n', '')
            if str.isdigit(rline):
                ret = int(rline)
        return ret

    def trim_frame(self):
        flist = []
        for i in range(self.video_list.count()):
            self.prog_bar.setValue((i / self.video_list.count()) * 90)
            mfile = self.video_list.item(i).text()
            self.statusbar.showMessage("Trim: {}".format(mfile))

            m_duration = self.get_movie_duration(mfile)
            st_time = self.tm_st_sp.value() / 24.0
            ed_time = self.tm_ed_sp.value() / 24.0

            trim_duration = m_duration - (st_time + ed_time)

            out_file = "trim_out{}.mp4".format(i)
            # -c:a copy はMp4の変換に失敗する -c:v copy もよくわからないがバグる
            # -c:a copy はMp4の変換に失敗する -c:v copy もよくわからないがバグる
            # cmd = "{} -ss {} -i \"{}\" -ss 0 -t {} -c:v copy -c:a copy -acodec copy {} -y".format(
            # -crf 1のクオリファイオプションだけ、あとはオート
            cmd = "{} -ss {} -i \"{}\" -ss 0 -t {} -crf 1 {} -y".format(
                self.ffmpeg,
                "{0:.5}".format(st_time),
                mfile,
                "{0:.5}".format(trim_duration),
                out_file
                )
            self.logger.info(cmd)
            print(cmd)
            cmd_ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            cmd_ret.wait()

            flist.append("file {}".format(out_file))

        save_file = open(self.concat_path, 'w')
        save_file.writelines("\n".join(flist))
        save_file.close()

    def ffprobe_item(self, file_path):
        r"""調べる"""
        cmd = "{} -loglevel quiet -show_streams -print_format json -i \"{}\"".format(
                self.ffprobe,
                file_path
                )
        cmd_ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        buffer = []
        
        while True:
            # バッファから1行読み込む.
            line = cmd_ret.stdout.readline().decode()
            buffer.append(line)
            self.statusbar.showMessage(line.replace('\r\n', ''))
            QtWidgets.QApplication.processEvents()
            if not line and cmd_ret.poll() is not None:
                break
        return "".join(buffer)

    def get_duration(self, file_path):
        r"""調べる"""
        cmd = "{} -loglevel quiet -show_entries format=duration -print_format json -i \"{}\"".format(
                self.ffprobe,
                file_path
                )
        cmd_ret = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        buffer = []
        while True:
            # バッファから1行読み込む.
            line = cmd_ret.stdout.readline().decode()
            buffer.append(line)
            self.statusbar.showMessage(line.replace('\r\n', ''))
            QtWidgets.QApplication.processEvents()
            if not line and cmd_ret.poll() is not None:
                break
        return "".join(buffer)

    def probe_bt_clicked(self):
        current_row = self.video_table.currentRow()
        if current_row == -1:
            return None
        fpath = os.path.join(
            self.video_table.item(current_row, 1).text(),
            self.video_table.item(current_row, 0).text()
            )
        # returnはjson
        ret = self.ffprobe_item(fpath)
        self.ret_win = SJVideoConvResultWindow(self)
        self.ret_win.result_textEdit.setText(ret)
        self.ret_win.show()

    def create_unique_path(self, path, fill=2):
        count = 1
        dirname = os.path.dirname(path)
        basename = os.path.basename(path)
        if os.path.isdir(path):
            while os.path.exists(path):
                path = os.path.join(
                    dirname, "{}_{}".format(basename, str(count).zfill(fill)))
                count += 1
        else:
            fname, ext = os.path.splitext(path)
            while os.path.exists(path):
                path = os.path.join(dirname, "{}_{}{}".format(
                    fname, str(count).zfill(fill), ext))
                count += 1
        return path

    def run_convert(self, mode=None):
        """コンバート"""
        if os.path.exists(self.ffmpeg) is False:
            self.statusbar.showMessage("ffmpegが見つかりません")
            self.statusbar.setStyleSheet("QStatusBar{color:rgb(245, 245, 245); background:rgb(98, 21, 21)}")
            QtWidgets.QApplication.processEvents()
            return None

        if mode == "mp4":
            vcodec = self.mp4_codec_comboBox.currentText()
            acodec = self.mp4_acodec_comboBox.currentText()
            pix_fmt = self.mp4_pixformat_comboBox.currentText()
        else:
            vcodec = self.avi_codec_comboBox.currentText()
            acodec = self.avi_acodec_comboBox.currentText()
            pix_fmt = self.avi_pixformat_comboBox.currentText()
        
        acodec_wav_mp3 = self.wav_acodec_comboBox.currentText()
        sample_rate = self.wav_samprate_comboBox.currentText()
        if mode == "wav" and acodec_wav_mp3 == "libmp3lame":
            mode = "mp3"
            # mp3は48000以上を指定できない
            if sample_rate != "44100" or sample_rate != "48000":
                sample_rate = "48000"

        # Playback Speed
        pl_spd = self.mp4_playbackspeed_sp.value()

        self.statusbar.showMessage("Check List")
        if self.video_table.rowCount() is 0:
            self.statusbar.showMessage("リストに動画がありません")
            self.statusbar.setStyleSheet("QStatusBar{color:rgb(245, 245, 245); background:rgb(98, 21, 21)}")
            QtWidgets.QApplication.processEvents()
            return None

        output_dir = os.path.dirname(self.save_path_le.text())
        if os.path.exists(output_dir) is False:
            os.makedirs(output_dir)
            self.statusbar.showMessage(u"フォルダを作成しています")
            while os.path.exists(output_dir) is False:
                time.sleep(1)

        self.statusbar.showMessage("Convert Start")
        self.statusbar.setStyleSheet("QStatusBar{color:rgb(245, 245, 245); background:rgb(204, 102, 51)}")
        QtWidgets.QApplication.processEvents()

        # 基本コマンド
        # cmd = "{} -ss {} -i \"{}\" -ss 0 -t {} -vcodec rawvideo -ac 2 -ar 48000 -acodec pcm_s32le -pix_fmt yuv420p -y \"{}\"".format(
        cmd = []
        start_time = datetime.datetime.now()
        for i in range(self.video_table.rowCount()):
            # 共通設定
            # input file
            fname = self.video_table.item(i, 0).text()
            fpath = self.video_table.item(i, 1).text()
            input_file = os.path.join(fpath, fname)

            # video probe returnはjson
            v_probe = json.loads(
                self.ffprobe_item(input_file),
                object_pairs_hook=collections.OrderedDict)

            self.info_lb.setText("Convert:{}".format(fname))
            QtWidgets.QApplication.processEvents()

            # 中にはdurationが無いものがある
            if "duration" in v_probe["streams"][0]:
                total_time = float(v_probe["streams"][0]["duration"])
            else:
                total_time = float(json.loads(
                    self.get_duration(input_file))["format"]["duration"])

            # ffmpeg
            cmd = [self.ffmpeg]

            # trim start time
            if self.tm_st_sp.value() > 0.0:
                cmd.append("-ss {}".format(self.tm_st_sp.value()))

            # input file
            cmd.append("-i \"{}\"".format(input_file))

            # trim end time
            if self.tm_ed_sp.value() > 0.0 or pl_spd != 1.0:
                # ビデオ全体の長さから 頭とおしりのタイムを引く
                trim_time = self.tm_st_sp.value() + self.tm_ed_sp.value()

                if total_time < trim_time:  # トリムタイムが大きすぎる
                    msg = u"{}\nトリム時間が大きすぎます\n処理をスキップします\nTotal duration {}s\nTrim time {}s".format(
                        fname,
                        total_time,
                        trim_time
                    )
                    self.msgbox.warning(self, "Warning", msg)
                    continue
                cmd.append("-ss 0 -t {}".format(
                    (total_time - trim_time) / pl_spd))

            # ------------個別設定
            # 動画size 音声はできない gifは別途指定
            if mode != "wav" and mode != "mp3" and mode !="gif" and self.resize_checkBox.isChecked():
                cmd.append("-s {}x{}".format(
                    self.resolution_x_sp.value(), self.resolution_y_sp.value()))

            # video cordec
            if mode == "mp4" or mode == "avi":
                # vcodec
                cmd.append("-vcodec {}".format(vcodec))

                # mp4 compression
                if mode == "mp4":
                    cmd.append("-qmax {}".format(self.mp4_compression_sp.value()))

                if vcodec == "mjpeg":
                    cmd.append("-q:v {}".format(self.mjepg_compression_sp.value()))

                # audio sampling
                cmd.append("-ac 2 -ar 44100")

                # audio codec
                cmd.append("-acodec {}".format(acodec))
                
                # pixcel format
                cmd.append("-pix_fmt {}".format(pix_fmt))

            # Playback speed
            if mode == "mp4" and pl_spd != 1.0:
                cmd.append(
                    "-vf setpts=PTS/{} -af atempo={}".format(pl_spd, np.clip(pl_spd, 0.1, 2.0)))

            # gif or pin frate
            if mode == "gif" or mode == "fbyf":
                frate = v_probe["streams"][0]["r_frame_rate"]
                # 音声ファイルの場合フレームレートが無い
                if frate == "0/0":
                    self.logger.info("Zero division error")
                    print("Zero division error")
                    continue
                frate = round(eval(frate))

            # gif anim
            if mode == "gif":
                if self.gif_autofps_checkBox.isChecked() is False:
                    frate = self.gif_fps_spinBox.value()
                sx = -1
                sy = -1
                if self.resize_checkBox.isChecked():
                    sx = self.resolution_x_sp.value() 
                    sy = self.resolution_y_sp.value()

                cmd.append(
                    "-filter_complex \"fps={}, scale={}:{}, {}\"".format(
                        frate,
                        sx,
                        sy,
                        # 比較的容量もかるく綺麗な指定
                        "split [a][b]; [a] palettegen [p]; [b][p] paletteuse"))

            # frame by frame
            if mode == "fbyf":
                img_format = self.frame_by_frame_format_comboBox.currentText()
                if self.gif_autofps_checkBox.isChecked() is False:
                    frate = self.gif_fps_spinBox.value()
                if img_format == "png":
                    cmd.append("-vcodec png -r {}".format(frate))
                if img_format == "jpg":
                    cmd.append("-vcodec mjpeg -q 0 -r {}".format(frate))
                if img_format == "tga":
                    cmd.append("-vcodec targa -pix_fmt rgba -r {}".format(frate))
                if img_format == "tif":
                    cmd.append("-vcodec tiff -pix_fmt rgba -r {}".format(frate))

            # Wav or mp3
            # -ab 256k -acodec libmp3lame
            if mode == "wav" or mode == "mp3":
                cmd.append("-vn -ac 2 -ar {}".format(sample_rate))
                # mp3だったら
                if acodec_wav_mp3 == "libmp3lame":
                    cmd.append("-ab {}".format(
                        self.mp3_bitrate_comboBox.currentText()))
                cmd.append("-acodec {}".format(acodec_wav_mp3))

            # orverwrite
            if self.overwrite_file_checkBox.isChecked():
                cmd.append("-y")
            else:
                cmd.append("-n")

            # out file
            name, ext = os.path.splitext(fname)
            out_name = "{}_converted.{}".format(name, mode)
            if mode == "fbyf":
                out_folder = "{}_converted".format(name)
                out_name = "{}_%04d.{}".format(name, img_format)

            # output file
            # 指定の場所
            if self.specific_dir_checkBox.isChecked():
                fpath = self.save_path_le.text()

            output_file = os.path.join(fpath, out_name)
            if mode == "fbyf":  # 連番はフォルダにまとめる
                output_file = os.path.join(fpath, out_folder, out_name)

            # 上書きしない場合
            if self.overwrite_file_checkBox.isChecked() is False:
                # 既にファイルがある場合はrename
                if mode == "fbyf":
                    ret = self.create_unique_path(
                        os.path.join(fpath, out_folder))
                    os.makedirs(ret)
                    output_file = os.path.join(ret, out_name)
                else:
                    output_file = self.create_unique_path(output_file)
            else:
                if mode == "fbyf":
                    out_folder = os.path.join(fpath, out_folder)
                    if not os.path.exists(out_folder):
                        os.makedirs(out_folder)

            cmd.append("\"{}\"".format(output_file))

            _full_cmd = "FullCommand: {}".format(" ".join(cmd))
            self.logger.debug("="*80)
            self.logger.debug(_full_cmd)
            self.logger.debug("="*80)
            self.logger.info("="*80)
            self.logger.info(_full_cmd)
            self.logger.info("="*80)
            print("="*80)
            print(_full_cmd)
            print("="*80)

            cmd_ret = subprocess.Popen(
                " ".join(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, shell=True)
            count = 0
            while True:
                # マルチバイトが弾かれたので適当にtryで逃げる
                try:
                    line = cmd_ret.stdout.readline().replace('\r\n', '')
                    self.statusbar.showMessage(line)
                    converted_time = re.search(r"time=(\d\d):(\d\d):(\d\d).(\d\d)", line)
                    if converted_time is not None:
                        td = datetime.timedelta(
                            hours=float(converted_time.groups()[0]),
                            minutes=float(converted_time.groups()[1]),
                            seconds=float(converted_time.groups()[2]),
                            milliseconds=float(converted_time.groups()[3])*10)
                        self.prog_bar.setValue(
                            (td.seconds / total_time) * 100.0)
                except UnicodeError as e:
                    self.prog_bar.setValue(count)
                    self.statusbar.showMessage("Convert {:08d}:".format(count))
                except RuntimeError as e:
                    self.prog_bar.setValue(count)
                    self.statusbar.showMessage("Convert {:08d}:".format(count))

                # total_time
                QtWidgets.QApplication.processEvents()
                if not line and cmd_ret.poll() is not None:
                    break
                count += 1

        stop_time = datetime.datetime.now()
        self.prog_bar.setValue(100)
        self.info_lb.setText("Info: Total Process Time={}".format(stop_time - start_time))
        self.statusbar.showMessage("Complete.")
        self.statusbar.setStyleSheet("QStatusBar{background: rgb(0, 102, 180)}")
        QtWidgets.QApplication.processEvents()
        return None


if __name__ == "__main__":
    pass
