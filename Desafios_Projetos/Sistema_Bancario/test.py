import pytest

# filepath: e:\Faculdade PUCPR\DevOps\AS1\Vivo---Python-AI-Backend-Developer\Desafios_Projetos\Sistema_Bancario\test_Sistema Bancário.py
from Sistema_Bancário import depositar, sacar, exibir_extrato, criar_usuario, criar_conta, filtrar_usuario


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
    criar_usuario(usuarios)
    assert len(usuarios) == 1
    assert usuarios[0]["cpf"] == "12345678900"  # Replace with test input

    criar_usuario(usuarios)
    assert len(usuarios) == 1  # No duplicate users


def test_criar_conta():
    usuarios = [{"nome": "Test User", "cpf": "12345678900", "data_nascimento": "01-01-2000", "endereco": "Test Address"}]
    contas = []
    conta = criar_conta("0001", 1, usuarios)
    assert conta is not None
    assert conta["agencia"] == "0001"
    assert conta["numero_conta"] == 1
    assert conta["usuario"]["cpf"] == "12345678900"

    conta = criar_conta("0001", 2, [])
    assert conta is None