class Filial:
    def __init__(self, codigo, nome, endereco, contato):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.estoque_filial = []

    def __str__(self):
        return f"FL#{self.codigo},{self.nome},{self.endereco},{self.contato}"