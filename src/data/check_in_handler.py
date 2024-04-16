import uuid
from src.models.repository.check_ins_repository import CheckInRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class CheckInHandler:
    def __init__(self) -> None:
        self.__check_in_respository = CheckInRepository()

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        checkin_info = {}

        attendee_id = http_request.param["attendee_id"]
        checkin_info["uuid"] = str(uuid.uuid4())
        checkin_info["attendee_id"] = attendee_id

        checkin = self.__check_in_respository.insert_check_in(checkin_info)
    
        return HttpResponse(
            body=checkin,
            status_code=201
        )
