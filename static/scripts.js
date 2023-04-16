function validarFormulario() {
    var nome = document.getElementById('campo-nome').value;
    var telefone = document.getElementById('telefone').value;
    var cpfCnpj = document.getElementById('cpf-cnpj').value;

    if (!nome || !telefone || !cpfCnpj) {
        alert('Por favor, preencha todos os campos obrigatórios!');
        return false;
    }

    return true;
}