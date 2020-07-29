import matplotlib.pyplot as plt

R = 2.912
Q = 340
sigma = 5.67*(10**(-8))

alpha_dir=[]
temp_dir=[]
x=0
alpha=-0.5
for i in range(90):
	T = ((1-alpha)*Q/sigma)**(0.25)
	if T==298.2754072480907:
		x=alpha
	alpha_dir.append(alpha)
	temp_dir.append(T)
	alpha=alpha+0.01

#print(x)
#print (temp_dir)

plt.plot(alpha_dir,temp_dir)
plt.title('Teq. for different values of alpha')
plt.annotate('Room temperature',xytext={-0.30,286.373},xy={-0.3199999999999995,298.2754072480907},arrowprops={'facecolor':'black'},ha='center')
plt.annotate('Global average temperature',xytext={-0.21,273.373},xy={-0.14999999999999997,288.16977314724636},arrowprops={'facecolor':'blue'},ha='center')
plt.xlabel('alpha')
plt.ylabel('Teq.')
plt.legend()
plt.show()
#alpha=0.1
#T = ((1-alpha)*Q/sigma)**(0.25)
#T_new = T**(0.25)
#print (T)