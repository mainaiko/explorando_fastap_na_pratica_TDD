from contrib import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, String, relationship
from atleta.models import AtletaModels

class CategoriaModel(BaseModel):
    __tablename__ = "categorias"
    
    pk_id: Mapped[int] = mapped_column(primary_key=True)

    modalidade: Mapped[str] =mapped_column(String(50), nullable=False)
    categoria: Mapped[str] =mapped_column(String(50), nullable=False)
    acessorios: Mapped[str] =mapped_column(String(50), nullable=False)
    atleta: Mapped[AtletaModels] = relationship(back_populates="categoria")