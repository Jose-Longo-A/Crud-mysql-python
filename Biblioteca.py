import mysql.connector

# conecta ao banco de dados
conn = mysql.connector.connect(host='localhost', 
                               database='Biblioteca', 
                               user='root',
                               password='root',
                               port = '700')

print("Contectado ao banco de dados MySQL")

tabela_livros = """
CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    ano_publicacao INT,
    editora VARCHAR(50)
)
"""

tabela_usuarios= """
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(50),
    telefone VARCHAR(20)
)
"""

tabela_emprestimos= """
CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    livro_id INT,
    usuario_id INT,
    data_emprestimo DATE NOT NULL,
    data_devolucao DATE,
    FOREIGN KEY (livro_id) REFERENCES livros(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
"""

cursor= conn.cursor()
cursor.execute(tabela_livros)
print("Tabela Livros criada com sucesso.")
cursor.execute(tabela_usuarios)
print("Tabela Usuarios criada com sucesso.")
cursor.execute(tabela_emprestimos)
print("Tabela Emprestimos criada com sucesso.")

conn.close()
print("Conexão fechada.")