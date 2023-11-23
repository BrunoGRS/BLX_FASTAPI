from sqlaclhemy import Column, Integer, String, Float, Boolean
from src.infra.sqlaclhemy.config.database import Base

class Produto(Base):
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    valor = Column(Float)
    descricao = Column(String)
    disponibilidade = Column(Boolean, default=True)
