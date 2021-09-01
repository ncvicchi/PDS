#%% numpy
import numpy as np

#%%
def dft(xx):

  N = xx.shape[0]
  nn = np.arange(N)    
  k = nn.reshape((N, 1))  
  XX = [0]*N

  e = np.exp(-2j * np.pi * k * nn / N)
    
  XX = np.dot(e, xx)

  return  XX
# %%