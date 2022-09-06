# Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma
# classe onde teremos o retorno do documento, o retorno do nome e
# verificação de tipo de pessoa, onde um método irá receber como
# parâmetro “F” ou “N” para trazer fumante ou não fumante.
# Feito isso, crie uma instância e retorne esses valores


class Pessoa:
    def __init__(self, pessoa, nome, idade):
        self.nome = nome
        self.pessoa = pessoa
        self.idade = idade
               
class PessoaFisica(Pessoa):
    def __init__(self, pessoa, cpf, nome, idade):
        self.cpf = cpf
        super().__init__(pessoa, nome, idade)
    
    def __CPF(self):
       return self.cpf

               
class PessoaJuridica(Pessoa):
    def __init__(self, pessoa, cnpj, nome, idade):
        self.cnpj = cnpj
        super().__init__(pessoa, nome, idade)
        
    def __cnpj(self):
        return f'seu CNPJ é {self.cnpj} '

pessoa1 = PessoaFisica('N','123456789','Bianca','22')        
pessoa2 = PessoaJuridica('F','12345679','Ana','22')

print(pessoa1.cpf)
print(pessoa2.cnpj)