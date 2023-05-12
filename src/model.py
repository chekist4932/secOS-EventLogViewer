from PyQt6.QtWidgets import QTreeWidgetItem
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from src.log_getter import get_event_logs
from src.schemas import LogSchema

import win32evtlog

from typing import Any

from pydantic import BaseModel

event_log_headers = ['System', 'Application', 'Security']
_event_logs = get_event_logs()

column_headers = ["Уровень", "Дата и время", "Источник", "Код источника", "Категория задачи"]
max_header_len = max([len(header) for header in column_headers])
count_headers = len(column_headers)

main_tree_model = QStandardItemModel()
main_tree_model.setHorizontalHeaderLabels(column_headers)
for event_log in _event_logs:
    sc = LogSchema(**event_log).dict()
    item = [QStandardItem(item_log) for item_log in sc.values()]
    for col_count, row in enumerate(item):
        row.setEditable(False)
        align_flag = Qt.AlignmentFlag.AlignLeft
        row.setTextAlignment(align_flag)
    main_tree_model.appendRow(item)

event_log_table_model = QStandardItemModel()
for event in event_log_headers:
    item = QStandardItem(event)
    item.setEditable(False)
    event_log_table_model.appendRow(item)
