import matplotlib.pyplot as plt
import pandas as pd

pliki = ['1ers.csv', '1crs.csv', '2crs.csv', '1c.csv', '2c.csv']
tabele = ["" for _ in range(len(pliki))]
kolory = ["b", "g", "r", "k", "m"] #https://matplotlib.org/stable/gallery/color/named_colors.html
legenda = ["1-Evol-RS", "1-Coev-RS", "2-Coev-RS", "1-Coev", "2-Coev"]  # Uporządkowane legendy
markery = ["o", "v", "d", "s", "D"] #https://matplotlib.org/stable/api/markers_api.html

plt.figure(figsize=(8,8))

plt.subplot(1,2,1)

for i in range(len(pliki)):
    tabele[i] = pd.read_csv(pliki[i],sep=",",header=0)
    plt.plot(tabele[i].iloc[:, 1:2]/1000,tabele[i].iloc[:, 2:].mean(axis=1)*100, c = kolory[i], label = legenda[i], marker = markery[i],markevery = 25, markersize = 7, markeredgecolor="k")

plt.grid(linestyle = "--")
plt.margins(x=0) #y nie na 0
plt.title("Pokolenie")
plt.xlabel(r"Rozeganych gier $\times$ 1000") #czy o to chodziło z czcionką?
plt.ylabel(r"Odstek wygranych gier [%]")
plt.legend(loc = "lower right", numpoints = 2) #moze byc jeszcze loc = 4
plt.ylim(60,100)
plt.xlim(0,500)
skala2 = plt.twiny()
skala2.set_xticks([i*40 for i in range(6)])

plt2=plt.subplot(1,2,2)
tabela_box = [i.iloc[:, 2:].mean(axis=1)*100 for i in tabele]
plt2.boxplot(tabela_box, showmeans = True, notch = True, boxprops = dict(color = 'blue'), meanprops = dict(marker = 'o', markerfacecolor = 'blue', markeredgecolor = 'blue'))
#plt2.errorbar(ecolor= "blue")
plt2.grid(linestyle = "--")
plt2.set_xticklabels(legenda, rotation = 20)
plt2.set_ylim(60,100)
plt2.yaxis.tick_right()




plt.tight_layout()
plt.show()