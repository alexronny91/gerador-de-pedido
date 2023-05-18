from database import db

class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True)
    nomeRazaoSocial = db.Column(db.String)
    dataNascimentoAbertura = db.Column(db.Date)
    telefone = db.Column(db.Integer)
    email = db.Column(db.String)
    endereco = db.Column(db.String)
    cpfCnpj = db.Column(db.Integer)
    dataCadastro = db.Column(db.Date)

    def __init__(self, 
                 nomeRazaoSocial, 
                 dataNascimentoAbertura,
                 telefone,
                 email,
                 endereco,
                 cpfCnpj,
                 dataCadastro):
        
        self.nomeRazaoSocial = nomeRazaoSocial
        self.dataNascimentoAbertura = dataNascimentoAbertura
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.cpfCnpj = cpfCnpj
        self.dataCadastro = dataCadastro

    def __repr__(self):
        return f'[{self.id}, {self.nomeRazaoSocial}, {self.dataNascimentoAbertura}, {self.telefone}, {self.email}, {self.cpfCnpj}, {self.dataCadastro}]'

    
class ProdutoServico(db.Model):
    __tablename__ = "produtoServico"
    id = db.Column(db.Integer, primary_key=True)
    nomeDescricao = db.Column(db.String)
    valorUnitario = db.Column(db.Float)

    def __init__(self, 
                 nomeDescricao, 
                 valorUnitario):
        
        self.nomeDescricao = nomeDescricao
        self.valorUnitario = valorUnitario

    def __repr__(self):
        return f'[{self.id}, {self.nomeDescricao}, {self.valorUnitario}]'

class Pedido(db.Model):
    __tablename__ = "pedidos"
    id = db.Column(db.Integer, primary_key=True)
    dataPedido = db.Column(db.Date)
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    idProdutoServico = db.Column(db.Integer, db.ForeignKey('produtoServico.id'))
    quantidade = db.Column(db.Integer)
    valorProdutoServico = db.Column(db.Float)
    valorTotalPedido = db.Column(db.Float)

    def __init__(self,
                 dataPedido,
                 idCliente,
                 idProdutoServico,
                 quantidade,
                 valorProdutoServico,
                 valorTotalPedido):
        
        self.dataPedido = dataPedido
        self.idCliente = idCliente
        self.idProdutoServico = idProdutoServico
        self.quantidade = quantidade
        self.valorProdutoServico = valorProdutoServico
        self.valorTotalPedido = valorTotalPedido

    def __repr__(self):
        return f'[{self.id}, {self.dataPedido}, {self.idCliente}, {self.idProdutoServico}, {self.quantidade}, {self.valorProdutoServico}, {self.valorTotalPedido}]'