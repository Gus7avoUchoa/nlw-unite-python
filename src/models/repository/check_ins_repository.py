from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError
from src.errors.error_types.http_conflict import HttpConflictError

class CheckInRepository:
    def insert_check_in(self, checkin_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                check_in = (
                    CheckIns(
                        id=checkin_info.get("uuid"),
                        attendee_Id=checkin_info.get("attendee_id")
                    )
                )
                database.session.add(check_in)
                database.session.commit()
                
                return check_in.id
            except IntegrityError:
                raise HttpConflictError('Check In ja cadastrado!')
            except Exception as exception:
                database.session.rollback()
                raise exception
