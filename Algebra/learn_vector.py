# -- coding: utf-8 --
import math
from math import sqrt, acos, pi
# 精确计算类 带小数点类型，类似于　java的浮点封装类
from decimal import Decimal, getcontext


class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector";

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    '''计算向量的长度, 输出结果将保留三位小数'''

    def math_len(self):
        if 2 == self.dimension:
            return round(sqrt(pow(self.coordinates[0], 2) + pow(self.coordinates[1], 2)), 3)
        elif 3 == self.dimension:
            return round(sqrt(pow(self.coordinates[0], 2) + pow(self.coordinates[1], 2) + pow(self.coordinates[2], 2)), 3)
        return -1;

    ''' 计算标准化向量 '''

    def math_std(self):
        vector_len = Decimal(self.math_len())
        if 2 == self.dimension:
            return [round(self.coordinates[0] / vector_len, 3), round(self.coordinates[1] / vector_len, 3)]
        elif 3 == self.dimension:
            return [round(self.coordinates[0] / vector_len, 3), round(self.coordinates[1] / vector_len, 3), round(self.coordinates[2] / vector_len, 3)]

    ''' 判断是否为零向量 '''

    def is_zero(self):
        zero = 0
        for x in self.coordinates:
            zero += x ** 2
        return zero == 0

    ''' 计算向量的内积 '''

    def inner_products(self, v):
        if self.is_zero() or v.is_zero():
            raise Exception('Cannot inner products the zero vector v')
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    ''' 计算向量的绝对值内积 '''

    def inner_products_abs(self, v):
        return self.magnitude() * v.magnitude()

    ''' 计算两个向量的孤度 '''

    def radians(self, v):
        return acos(self.inner_products(v) / self.inner_products_abs(v))

    ''' 计算两个向量的角度 '''

    def angle(self, v):
        # 角度计算，使用三角函数中的 π
        degrees_per_radian = 180. / pi
        return self.radians(v) * degrees_per_radian

    ''' 比对两个向量是否为平行向量 '''

    def is_parallelism(self, v):
        parallel = self.is_zero() or v.is_zero()
        if parallel:
            return parallel

        ssss = [abs(x) / abs(y) for x, y in zip(self.coordinates, v.coordinates)]
        print ssss
        avg = sum(ssss) / len(ssss)
        for a in ssss:
            parallel |= avg == a

        return parallel

    ''' 比对两个向量是否为正交向量 '''

    def is_orthogonality(self, v):
        try:
            parallel = False | self.is_zero() | v.is_zero() \
                       | Vector([x * y for x, y in zip(self.coordinates, v.coordinates)]).is_zero()
            return parallel
        except ZeroDivisionError:
            return False

    '''
    =============================================================================== 
    教学模板代码==================================================================== 
    教学提供的向量长度/大小计算实现 
    ===============================================================================
    '''

    def magnitude(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return Decimal(sqrt(sum(coordinates_squared)))

    def times_scalar(self, scalar):
        return Vector([x / scalar for x in self.coordinates])

    ''' 教学提供的向量加法计算实现 '''

    def plus(self, v):
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return new_coordinates

    '''　教学提供的向量标准化计算实现　'''

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal(1.0) / magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    ''' 乘积 '''

    def dot(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    ''' 孤度和角度 '''

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = Decimal(180) / pi
                return Decimal(angle_in_radians) * Decimal(degrees_per_radian)
            else:
                return angle_in_radians

        except Exception as e:
            if (str(e)) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with the zero vector")
            else:
                raise e


my_vector1 = Vector([-0.221, 7.437])
my_vector2 = Vector([8.813, -1.331, -6.247])
my_vector3 = Vector([5.581, -2.136])
my_vector4 = Vector([1.996, 3.108, -4.554])

print my_vector1.math_len()
print my_vector2.math_len()
print my_vector3.math_std()
print my_vector4.normalized()

print '\n\n练习二--------------------------------------\n\n'

my_vector2_v = Vector([7.887, 4.138])
my_vector2_w = Vector([-8.802, 6.776])
my_vector2_0 = Vector([0, 0])

my_vector2_v2 = Vector([-5.955, -4.904, -1.874])
my_vector2_w2 = Vector([-4.496, -8.755, 7.103])

print my_vector2_v.inner_products(my_vector2_w)
print my_vector2_v2.inner_products(my_vector2_w2)
print my_vector2_v2.inner_products_abs(my_vector2_w2)
print Vector([1, 2, -1]).inner_products(Vector([3, 1, 0]))
print Vector([1, 2, -1]).inner_products_abs(Vector([3, 1, 0]))
print Vector([1, 2, -1]).radians(Vector([3, 1, 0]))
print Vector([1, 2, -1]).angle(Vector([3, 1, 0]))

my_vector2_v3 = Vector([3.183, -7.627])
my_vector2_w3 = Vector([-2.668, 5.319])

my_vector2_v4 = Vector([7.35, 0.221, 5.188])
my_vector2_w4 = Vector([2.751, 8.259, 3.985])
# print my_vector2_v.radians(my_vector2_w)
# print my_vector2_v.angle(my_vector2_w)
# print my_vector2_v3.angle_with(my_vector2_w3)
# print my_vector2_v4.angle_with(my_vector2_w4, True)

print '\n\n练习三--------------------------------------\n\n'

my_vector3_v = Vector([-7.579, -7.88])
my_vector3_w = Vector([22.737, 23.64])

my_vector3_v1 = Vector([-2.029, -9.97, 4.172])
my_vector3_w1 = Vector([-9.231, -6.639, -7.245])

my_vector3_v2 = Vector([-2.328, -7.284, -1.214])
my_vector3_w2 = Vector([-1.821, 1.072, -2.94])

my_vector3_v3 = Vector([2.118, 4.827])
my_vector3_w3 = Vector([0, 0])

print my_vector3_v.is_parallelism(my_vector3_w)
print my_vector3_v1.is_parallelism(my_vector3_w1)
print my_vector3_v2.is_parallelism(my_vector3_w2)
print my_vector3_v3.is_parallelism(my_vector3_w3)

print my_vector3_v.is_orthogonality(my_vector3_w)
print my_vector3_v1.is_orthogonality(my_vector3_w1)
print my_vector3_v2.is_orthogonality(my_vector3_w2)
print my_vector3_v3.is_orthogonality(my_vector3_w3)

print 1e-10



