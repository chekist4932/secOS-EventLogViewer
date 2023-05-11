from PyQt6.QtGui import QStandardItemModel, QStandardItem
import random

column_headers = ["Уровень", "Дата и время", "Источник", "Код источника", "Категория задачи"]
event_logs = [["Сведения", "11.05.2023 12:09:55", "SecurityCenter", f"{random.randint(0, 100)}", "Отсутствует"],
              ["Сведения", "11.05.2023 12:09:54", "RestartManager", f"{random.randint(0, 100)}", "Отсутствует"],
              ["Сведения", "11.05.2023 12:09:32", "VSS", f"{random.randint(0, 100)}", "Отсутствует"],
              ["Сведения", "11.05.2023 12:09:45", "SecurityCenter", f"{random.randint(0, 100)}", "Отсутствует"]]

model = QStandardItemModel()
model.setHorizontalHeaderLabels(column_headers)

for event_log in event_logs:
    item = []
    for item_log in event_log:
        item.append(QStandardItem(item_log))
    model.appendRow(item)
