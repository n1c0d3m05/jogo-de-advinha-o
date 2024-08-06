import random
import sqlite3
import os
import time

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS ponto(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    PONT INT NOT NULL
)''')


def verificar_nome(nome):
    data = cursor.execute('''SELECT * FROM ponto WHERE NOME=?''', (nome,))

    resultado = cursor.fetchone()

    # Fechar a conexão com o banco de dados

    return resultado is not None

def deletar():
    for i in cursor.execute("""SELECT * FROM ponto"""):
        print(f"USER: {i[1]}\n")
    nome_escolhido = input("qual nome você quer deletar? ")

    cursor.execute("""SELECT * FROM ponto WHERE NOME=? """, (nome_escolhido, ))
    result = cursor.fetchone()

    if result is not None:
        cursor.execute("DELETE FROM ponto WHERE nome=?", (nome_escolhido, ))
        conn.commit()
        print(f"Usuario: '{nome_escolhido}' deletado com sucesso!")
        time.sleep(3)
    else:
        print(f"Usuario: '{nome_escolhido}'  não encontrado voltando ao menu")
        time.sleep(3)
        

def limpar():
    os.system("cls")

tent = 0
count = 0
esc = 0
num = 0

def start():
    global tent, count, num, esc
    # count = 0
    
    nome = input("Qual é o seu nome: ")
    if verificar_nome(nome):
        print('nome invalido voltando em alguns segundos')
        time.sleep(3)
        return 
    else:
            tent = 0
            num = random.randint(1, 100)
            while esc != num:
        
                esc = int(input("Chute um número entre 1 e 100: "))
                if esc > 100:
                    print('numero invalido')
                elif esc < num:
                    print('o numero que você falou é menor do que o escolhido')
                    tent += 1
                elif esc > num:
                    print('o numero que você falou é maior do que o escolhido')
                    tent += 1
                else:
                    tent +=1
                    break
            limpar()
    
            print(f"Você acertou e tentou {tent} vezes")
            conn.execute('''INSERT INTO ponto( NOME, PONT)
            VALUES(?,?)''', ( nome, tent))
            conn.commit()
            input()

def show_rank():
    data = cursor.execute("SELECT * FROM ponto ORDER BY PONT")
    for record in data:
        print(f'USER: {record[1]}')
        print(f'TENTATIVAS: {record[2]} \n')
    input()
    
sen = 0

while sen != 4:
    limpar()
    print('1-Jogar\n2-Ver Rank\n3-deletar nome\n4-Sair')
    try:
        sen = int(input("Resposta: "))
        if sen == 1:
            limpar()
            start()
        elif sen == 2:
            limpar()
            show_rank()
        elif sen == 3:
            limpar()
            deletar()
    except ValueError:
            limpar()
            print('ERRO!\npor favor coloque umas da opções do menu')
            time.sleep(3)
conn.close()
