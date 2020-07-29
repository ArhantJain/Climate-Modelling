import matplotlib.pyplot as plt

R = 2.912
Q = 340
sigma = 5.67*(10**(-8))

ep_dir=[]
temp_dir=[]
alpha=0.3
eps=0.1
x=0
for i in range(90):
	T = ((1-alpha)*Q/(eps*sigma))**(0.25)
	if T==298.3180332452128:
		x=eps
	ep_dir.append(eps)
	temp_dir.append(T)
	eps=eps + 0.01

print(x)
print(ep_dir)
print(temp_dir)

plt.plot(ep_dir,temp_dir)
plt.title('Teq. for different values of epsilon')
plt.annotate('Room temperature',xy={0.5300000000000004,298.3180332452128},xytext={0.52,331.8},arrowprops={'facecolor':'black'},ha='center')
plt.annotate('Global average temperature',(0.6,289.20823960697345),xytext={0.32,277.989},arrowprops={'facecolor':'blue'},ha='center')
plt.xlabel('alpha')
plt.ylabel('Teq.')
plt.legend()
plt.show()