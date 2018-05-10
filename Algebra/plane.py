from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Plane(object):
    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0'] * self.dimension
            normal_vector = Vector(all_zeros)
            print("ifnot")
        self.normal_vector = normal_vector

        if not constant_term:
            print("ifnot")
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0'] * self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            print(c)
            basepoint_coords[initial_index] = c / initial_coefficient
            print(basepoint_coords)
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def __str__(self):

        # num_decimal_places = 3
        #
        # def write_coefficient(coefficient, is_initial_term=False):
        #     coefficient = round(coefficient, num_decimal_places)
        #     if coefficient % 1 == 0:
        #         coefficient = int(coefficient)
        #
        #     output = ''
        #
        #     if coefficient < 0:
        #         output += '-'
        #     if coefficient > 0 and not is_initial_term:
        #         output += '+'
        #
        #     if not is_initial_term:
        #         output += ' '
        #
        #     if abs(coefficient) != 1:
        #         output += '{}'.format(abs(coefficient))
        #
        #     return output
        #
        # n = self.normal_vector
        #
        # try:
        #     initial_index = Plane.first_nonzero_index(n)
        #     terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
        #              for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
        #     output = ' '.join(terms)
        #
        # except Exception as e:
        #     if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
        #         output = '0'
        #     else:
        #         raise e
        #
        # constant = round(self.constant_term, num_decimal_places)
        # if constant % 1 == 0:
        #     constant = int(constant)
        # output += ' = {}'.format(constant)
        output = "x{} + y{} + z{} = {}".format(self.normal_vector[0], self.normal_vector[1], self.normal_vector[2], self.constant_term)
        return output

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)

    '''是否平行'''

    def is_parallel_to(self, l) -> bool:
        return self.normal_vector.is_parallel_to(l.normal_vector)

    '''是否同一平面'''

    def __eq__(self, o: object) -> bool:
        if self.normal_vector[0] == o.normal_vector[0] \
                and self.normal_vector[1] == o.normal_vector[1] \
                and self.normal_vector[2] == o.normal_vector[2] \
                and self.constant_term == o.constant_term:
            return True
        try:
            if not self.is_parallel_to(o):
                return False
            vector1 = self.basepoint.minus(o.basepoint)
            return vector1.is_parallel_to(o.normal_vector) and vector1.is_parallel_to(self.normal_vector)
        except Exception:
            return False

    def __getitem__(self, item):
        return self.normal_vector[item]


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps