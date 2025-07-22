from datetime import datetime

class Cliente:
    def __init__(self, i, n, e, f, b):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
    def set_nome(self, nome2):
        self.__nome = nome2
    def get_nome(self):
        return self.__nome
    def get_id(self):
        return self.__id 
    def set_email(self, email2):
        self.__email = email2
    def get_email(self):
        return self.__email
    def set_fone(self, fone2):
        self.__fone = fone2 
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
        
class ClienteUI:
    __clientes = []

    @classmethod
    def main(cls):
        op = 0
        while op != 8:
            op = cls.menu()
            if op == 1: cls.inserir()
            if op == 2: cls.listar()
            if op == 3: cls.listar_id()
            if op == 4: cls.atualizar()
            if op == 5: cls.excluir()
            if op == 6: cls.abrir()
            if op == 7: cls.salvar()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Listar por ID, 4-Atualizar, 5-Excluir, 6-Abrir, 7-Salvar, 8-Fim")
        return int(input("Informe uma opção: "))
    
    @classmethod
    def inserir(cls):
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        for c in cls.__clientes:
            if c.get_email() == email:
                print("Email já cadastrado. Digite novamente")
                return
        id = 1
        for c in cls.__clientes:
            id += 1
        c = Cliente(id, nome, email, fone)
        cls.__clientes.append(c)

    @classmethod
    def listar(cls):
        if len(cls.__contatos) == 0:
            print("Nenhum contato cadastrado")
        for c in cls.__clientes:
            print(c)

    @classmethod
    def listar_id(cls, id):
        for c in cls.__clientes:
            if c.get_id() == id: return c
        return None    

    @classmethod
    def atualizar(cls):
        cls.listar()
        id = int(input("Informe o id do contato a ser atualizado: "))
        c = cls.listar_id(id)
        if c == None: 
            print("Esse cliente não existe")
        else:
            nome2 = input("Informe o novo nome: ")
            email2 = input("Informe o novo email: ")
            fone2 = input("Informe o novo fone: ")
            c.set_nome(nome2)
            c.set_email(email2)
            c.set_fone(fone2)
            print("cliente atualizado")

    @classmethod
    def excluir(cls):
        cls.listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        c = cls.listar_id(id)
        if c == None: 
            print("Esse cliente não existe")
        else: 
            cls.__clientes.remove(c)
            
    @classmethod
    def abrir(cls):
        pass

    @classmethod
    def salvar(cls):
        pass

ClienteUI.main()