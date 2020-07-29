import matplotlib.pyplot as plt

R = 2.912
Q = 340
sigma = 5.67*(10**(-8))
ep = 0.53
alpha_dir=[]
temp_dir=[]
alpha=0.3
T = ((1-alpha)*Q/(sigma*ep))**(0.25)
print(T)