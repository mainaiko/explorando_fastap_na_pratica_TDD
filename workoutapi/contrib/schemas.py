from contrib import BaseModel

class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_atributes = True