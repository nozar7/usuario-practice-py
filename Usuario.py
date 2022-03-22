class Usuario:
    # los atributos de clase se definen en la clase
    nombre_banco = "Primer Dojo Nacional"
    # ¡ahora nuestro método tiene 2 parámetros!
    def __init__(self , name, email_address):
    	# los asignamos en consecuencia
        self.name = name
        self.email = email_address
    	# el balance de la cuenta se establece en $0
        self.balance_cuenta = 92000
    # function hacer retiro
    def hacer_retiro(self, amount):
        self.balance_cuenta -=amount
        return self
        # print("Tienes un balance de cuenta de:", self.balance_cuenta)
    def hacer_deposito(self, amount):
        self.balance_cuenta +=amount
        return self
    def mostrar_balance_usuario(self):
        print("Estimado",self.name,"tienes un balance de cuenta de:", self.balance_cuenta)
    def transfer_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)
        print("se hizo la transferencia!!!")
guido = Usuario("Guido van Rossum", "guido@python.com")
monty = Usuario("Monty Python", "monty@python.com")
guido.hacer_deposito(100).hacer_deposito(200).hacer_deposito(300).hacer_retiro(50).mostrar_balance_usuario()
