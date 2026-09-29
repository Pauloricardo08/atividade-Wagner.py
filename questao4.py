def calcular_saldo(saldo_atual, valor, tipo_operacao):
  operacao = tipo_operacao.strip().lower()

  if operacao == "deposito":
    return saldo_atual + valor
  elif operacao == "saque":
    return saldo_atual - valor
  else:
    raise ValueError(
        "Operação inválida. Utilize 'deposito' ou 'saque'."
    )



saldo_inicial = 1000.00
saldo_pos_deposito = calcular_saldo(saldo_inicial, 250.00, "deposito")
print(f"Novo saldo após depósito: R$ {saldo_pos_deposito:.2f}")

saldo_pos_saque = calcular_saldo(saldo_pos_deposito, 150.00, "saque")
print(f"Novo saldo após saque: R$ {saldo_pos_saque:.2f}")