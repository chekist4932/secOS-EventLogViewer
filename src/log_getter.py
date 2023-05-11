import win32evtlog
import socket


def get_event_logs(server_: str, log_type_: str):
    hand = win32evtlog.OpenEventLog(server_, log_type_)
    total_count_events = win32evtlog.GetNumberOfEventLogRecords(hand)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    try:
        events = 1
        while events:
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            for event in events:
                print(
                    f"{event.SourceName} | {event.TimeGenerated} | {event.StringInserts}")
    except Exception as error:
        print(error)


server = 'localhost'  # name of the target computer to get event logs
log_type = 'System'
get_event_logs(server, log_type)
