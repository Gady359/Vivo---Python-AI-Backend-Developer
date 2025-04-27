import pytest
from unittest.mock import patch

from Sistema_Bancario import depositar, sacar, exibir_extrato, criar_usuario, criar_conta, filtrar_usuario, menu




def test_depositar():
    saldo, extrato = 100, ""
    saldo, extrato = depositar(saldo, 50, extrato)
    assert saldo == 150
    assert "Depósito:\tR$ 50.00" in extrato

    saldo, extrato = depositar(saldo, -10, extrato)
    assert saldo == 150  # No change
    assert "Depósito:\tR$ -10.00" not in extrato


def test_sacar():
    saldo, extrato = 100, ""
    saldo, extrato = sacar(saldo=saldo, valor=50, extrato=extrato, limite=500, numero_saques=0, limite_saques=3)
    assert saldo == 50
    assert "Saque:\t\tR$ 50.00" in extrato

    saldo, extrato = sacar(saldo=saldo, valor=200, extrato=extrato, limite=500, numero_saques=1, limite_saques=3)
    assert saldo == 50  # No change
    assert "Saque:\t\tR$ 200.00" not in extrato


def test_exibir_extrato(capsys):
    saldo, extrato = 100, "Depósito:\tR$ 100.00\n"
    exibir_extrato(saldo, extrato=extrato)
    captured = capsys.readouterr()
    assert "Depósito:\tR$ 100.00" in captured.out
    assert "Saldo:\t\tR$ 100.00" in captured.out

    saldo, extrato = 0, ""
    exibir_extrato(saldo, extrato=extrato)
    captured = capsys.readouterr()
    assert "Não foram realizadas movimentações." in captured.out
    assert "Saldo:\t\tR$ 0.00" in captured.out


def test_criar_usuario():
    usuarios = []

    def mock_input(prompt):
        return mock_inputs.pop(0)

    def mock_output(message):
        mock_outputs.append(message)

    # Testar criação de usuário
    mock_inputs = ["12345678900", "Test User", "01-01-2000", "Test Address"]
    mock_outputs = []
    criar_usuario(usuarios, input_func=mock_input, output_func=mock_output)
    assert len(usuarios) == 1
    assert usuarios[0]["nome"] == "Test User"
    assert usuarios[0]["cpf"] == "12345678900"
    assert "\n=== Usuário criado com sucesso! ===" in mock_outputs

    # Testar duplicação de usuário
    mock_inputs = ["12345678900", "Test User", "01-01-2000", "Test Address"]
    mock_outputs = []
    criar_usuario(usuarios, input_func=mock_input, output_func=mock_output)
    assert len(usuarios) == 1  # Não deve adicionar duplicatas
    assert "\n@@@ Já existe usuário com esse CPF! @@@" in mock_outputs


def test_criar_conta():
    usuarios = [{"nome": "Test User", "cpf": "12345678900", "data_nascimento": "01-01-2000", "endereco": "Test Address"}]
    contas = []
    with patch("builtins.input", side_effect=["12345678900"]):
        conta = criar_conta("0001", 1, usuarios)
    assert conta is not None
    assert conta["agencia"] == "0001"
    assert conta["numero_conta"] == 1
    assert conta["usuario"]["cpf"] == "12345678900"

    # Testar com CPF inexistente
    with patch("builtins.input", side_effect=["00000000000"]):
        conta = criar_conta("0001", 2, usuarios)
    assert conta is None