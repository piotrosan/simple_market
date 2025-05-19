from datetime import datetime
from pydantic import BaseModel
from enum import Enum, IntEnum

# for development

class Przelewy24GatewayConfiguration(BaseModel):
    register_url: str



class Przelewy24Credetial(BaseModel):
    pass




def conf_loader():
    pass