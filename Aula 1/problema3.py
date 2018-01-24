saldo_atualizado = saldo_devedor = float(raw_input('Insira o saldo devedor em seu cartão de crédito: '))
taxa_juros_anual = float(raw_input('Insira a taxa de juros anual do cartão de crédito como uma decimal: '))
taxa_juros_mensal = taxa_juros_anual / 12.0
limite_inferior = saldo_atualizado / 12.0
limite_superior = (saldo_atualizado * (1 + (taxa_juros_anual / 12.0)) ** 12) / 12
saldo_atualizado = saldo_devedor
while (saldo_atualizado > 0):
    limite_mediano  = (limite_inferior + limite_superior) /  2.0
    numero_meses_necessarios = 0
    while numero_meses_necessarios < 12 and saldo_atualizado > 0:
        saldo_atualizado = saldo_atualizado * (1.0 + taxa_juros_mensal) - limite_mediano
        numero_meses_necessarios += 1
    
        
print('RESULTADO')
print('Pagamento mensal para pagar dividas em 1 ano: %.2f' % limite_inferior)
print('Número de meses necessários: %d' % limite_superior)
print('Saldo: %.2f' % saldo_atualizado)