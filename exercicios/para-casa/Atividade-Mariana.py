# Exercício 27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

#Vamos começar retirando os inputs do user. Os dois últimos prints vazios são para fins de espaçamento.
print("*** CALCULADORA DE PREÇOS 🍎🍓 ***")
morangos_quantidade = float(input("🍓 DIGITE QUANTOS KGS DE MORANGO IRÁ COMPRAR: "))
maca_quantidade = float(input("🍎 DIGITE QUANTOS KGS DE MAÇÃ IRÁ COMPRAR: "))
print("")

#Aqui vamos construir a nossa lógica:
#Primeiro calculando o preço de acordo com a quantidade de preço por quilos da tabela do morango e da maçã
if (morangos_quantidade <= 5):
    valor_morango = morangos_quantidade*2.50
else:
    valor_morango = morangos_quantidade*2.20
  
if(maca_quantidade <= 5):
    valor_maca = maca_quantidade*1.80
else:
    valor_maca = maca_quantidade*1.50

#Agora somando tudo pra dar o resultado
valor_final = valor_maca + valor_morango

#Agora vamos lidar com o desconto (caso haja, caso não haja, o valor vai ser o que já apareceu acima, hehe)
if(valor_final >= 25):
    valor_desconto = valor_final * 0.1
    valor_final_desconto =  valor_final - valor_desconto
else:
    valor_desconto = 0
    valor_final_desconto = valor_final

#Agora vamos para o print
print(f"***NOTA FISCAL***")
print(f"🍓 VALOR DO MORANGO: R${valor_morango:.2f}")
print(f"🍎 VALOR DA MAÇÃ: R${valor_maca:.2f}")
print(f"🪙  VALOR FINAL: R${valor_final:.2f}")
print(f"💸 DESCONTO: R${valor_desconto:.2f}")
print(f"💵 TOTAL A PAGAR: R${valor_final_desconto:.2f}")
