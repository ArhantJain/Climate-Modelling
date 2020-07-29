import matplotlib.pyplot as plt

R = 2.912
Q = 440
sigma = 5.67*(10**(-8))

Q_dir=[]
temp_dir=[]
alpha=0.3
for i in range(240):
	T = ((1-alpha)*Q/sigma)**(0.25)
	if T==298.4911701409791:
		x=Q
	Q_dir.append(Q)
	temp_dir.append(T)
	Q=Q+1

#print(x)
T_b = ((1-alpha)*x/sigma)**(0.25)
#print(T_b)
#print (temp_dir)
#561,288.4824917550765
plt.plot(Q_dir,temp_dir)
plt.title('Teq. for different values of Q')
plt.annotate('Room temperature',(643,298.4911701409791),xytext=(650.6,294.9),arrowprops={'facecolor':'black'})
plt.annotate('Global Avg. temperature',(562.504,288.633),xytext=(584.766,284.146),arrowprops={'facecolor':'black'})
plt.xlabel('alpha')
plt.ylabel('Q')
plt.legend()
plt.show()