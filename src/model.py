from PyQt6.QtGui import QStandardItemModel

import win32evtlog

from typing import Any

from pydantic import BaseModel

column_headers = ["Уровень", "Дата и время", "Источник", "Код источника", "Категория задачи"]
max_header_len = max([len(header) for header in column_headers])
count_headers = len(column_headers)

tabel_model = QStandardItemModel()
tabel_model.setHorizontalHeaderLabels(column_headers)
