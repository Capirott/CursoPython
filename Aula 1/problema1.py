saldo_devedor = float(raw_input('Insira o saldo devedor em seu cartão de crédito: '))
taxa_juros_anual = float(raw_input('Insira a taxa de juros anual do cartão de crédito como uma casa decimal: '))
taxa_minima_pagamento_mensal = float(raw_input('Digite a taxa mínima de pagamento mensal como uma decimal: '))
valor_total_pago = 0.0
for i in range(1, 13):
    pagamento_minimo_mensal = taxa_minima_pagamento_mensal * saldo_devedor
    juros_pagos = taxa_juros_anual / 12.0 * saldo_devedor
    principal_pago = pagamento_minimo_mensal - juros_pagos
    valor_total_pago += pagamento_minimo_mensal
    saldo_restante = saldo_devedor - principal_pago
    print('Mês: ' + str(i))
    print('Pagamento mensal mínimo: $ %.2f' % pagamento_minimo_mensal)
    print('Princípio pago: $ %.2f' % principal_pago)
    print('Saldo restante: $ %.2f' % saldo_restante)
    saldo_devedor = saldo_restante
print('RESULTADO')
print('Valor total pago: $ %.2f' % valor_total_pago)
print('Saldo remanescente: $ %.2f' % saldo_restante)