from flask import render_template, request, Blueprint
from models import Cliente, ProdutoServico, Pedido
from database import db
import datetime as dt
from datetime import datetime
from markupsafe import Markup

bp = Blueprint('rotas', __name__, template_folder="templates")

@bp.app_template_global()
def buscarNomeCliente(listaClientes, idCliente):
    cliente = ''
    for c in listaClientes:
        if c.id == idCliente:
            cliente = c.nomeRazaoSocial
    return Markup(cliente)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route("/clientes")
def clientes():
    listaClientes = Cliente.query.all()
    return render_template('clientes.html', clientes=listaClientes)


@bp.route("/cadastrar-cliente", methods=['GET', 'POST'])
def telaCadastroCliente():
    if request.method == 'GET':
        return render_template('cadastrarCliente.html')

    if request.method == 'POST':
        nomeRazaoSocial = request.form.get('nome')
        dataNascimentoAbertura = request.form.get('data')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        endereco = request.form.get('endereco')
        cpfCnpj = request.form.get('cpf-cnpj')
        dataCadastro = dt.date.today()

        if dataNascimentoAbertura is not None and dataNascimentoAbertura != '':
            converterDataNascimentoAbertura = datetime.strptime(
                dataNascimentoAbertura, '%Y-%m-%d').date()
            c = Cliente(nomeRazaoSocial, converterDataNascimentoAbertura,
                        telefone, email, endereco, cpfCnpj, dataCadastro)
        else:
            dataNascimentoAbertura = None
            c = Cliente(nomeRazaoSocial, dataNascimentoAbertura,
                        telefone, email, endereco, cpfCnpj, dataCadastro)

        db.session.add(c)
        db.session.commit()
        return render_template('posCadastro.html', msgSucesso='Cliente cadastrado com sucesso!!!')


@bp.route("/produtos-servicos")
def produtosServicos():
    listaProdutosServicos = ProdutoServico.query.all()
    return render_template('produtos-servicos.html', produtos_servicos=listaProdutosServicos)


@bp.route("/cadastrar-produto-servico", methods=['GET', 'POST'])
def telaCadastroProdutoServico():
    if request.method == 'GET':
        return render_template('cadastrarProdutoServico.html')

    if request.method == 'POST':
        nomeDescricao = request.form.get('nome-descricao')
        valorUnitario = request.form.get('valor-unitario')

        i = ProdutoServico(nomeDescricao, valorUnitario)

        db.session.add(i)
        db.session.commit()
        return render_template('posCadastro.html', msgSucesso='Produto/Serviço cadastrado com sucesso!!!')


@bp.route("/pedidos")
def pedidos():
    listaPedidos = Pedido.query.all()
    listaClientes = Cliente.query.all()
    return render_template('pedidos.html', pedidos=listaPedidos, clientes=listaClientes)


@bp.route("/cadastrar-pedido", methods=['GET', 'POST'])
def telaCadastroPedido():
    listaPedidos = Pedido.query.all()
    listaClientes = Cliente.query.all()
    listaProdutosServicos = ProdutoServico.query.all()

    valorUnitario = 0

    if request.method == 'GET':
        return render_template('cadastrarPedido.html', pedidos=listaPedidos, clientes=listaClientes, produtos_servicos=listaProdutosServicos)

    if request.method == 'POST':
        cliente = request.form.get('cliente')
        produto = request.form.get('produto-servico')
        quantidade = request.form.get('quantidade')
        dataPedido = dt.date.today()
        valorUnitario = 0
        for p in listaProdutosServicos:
            if p.id == int(produto):
                valorUnitario = p.valorUnitario
        valorTotal = valorUnitario * int(quantidade)

        i = Pedido(dataPedido, cliente, produto, quantidade,
                   valorUnitario, valorTotal)

        db.session.add(i)
        db.session.commit()

        return render_template('posCadastro.html', msgSucesso='Pedido cadastrado com sucesso!!!')


@bp.route("/clientes/editar/<int:id>", methods=['PUT'])
def editarCliente(id):
    cliente = Cliente.query.get(id)

    if not cliente:
        return 'Cliente não encontrado', 404

    cliente.nomeRazaoSocial = request.json.get('nomeRazaoSocial')
    dataNascimentoAbertura = request.json.get('dataNascimentoAbertura')
    cliente.telefone = request.json.get('telefone')
    cliente.email = request.json.get('email')
    cliente.endereco = request.json.get('endereco')
    cliente.cpfCnpj = request.json.get('cpfCnpj')
    dataCadastro = request.json.get('dataCadastro')

    if dataNascimentoAbertura is not None and dataNascimentoAbertura != '':
        converterDataNascimentoAbertura = datetime.strptime(
            dataNascimentoAbertura, '%Y-%m-%d').date()
        cliente.dataNascimentoAbertura = converterDataNascimentoAbertura
    else:
        dataNascimentoAbertura = None
        cliente.dataNascimentoAbertura = dataNascimentoAbertura
    if dataCadastro is not None and dataCadastro != '':
        converterDataCadastro = datetime.strptime(
            dataCadastro, '%Y-%m-%d').date()
        cliente.dataCadastro = converterDataCadastro
    else:
        dataCadastro = None
        cliente.dataCadastro = dataCadastro

    db.session.commit()
    return 'Cliente atualizado com sucesso!'

@bp.route("/clientes/excluir/<int:id>", methods=['DELETE'])
def excluirCliente(id):
    cliente = Cliente.query.get(id)
    if cliente:
        pedidosCliente = Pedido.query.filter(Pedido.idCliente == id).all()
        if (len(pedidosCliente) >= 1):
            return 'Existe pedido desse cliente, não será possivel excluir.'
        else:
            db.session.delete(cliente)
            db.session.commit()
            return 'Cliente excluido com sucesso!'
    else:
        return 'Cliente não encontrado.', 404
    
@bp.route("/produtos-servicos/editar/<int:id>", methods=['PUT'])
def editarProdutoServico(id):
    produto = ProdutoServico.query.get(id)

    if not produto:
        return 'Produto não encontrado', 404
    
    nomeDescricao = request.json.get('nomeDescricao')
    valorUnitario = request.json.get('valorUnitario')
    
    if nomeDescricao is not None and nomeDescricao != '' and valorUnitario is not None and valorUnitario != 0: 
        produto.nomeDescricao = nomeDescricao
        produto.valorUnitario = valorUnitario
        db.session.commit()
        return 'Produto atualizado com sucesso!'
    else:
        return 'Todos os campos são obrigatórios!'

@bp.route("/produtos-servicos/excluir/<int:id>", methods=['DELETE'])
def excluirProdutoServico(id):
    produtoServico = ProdutoServico.query.get(id)
    if produtoServico:
        pedidosComProdutoServico = Pedido.query.filter(Pedido.idProdutoServico == id).all()
        if (len(pedidosComProdutoServico) >= 1):
            return 'Existe pedido com esse produto/serviço, não será possivel excluir.'
        else:
            db.session.delete(produtoServico)
            db.session.commit()
            return 'Produto/Serviço excluido com sucesso.'
    else:
        return 'Produto não encontrado.', 404