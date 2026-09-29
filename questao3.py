def verificar_carga_horaria(horas_trabalhadas):
  if horas_trabalhadas >= 40:
    return "Carga completa"
  else:
    return "Carga incompleta"


# Exemplo de uso:
print(verificar_carga_horaria(42))  # Saída: Carga completa
print(verificar_carga_horaria(35))  # Saída: Carga incompleta