"""
    Gerador de Senhas
        ...
        O programa Gerador de Senhas tem como objetivo gerar senhas de forma aleatória com um número de caracteres definido pelo usuário.

        Recomenda-se o uso em sistemas onde exista a necessidade de um gerador de senhas.
"""


import string
import random

class GeradorSenha():
    """
        Classe responsável por gerar as funções de inicialização e de execução do programa.

        
        Não exige parâmetros.
    """

    def __init__(self):
        """
            Função para inicialização do programa.

            Não exige parâmetros.
        """
        pass

    print("\nGerador de Senhas")

    def obter_tamanho_senha(self):
        """
            Função para obter o tamanho da senha.


            Solicita ao usuário o número de caracteres para a senha, entre 4 e 10.
                ...
                Se o valor de entrada for diferente do tipo inteiro, menor que 4 ou maior que 10, o programa emite uma mensagem de erro ao usuário.
            
            Não exige parâmetros.
        """
        while True:
            try:
                tamanho = input("\nInsira o número de caracteres para sua senha (4 a 10): ")
                if tamanho.lower() == "sair":
                    print("\nPrograma encerrado.\n")
                    exit()
                if 4 <= int(tamanho) <= 10:
                    return int(tamanho)
                else:
                    print("Entrada inválida. O tamanho deve estar entre 4 e 10.")
            except ValueError:
                print("Entrada inválida. Insira um número inteiro.")

    def gerar_senha(self):
        """
            Função para a gerar a senha.

            
            Será gerada uma lista recebendo os valores para a senha, aceitando caracteres do tipo letra (maiúscula e minúscula), número e ponto (.).
            Será gerada uma varíavel auxiliar recebendo 1 valor para cada possibilidade.
                ...
                A senha receberá os caracteres letra, número e ponto de forma aleatória, de acordo com o tamanho inserido para a senha.

            Após gerar a senha, será permitida ao usuário a opção de saída através de um loop, encerrando o programa.


            Não exige parâmetros.
        """
        tamanho = self.obter_tamanho_senha()

        senha = [
            random.choice(string.ascii_letters),  # Uma letra aleatória.
            random.choice(string.digits),         # Um número aleatório.
            random.choice("."),                   # Um ponto (".") aleatório.
            ]
        
        possibilidades = "".join([string.ascii_letters, string.digits, "."]) # Variável auxiliar recebendo as 3 possibilidades para a senha: letra, número e ponto.
        senha.extend(random.choices(possibilidades, k=tamanho-3)) # Preenche até o tamanho desejado subtraindo 3, referente a letra, número e ponto já adicionados.


        random.shuffle(senha) # Embaralha a senha gerada para garantir aleatoriedade.    
    
        print("\nSenha gerada com sucesso!")
        print("Senha do usuário: ","".join(senha))
        print("\nDeseja gerar outra senha?")
        while True:
            resposta = input("Insira 'sim' para continuar ou 'nao' para sair: ")
            if resposta == 'sim':
                return self.gerar_senha()
            elif resposta == 'nao':
                print("\nPrograma encerrado.\n")
                exit() 
            else:
                print("Entrada inválida. Tente novamente.")


"""
    Instruções para execução do programa.


    Deve-se criar uma variável que receba uma instância da classe GeradorSenha.
    Para a execução do teste, deve-se chamar o método gerar_senha() na instância criada.
        ...
        Exemplo de uso:
            
            senha = GeradorSenha()
            senha.gerar_senha()
        
    Para importar a classe, deve-se criar um novo arquivo e mantê-lo no mesmo diretório do arquivo GeradorSenha.
        ...
        Exemplo de uso:
            
            from GeradorSenha import GeradorSenha
"""