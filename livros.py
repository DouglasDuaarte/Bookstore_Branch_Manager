class Livros:
    def __init__(self, titulo, codigo, editora, area, ano, valor, quantidadeEstoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.quantidadeEstoque = quantidadeEstoque

    def __str__(self):
        valortotal = self.valor * self.quantidadeEstoque
        return (f">>>>>Cod#{self.codigo}\n"
                f"Titulo/Editora: {self.titulo}/{self.editora}\n"
                f"Categoria: {self.area}\n"
                f"Valor: {self.valor}\n"
                f"Estoque: {self.quantidadeEstoque}\n"
                f"Valor total em estoque: R${valortotal:.2f}\n"
                "-----------------------")

#add class and methods livros





