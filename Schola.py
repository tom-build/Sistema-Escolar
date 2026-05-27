import sqlite3
import os
import sys
import os

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, "escola.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def criar_tabelas():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS turmas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        materia TEXT NOT NULL,
        professor_id INTEGER,
        FOREIGN KEY (professor_id) REFERENCES professores(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER,
        turma_id INTEGER,
        nota REAL,
        FOREIGN KEY (aluno_id) REFERENCES alunos(id),
        FOREIGN KEY (turma_id) REFERENCES turmas(id)
    )
    """)

    conn.commit()

def adicionar_aluno(nome):
    cursor.execute("INSERT INTO alunos (nome) VALUES (?)", (nome,))
    conn.commit()


def adicionar_professor(nome):
    cursor.execute("INSERT INTO professores (nome) VALUES (?)", (nome,))
    conn.commit()


def adicionar_turma(nome, materia, professor_id):
    cursor.execute("INSERT INTO turmas (nome, materia, professor_id) VALUES (?, ?, ?)",
                   (nome, materia, professor_id))
    conn.commit()


def adicionar_nota(aluno_id, turma_id, nota):
    cursor.execute("INSERT INTO notas (aluno_id, turma_id, nota) VALUES (?, ?, ?)",
                   (aluno_id, turma_id, nota))
    conn.commit()

def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    print("\n=== ALUNOS ===")
    for a in alunos:
        print(f"ID: {a[0]} | Nome: {a[1]}")


def listar_professores():
    cursor.execute("SELECT * FROM professores")
    profs = cursor.fetchall()
    print("\n=== PROFESSORES ===")
    for p in profs:
        print(f"ID: {p[0]} | Nome: {p[1]}")


def listar_turmas():
    cursor.execute("""
    SELECT turmas.id, turmas.nome, turmas.materia, professores.nome
    FROM turmas
    LEFT JOIN professores ON turmas.professor_id = professores.id
    """)
    turmas = cursor.fetchall()
    print("\n=== TURMAS ===")
    for t in turmas:
        print(f"ID: {t[0]} | Turma: {t[1]} | Matéria: {t[2]} | Professor: {t[3]}")

def deletar_aluno(aluno_id):
    cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
    conn.commit()

def deletar_professor(professor_id):
    cursor.execute("DELETE FROM professores WHERE id = ?", (professor_id,))
    conn.commit()

def deletar_turma(turma_id):
    cursor.execute("DELETE FROM turmas WHERE id = ?", (turma_id,))
    conn.commit()

def calcular_media(aluno_id, turma_id):
    cursor.execute("SELECT AVG(nota) FROM notas WHERE aluno_id = ? AND turma_id = ?",
                   (aluno_id, turma_id))
    media = cursor.fetchone()[0]
    return round(media, 2) if media else 0

def fechar_conexao():
    conn.close()

def menu():
    while True:
        print("\n===== SISTEMA ESCOLAR =====")
        print("\n")
        print("1 - Cadastrar Professor")
        print("2 - Cadastrar Aluno")
        print("3 - Criar Turma")
        print("4 - Lançar Nota")
        print("5 - Ver Média do Aluno")
        print("6 - Listar Professores")
        print("7 - Listar Alunos")
        print("8 - Listar Turmas")
        print("9 - Deletar Professor")
        print("10 - Deletar Aluno")
        print("11 - Deletar Turma")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do professor: ")
            adicionar_professor(nome)

        elif opcao == "2":
            nome = input("Nome do aluno: ")
            adicionar_aluno(nome)

        elif opcao == "3":
            listar_professores()
            nome = input("Nome da turma: ")
            materia = input("Matéria: ")
            professor_id = int(input("ID do professor: "))
            adicionar_turma(nome, materia, professor_id)

        elif opcao == "4":
            listar_alunos()
            listar_turmas()
            aluno_id = int(input("ID do aluno: "))
            turma_id = int(input("ID da turma: "))
            nota = float(input("Nota: "))
            adicionar_nota(aluno_id, turma_id, nota)

        elif opcao == "5":
            listar_alunos()
            listar_turmas()
            aluno_id = int(input("ID do aluno: "))
            turma_id = int(input("ID da turma: "))
            media = calcular_media(aluno_id, turma_id)
            print(f"Média: {media}")

        elif opcao == "6":
            listar_professores()

        elif opcao == "7":
            listar_alunos()

        elif opcao == "8":
            listar_turmas()

        elif opcao == "9":
            listar_professores()
            pid = int(input("ID do professor: "))
            deletar_professor(pid)

        elif opcao == "10":
            listar_alunos()
            aid = int(input("ID do aluno: "))
            deletar_aluno(aid)

        elif opcao == "11":
            listar_turmas()
            tid = int(input("ID da turma: "))
            deletar_turma(tid) 

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida")

if __name__ == "__main__":
    criar_tabelas()
    menu()
    fechar_conexao()
    input("Pressione Enter para sair...") 
