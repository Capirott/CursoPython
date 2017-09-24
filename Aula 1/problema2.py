saldo_atualizado = saldo_devedor = float(raw_input('Insira o saldo devedor em seu cartão de crédito: '))
taxa_juros_anual = float(raw_input('Insira a taxa de juros anual do cartão de crédito como uma decimal: '))
minimo_pagamento_mensal = 0.0
taxa_juros_mensal = taxa_juros_anual / 12.0
while saldo_atualizado > 0:
    minimo_pagamento_mensal += 10.0
    saldo_atualizado = saldo_devedor
    numero_meses_necessarios = 0
    while numero_meses_necessarios < 12 and saldo_atualizado > 0:
        saldo_atualizado = saldo_atualizado * (1.0 + taxa_juros_mensal) - minimo_pagamento_mensal
        numero_meses_necessarios += 1
print('RESULTADO')
print('Pagamento mensal para pagar dividas em 1 ano: %.2f' % minimo_pagamento_mensal)
print('Número de meses necessários: %d' % numero_meses_necessarios)
print('Saldo: %.2f' % saldo_atualizado)