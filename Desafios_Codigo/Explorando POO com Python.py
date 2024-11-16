"""
# TODO: Crie uma classe UsuarioTelefone.
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.

class UsuarioTelefone:

    # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

        # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.

    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."


# Entrada:
nome = input()
numero = input()
plano = input()
# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:

usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)

"""

"""
# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':

class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo


# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:

    def verificar_saldo(self):
        if self.__saldo < 10:
            return "SeSeu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."


# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo:

    def mensagem_personalizada(self):
        return f"{self.verificar_saldo()}"

# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    # TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
    def verificar_saldo(self):
        mensagem= self.plano.mensagem_personalizada()
        return f"{mensagem}"






# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:

print(usuario.verificar_saldo())

"""

# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):

        self.nome = nome
        self.numero = numero
        self.plano = plano

# TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:

    def fazer_chamada(self,destinatario, duracao):
        # TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
        custo_chamada = self.plano.custo_chamada()

        # TODO: Verifique se o saldo do plano é suficiente para a chamada.
        if saldo_inicial >= custo_chamada:
            # TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
            saldo = saldo_inicial-custo_chamada
            # TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo:.2f}"
        else:
            return f"Saldo insuficiente para fazer a chamada."

# Classe Plano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

# TODO: Crie um método para verificar_saldo e retorne o saldo atual:

    def verificar_saldo(self):
        return self.saldo

# TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def custo_chamada(self):
        return duracao*0.10


# TODO: Crie um método deduzir_saldo para deduz o valor do saldo do plano:
    def deduzir_saldo(self):
        return self.saldo-self.custo_chamada()


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))