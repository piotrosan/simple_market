from datetime import datetime
from pydantic import BaseModel
from enum import Enum, IntEnum

# for development

class GraphicComplex(IntEnum):
    simple = 1
    complex = 2

class Site(BaseModel):
    site_amount: int
    site_graphic_complex: GraphicComplex
    database_support: bool
