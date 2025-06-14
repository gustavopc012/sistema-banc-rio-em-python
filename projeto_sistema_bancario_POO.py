from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @staticmethod
    def nova_conta(cliente, numero):
        return Conta(numero, cliente)

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        self.historico.adicionar_transacao(Saque(valor))
        print(f"Saque de R${valor:.2f} realizado.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor))
        print(f"Depósito de R${valor:.2f} realizado.")
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if valor > self.limite:
            print("Saque excede o limite por saque.")
            return False
        if self.numero_saques >= self.limite_saques:
            print("Limite de saques diários atingido.")
            return False
        resultado = super().sacar(valor)
        if resultado:
            self.numero_saques += 1
        return resultado

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


cliente1 = PessoaFisica("João Silva", "12345678900", "01/01/1990", "Rua Exemplo, 123")
conta1 = ContaCorrente(1, cliente1)
cliente1.adicionar_conta(conta1)

cliente1.realizar_transacao(conta1, Deposito(1000))
cliente1.realizar_transacao(conta1, Saque(200))

print("\n=== Extrato ===")
for transacao in conta1.historico.transacoes:
    print(transacao)
print(f"Saldo final: R${conta1.saldo:.2f}")
