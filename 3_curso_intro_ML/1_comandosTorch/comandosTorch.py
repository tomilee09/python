import torch
print(torch.__version__, "\n")

# crear un tensor dando sus valores
tensor = torch.tensor([[1., 2.], [3., 4.]])
print(tensor, "\n")

# tener un tensor con puros 1's
tensor_unos = torch.ones(2, 2)
print(tensor_unos, "\n")

# tensor con puros ceros
tensor_ceros = torch.zeros(2, 2)
print(tensor_ceros, "\n")

# tensor con numeros aleatorios entre 0 y 1
tensor_random = torch.rand(2, 2)
print(tensor_random, "\n")

# cambiar la forma de un tensor
tensor_reformado = tensor_random.view(1, 4)
print(tensor_reformado, "\n")

# hacer la transpuesta
tensor_t = tensor.t()
print(tensor_t, "\n")

# crear un tensor a partir de numpy
import numpy as np
tensor_np = np.array([[1, 2], [3, 4]])
tensor_np2torch = torch.from_numpy(tensor_np)
print(tensor_np2torch, "\n")

# calcular el promedio de los valores de un tensor
media = torch.mean(tensor)
print(media, "\n")

# calcular media de todas las columnas
media_columna = torch.mean(tensor, dim=0)
print(media_columna, "\n")

# calcular media de todas las filas
media_filas = torch.mean(tensor, dim=1)
print(media_filas, "\n")

# calcular desviacion estandar
des_std = torch.std(tensor)
print(des_std, "\n")

# calcular desviacion estandar de las columnas
des_std_columnas = torch.std(tensor, dim = 0)
print(des_std_columnas, "\n")

# calcular desviacion estandar de las filas
des_std_filas = torch.std(tensor, dim = 1)
print(des_std_filas, "\n")