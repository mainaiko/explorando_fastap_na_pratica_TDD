from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from workoutapi.categoria.models import CategoriaModel
    from workoutapi.centro_treinamento.models import CentroTreinamentoModels

from datetime import datetime

from workoutapi.contrib.models import BaseModel

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey, String, Integer, Float

class AtletaModels(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    creat_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    categoria: Mapped["CategoriaModel"] = relationship(back_populates="atleta")
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"))

    centro_treinamento: Mapped["CentroTreinamentoModels"] = relationship(back_populates="atleta")
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centro_treinamento.pk_id"))