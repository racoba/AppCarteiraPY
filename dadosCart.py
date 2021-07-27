from datetime import date

from matplotlib import pyplot 
data = date.today()
today = data.strftime("%Y-%m-%d")

#DADOS CARTEIRA

#O padrão é CODIGO , QUANTIDADE, PREÇO MÉDIO

cartAcao = [['ITSA4.SA' , 80 , 10.30],['CMIN3.SA' , 55 , 9.06],['ARZZ3.SA' , 5 , 74.23],['JHSF3.SA' , 80 , 6.68],['PETZ3.SA' , 37 ,20.51],['TAEE11.SA' , 15 , 37.40],['MGLU3.SA' ,45 , 20.43],['BBAS3.SA' , 22 ,29.64]]

cartFI = [['HGLG11.SA' , 6 , 173.07],['BCFF11.SA' , 12 , 88.34],['KNRI11.SA' , 7 , 151.65]]

cartBDR = [['MSFT34.SA' , 11 , 57.99],['GOGL34.SA' , 9 , 80.42],['MELI34.SA' , 10 , 64.86],['NIKE34.SA' , 9 , 73.47],['JNJB34.SA', 10 , 60.9]]

cartCaixa = 1303.39

cartCrypto = 3600



#RESUMO DA CARTEIRA + BALANCEAMENTO

valorAcoes = 0
valorFI = 0
valorBDR = 0

for i in range(len(cartAcao)):
    valorAcoes += cartAcao[i][1]*cartAcao[i][2]
for i in range(len(cartFI)):
    valorFI+= cartFI[i][1]*cartFI[i][2]
for i in range(len(cartBDR)):
    valorBDR+= cartBDR[i][1]*cartBDR[i][2]


#RESUMO DE RENTABILIDADE DA CARTEIRA

valorCartMensal = [5000,7068,16228,16576]
meses = ['Fevereiro','Março','Abril','Maio']


