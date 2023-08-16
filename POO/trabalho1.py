class Cliente: 
   def __init__(self, nome, cpf, dia):
      self.nome = nome
      self.cpf = cpf
      self.dia = dia      

class Conta:
    def __init__(self, agencia, numero, saldo, cliente):
      self.cliente = cliente 
      self.agencia = agencia
      self.numero = numero
      self.saldo = saldo
      self.depositar = depositar
      self.sacar = sacar
      self.transferir = transferir

      def depositar(self, valor):
         if(valor):

         else:
         

      def sacar(self, valor):
         
         if(valor):

        else:

      def transferir(self, valor):
         
        if(valor):
           
        else:
         

      def __repr__():
       

cliente1 = Conta("Ana", 1470, 29190, 1400, 120)   
print(f'Cliente:{cliente1.cliente} - Agência;{cliente1.agencia} - Numero:{cliente1.numero} - Saldo:{cliente1.saldo}')
