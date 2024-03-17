from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Comment:
    tag : str
    author : str
    content : str
    _sourse_year : int
    _ip_datetime : str | None
    ip : str = field(init=False)
    date_time : datetime = field(init=False)

    def __post_init__(self):
        ip_datetime = self._ip_datetime.split()

        if (len(ip_datetime) == 3):
            self.ip = ip_datetime[0]
            self.date_time = datetime.strptime(ip_datetime[1] + " " + ip_datetime[2] + " " + str(self._sourse_year) , "%m/%d %H:%M %Y")
        elif (len(ip_datetime) == 2):
            self.ip = None
            self.date_time = datetime.strptime(ip_datetime[0] + " " + ip_datetime[1] + " " + str(self._sourse_year) , "%m/%d %H:%M %Y")