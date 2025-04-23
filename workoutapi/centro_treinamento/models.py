from contrib import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, String, relationship
from atleta.models import AtletaModels

class CentroTreinamentoModels(BaseModel):
    __tablename__ = "centro_treinamento"

    pk_id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(20), nullable=False)
    endereco: Mapped[str] = mapped_column(String(50), nullable=False)
    proprietario: Mapped[str] =mapped_column(String(20), nullable=False)
    centro_treinamento: Mapped[AtletaModels] = relationship(back_populates="centro_treinamento")