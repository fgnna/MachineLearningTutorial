# -- coding: utf-8 --

from math import sqrt, acos, pi
from decimal import Decimal


class Vector(object):
    ERROR_MSG_ZERO_VECTOR = "Cannot normalize the zero vector"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)
            self.is_zero = sum([abs(x) for x in coordinates]) == 0
            self.magnitude = self.magnitude()

        except ValueError:
            raise ValueError("The coordinates must be nonempty")
        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    ''' 计算向量的大小 '''

    def magnitude(self):
        return Decimal(sqrt(sum([x ** 2 for x in self.coordinates])))

    ''' 计算两个向量的点积 '''

    def inner_products(self, v):
        return Decimal(sum([x * y for x, y in zip(self.coordinates, v.coordinates)]))

    ''' 向量标准化计算,并输出一个标准化的新向量 '''

    def normalized(self):
        try:
            scalar = Decimal(1) / self.magnitude
            return Vector([x * scalar for x in self.coordinates])

        except ZeroDivisionError:
            raise Exception(Vector.ERROR_MSG_ZERO_VECTOR)

    ''' 计算两个向量的孤度 '''

    def radians(self, v):
        return Decimal(acos(self.inner_products(v) / (self.magnitude * v.magnitude)))

    ''' 计算两个向量的角度 '''

    def angle(self, v):
        # 角度计算，使用三角函数中的 π
        degrees_per_radian = Decimal(180. / pi)
        return self.radians(v) * degrees_per_radian


my_vector1 = Vector([-0.221, 7.437])
my_vector2 = Vector([8.813, -1.331, -6.247])
my_vector3 = Vector([5.581, -2.136])
my_vector4 = Vector([1.996, 3.108, -4.554])

my_vector5 = Vector([1, 2, -1])
my_vector6 = Vector([3, 1, 0])

print my_vector5.inner_products(my_vector6)

print '\n\n练习一 加减乘法　--------------------------------------\n\n'

print '\n\n练习二 大小和方向--------------------------------------\n\n'

print my_vector1.magnitude
print my_vector2.magnitude
print my_vector3.normalized()
print my_vector4.normalized()
print '\n\n练习二 点积和夹角--------------------------------------\n\n'

my_vector2_v = Vector([7.887, 4.138])
my_vector2_w = Vector([-8.802, 6.776])
my_vector2_v1 = Vector([-5.955, -4.904, -1.874])
my_vector2_w1 = Vector([-4.496, -8.755, 7.103])

print my_vector2_v.inner_products(my_vector2_w)
print my_vector2_v1.inner_products(my_vector2_w1)

my_vector2_v2 = Vector([3.183, -7.627])
my_vector2_w2 = Vector([-2.668, 5.319])
my_vector2_v3 = Vector([7.35, 0.221, 5.188])
my_vector2_w3 = Vector([2.751, 8.259, 3.985])

print my_vector2_v2.radians(my_vector2_w2)
print my_vector2_v3.angle(my_vector2_w3)

print '\n\n练习三 平行　或　　正交--------------------------------------\n\n'

my_vector3_v = Vector([-7.579, -7.88])
my_vector3_w = Vector([22.737, 23.64])

my_vector3_v1 = Vector([-2.029, -9.97, 4.172])
my_vector3_w1 = Vector([-9.231, -6.639, -7.245])

my_vector3_v2 = Vector([-2.328, -7.284, -1.214])
my_vector3_w2 = Vector([-1.821, 1.072, -2.94])

my_vector3_v3 = Vector([2.118, 4.827])
my_vector3_w3 = Vector([0, 0])
