from PyQt6.QtGui import QStandardItemModel, QStandardItem
from log_getter import get_event_logs
from schemas import LogModel

column_headers = ["Уровень", "Дата и время", "Источник", "Код источника", "Категория задачи"]
max_header_len = max([len(header) for header in column_headers])
count_headers = len(column_headers)

event_logs = get_event_logs()

model = QStandardItemModel()
model.setHorizontalHeaderLabels(column_headers)

for event_log in event_logs:
    sc = LogModel(**event_log).dict()
    item = [QStandardItem(str(item_log)) for item_log in sc.values()]
    for i in item:
        i.setEditable(False)
    model.appendRow(item)
