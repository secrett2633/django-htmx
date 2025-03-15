from pydantic import BaseModel as PydanticBaseModel
from django.http.response import HttpResponse
from typing import Annotated


class BaseModel(PydanticBaseModel):    
    response: Annotated[HttpResponse, ...]
    
    class Config:
        arbitrary_types_allowed: bool = True
