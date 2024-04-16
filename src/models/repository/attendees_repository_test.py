import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    event_id = "meu-uuid-e-nois"
    attendees_info = {
        "uuid": "meu_uuid_attendee3",
        "name": "atendee name3",
        "email": "email3@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="...")
def test_get_attendee_badge_by_id():
    attendde_id = "meu_uuid_attendee3"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendde_id)
    print(attendee)
    print(attendee.title)

# @pytest.mark.skip(reason="...")
def test_get_attendees_by_event_id():
    event_id = "64E0FC4B-A256-4420-85A0-DC4D7FED8338"
    attendees_repository = AttendeesRepository()
    attendees = attendees_repository.get_attendees_by_event_id(event_id)
    print(attendees)
