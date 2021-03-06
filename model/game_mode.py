from enum import Enum

class GameMode(Enum):
    def __str__(self):
        return str(self.value)

    @classmethod
    def fromstring(cls, str):
        return getattr(cls, str.upper(), None)

    LOCAL = "local"
    AI = "AI"    
    AI2 = "AI2"
    AI3 = "AI3"
    REMOTE = "remote"

class REMOTE_GAME_REQUEST_STATUS(Enum):
    PENDING = "Pending"
    DECLINED = "Declined"
    DISCONNECTED = "Disconnected"
    ACCEPTED = "Accepted"
