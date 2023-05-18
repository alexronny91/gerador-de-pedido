function validarFormulario(nomeFormulario) {
    if (nomeFormulario == 'cliente') {
        
        var nome = document.getElementById('campo-nome').value;
        var telefone = document.getElementById('telefone').value;
        var cpfCnpj = document.getElementById('cpf-cnpj').value;
    
        if (!nome || !telefone || !cpfCnpj) {
            alert('Por favor, preencha todos os campos obrigatórios!');
            return false;
        }
    
        return true;

    } 
    
    if (nomeFormulario == 'produto-servico') {
        var nomeDescricao = document.getElementById('input-cadastro-nome-descricao').value;
        var precoUnitario = document.getElementById('input-cadastro-valor-unitario').value;
        
        if (!nomeDescricao || !precoUnitario) {
            alert('Por favor, preencha todos os campos!');
            return false;
        }
    
        return true;
    }
    
    if (nomeFormulario == 'pedido') {
        var cliente = document.getElementById('option-cliente').value;
        var produto = document.getElementById('option-produto-servico').value;
        var quantidade = document.getElementById('quantidade-produtos-servicos').value;
        
        if (!cliente || !produto || !quantidade) {
            alert('Por favor, preencha todos os campos!');
            return false;
        }
    
        return true;
    }
}