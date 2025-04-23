from typing import Annotated
from pydantic import Field, PositiveFloat
from contrib import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", examples="Joao", max_length=50)]
    cpf: Annotated[int, Field(description="CPF do atleta", examples="555.555.555-55", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", examples="25")]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", examples="81")]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", examples="1.80")]
    sexo: Annotated[str, Field(description="Sexo do atleta", examples="F", max_length=1)]