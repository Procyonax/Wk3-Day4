from models.event import *
from datetime import date

event1 = Event(1, "Glastonbury", date(2023, 6, 29), 100000, "Dance Room", "Its a festival with musical acts, thats popular")
event2 = Event(2, "Download", date(2023, 4, 23), 56000, "Rock Room", "Rock music festival etc")
event3 = Event(1, "Reading", date(2022, 11, 3), 40000, "Boring Room", "The other, not as popular generic music festival")
event4 = Event(4, "T In The Park", date(2023, 7, 24), 98000, "Outside Room", "The scottish one")
events = [event1, event2, event3, event4]

def find_event_by_id(id):
    for event in events:
        if event.id == id:
            return event
    return None

def add_new_event(event):
    events.append(event)