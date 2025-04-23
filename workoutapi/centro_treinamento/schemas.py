from typing import Annotated
from pydantic import Field, PositiveFloat
from contrib import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome da academia", examples="World gym",max_length=20)]
    endereco: Annotated[str, Field(description="Endereço da academia", examples="Rua das flores, 123", max_length=50)]
    proprietario: Annotated[str, Field(description="Nome do caba", examples="Jonas bombado", max_length=20)]
    