def filtrar_aprovados(notas, nota_corte=7.0):
  return [nota for nota in notas if nota >= nota_corte]



notas_turma = [5.5, 7.0, 8.5, 6.0, 9.2, 4.8]
aprovados = filtrar_aprovados(notas_turma)
print(f"Notas de aprovação: {aprovados}")  