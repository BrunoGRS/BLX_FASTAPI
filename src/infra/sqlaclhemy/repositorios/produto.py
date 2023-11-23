from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlaclhemy.models import model

class RepositorioProduto():
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto:schemas.Produto):
        db_produto = model.Produto(nome=produto.nome, valor = produto.valor, 
                                   descricao = produto.descricao, 
                                   disponibilidade = produto.disponibilidade )#transforma schema em modelo
    
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(model.Produto).all()
        return produtos

    def obter(self, produto:schemas.Produto, id):
        produto = model.Produto.get(id = produto.id)
        print(produto)

    def remover(self):
        pass

