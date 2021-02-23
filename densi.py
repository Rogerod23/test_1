import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
rcParams['font.family'] = 'serif'


def density_matrix(file):
	matrix = np.zeros([200,200], dtype = np.float64)
	cols = np.arange(0, 200)
	for j in range(200):
		if j == 0:
			counter = 0
		for i in range(200):
			matrix[i,j] = file[counter]
			if i == 199:
				counter =  counter + 1
			else:
				counter += 1
	matrix = pd.DataFrame(matrix, columns = cols)


	return matrix



densi_05_0 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_05/zud000c1")
densi_05_5 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_05/zud050c1")
densi_05_10 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_05/zud100c1")

matrix_densi_05_0 = density_matrix(densi_05_0)
matrix_densi_05_5 = density_matrix(densi_05_5)
matrix_densi_05_10 = density_matrix(densi_05_10)

###############################################################################################
densi_65_0 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_65/zud000c1")
densi_65_5 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_65/zud050c1")
densi_65_10 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_65/zud100c1")

matrix_densi_65_0 = density_matrix(densi_65_0)
matrix_densi_65_5 = density_matrix(densi_65_5)
matrix_densi_65_10 = density_matrix(densi_65_10)
##############################################################################################
densi_75_0 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_75/zud000c1")
densi_75_5 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_75/zud050c1")
densi_75_10 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_75/zud100c1")

matrix_densi_75_0 = density_matrix(densi_75_0)
matrix_densi_75_5 = density_matrix(densi_75_5)
matrix_densi_75_10 = density_matrix(densi_75_10)
##############################################################################################
densi_85_0 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_85/zud000c1")
densi_85_5 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_85/zud050c1")
densi_85_10 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_85/zud100c1")

matrix_densi_85_0 = density_matrix(densi_85_0)
matrix_densi_85_5 = density_matrix(densi_85_5)
matrix_densi_85_10 = density_matrix(densi_85_10)
##############################################################################################
densi_95_0 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_95/zud000c1")
densi_95_5 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_95/zud050c1")
densi_95_10 = np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_95/zud100c1")

matrix_densi_95_0 = density_matrix(densi_95_0)
matrix_densi_95_5 = density_matrix(densi_95_5)
matrix_densi_95_10 = density_matrix(densi_95_10)
##############################################################################################

distance =  np.genfromtxt("C:/Users/Rogelio/Documents/Doctorado_2020_2/densi_05/x1b000c1")

distance = distance/3.086e18

fontsize = 18
fig = plt.figure(figsize = (12,17))
fig.subplots_adjust(hspace = 0)
ax1 = fig.add_subplot(5,1,1)
ax2 = fig.add_subplot(5,1,2)
ax3 = fig.add_subplot(5,1,3)
ax4 = fig.add_subplot(5,1,4)
ax5 = fig.add_subplot(5,1,5)

axs = [ax1, ax2, ax3, ax4, ax5]

matrix_0 = [matrix_densi_05_0, matrix_densi_65_0, matrix_densi_75_0, matrix_densi_85_0, matrix_densi_95_0] 
matrix_5 = [matrix_densi_05_5, matrix_densi_65_5, matrix_densi_75_5, matrix_densi_85_5, matrix_densi_95_5] 
matrix_10 = [matrix_densi_05_10, matrix_densi_65_10, matrix_densi_75_10, matrix_densi_85_10, matrix_densi_95_10] 
xc = ["0.5", "0.65", "0.75", "0.85", "0.95"]


for ax, m0, m5, m10, x in zip(axs, matrix_0, matrix_5, matrix_10, xc):

	ax.plot(distance, m0.iloc[:,0].to_numpy(), label = r"t = 0")
	ax.plot(distance, m5.iloc[:,0].to_numpy(), label = r"t = 5 Myr")
	ax.plot(distance, m10.iloc[:,0].to_numpy(), label = r"t = 10 Myr")
	ax.set_yscale("log")
	ax.set_xlabel("")
	ax.set_ylabel(r"Density (g/cm$^{3}$)", fontsize = fontsize)
	#ax.set_title(r"x$_{{c}} = {}$".format(x))
	ax.tick_params(size = 20)
#	ax.set_xticklabels([])
	ax.text(x = 90, y= 3.7e-28, s = r"x$_{{c}}$ = {}".format(x), size = fontsize)
	
ax1.legend(fontsize = 10, loc="upper left")
ax5.set_xlabel("Distance (pc)", fontsize = fontsize)
plt.savefig("density.png", bbox_inches = "tight")
plt.show();