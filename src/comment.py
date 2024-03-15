from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Comment:
    tag : str
    author : str
    content : str
    ip_datetime : str
    ip : str = field(init=False)
    date_time : datetime = field(init=False)

    def __post_init__(self):
        ip_datetime = self.ip_datetime.split()
        self.ip = ip_datetime[0]
        self.date_time = datetime.strptime(ip_datetime[1] + " " + ip_datetime[2] , "%m/%d %H:%M")