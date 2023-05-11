import win32evtlog

server = 'localhost'


def get_event_logs(log_type: str = 'System'):
    event_logs = []

    hand = win32evtlog.OpenEventLog(server, log_type)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    try:
        events = 1
        while events:
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            for event in events:
                event_logs.append(
                    {"EventType": event.EventType, "TimeGenerated": str(event.TimeGenerated),
                     "SourceName": event.SourceName,
                     "EventID": event.EventID, "EventCategory": event.EventCategory,
                     "ClosingRecordNumber": event.ClosingRecordNumber, "ComputerName": event.ComputerName,
                     "Data": event.Data, "RecordNumber": event.RecordNumber, "Reserved": event.Reserved,
                     "ReservedFlags": event.ReservedFlags, "Sid": event.Sid, "StringInserts": event.StringInserts
                     })
        return event_logs
    except Exception as error:
        print(error)
        return event_logs

# for event in get_event_logs():
#     print(event)
#     print(f"{event.EventType} | {event.SourceName} | {event.EventID}"
#           f"{event.ClosingRecordNumber} | {event.ComputerName} | {event.Data}"
#           f"{event.EventCategory} | {event.RecordNumber} | {event.Reserved}"
#           f"{event.ReservedFlags} | {event.Sid} | {event.StringInserts}")
