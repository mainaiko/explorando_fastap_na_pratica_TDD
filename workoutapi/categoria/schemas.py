from typing import Annotated
from pydantic import BaseModel, Field
from contrib import BaseSchema

class Categoria(BaseSchema):
    modalidade: Annotated[str, Field(description="Nome da Modalidade", examples="Strongman", max_length=20)]
    categoria: Annotated[str, Field(description="open ou natural", examples="natural", max_length=20)]
    acessorios: Annotated[str, Field(description="Acessorios utilizados", examples="munhequeira, joelheira, cinturao", max_length=50)]
