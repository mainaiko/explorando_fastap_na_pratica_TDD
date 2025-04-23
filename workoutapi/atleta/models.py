from datetime import datetime
from contrib import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, String, Integer, Float
from sqlalchemy import DateTime


class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    creat_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)