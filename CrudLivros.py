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

def LIVROS():
    cursor = conn.cursor()
    
    def add_livro():
        titulo = input("Titulo: ")
        autor = input("Autor:  ")
        ano = int(input("Ano de publicação: "))
        editora = input("Editora: ")

        sql = 'insert into livros (titulo, autor, ano_publicacao, editora) values (%s, %s, %s, %s)'
        cursor.execute(sql, (titulo, autor, ano, editora))
        conn.commit()
        print("Registros inseridos com sucesso.")
        
    def listar_livros():
        cursor.execute('''select * from livros
                            left join emprestimos
                            e on livros.id = e.livro_id;
                        ''')
        print("")
        for linha in cursor.fetchall():
            print(linha)
    
    def atualizar_livro():
                
        id = int(input("Digite o id do livro que deseja atualizar: "))
        titulo = input("Digite o novo titulo: ")
        autor = input("Digite o novo autor: ")
        ano = int(input("Digite o novo ano de publicação: "))
        editora = input("Digite a nova editora: ")
        
        if id == None:
            print("Id não encontrado.")
        else:
            sql = 'update livros set titulo = %s, autor = %s, ano_publicacao = %s, editora = %s where id = %s'
            cursor.execute(sql, (titulo, autor, ano, editora, id))
            conn.commit()
            
            print("Registro atualizado com sucesso.")
            
    def deletar_livro():
        
        id = int(input("Digite o id do livro que deseja deletar: "))
        
        sql = 'delete from livros where id = %s'
        cursor.execute(sql, (id,))
        conn.commit()

        print("registo excluído com sucesso.")

    while True:
        print("- MENU CRUDE LIVROS -")
        print("")
        print("1 - Adicionar livro")
        print("2 - listar livros")
        print("3 - Atualizar livro")
        print("4 - Deletar livro")
        print("5 - Sair")
        print("")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            add_livro()
        if opcao == 2:
            listar_livros()
        elif opcao == 3:
            atualizar_livro()
        elif opcao == 4:
            deletar_livro()
        elif opcao == 5:
            break
        else:
            print("Opção inválida.")
