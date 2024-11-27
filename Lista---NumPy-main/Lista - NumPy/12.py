#2.Use numpy.linspace para criar um array com 50 valores igualmente
#espaçados entre 0 e 10. Use numpy.arange para criar um array com
#valores de 0 a 10, incrementando de 0.2.
import numpy as np

array_linspace = np.linspace(0, 10, 50)


array_arange = np.arange(0, 10, 0.2) 


print("\nArray com np.linspace:")
print(array_linspace)
print("\nArray com np.arange:")
print(array_arange)