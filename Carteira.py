import numpy as np;
import pandas as pd
import matplotlib.pyplot as plt;
from pandas_datareader import data as web   
import yfinance as yf
yf.pdr_override()
import os
import dadosCart as c

somaPal=0
somaEu=0
rentTotal=0
decisao=1
while decisao!=5:
    os.system('cls')
    decisao = int(input('Digite o que você deseja fazer:\n1-Calcular carteira\n2-Acompanhamento ao vivo\n3-Evolução mensal da carteira\n4-Análise individual de ativos da carteira\n5-Sair\n'))


    os.system('cls')
    if decisao==1:
        
        total = c.valorAcoes + c.valorFI + c.valorBDR + c.cartCaixa

        print(
            f"""O valor da sua carteira é de R${total} e ela atualmente está distribuida da seguinte forma:\n 
            Ações = {c.valorAcoes*100/total:.2f}% = R${c.valorAcoes}\n 
            Fundos Imobiliários = {c.valorFI*100/total:.2f}% = R${c.valorFI}\n 
            Internacional = {(c.valorBDR)*100/total:.2f}% = R${c.valorBDR}\n 
            Caixa = {c.cartCaixa*100/total:.2f}% = R${c.cartCaixa}\n\n
            Além disso também possui R${c.cartCrypto} em Cryptomoedas\n"""
            )


        y=np.array([int(c.valorAcoes*100/total),int(c.valorFI*100/total),int((c.valorBDR)*100/total),int(c.cartCaixa*100/total)]);
        mylabels = ['Ação','FII','Internacional','Caixa'];

        myexplode = [0,0,0,0];

        plt.pie(y,labels=mylabels,explode=myexplode,shadow=True);
        plt.show();

    elif decisao==2:
        decisao2=1
        while (decisao2):
            decisao2 = int(input("Digite o que você deseja ver:\n1-Carteira Completa\n2-Ações\n3-FII\n4-BDR\n5-Sair\n"))
            
            if decisao2==1: ativo = c.cartAcao + c.cartFI + c.cartBDR  
            elif decisao2==2: ativo = c.cartAcao
            elif decisao2==3: ativo = c.cartFI
            elif decisao2==4: ativo = c.cartBDR
            elif decisao2==5:
                os.system('cls')
                break
        
            os.system('cls')
            for x in range(len(ativo)):    
                df = web.get_data_yahoo(ativo[x][0], start=c.today)["Adj Close"].to_frame()

                mostra = str(df) + '@'
                for y in range(mostra.index('@'),0,-1):
                    if mostra[y]==' ':
                        inicioNum=y+1
                        break
                pal = float(mostra[inicioNum:mostra.index('@')])
                somaPal += pal
                somaEu += ativo[x][2]

                print(f'\n{ativo[x][0].replace(".SA","")} {c.today[8:10]}/{c.today[5:7]}\nValor de fechamento do dia: {pal:.2f}\nPreço Médio de Aquisição: {ativo[x][2]}\nValor Investido: {ativo[x][2]*ativo[x][1]:.2f}\nValor Atual em Carteira: {(pal*ativo[x][1]):.2f}')
                
                rent = (pal)/ativo[x][2]
                if rent > 1:
                    print(f'Rentabilidade: \033[1;32m+{((rent-1)*100):.2f}%\033[0;0m\n')
                elif rent < 1:
                    print(f'Rentabilidade: \033[1;31m{((rent-1)*100):.2f}%\033[0;0m\n')
                elif rent ==1:
                    print(f'Rentabilidade: \033[1;37m{((rent-1)*100):.2f}%\033[0;0m\n')
            print('-'*80+'\n')
            print('Rentabilidade atual: ')
            rentTotal = somaPal/somaEu
            if rentTotal > 1:
                    print(f'\033[1;32m+{((rentTotal-1)*100):.2f}%\033[0;0m\n')
            elif rentTotal < 1:
                    print(f'\033[1;31m{((rentTotal-1)*100):.2f}%\033[0;0m\n')
            elif rentTotal ==1 :
                    print(f'\033[1;37m{((rentTotal-1)*100):.2f}%\033[0;0m\n')    
            

    elif decisao==3:
        plt.plot(c.meses,c.valorCartMensal,'r-',)
        plt.title('Evolução Mensal da Carteira')
        plt.show()
    


    elif decisao==4:
        decisao2=1
        while (decisao2):
            decisao2 = int(input("Digite o que você deseja ver:\n1-Ações\n2-FII\n3-BDR\n4-Sair\n"))
        
            if decisao2==1: ativo = c.cartAcao
            elif decisao2==2: ativo = c.cartFI
            elif decisao2==3: ativo = c.cartBDR
            elif decisao2==4:
                os.system('cls')
                break
            print("Qual ativo você deseja análisar?\n")
            for x in range(len(ativo)):
                print(f'{x+1}-{ativo[x][0].replace(".SA","")}\n')
            menu = int(input())
            df = web.get_data_yahoo(ativo[menu-1][0])["Close"]
            df.plot()
            plt.title("Histórico de fechamento (R$)")
            plt.show()


