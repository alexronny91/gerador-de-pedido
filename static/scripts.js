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

$(document).ready(function () {

    $('.excluir-btn').click(function () {
        var id = $(this).data('id');
        var textoH2 = $('h2').text();

        if (textoH2 == 'Clientes') {
            $.ajax({
                url: '/clientes/excluir/' + id,
                method: 'DELETE',
                contentType: 'application/json',
                success: function (response) {
                    if (response == 'Existe pedido desse cliente, não será possivel excluir.') {
                        alert(response)
                    } else {
                        var linhaRemover = $("#linha-cliente-" + id);
                        linhaRemover.remove()
                        alert(response)
                    }
                },
                error: function (error) {
                    alert('Erro ao excluir cliente: ' + error.responseText);
                }
            });
        } else if (textoH2 == 'Produtos / Serviços') {
            $.ajax({
                url: '/produtos-servicos/excluir/' + id,
                method: 'DELETE',
                contentType: 'application/json',
                success: function (response) {
                    if (response == 'Existe pedido com esse produto/serviço, não será possivel excluir.') {
                        alert(response)
                    } else {
                        var linhaRemover = $("#linha-produto-" + id);
                        linhaRemover.remove()
                        alert(response)
                    }
                },
                error: function (error) {
                    alert('Erro ao excluir cliente: ' + error.responseText);
                }
            });
        } else {
            
        }
        
        
    })

    $('.editar-btn').click(function () {
        var id = $(this).data('id');
        var textoH2 = $('h2').text();

        if (textoH2 == 'Clientes') {
            $('#nomeRazaoSocial-' + id).removeAttr('readonly');
            $('#dataNascimentoAbertura-' + id).removeAttr('readonly');
            $('#telefone-' + id).removeAttr('readonly');
            $('#email-' + id).removeAttr('readonly');
            $('#endereco-' + id).removeAttr('readonly');
            $('#cpfCnpj-' + id).removeAttr('readonly');
            $('#dataCadastro-' + id).removeAttr('readonly');
            $(this).hide();
            $('.salvar-btn[data-id="' + id + '"]').show();
        } else if (textoH2 == 'Produtos / Serviços') {
            $('#nomeDescricao-' + id).removeAttr('readonly');
            $('#valorUnitario-' + id).removeAttr('readonly');
            $(this).hide();
            $('.salvar-btn[data-id="' + id + '"]').show();
        } else {

        }
    });

    $('.salvar-btn').click(function () {
        var id = $(this).data('id');
        var textoH2 = $('h2').text();

        if (textoH2 == 'Clientes') {
            var nomeRazaoSocial = $('#nomeRazaoSocial-' + id).val();
            var dataNascimentoAbertura = $('#dataNascimentoAbertura-' + id).val();
            var telefone = $('#telefone-' + id).val();
            var email = $('#email-' + id).val();
            var endereco = $('#endereco-' + id).val();
            var cpfCnpj = $('#cpfCnpj-' + id).val();
            var dataCadastro = $('#dataCadastro-' + id).val();
    
            var data = {
                nomeRazaoSocial: nomeRazaoSocial,
                dataNascimentoAbertura: dataNascimentoAbertura,
                telefone: telefone,
                email: email,
                endereco: endereco,
                cpfCnpj: cpfCnpj,
                dataCadastro: dataCadastro
            };
    
            var btnSalvar = $(this);
            var btnEditar = $('.editar-btn[data-id="' + id + '"]');
    
            $.ajax({
                url: '/clientes/editar/' + id,
                method: 'PUT',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function (response) {
                    alert(response);
                    $('#nomeRazaoSocial-' + id).attr('readonly', 'readonly');
                    $('#dataNascimentoAbertura-' + id).attr('readonly', 'readonly');
                    $('#telefone-' + id).attr('readonly', 'readonly');
                    $('#email-' + id).attr('readonly', 'readonly');
                    $('#endereco-' + id).attr('readonly', 'readonly');
                    $('#cpfCnpj-' + id).attr('readonly', 'readonly');
                    $('#dataCadastro-' + id).attr('readonly', 'readonly');
                    btnSalvar.hide();
                    btnEditar.show();
                },
                error: function (error) {
                    alert('Erro ao atualizar cliente: ' + error.responseText);
                }
            });
        } else if (textoH2 == 'Produtos / Serviços') {
            var nomeDescricao =  $('#nomeDescricao-' + id).val();
            var valorUnitario = $('#valorUnitario-' + id).val();

            if (valorUnitario == '') {
                valorUnitario = 0
            }

            var data = {
                nomeDescricao: nomeDescricao,
                valorUnitario: valorUnitario
            }
            
            var btnSalvar = $(this);
            var btnEditar = $('.editar-btn[data-id="' + id + '"]');

            $.ajax({
                url: '/produtos-servicos/editar/' + id,
                method: 'PUT',
                contentType: 'application/json',
                data: JSON.stringify(data),
                success: function (response) {
                    if (response == 'Produto atualizado com sucesso!') {
                        alert(response);
                        $('#nomeDescricao-' + id).attr('readonly', 'readonly');
                        $('#valorUnitario-' + id).attr('readonly', 'readonly');
                        btnSalvar.hide();
                        btnEditar.show();
                    } else {
                        alert(response);
                    }
                },
                error: function (error) {
                    alert('Erro ao atualizar cliente: ' + error.responseText);
                }
            });
        } else {

        }
    });
});