'''
Copyright (c) SAKAIDEN and CaptainHansode
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
import sys
import os

"""PyInstaller"""
if hasattr(sys, "frozen"):
    # If the application is frozen, set the base path to the directory of the executable
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(base_path))
sys.path.append(os.path.join(os.path.dirname(base_path)))

from sj_video_conv import main
from PySide2 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])

    win = main.SJVideoConv()
    win.show()
    app.exec_()
