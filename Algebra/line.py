from decimal import Decimal, getcontext

from vector import Vector

# 设置计算精度
getcontext().prec = 30


class Line(object):
    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    '''
    构造函数需要一个直线常量和一个法向量
    '''

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0'] * self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0'] * self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c / initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i == initial_index)) + 'x_{}'.format(i + 1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)

    '''
    判断两条直线是否平行
    '''

    def is_parallel_to(self, l):
        return self.normal_vector.is_parallel_to(l.normal_vector)
        # return round(self.normal_vector[0] / l.normal_vector[0], 3) == round(self.normal_vector[1] / l.normal_vector[1], 3)

    '''
    接着写一个函数检测两条直线是否相等，相等是指相等的点集合
    '''

    def __eq__(self, l) -> bool:
        if not self.is_parallel_to(l):
            return False

        vector1 = self.basepoint.minus(l.basepoint)
        return vector1.is_parallel_to(l.normal_vector) and vector1.is_parallel_to(self.normal_vector)

    '''
    算出两条直线的交点
    理想情况是，如果这两条直线不相等，但是平行函数应该返回一条消息
    '''

    def get_intersection(self, l):
        if self.is_parallel_to(l):
            return [0, 0]

        k1 = self.constant_term
        k2 = l.constant_term
        a = self.normal_vector[0]
        b = self.normal_vector[1]
        c = l.normal_vector[0]
        d = l.normal_vector[1]
        x = (d * k1 - b * k2) / (a * d - b * c)
        y = (-c * k1 + a * k2) / (a * d - b * c)
        return [x, y]


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
