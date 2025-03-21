from livros import Livros

class Livraria():
    def __init__(self):
        self.livros = [
            Livros("O Senhor dos Anéis", 1, "HarperCollins", "Fantasia", 1954, 59.90, 10),
            Livros("O Hobbit", 2, "HarperCollins", "Fantasia", 1937, 39.90, 15),
            Livros("Jogos Vorazes", 3, "Rocco", "Ficção Científica", 2008, 29.90, 20)
        ]
#add methods to Livraria
    def cadastroLivros(self):
        titulo = input("Titulo do livro: ") 
        codigo = int(input("Informe o codigo do livro: "))
        editora = input("Informe a editora do livro: ")
        area = input("Informe o genero: ")
        ano = int(input("Informe seu ano de lançamento: "))
        valor = float(input("Qual valor deste livro: "))
        quantidadeEstoque = int(input("Quantidade de livros disponiveis: "))

        livro = Livros(titulo, codigo, editora, area, ano, valor, quantidadeEstoque)
      
        self.livros.append(livro)
    
    def listarLivros(self):
        for livro in self.livros:
            print(livro)

    def buscarLivros(self):
        titulo = input("Informe o titulo do livro: ")
        for livro in self.livros:
            if livro.titulo.lower==titulo.lower:
                print(livro)
                break   
    
    def buscarValor(self):
        valor = float(input("Informe o valor do livro: "))
        for livro in self.livros:
            if livro.valor<valor:
                print(livro)
                break

    def buscarArea(self):
        area = input("Informe a area do livro: ")
        for livro in self.livros:
            if livro.area.lower==area.lower:
                print(livro)
                break
    
    
    def buscarValorEstoqueMaior(self):
        valor = float(input("Informe o valor total em estoque: "))
        for livro in self.livros:
            valortotal = livro.valor * livro.quantidadeEstoque
            if valortotal > valor:
                print(livro)
                break

#add Menu requirements 6 
if __name__ == "__main__":
    livraria = Livraria()
    while True:
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro por Título")
        print("4. Buscar Livro por Valor")
        print("5. Buscar Livro por Área")
        print("6. Buscar Livro por Valor Total em Estoque Maior que o Indicado")
        print("7. Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            livraria.cadastroLivros()
        elif opcao == 2:
            livraria.listarLivros()
        elif opcao == 3:
            livraria.buscarLivros()
        elif opcao == 4:
            livraria.buscarValor()
        elif opcao == 5:
            livraria.buscarArea()
        elif opcao == 6:
            livraria.buscarValorEstoqueMaior()
        elif opcao == 7:
            break
        else:
            print("Opção inválida!")