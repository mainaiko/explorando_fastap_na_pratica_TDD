from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from workoutapi.atleta.models import AtletaModels

from workoutapi.contrib.models import BaseModel

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class CentroTreinamentoModels(BaseModel):
    __tablename__ = "centro_treinamento"

    pk_id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(50), nullable=False)
    proprietario: Mapped[str] =mapped_column(String(20), nullable=False)

    centro_treinamento: Mapped["AtletaModels"] = relationship(back_populates="centro_treinamento")