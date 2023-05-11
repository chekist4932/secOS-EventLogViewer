from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from src.log_getter import get_event_logs

import win32evtlog

from typing import Any

from pydantic import BaseModel

event_log = ['System', 'Application', 'Security']

column_headers = ["Уровень", "Дата и время", "Источник", "Код источника", "Категория задачи"]
max_header_len = max([len(header) for header in column_headers])
count_headers = len(column_headers)


class StandardItemModel(QStandardItemModel):
    checkStateChanged = pyqtSignal(QStandardItem)


@pyqtSlot(QStandardItem)
def foo_slot():
    print("clicked")


main_tree_model = QStandardItemModel()
main_tree_model.setHorizontalHeaderLabels(column_headers)

event_log_table_model = QStandardItemModel()
# event_log_table_model.checkStateChanged.connect(foo_slot)
for event in event_log:
    item = QStandardItem(event)
    # item.setCheckable(True)
    item.setEditable(False)
    event_log_table_model.appendRow(item)
