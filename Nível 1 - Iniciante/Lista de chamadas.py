# ---- Funções ----

def separaEntrada(entrada):
    lista = []
    concatenacao = ''

    for letra in entrada:
        if letra == ' ':
            lista.append(concatenacao)
            concatenacao = ''
        else:
            concatenacao += letra
    lista.append(concatenacao)        
    return lista

def listaAlunos():
    listaAlunos = []
    contador = 0
    
    while contador < int(qtdAlunos):
        aluno = input()
        listaAlunos.append(aluno)
        contador += 1
        listaAlunos.sort()
    return listaAlunos

# ---- Programa Principal ----

entrada = input()
entrada = separaEntrada(entrada)

qtdAlunos       = entrada[0]
alunoVencedor   = int(entrada[1]) 

alunos = listaAlunos()
print(alunos[alunoVencedor-1])
