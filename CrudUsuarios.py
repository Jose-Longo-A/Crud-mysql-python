import mysql.connector

conn = mysql.connector.connect(host='localhost', 
                                database='Biblioteca', 
                                user='root',
                                password='root',
                                port = '700')

print("-------------------------------------")
print("Contectado ao banco de dados MySQL")
print("-------------------------------------")
print("")

def USUARIO():
    cursor = conn.cursor()
    
    def add_usuario():
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")

        sql = 'insert into usuarios (nome, email, telefone) values (%s, %s, %s)'
        cursor.execute(sql, (nome, email, telefone))
        conn.commit()
        print("Registros inseridos com sucesso.")
        
    def listar_usuarios():
    
        cursor.execute('''select * from usuarios
                            left join emprestimos
                            e on usuarios.id = e.usuario_id;
                        ''')
        print("")
        for linha in cursor.fetchall():
            print(linha)
    
    def atualizar_usuario():
        
        id = int(input("Digite o id do Usuario que deseja atualizar: "))
        nome = input("Digite o novo nome: ")
        email = input("Digite o novo email: ")
        telefone = input("Digite o novo telefone: ")
        
        if id == None:
            print("Id não encontrado.")
        else:
            sql = 'update usuarios set nome = %s, email = %s, telefone = %s where id = %s'
            cursor.execute(sql, (nome, email, telefone, id))
            conn.commit()
            
            print("Registro atualizado com sucesso.")
            
    def deletar_usuario():
        
        id = int(input("Digite o id do usuario que deseja deletar: "))
        
        sql = 'delete from usuarios where id = %s'
        cursor.execute(sql, (id,))
        conn.commit()

        print("registo excluído com sucesso.")

    while True:
        print("- MENU CRUDE USUARIOS -")
        print("")
        print("1 - Adicionar usuario")
        print("2 - Listar usuarios")
        print("3 - Atualizar usuario")
        print("4 - Deletar usuario")
        print("5 - Sair")
        print("")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            add_usuario()
        elif opcao == 2:
            listar_usuarios()
        elif opcao == 3:
            atualizar_usuario()
        elif opcao == 4:
            deletar_usuario()
        elif opcao == 5:
            break
        else:
            print("Opção inválida.")
