def calcular_media(notas):
  if not notas:
    return 0.0
  return sum(notas) / len(notas)



notas_aluno = [8.5, 7.0, 9.2, 6.5]
print(f"Média: {calcular_media(notas_aluno)}")  