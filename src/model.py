from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from src.log_getter import get_event_logs

log_column = ['Windows logs']
event_log_headers = ['System', 'Application', 'Security']
log_column_headers = ["Number", "EventType", "TimeGenerated", "SourceName", "EventID", "EventCategory"]

event_tree_model = QStandardItemModel()
event_tree_model.setHorizontalHeaderLabels(log_column_headers)


def event_log_changer(log_type: str):
    event_tree_model.clear()
    event_tree_model.setHorizontalHeaderLabels(log_column_headers)

    get_event_logs.create_logs(log_type)
    _event_logs = get_event_logs.get_logs()

    for event_log in _event_logs:
        item_ = [QStandardItem(str(event_log[item_log_key])) for item_log_key in log_column_headers]
        for col_count, row in enumerate(item_):
            row.setEditable(False)
            align_flag = Qt.AlignmentFlag.AlignLeft
            row.setTextAlignment(align_flag)
        event_tree_model.appendRow(item_)


event_headers_model = QStandardItemModel()
event_headers_model.setHorizontalHeaderLabels(log_column)
for event in event_log_headers:
    item = QStandardItem(event)
    item.setEditable(False)
    item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
    event_headers_model.appendRow(item)
