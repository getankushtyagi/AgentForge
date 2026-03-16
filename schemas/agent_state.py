from typing import TypedDict , Optional
from schemas.product_schema import ProductSpecification


class AgentState(TypedDict):
    #User input
    idea:str
    
    #Product Manager Output
    product_spec: Optional[ProductSpecification]
    
    #Architect Output
    architecture=Optional[dict]
    
    #Backend Engineer Output
    backend_design:Optional[dict]
    
    # QA Engineer Output
    qa_plan:Optional[dict]