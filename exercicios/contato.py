from datetime import datetime
import json

class Contato:
    def __init__(self, i, n, e, f, b):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
        self.__nasc = b
        self.set_nasc(self.__nasc) 
    def set_nasc(self, b):
        if b > datetime.today(): 
            raise ValueError("A data de nascimento é inválida")
        self.__nasc = b
    def get_nasc(self):
        return self.__nasc
    def set_nome(self, n):
        if n == "": raise ValueError("Nome não pode ser vazio.")
        self.__nome = n
    def get_nome(self):
        return self.__nome
    def set_id(self, i):
        if i < 0: raise ValueError("ID não pode ser negativo.")
        self.__id = i
    def get_id(self):
        return self.__id 
    def set_email(self, e):
        self.__email = e
    def get_email(self):
        return self.__email
    def set_fone(self, f):
        self.__fone = f
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc.strftime('%d/%m/%Y')}"
    def dict1(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "e-mail": self.__email,
            "fone": self.__fone,
            "nasc": self.__nasc.strftime('%d/%m/%Y')
        }
    @classmethod
    def dict2(cls, d):
        nasc = datetime.strptime(d["nasc"], '%d/%m/%Y')
        return cls(d["id"], d["nome"], d["e-mail"], d["fone"], nasc)

class ContatoUI:
    __contatos = []

    @classmethod
    def main(cls):
        op = 0
        while op != 10:
            op = cls.menu()
            if op == 1: cls.inserir()
            if op == 2: cls.listar()
            if op == 3: cls.listar_id()
            if op == 4: cls.atualizar()
            if op == 5: cls.excluir()
            if op == 6: cls.pesquisar()
            if op == 7: cls.aniversariantes()
            if op == 8: cls.abrir()
            if op == 9: cls.salvar()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Listar pelo ID, 4-Atualizar, 5-Excluir, 6-Pesquisar, 7-Aniversariantes, 8-Abrir, 9-Salvar, 10-Fim")
        return int(input("Informe uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = int(input("Informe o ID: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        nasc = datetime.strptime(input("Informe a data de nascimento (dd/mm/aaaa): "), "%d/%m/%Y")
        for c in cls.__contatos:
            if c.get_email() == email:
                print("Email já cadastrado. Digite novamente")
                return
            if c.get_id() == id:
                print("ID já cadastrado. Digite novamente")
                return
        c = Contato(id, nome, email, fone, nasc)
        cls.__contatos.append(c)

    @classmethod
    def listar(cls):
        if len(cls.__contatos) == 0:
            print("Nenhum contato cadastrado")
        for c in cls.__contatos:
            print(c)

    @classmethod
    def listar_id(cls):
        id = int(input("Informe o id do contato: "))
        for c in cls.__contatos:
            if c.get_id() == id: 
                print(c)
                return
        return None    
    
    @classmethod
    def buscar_id(cls, id):
        for c in cls.__contatos:
            if c.get_id() == id:
                return c
        return None

    @classmethod
    def atualizar(cls):
        cls.listar()
        id = int(input("Informe o id do contato: "))
        c = cls.buscar_id(id)
        if c == None: 
            print("Esse contato não existe")
        else:
            nome2 = input("Informe o novo nome: ")
            email2 = input("Informe o novo email: ")
            fone2 = input("Informe o novo fone: ")
            c.set_nome(nome2)
            c.set_email(email2)
            c.set_fone(fone2)
            print("Contato atualizado")

    @classmethod
    def excluir(cls):
        cls.listar()
        id = int(input("Informe o id do contato: "))
        c = cls.buscar_id(id)
        if c == None: 
            print("Esse contato não existe")
        else: 
            cls.__contatos.remove(c)

    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome do contato: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome):
                print(c)
    @classmethod
    def aniversariantes(cls):
        mes = int(input("Informe o mês para ver os aniversariantes: "))
        achou = False
        for c in cls.__contatos:
            if c.get_nasc().month == mes:
                print(c)
                achou = True
        if achou == False:
            print("Não há nenhum contato que faz aniversário nesse mês")

    @classmethod
    def abrir(cls, nome_arq="contatos.json"):
        with open(nome_arq, mode="r") as arquivo:
            contatos_json = json.load(arquivo)
            for obj in contatos_json:
                c = Contato.dict2(obj)
                cls.__contatos.append(c)
        print("Contatos carregados")

    @classmethod
    def salvar(cls, nome_arq="contatos.json"):
        lista = []
        for c in cls.__contatos:
            lista.append(c.dict1())
        with open(nome_arq, mode="w") as arquivo:
            json.dump(lista, arquivo)
        print("Contatos salvos")


ContatoUI.main()