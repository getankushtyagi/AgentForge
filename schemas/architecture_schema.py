from pydantic import BaseModel
from typing import List


class SystemArchitecture(BaseModel):
    
    services: List[str]
    database_table: List[str]
    tech_stack: List[str]