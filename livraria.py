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
            if livro.titulo.lower()==titulo.lower():
                print(livro)
                break
                   
    
    def buscarValor(self):
        valor = float(input("Informe o valor do livro: "))
        for livro in self.livros:
            if livro.valor<valor:
                print(livro)
                break
            else:
                print("Nenhum livro encontrado com esse titulo")

    def buscarArea(self):
        area = input("Informe a area do livro: ")
        for livro in self.livros:
            if livro.area.lower()==area.lower():
                print(livro)
                break
            else:
                print("Nenhum livro encontrado nessa área")
                
    
    
    def buscarValorEstoqueMaior(self):
        valor = float(input("Informe o valor total em estoque: "))
        for livro in self.livros:
            valortotal = livro.valor * livro.quantidadeEstoque
            if valortotal > valor:
                print(livro)


#V2.1 08/04/2024 add new function (8) 

    def carregarLivrosEstoque (self):
        try:
            with open ("estoque_livros.txt", "r") as arquivo: #with open ele abre e fecha automaticamente e o AS é como se fosse um apelido para o programa .txt
                for linha in arquivo:
                    dados = linha.split(",")
                    if len(dados)!=7:
                        print(f"Formato inválido na linha: {linha}") #tratamento caso o tenha entradado dado a mais. sinaliza a linha errda
                    else:

                        codigo = int(dados[0])
                        titulo = (dados[1])
                        ano = int(dados[2])
                        area = (dados[3])
                        editora = (dados[4])
                        valor = float(dados[5].replace("R$", ""))
                        quantidadeEstoque = int(dados[6])

                        livro = Livros(titulo, codigo, editora, area, ano, valor, quantidadeEstoque)
                        self.livros.append(livro)

                        print("Livros carregados")

                
        except FileNotFoundError:
            print("Arquivo 'estoque_livros.txt' não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar os livros: {e}")



#V2.2 20/04/2024 add new function (9) 

    def atualizarArquivoEstoque(self):
        try:
            with open("estoque_livros.txt", "w", encoding="utf-8") as arquivo: #Abre o arquivo no modo escrita.
                for livro in self.livros:
                    linha = f"{livro.codigo},{livro.titulo},{livro.ano},{livro.area},{livro.editora},R${livro.valor:.2f},{livro.quantidadeEstoque}\n"
                    arquivo.write(linha) #Escreve cada livro no arquivo.
            print("Arquivo de estoque atualizado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o arquivo: {e}")



#add Menu requirements 6 
#att with news functions 8, 9 e 0!
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
        print("8. Carregar Livros do Estoque")
        print("9. Atualizar Arquivo de Estoque") 
        print("0. Encerrar Atividades")
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
        elif opcao == 8:
            livraria.carregarLivrosEstoque()
        elif opcao == 9:
            livraria.atualizarArquivoEstoque()
        elif opcao == 0:
            salvar = input("Deseja atualizar o arquivo de estoque antes de encerrar? (s/n): ").strip().lower()
            if salvar == "s":
                livraria.atualizarArquivoEstoque()
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")