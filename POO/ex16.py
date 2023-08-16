class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        if(idade > 0):
            self.idade = idade

    def __repr__(self):
        return f'Pessoa'("{self.nome}, {self.idade}")
    
p = Pessoa(nome="fulano", idade=10)
print(p)

