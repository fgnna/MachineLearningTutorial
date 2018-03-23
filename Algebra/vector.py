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
            self.is_zero = sum([abs(x) for x in coordinates]) < 1e-10
            self.magnitude = self.magnitude()

        except ValueError:
            raise ValueError("The coordinates must be nonempty")
        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    ''' 相减 '''

    def minus(self, v):
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    ''' 相减 '''

    def sum(self, v):
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])

    ''' 计算向量的大小 '''

    def magnitude(self):
        return Decimal(sqrt(sum([x ** 2 for x in self.coordinates])))

    ''' 计算两个向量的点积 '''

    def inner_products(self, v):
        return Decimal(sum([x * y for x, y in zip(self.coordinates, v.coordinates)]))

    ''' 向量标准化计算,并输出一个标准化的新向量 ,也叫向量的方向'''

    def normalized(self):
        try:
            scalar = Decimal(1) / self.magnitude
            return Vector([x * scalar for x in self.coordinates])

        except ZeroDivisionError:
            raise Exception(Vector.ERROR_MSG_ZERO_VECTOR)

    ''' 计算两个向量的孤度 '''

    def radians(self, v):
        return Decimal(acos(round(self.inner_products(v) / (self.magnitude * v.magnitude), 9)))

    ''' direction　计算向量的方向，基于零向量 '''

    def direction(self):
        return Vector([0 if x == 0 else x / abs(x) for x in self.coordinates])

    ''' 计算两个向量的角度 '''

    def angle(self, v):
        # 角度计算，使用三角函数中的 π
        degrees_per_radian = Decimal(180. / pi)
        return round(self.radians(v) * degrees_per_radian, 10)

    ''' 计算两个向量是否平行 '''

    def is_parallel_to(self, v):
        return self.is_zero or v.is_zero or self.angle(v) == 0 or self.angle(v) == 180

    ''' 
    计算两个向量是否正交 最终，要注意小数位数　1e-10代表小数点后10位，
    加入这个判断，只要绝对值小于0.0000000001即代表0
    '''

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.inner_products(v)) < tolerance

    ''' 分量平行 计算self向量 在 v向量上的投影向量 即self平行向量 '''

    def component_products_to(self, v):
        if v.is_zero:
            raise Exception(self.ERROR_MSG_ZERO_VECTOR)
        v_normalized = v.normalized()
        product = self.inner_products(v_normalized)
        return Vector([x * product for x in v_normalized.coordinates])

    ''' 分量正交 self垂直 '''

    def component_orthongonal_to(self, v):
        product = self.component_products_to(v)
        return self.minus(product)

    ''' 下面公式也可以作用于2维空间，只是Z轴坐标默认为0即可 '''

    ''' 计算向量积  '''

    def cross_product(self, v):
        ''' 因为数组是元组类型，所以不能这样操作,要处理必须产生新的对像 '''
        # if self.coordinates.dimension == 2:
        #     self.coordinates.append(0)
        # if v.coordinates.dimension == 2:
        #     v.coordinates.append(0)

        x_1, y_1, z_1 = self.coordinates
        x_2, y_2, z_2 = v.coordinates

        return Vector([y_1 * z_2 - y_2 * z_1,
                       -(x_1 * z_2 - x_2 * z_1),
                       x_1 * y_2 - x_2 * y_1
                       ])

    ''' 计算向量形成的平行四边形的面积 '''

    def area_of_parallelogram(self, v):
        product_vector = self.cross_product(v)
        return sqrt(product_vector.coordinates[0] ** 2 +
                    product_vector.coordinates[1] ** 2 +
                    product_vector.coordinates[2] ** 2)

        ''' 向量形成的三角形的面积  即平行四边形的面积的一半 '''

    def area_of_triangle(self, v):
        return self.area_of_parallelogram(v) / 2
