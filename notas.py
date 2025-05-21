# Lista para armazenar as notas válidas
Notas = []

while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            Notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite uma nota numérica ou 'fim'.")

# Verifica se alguma nota válida foi inserida
if len(Notas) > 0:
    media = sum(Notas) / len(Notas)
    print(f"\nTotal de notas válidas: {len(Notas)}")
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")
