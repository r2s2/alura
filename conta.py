class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def extrato(self):
        print(f"numero: {self.numero} \ntitular: {self.titular} \nsaldo: {self.saldo} \nlimite: {self.limite}")

    def transfere(self, destino, valor):
        self.saldo -= valor
        destino.saldo += valor

    def get_saldo(self):
        return self.saldo

    def get_titular(self):
        return self.titular

    def get_numero(self):
        return self.numero

    def get_limite(self):
        return self.limite

    def set_limite(self, limite):
        self.limite = limite

    def set_titular(self, titular):
        self.titular = titular

    def set_numero(self, numero):
        self.numero = numero

    def set_saldo(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return f"numero: {self.numero} \ntitular: {self.titular} \nsaldo: {self.saldo} \nlimite: {self.limite}"

    def __eq__(self, other):
        if self.numero == other.numero and self.titular == other.titular:
            return True
        else:
            return False



