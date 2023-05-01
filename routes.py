from flask import render_template, request, flash, Blueprint
from models import Cliente, ProdutoServico
from database import db
import datetime as dt
from datetime import datetime

bp = Blueprint('rotas', __name__, template_folder="templates")

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
                converterDataNascimentoAbertura = datetime.strptime(dataNascimentoAbertura, '%Y-%m-%d').date()
                c = Cliente(nomeRazaoSocial, converterDataNascimentoAbertura, telefone, email, endereco, cpfCnpj, dataCadastro)
            else:
                dataNascimentoAbertura = None
                c = Cliente(nomeRazaoSocial, dataNascimentoAbertura, telefone, email, endereco, cpfCnpj, dataCadastro)
                
            
            
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
