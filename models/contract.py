from pydantic import BaseModel
from datetime import date
from math import ceil


class Contract(BaseModel):
    id: int
    school_id: int
    mat: str
    start: date
    end: date
    work_hours: int

    @property
    def planning_hours(self):
        return ceil(self.work_hours / 3)

    @property
    def total_hours(self):
        return self.work_hours + self.planning_hours
