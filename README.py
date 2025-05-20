# aleprojeto
# Lista de alunos com suas respectivas notas
alunos = [
    {"nome": "Ana", "notas": [7, 8, 6]},
    {"nome": "Carlos", "notas": [5, 4, 6]},
    {"nome": "Beatriz", "notas": [9, 8, 10]},
    {"nome": "Daniel", "notas": [5, 6, 5]},
]

# Função para calcular a média das notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Filtrando alunos com média abaixo de 6
alunos_filtrados = [aluno for aluno in alunos if calcular_media(aluno["notas"]) < 6]

# Exibindo os alunos com baixo desempenho
print("Alunos com desempenho abaixo de 6:")
for aluno in alunos_filtrados:
    print(f"{aluno['nome']} - Média: {calcular_media(aluno['notas']):.2f}")
