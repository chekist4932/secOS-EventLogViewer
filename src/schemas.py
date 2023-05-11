from pydantic import BaseModel


class LogModel(BaseModel):
    TimeGenerated: None
    SourceName: None
    EventID: None
    EventType: None
    EventCategory: None


['ClosingRecordNumber', 'ComputerName', 'Data', 'EventCategory', 'EventID', 'EventType', 'RecordNumber', 'Reserved',
 'ReservedFlags', 'Sid', 'SourceName', 'StringInserts', 'TimeGenerated', 'TimeWritten']
