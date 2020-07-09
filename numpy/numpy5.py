import numpy as np

a1=(1,0,0)
a2=(2,1,3)
print(np.einsum("m,n",a1,a2))