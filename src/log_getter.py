import win32evtlog
import timeit

server = 'localhost'


class GetLogs:
    def __init__(self):
        self.event_logs = None

    def create_logs(self, log_type: str = 'System'):
        self.event_logs = []
        hand = win32evtlog.OpenEventLog(server, log_type)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

        count = 1
        try:
            events = 1
            while events:
                events = win32evtlog.ReadEventLog(hand, flags, 0)

                for event in events:
                    self.event_logs.append(
                        {"Number": count, "EventType": event.EventType, "TimeGenerated": str(event.TimeGenerated),
                         "SourceName": event.SourceName,
                         "EventID": event.EventID, "EventCategory": event.EventCategory,
                         "ClosingRecordNumber": event.ClosingRecordNumber, "ComputerName": event.ComputerName,
                         "Data": event.Data, "RecordNumber": event.RecordNumber, "Reserved": event.Reserved,
                         "ReservedFlags": event.ReservedFlags, "Sid": event.Sid, "StringInserts": event.StringInserts
                         })
                    count += 1
        except Exception as error:
            print(error)

    def get_logs(self):
        return self.event_logs

    def find_log(self, log_number: str):
        for log in self.event_logs:
            if int(log['Number']) == int(log_number):
                return log


get_event_logs = GetLogs()
