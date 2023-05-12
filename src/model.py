from PyQt6.QtWidgets import QTreeWidgetItem
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtCore import Qt
from src.log_getter import get_event_logs
from src.schemas import LogSchema

log_column_headers = ["Уровень", "Дата и время", "Источник", "Код источника", "Категория задачи"]
log_column = ['Windows logs']
max_header_len = max([len(header) for header in log_column_headers])
count_headers = len(log_column_headers)

event_tree_model = QStandardItemModel()
event_tree_model.setHorizontalHeaderLabels(log_column_headers)


def event_log_changer(log_type: str):
    _event_logs = get_event_logs(log_type)
    if event_tree_model.rowCount() > 0:
        while event_tree_model.rowCount() != 0:
            event_tree_model.removeRow(0)
    for event_log in _event_logs:
        sc = LogSchema(**event_log).dict()
        item_ = [QStandardItem(item_log) for item_log in sc.values()]
        for col_count, row in enumerate(item_):
            row.setEditable(False)
            align_flag = Qt.AlignmentFlag.AlignLeft
            row.setTextAlignment(align_flag)
        event_tree_model.appendRow(item_)


event_log_headers = ['System', 'Application', 'Security']


event_headers_model = QStandardItemModel()
event_headers_model.setHorizontalHeaderLabels(log_column)
for event in event_log_headers:
    item = QStandardItem(event)
    item.setEditable(False)
    item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
    event_headers_model.appendRow(item)
