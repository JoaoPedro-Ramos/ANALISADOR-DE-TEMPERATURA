import numpy as np
from matplotlib import pyplot as plt

num = int(input('Quantidade de dias a serem verificados: '))
t = []
for tem in range(1, num + 1):
  n = float(input(f'Digite a temperatura no {tem}º dia: '))
  t.append(n)


t_min = min(t)
t_max = max(t)
t_med = sum(t) / len(t)


dias = []
for dia in range(1, num + 1):
  dias.append(f'{dia}º dia')

print()
plt.bar(dias, t)
plt.title('Comparação das temperaturas nos 5 dias')
plt.xlabel('Variação de dias')
plt.ylabel('Variação de temperaturas em ºC')
plt.xticks(rotation=45)
plt.show()
print()

print('A menor temperatura registrada foi: ', t_min)
print('A maior temperatura registrada foi: ', t_max)
print('A temperatura média registrada foi: ', t_med)
