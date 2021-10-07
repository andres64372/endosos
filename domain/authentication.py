import dataclasses

from utils.dataclass_classmethods import FromDictMixin

@dataclasses.dataclass
class Token(FromDictMixin):
    token: str = None
    idle_timeout_in_minutes: int = 0

    def get_api_token(self):
        return self.token

    def get_time_out(self):
        return self.idle_timeout_in_minutes

