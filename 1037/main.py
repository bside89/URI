# URI Online Judge | 1037
# Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1037

__author__ = 'darkwolf'


var = float(input())

if 0 <= var <= 25:
    print("Intervalo [0,25]")
elif 25 < var <= 50:
    print("Intervalo (25,50]")
elif 50 < var <= 75:
    print("Intervalo (50, 75]")
elif 75 < var <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
