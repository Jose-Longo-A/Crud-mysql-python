import mysql.connector
from Biblioteca.CrudEmprestimo import EMPRESTIMO
from Biblioteca.CrudLivros import LIVROS
from Biblioteca.CrudUsuarios import USUARIO

conn = mysql.connector.connect(host='localhost', 
                                database='Biblioteca', 
                                user='root',
                                password='root',
                                port = '700')

print("-------------------------------------")
print("Contectado ao banco de dados MySQL")
print("-------------------------------------")
print("")

while True:
    print("- MENU PRINCIPAL -")
    print("")
    print("- O que quer fazer?")
    print("1 - USUÁRIO")
    print("2 - LIVROS")
    print("3 - EMPRESTIMO")
    print("4 - Sair")
    print("")

    opcao = int(input("Digite a opção desejada: "))
    print("")

    if opcao == 1:
        USUARIO()
    elif opcao == 2:
        LIVROS()
    elif opcao == 3:
        EMPRESTIMO()
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")

