import matplotlib.pyplot as plt
import numpy as np

def hsv2rgb(h, s, v):
    if s == 0:
        return (v, v, v)
    kolo = int(h * 6)
    f = (h * 6) - kolo
    najc = v * (1 - s)
    sr = v * (1 - f * s)
    posr = v * (1 - (1 - f) * s)
    kolo = kolo % 6
    if kolo == 0:
        return (v, posr, najc)
    elif kolo == 1:
        return (sr, v, najc)
    elif kolo == 2:
        return (najc, v, posr)
    elif kolo == 3:
        return (najc, sr, v)
    elif kolo == 4:
        return (posr, najc, v)
    elif kolo == 5:
        return (v, najc, sr)

def gradient(v,t):
    hue =1/3*(1-v)
    if t >=0:
        saturacja= 1
        jasnosc=1-t
    else:
        saturacja=1+ t
        jasnosc = 1
    return hsv2rgb(hue,saturacja,jasnosc)

def normalizacja(v,maxw,minw):
    return (v -minw)/(maxw - minw)

with open("big.dem", 'r') as file:
    wiel,wys,odl = map(float, file.readline().strip().split())
    wiel,wys = int(wiel), int(wys)
    wys_map = []
    for _ in range(wys):
        wys_map.append(list(map(float, file.readline().strip().split())))
    wys_map= np.array(wys_map)

max_wart = np.amax(wys_map)
min_wart = np.amin(wys_map)

swiatlo = np.empty((wys,wiel,3))
odl= odl/100

for i in range(wys-1):
    for j in range(wiel-1):
        oWys = wys_map[i,j]
        if j >0:
            tangens =(wys_map[i,j-1]-oWys)/odl
            if tangens > 0.25 or tangens < -0.25:
                if tangens > 0:
                    tangens = 1
                else:
                    tangens = -1
            else:
                tangens = 4*tangens
        else:
            tangens = 0
        swiatlo[i][j] = gradient(normalizacja(oWys,max_wart,min_wart),tangens)

plt.imshow(swiatlo)
#plt.savefig("kck2.png")
plt.show()
