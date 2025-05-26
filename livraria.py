from livros import Livros
import os
from filial import Filial

#v3.1 create branch stores

class Livraria():
    def __init__(self):
        self.estoque_geral = [
            Livros("O Senhor dos Anéis", 1, "HarperCollins", "Fantasia", 1954, 59.90, 10),
            Livros("O Hobbit", 2, "HarperCollins", "Fantasia", 1937, 39.90, 15),
            Livros("Jogos Vorazes", 3, "Rocco", "Ficção Científica", 2008, 29.90, 20)
        ]
        self.filiais = {} #guardo minhas filiais num dicionario. depois acesso por chave 

        
#add methods to Livraria versão antiga

#v1/v2   
    def listarLivros(self):
        for livro in self.estoque_geral:
            print(livro)

#v3.4 add att method the search 
    def buscarLivros(self):
        if not self.filiais:
            print("Nenhuma Filial Cadastrada!")
            return
        
        print(f"\n--Filiais Disponiveis--")
        for cod, filial in self.filiais.items():
            print(f"Codigo: {cod} - Nome: {filial.nome}")

        try:
            codigo = int(input("Digite o Codigo da Filial que deseja Buscar: "))

            if codigo not in self.filiais:
                print ("Codigo da filial invalido!")
                return
            
            titulo = input("Digite o titulo do livro que deseja buscar: ").strip().lower()

            encontrado = None

            for livro in self.filiais[codigo].estoque_filial:
                if livro.titulo.lower() == titulo:
                    encontrado = livro
                    break
            if encontrado:
                encontrado.mostrarDados()
            else:
                print("Não Encontrado em Estoque")
        
        except ValueError:
            print("Valor errado, digite um dos codigos existentes")


#v3.4                        
    
    def buscarValor(self):
        if not self.filiais:
            print("Nenhuma Filial Cadastrada!")
            return
        
        print(f"\n--Filiais Disponiveis--")
        for cod, filial in self.filiais.items():
            print(f"Codigo: {cod} - Nome: {filial.nome}")

        try:
            codigo = int(input("Digite o código da filial onde deseja buscar o livro: "))

            if codigo not in self.filiais:
                print("Código de filial inválido.")
                return

            valor = float(input("Digite o valor do livro que deseja buscar: "))
            encontrados = []

            for livro in self.filiais[codigo].estoque_filial:
                if livro.valor <= valor:
                    encontrados.append(livro)

            if encontrados:
                for livro in encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado com esse valor na filial selecionada.")

        except ValueError:
            print("Entrada inválida. Informe um número.")



      

#v3.4 area

    def buscarArea(self):
        if not self.filiais:
            print("Nenhuma filial cadastrada.")
            return

        print("\nFiliais disponíveis:")

        for cod, filial in self.filiais.items():
            print(f"Código: {cod} - Nome: {filial.nome}")

        try:
            codigo = int(input("Digite o código da filial onde deseja buscar o livro: "))
            if codigo not in self.filiais:
                print("Código de filial inválido.")
                return
            

            area = input("Digite a área do livro que deseja buscar: ").strip().lower()
            encontrados = []

            for livro in self.filiais[codigo].estoque_filial:
                if livro.area.lower() == area:
                    encontrados.append(livro)

            if encontrados:
                for livro in encontrados:
                    print(livro)
                
            
            print("Nenhum livro encontrado com essa área na filial selecionada.")

        except ValueError:
            print("Entrada inválida. Informe um número.")
                

#v3.4 att  estoque maior
        
    def buscarValorEstoqueMaior(self):
       
        if not self.filiais:
            print("Nenhuma filial cadastrada.")
            return

        print("\nFiliais disponíveis:")
        for cod, filial in self.filiais.items():
            print(f"Código: {cod} - Nome: {filial.nome}")

        try:
            codigo = int(input("Digite o código da filial onde deseja buscar os livros: "))
            if codigo not in self.filiais:
                print("Código de filial inválido.")
                return

            minimo = float(input("Digite o valor mínimo total em estoque: "))
            encontrados = []

            for livro in self.filiais[codigo].estoque_filial:
                valor_total = livro.valor * livro.quantidade
                if valor_total > minimo:
                    encontrados.append(livro)

            if encontrados:
                print(f"\nLivros com valor total em estoque maior que {minimo}:")
                for livro in encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado com valor total acima do mínimo.")

        except ValueError:
            print("Entrada inválida. Informe números corretamente.")
                


#V2.1 08/04/2024 add new function (7) 
#v3 mantive a estoque geral
    def carregarLivrosEstoqueGeral (self):
        try:
            with open ("Estoque_geral.txt", "r") as arquivo: #with open ele abre e fecha automaticamente e o AS é como se fosse um apelido para o programa .txt
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
                        self.estoque_geral.append(livro)

                        print("Livros carregados")

                
        except FileNotFoundError:
            print("Arquivo 'estoque_geral.txt' não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar os livros: {e}")



#V2.2 20/04/2024 add new function general stock (8) 

    def salvarArquivoEstoqueGeral(self):
        try:
            with open("estoque_geral.txt", "w", encoding="utf-8") as arquivo: #Abre o arquivo no modo escrita.
                for livro in self.livros:
                    linha = f"{livro.codigo},{livro.titulo},{livro.ano},{livro.area},{livro.editora},R${livro.valor:.2f},{livro.quantidadeEstoque}\n"
                    arquivo.write(linha) #Escreve cada livro no arquivo.
            print("Arquivo de estoque atualizado com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o arquivo: {e}")
    


#v3.1 add function new brench:

    def cadastrarFilial(self):
        
        codigo = int(input("Informe o codigo da Filial(Apenas numerico): "))
        nome = input("Nome da filial: ")
        endereco = input("Informe o endereço(exp: rua A,98): ")
        contato = input("Informe um numero de contato da filial: ")
        if codigo in self.filiais:
            print("Filial já existe! ")
            return
        
        nova_Filial = Filial(codigo, nome, endereco, contato)
        self.filiais[codigo] = nova_Filial
        print(f"Filial: {nome} cadastrada com sucesso!!!")

#v3.1 register books in branches method:

    def cadastrarLivroEmFilial(self):
        if not self.filiais:
            print("Cadastre Uma Filial Primeiro! ")
            return
        titulo = input("Titulo do livro: ")
        codigo = int(input("Codigo do livro: "))
        editora = input("Editora do livro: ")
        area = input("Gênero do livro: ")
        ano = int(input("Ano do livro: "))
        valor = float(input("Valor do livro: "))
        quantidadeEstoque = int(input("Estoque do livro: "))

        print("\nfiliais Disponiveis:")
        for cod, filial in self.filiais.items():
            print(f"{cod} - {filial.nome}") #aqui nesse bloco eu mostro as filiais disponiveis para armazenar nos estoques.

        filial_codigo = int(input("Digite o Codigo da filial que voce esta cadastrando o livro: "))
       

        if filial_codigo not in self.filiais:
            print("Codigo invalido!")
            return
        
        livro = Livros(titulo, codigo, editora, area, ano, valor, quantidadeEstoque) #bloco que adiciona o livro a filial.
        self.filiais[filial_codigo].estoque_filial.append(livro) 

        existe = any(l.codigo == codigo for l in self.estoque_geral) #verifica e adiciona ao estoque geral
        if not existe:
            self.estoque_geral.append(livro)

        print("____Livro cadastrado___\n")


#V3.2 18/05 add function branch stock save/charge

    def salvarArquivosEstoqueFilial(self, codigo_filial):
        if codigo_filial not in self.filiais:
            print("Filial não encontrada.")
            return
        
        filial = self.filiais[codigo_filial]
        nome_arquivo = f"Estoque_filial_{filial.codigo}.txt"

        try:
            with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                linha_filial = f"#FL{filial.codigo}, {filial.nome}, {filial.endereco}, {filial.telefone}"
                arquivo.write(linha_filial)

                for livro in filial.estoque_filial:
                    linha_livro = f"{livro.codigo},{livro.titulo},{livro.ano},{livro.area},{livro.editora},{livro.valor:.2f},{livro.quantidadeEstoque}\n" 
                    arquivo.write(linha_livro)

                print(f"Estoque da filial {filial.nome} salvo no arquivo {nome_arquivo}.")


        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o arquivo: {e}")



    def carregarEstoqueFilial(self):

        try:
            for nome_arquivo in os.listdir():
                if nome_arquivo.startswith("Estoque_filial_") and nome_arquivo.endswith(".txt"):
                    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                        linhas = arquivo.readlines()

                        if not linhas or not linhas[0].startswith("#FL"):
                            print(f"Arquivo {nome_arquivo} com formato invalido!")
                            continue  #esse continue impede o uso de 'linhas' abaixo se estiver inválido

                        dados_filial = linhas[0].strip().split(",")
                        cod_filial = int(dados_filial[0][3:])  #Pula "#FL" [:splice] pefa do indice em diante
                        nome = dados_filial[1].strip()
                        endereco = dados_filial[2].strip()
                        contato = dados_filial[3].strip()

                        self.filiais[cod_filial] = Filial(cod_filial, nome, endereco, contato)

                        for linha in linhas[1:]:
                            dados = linha.strip().split(",")
                            if len(dados) != 7:
                                print(f"Erro na linha: {linha}")
                                continue

                            codigo = int(dados[0])
                            titulo = dados[1]
                            ano = int(dados[2])
                            area = dados[3]
                            editora = dados[4]
                            valor = float(dados[5].replace("R$", "").replace(",", "."))
                            quantidadeEstoque = int(dados[6])

                            livro = Livros(titulo, codigo, editora, area, ano, valor, quantidadeEstoque)
                            self.filiais[cod_filial].estoque_filial.append(livro)

                            if not any(l.codigo == codigo for l in self.estoque_geral):
                                self.estoque_geral.append(livro)

            print("\nEstoques das filiais carregados com sucesso!")

        except Exception as e:
            print(f"Ocorreu um erro ao carregar os estoques das filiais: {e}")  


#v3.3 add function stock listing 


    def listagemEstoque(self):
        if not self.filiais:
            print("Nenhuma filial cadastrada. ")
            return

        print("\n >>Filiais Disponiveis<<")

        for cod, filial in self.filiais.items():  #Desempacotando o dicionario
            print(f"{cod} - {filial.nome}")

        try:
            codigo = int(input("Informe o codigo da filial que deseja consultar: "))
        except ValueError:
            print("Codigo invalido! (digite um numero de uma filial existente) ")
            return

        filial = self.filiais.get(codigo)
        if not filial:
            print("Filial não encontrada.")
            return

        if not filial.estoque_filial:
            print(f"Filial {filial.nome} não possui livros em estoque")
            return

        print(f"\nEstoque da Filial -> {filial.nome}:")
        valor_total = 0
        for livro in filial.estoque_filial:
            print(livro)
            valor_total += livro.valor * livro.quantidadeEstoque

        print(f"\nValor total do estoque: R${valor_total:.2f}")

#v3.4

#v3.5 add function search for cod
     
    def buscarPorCodigo (self):
        codigo_livro = int(input("Informe o codido do livro que deseja verificar: ").strip())

        encontrado = False
        total_valor = 0
        resultado_filiais =[]

        for cod_filial, filial in self.filiais.items():
            for livro in filial.estoque_filial:
                if livro.codigo == codigo_livro:
                    if not encontrado:
                        encontrado = True
                        print(f"___Encontrados na busca___\n")
                        print(f"\nCod#{livro.codigo}")
                        print(f"Título/Editora: {livro.titulo}/{livro.editora}")
                        print(f"Categoria: {livro.area}")
                        print(f"Ano: {livro.ano}")
                    valor_total_filial = livro.valor * livro.quantidadeEstoque
                    total_valor += valor_total_filial 
                    resultado_filiais.append(f"Valor: R$ {livro.valor:.2f} >>> Filial {filial.nome}, estoque: {livro.quantidadeEstoque} unidades")
        
        if encontrado:
            for linha in resultado_filiais:
                print(linha)
            print(f"Valor total em estoque: R$ {total_valor:.2f}")

        else:
             print("\nLivro não encontrado em nenhuma filial.")



#trocando por swich-case para melhor visualização do menu
if __name__ == "__main__":
    livraria = Livraria()
    while True:
        print("\n====== Menu da Livraria ======")
        print("1. Cadastrar Nova Filial")
        print("2. Cadastrar Livro em uma Filial")
        print("3. Listar Livros do Estoque Geral")
        print("4. Listar Estoque de uma Filial")
        print("5. Buscar Livro por Título em Filial")
        print("6. Buscar Livro por Valor em Filial")
        print("7. Buscar Livro por Área em Filial")
        print("8. Buscar Livros com Valor Total em Estoque Maior que o Indicador em Filial")
        print("9. Carregar Estoque Geral de Arquivo")
        print("10. Salvar Estoque Geral em Arquivo")
        print("11. Carregar Estoques das Filiais de Arquivos")
        print("12. Salvar Estoque de uma Filial em Arquivo")
        print("13. Buscar por codigo, entre as filiais")
        print("0. Encerrar Sistema")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        match opcao:
            case 1:
                livraria.cadastrarFilial()
            case 2:
                livraria.cadastrarLivroEmFilial()
            case 3:
                livraria.listarLivros()
            case 4:
                livraria.listagemEstoque()
            case 5:
                livraria.buscarLivros()
            case 6:
                livraria.buscarValor()
            case 7:
                livraria.buscarArea()
            case 8:
                livraria.buscarValorEstoqueMaior()
            case 9:
                livraria.carregarLivrosEstoqueGeral()
            case 10:
                livraria.salvarArquivoEstoqueGeral()
            case 11:
                livraria.carregarEstoqueFilial()
            case 12:
                codigo = int(input("Informe o código da filial para salvar o estoque: "))
                livraria.salvarArquivosEstoqueFilial(codigo)
            case 13:
                livraria.buscarPorCodigo()
            case 0:
                salvar = input("Deseja atualizar o arquivo de estoque antes de encerrar? (s/n): ").strip().lower()
                if salvar == "s":
                    livraria.salvarArquivoEstoqueGeral()
                print("Encerrando o sistema...")
                break
            case _:
                print("Opção inválida! Tente novamente.")