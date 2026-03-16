from pydantic import BaseModel
from typing import List

class QAPlan(BaseModel):
    test_cases:List[str]
    edge_cases:List[str]
    api_test:List[str]