from pydantic import BaseModel, Field
from typing import List, Annotated


class ProductSpecification(BaseModel):

    product_name: str = Field(description="Name of the product")

    description: str = Field(description="Detailed description of the product")

    target_users: Annotated[
        List[str],
        Field(description="Target user groups")
    ]

    core_features: Annotated[
        List[str],
        Field(description="Main product features")
    ]

    success_metrics: Annotated[
        List[str],
        Field(description="Metrics used to measure success")
    ]