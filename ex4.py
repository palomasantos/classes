#  Crie um professor de classe com atributos nome, idade e salário, onde
# o salário deve ter um método privado que não pode ser acessado fora
# da classe.
# a. Crie um método para acessar o método privado, onde é passada
# a identificação do usuário se ele pode ou não acessar.


class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
    def __valor(self):
        return f'Você pode acessar o salário'
    
    def usuario(self,nome):
        if nome == "Paloma":
            return self.__valor()
  

a = Professor('Bianca','24','2 reais').usuario('Camila')
print(a)
