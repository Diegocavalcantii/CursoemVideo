import pyttsx3
# Criar objeto para síntese de fala
engine = pyttsx3.init()

# Função para falar as saídas
def speak(text):
    engine.say(text)
    engine.runAndWait()

from datetime import date
data_atual = date.today()
print('-'*35)
# Falar o texto do print
print(f' A data de hoje é: {data_atual}')
print('-'*35)

print('''Neste programa iremos calcular os valores correspondentes ao Contrato de Promessa de Compra e Venda de Imóvel
Referente ao Pagamento, CLÁUSULA 5ª:
Aplica-se sobre cada parcela em atraso multa de 10%(dez por cento) sobre os valores devidamente corrigidos,
correção monetária calculada com base no IGP-M
e juros de mora de 1%(um por cento) ao mês, ou fração mensal.''')
#speak('''Neste programa iremos calcular os valores correspondentes ao Contrato de Promessa de Compra e Venda de Imóvel
#Referente ao Pagamento, CLÁUSULA 5ª:
#Aplica-se sobre cada parcela em atraso multa de 10% sobre os valores devidamente corrigidos,
#correção monetária calculada com base no IGP-M
#e juros de mora de 1% ao mês, ou fração mensal.''')

print('Olá, me informe quantos dias atrasou o pagamento?')
speak('Olá, me informe quantos dias atrasou o pagamento? ')
dias=(float(input()))

print('Por favor, digite o valor da mensalidade: ')
speak('Por favor, digite o valor da mensalidade: ')
valor=(float(input()))

print('Agora insira o valor correspondente ao IGP-M (Indicador Geral de Preços do Mercado): ')
speak('Agora insira o valor correspondente ao IGP-M (Indicador Geral de Preços do Mercado): ')
igpm=(float(input()))

multa10=(valor*1.1)
jurosmora=valor*(0.01/30)*dias
correcao=igpm/100+1
valormulta=(valor*10/100)+valor

print('Obrigado! Aguarde o resultado!')
speak('Obrigado! Aguarde o resultado!')

print(f'''O valor da multa custará {multa10}reais em adicional da mensalidade atrasada!
Totalizando um valor de: {valormulta}reais''')
speak(f'''O valor da multa custará {multa10} reais em adicional da mensalidade atrasada!
Totalizando um valor de: {valormulta} reais''')

print(f'O valor da multa {valormulta}reais + juros de mora de 1% de {jurosmora:.2f} é = {(valormulta+jurosmora):.2f}')
speak(f'O valor da multa {valormulta}reais + juros de mora de 1% de {jurosmora:.2f} é = {(valormulta+jurosmora):.2f}')
#Sendo assim, o cálculo é: 1000,00 x ( 1% ÷ 30 ) x 20 dias de atraso = 1000 x 0,67% = R$ 6,70.
#Como atualizar um valor com base no Igp-m?
#Para saber como calcular o IGP-M sobre um contrato de aluguel reajustado anualmente, você poderá utilizar a
#seguinte fórmula: VALOR ATUALIZADO = VALOR ATUAL x FATOR (IGP-M ANUAL + 1)









#IGPM
#60% IPA indice de preço por atacado.
#30% IPC indice de preço ao consumidor.
#10% INCC indice nacional de custo e construção.
#O indice que mais afeta o IGPM é o IPA.

#IGPM x IGPTI
#IGP-M (mensal)= reference ao dia 21 do mês anterior ao dia 20 do mês atual.
#IGP-DI (diário)= refere ao dia 1 ao dia 30 do mês atual.
