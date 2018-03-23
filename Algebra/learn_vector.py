# -- coding: utf-8 --
from math import sqrt
from vector import Vector

my_vector1 = Vector([-0.221, 7.437])
my_vector2 = Vector([8.813, -1.331, -6.247])
my_vector3 = Vector([5.581, -2.136])
my_vector4 = Vector([1.996, 3.108, -4.554])

my_vector5 = Vector([1, 2, -1])
my_vector6 = Vector([3, 1, 0])

print(my_vector5.inner_products(my_vector6))

print('\n\n练习一 加减乘法　--------------------------------------\n\n')

print('\n\n练习二 大小和方向--------------------------------------\n\n')

print(my_vector1.magnitude)
print(my_vector2.magnitude)
print(my_vector3.normalized())
print(my_vector4.normalized())
print('\n\n练习二 点积和夹角--------------------------------------\n\n')

my_vector2_v = Vector([7.887, 4.138])
my_vector2_w = Vector([-8.802, 6.776])
my_vector2_v1 = Vector([-5.955, -4.904, -1.874])
my_vector2_w1 = Vector([-4.496, -8.755, 7.103])

print(my_vector2_v.inner_products(my_vector2_w))
print(my_vector2_v1.inner_products(my_vector2_w1))

my_vector2_v2 = Vector([3.183, -7.627])
my_vector2_w2 = Vector([-2.668, 5.319])
my_vector2_v3 = Vector([7.35, 0.221, 5.188])
my_vector2_w3 = Vector([2.751, 8.259, 3.985])

print(my_vector2_v2.radians(my_vector2_w2))
print(my_vector2_v3.angle(my_vector2_w3))

print('\n\n练习三 平行　或　　正交--------------------------------------\n\n')

my_vector3_v = Vector([-7.579, -7.88])
my_vector3_w = Vector([22.737, 23.64])

my_vector3_v1 = Vector([-2.029, -9.97, 4.172])
my_vector3_w1 = Vector([-9.231, -6.639, -7.245])

my_vector3_v2 = Vector([-2.328, -7.284, -1.214])
my_vector3_w2 = Vector([-1.821, 1.072, -2.94])

my_vector3_v3 = Vector([2.118, 4.827])
my_vector3_w3 = Vector([0, 0])

print(my_vector3_v.is_parallel_to(my_vector3_w))
print(my_vector3_v1.is_parallel_to(my_vector3_w1))
print(my_vector3_v2.is_parallel_to(my_vector3_w2))
print(my_vector3_v3.is_parallel_to(my_vector3_w3))
print("")
print(my_vector3_v.is_orthogonal_to(my_vector3_w))
print(my_vector3_v1.is_orthogonal_to(my_vector3_w1))
print(my_vector3_v2.is_orthogonal_to(my_vector3_w2))
print(my_vector3_v3.is_orthogonal_to(my_vector3_w3))

# print 1E-10 == 0.0000000001

print('\n\n练习四 向量投影--------------------------------------\n\n')
my_vector4_v = Vector([3.039, 1.879])

my_vector4_b = Vector([0.825, 2.036])

print(my_vector4_v.component_products_to(my_vector4_b))

my_vector4_v = Vector([-9.88, -3.264, -8.159])
my_vector4_b = Vector([-2.155, -9.353, -9.473])

print(my_vector4_v.component_orthongonal_to(my_vector4_b))

my_vector4_v = Vector([3.009, -6.172, 3.692, -2.51])
my_vector4_b = Vector([6.404, -9.144, 2.759, 8.718])

print(my_vector4_v.component_products_to(my_vector4_b))
print(my_vector4_v.component_orthongonal_to(my_vector4_b))

print('\n\n练习五 向量积  -------------------------------------\n\n')

my_vector_v = Vector([8.462, 7.893, -8.187])
my_vector_w = Vector([6.984, -5.975, 4.778])
print(my_vector_v.cross_product(my_vector_w))
my_vector_v = Vector([-8.987, -9.838, 5.031])
my_vector_w = Vector([-4.268, -1.861, -8.866])
print(my_vector_v.area_of_parallelogram(my_vector_w))
my_vector_v = Vector([1.5, 9.547, 3.691])
my_vector_w = Vector([-6.007, 0.124, 5.772])

print(my_vector_v.area_of_triangle(my_vector_w))

