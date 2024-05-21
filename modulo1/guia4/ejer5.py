import numpy as np

# a) Crear un array de dimensión (3,3) y aplicar los métodos mean(), std(), var() y sum().
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

mean_total = arr.mean()
std_total = arr.std()
var_total = arr.var()
sum_total = arr.sum()

print("Array:")
print(arr)
print()

print("Mean total:", mean_total)
print("Standard Deviation total:", std_total)
print("Variance total:", var_total)
print("Sum total:", sum_total)
print()

# b) Repetir el ejercicio anterior utilizando el parámetro axis=0 y axis=1.
mean_axis0 = arr.mean(axis=0)
std_axis0 = arr.std(axis=0)
var_axis0 = arr.var(axis=0)
sum_axis0 = arr.sum(axis=0)

mean_axis1 = arr.mean(axis=1)
std_axis1 = arr.std(axis=1)
var_axis1 = arr.var(axis=1)
sum_axis1 = arr.sum(axis=1)

print("Mean along axis 0:", mean_axis0)
print("Standard Deviation along axis 0:", std_axis0)
print("Variance along axis 0:", var_axis0)
print("Sum along axis 0:", sum_axis0)
print()

print("Mean along axis 1:", mean_axis1)
print("Standard Deviation along axis 1:", std_axis1)
print("Variance along axis 1:", var_axis1)
print("Sum along axis 1:", sum_axis1)
