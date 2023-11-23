from pydantic import BaseModel
from typing import Optional, List


class Produto(BaseModel):
    id: int
    nome: str
    valor: float
    descricao: str
    disponibilidade: bool = False

class User(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    produtos: List[Produto]

class Pedido(BaseModel):
    id: int
    usuario: User #relaciona com a class user para acessar os dados
    produto: Produto #relaciona com a class user para acessar os dados
    quantidade: int
    entrega: bool = True
    endereco: str
    observacao: Optional[str] = "Sem Observação"

class Lista(BaseModel):
    id: int
    vendas: List[Pedido]
    pedidos: List[Pedido]