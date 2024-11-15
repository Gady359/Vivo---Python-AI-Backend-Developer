from abc import  ABC, abstractclassmethod,abstractproperty

from datetime import  datetime
from msilib.schema import Property


class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas=[]

    def realizar_transacao(self,conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self,endereco, nome, data_nascimento,cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf



class Conta():

    def __init__(self,numero,cliente):
        self._saldo=0
        self._numero=numero
        self._agencia="0001"
        self._cliente=cliente
        self._historico=Historico()

    @classmethod
    def nova_conta(cls,cliente, numero):
        return cls(numero,cliente)

    @Property
    def saldo(self):
        return self.saldo

    @Property
    def numero(self):
        return self.numero

    @Property
    def agencia(self):
        return self.agencia

    @Property
    def cliente(self):
        return self.cliente

    @property
    def historico(self):
        return self.historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self,numero,cliente,limite=500, limite_saques=3):
        super().__init__(numero,cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        def __init__(self, numero, cliente, limite=500, limite_saques=3):
            super().__init__(numero, cliente)
            self.limite = limite
            self.limite_saques = limite_saques

        def sacar(self, valor):
            numero_saques = len(
                [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
            )

            excedeu_limite = valor > self.limite
            excedeu_saques = numero_saques >= self.limite_saques

            if excedeu_limite:
                print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

            elif excedeu_saques:
                print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

            else:
                return super().sacar(valor)

            return False

        def __str__(self):
            return f"""\
                Agência:\t{self.agencia}
                C/C:\t\t{self.numero}
                Titular:\t{self.cliente.nome}
            """

class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


