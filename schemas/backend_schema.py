from pydantic import BaseModel
from typing import List

class BackendDesign(BaseModel):
    api_endpoints:List[str]
    database_models:List[str]
    backend_services:List[str]