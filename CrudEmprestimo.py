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

def EMPRESTIMO():
    cursor = conn.cursor()
    
    def add_emprestimo():
        
        Livro_id = int(input("Livro_id: "))
        Usuario_id = int(input("Usuario_id: "))
        dt_emprestimo = int(input("Data de emprestimo: "))
        dt_devolucao = int(input("Data de devolução: "))
        
        sql = 'insert into emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao) values (%s, %s, %s, %s)'
        cursor.execute(sql, (Livro_id, Usuario_id, dt_emprestimo, dt_devolucao))
        conn.commit()
        print("Registros inseridos com sucesso.")
        
    def listar_emprestimos():
        
        cursor.execute('''select * from emprestimos
                            inner join livros
                            l on emprestimos.livro_id = l.id
                            inner join usuarios
                            u on emprestimos.usuario_id = u.id;
                        ''')
        print("")
        for linha in cursor.fetchall():
            print(linha)
    
    def atualizar_emprestimo():
        
        id = int(input("Digite o id do emprestimo que deseja atualizar: "))
        Livro_id = int(input("Livro_id: "))
        Usuario_id = int(input("Usuario_id: "))
        dt_emprestimo = input("Data de emprestimo: ")
        dt_devolucao = input("Data de devolução: ")
        
        if id == None:
            print("Id não encontrado.")
        else:
            sql = 'update emprestimos set livro_id = %s, usuario_id = %s, data_emprestimo = %s, data_devolucao = %s where id = %s'
            cursor.execute(sql, (Livro_id, Usuario_id, dt_emprestimo, dt_devolucao, id))
            conn.commit()
            
            print("Registro atualizado com sucesso.")
            
    def deletar_emprestimo():
        
        id = int(input("Digite o id do emprestimo que deseja deletar: "))
        
        sql = 'delete from emprestimos where id = %s'
        cursor.execute(sql, (id,))
        conn.commit()

        print("registo excluído com sucesso.")

    while True:
        print("- MENU CRUDE EMPRESTIMOS -")
        print("")
        print("1 - Adicionar emprestimo")
        print("2 - Listar emprestimos")
        print("3 - Atualizar emprestimo")
        print("4 - Deletar emprestimo")
        print("5 - Sair")
        print("")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            add_emprestimo()
        if opcao == 2:
            listar_emprestimos()
        elif opcao == 3:
            atualizar_emprestimo()
        elif opcao == 4:
            deletar_emprestimo()
        elif opcao == 5:
            break
        else:
            print("Opção inválida.")
