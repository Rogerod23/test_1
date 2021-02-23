import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

pos = [0,1,2,3,4,5,6,7,8,9]

lumx_05 = []
lumx_65 = []
lumx_75 = []
lumx_85 = []
lumx_95 = []


lumx_out = []
lumx_in = []
lam_x = 1.7 * 9e-20
lam = 9e-20

ages = np.arange(0, 10, 0.1)


for i in range(10):
	for j in range(10):
		lum = np.genfromtxt('C:/Users/Rogelio/Documents/Doctorado_2020_2/lumi_05/zlxry0{}{}c1'.format(i,j))
		lumx_05.append(lum)
		lum = np.genfromtxt('C:/Users/Rogelio/Documents/Doctorado_2020_2/lumi_65/zlxry0{}{}c1'.format(i,j))
		lumx_65.append(lum)
		lum = np.genfromtxt('C:/Users/Rogelio/Documents/Doctorado_2020_2/lumi_75/zlxry0{}{}c1'.format(i,j))
		lumx_75.append(lum)
		lum = np.genfromtxt('C:/Users/Rogelio/Documents/Doctorado_2020_2/lumi_85/zlxry0{}{}c1'.format(i,j))
		lumx_85.append(lum)
		lum = np.genfromtxt('C:/Users/Rogelio/Documents/Doctorado_2020_2/lumi_95/zlxry0{}{}c1'.format(i,j))
		lumx_95.append(lum)

all_lumx = [lumx_05, lumx_65, lumx_75, lumx_85, lumx_95]



color = ["black", "green", "blue", "red", "magenta"]
markers = ["o", "^", "p", "*", "s"]
distance = ["0.5", "0.65", "0.75", "0.85", "0.95"]
rcParams['font.family'] = 'serif'
linestyle = "--"

plt.figure(figsize=(12,12))
for elems, col, mark, dist in zip(all_lumx, color, markers, distance):
	elems = np.array(elems)
	elems = elems/1e35
#plt.plot(f_ele, lumx_in, label = "SN inside", linewidth = 1.5, linestyle="--", color=color[0])
	plt.plot(ages, elems, label = r"x$_{{c}}$ =  {}".format(dist), linewidth = 1.5, linestyle=linestyle, color=col, marker = mark)
#plt.plot(f_ele, lumx_out, label= "SN border, n = 100", linewidth = 1.5, linestyle="--", color=color[2])
plt.xlabel("Age (Myr)", size = 15)
plt.xlim(0, 0.75)
plt.ylabel(r"Luminosity$_{\rm x-ray}$ (10$^{35}$ erg/s)", size = 15)
#plt.yscale("log")
#plt.ylim(1e33, 1e38)
plt.legend(fontsize = 15)
plt.savefig("lumi_chu.png")
plt.show()