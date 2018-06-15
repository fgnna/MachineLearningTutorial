from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):
    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    '''交换行'''

    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]

    '''给某一行的左右乘以一个倍数'''

    def multiply_coefficient_and_row(self, coefficient, row):
        p = self.planes[row]
        self.planes[row] = Plane(p.normal_vector.times_scalar(coefficient), p.constant_term * coefficient)

    '''
    某一行加法到另一行
    row_to_add 添加行
    row_to_be_added_to 被添加的行
    '''

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        if coefficient == 0:
            return

        self.multiply_coefficient_and_row(coefficient, row_to_add)
        print()
        p_to_add = self.planes[row_to_add]
        p_added_to = self.planes[row_to_be_added_to]
        p_new = Plane(Vector([x + y for x, y in zip(p_to_add.normal_vector, p_added_to.normal_vector)]),
                      p_to_add.constant_term + p_added_to.constant_term)
        self.planes[row_to_be_added_to] = p_new

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i, p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def swap_with_row_below_for_nonzero_coefficient_if_able(self, row, col):
        #平面数
        num_equations = len(self)
        #从下一个平面开始计算交换
        for k in range(row + 1, num_equations):
            #直到找到一个指定维度不为0的平面，并进行交换后 返回
            coefficient = MyDecimal(self[k].normal_vector[col])
            if not coefficient.is_near_zero():
                self.swap_rows(row, k)
                return True
        return False

    def clear_coefficients_below(self, row, col):
        #平面数
        num_equations = len(self)
        #要消除的系数
        beta = MyDecimal(self[row].normal_vector[col])
        #找出下面每行的同位系数，进行倍减消除
        for k in range(row + 1, num_equations):
            n = self[k].normal_vector
            gamma = n[col]
            #计算出倍数值，使负倍数并让其相加，得出消除系数的倍数
            alpha = -gamma / beta
            print(alpha)
            print(self[k])
            self.add_multiple_times_row_to_row(alpha, row, k)

    def compute_triangular_form(self):
        system = deepcopy(self)

        def printLinsys():
            if len(system) == 2:
                print("第次冒泡：\n{}\n{}:".format(system[0], system[1]))
            if len(system) == 3:
                print("第次冒泡：\n{}\n{}\n{}:".format(system[0], system[1], system[2]))
            if len(system) == 4:
                print("第次冒泡：\n{}\n{}\n{}\n{}:".format(system[0], system[1], system[2], system[3]))

        #维度
        num_equations = len(system)
        #平面数
        num_variables = system.dimension
        j = 0
        for i in range(num_equations):
            while j < num_variables:
                c = MyDecimal(system[i].normal_vector[j])
                if c.is_near_zero():
                    #这一维度为零，进行交换环节
                    swap_succeeded = system.swap_with_row_below_for_nonzero_coefficient_if_able(i, j)
                    #如何没有可进行交换行，维度位置右移一位，继续进行交换环节
                    if not swap_succeeded:
                        j += 1
                        continue
                #当前平面交换完毕后，进行系数消除
                print("sssss--------------------------------------")
                printLinsys()
                system.clear_coefficients_below(i, j)
                print("+++++--------------------------------------")
                printLinsys()
                j += 1
                break
        printLinsys()
        return system

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i + 1, p) for i, p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


'''测试用例'''

# p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
#
# s = LinearSystem([p0, p1, p2, p3])
# s.swap_rows(0, 1)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print('test case 1 failed')
#
# s.swap_rows(1, 3)
# if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
#     print('test case 2 failed')
#
# s.swap_rows(3, 1)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print('test case 3 failed')
#
# s.multiply_coefficient_and_row(1, 0)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print('test case 4 failed')
#
# s.multiply_coefficient_and_row(-1, 2)
# if not (s[0] == p1 and
#         s[1] == p0 and
#         s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
#         s[3] == p3):
#     print('test case 5 failed')
#
# s.multiply_coefficient_and_row(10, 1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
#         s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
#         s[3] == p3):
#     print('test case 6 failed')
#
# print(s)
# print("------------------")
#
# s.add_multiple_times_row_to_row(0, 0, 1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10') and
#         s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
#         s[3] == p3):
#     print('test case 7 failed')
#
# s.add_multiple_times_row_to_row(1, 0, 1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
#         s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
#         s[3] == p3):
#     print('test case 8 failed')
#
# s.add_multiple_times_row_to_row(-1, 1, 0)
# if not (s[0] == Plane(normal_vector=Vector(['-10', '-10', '-10']), constant_term='-10') and
#         s[1] == Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12') and
#         s[2] == Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3') and
#         s[3] == p3):
#     print('test case 9 failed')

''' 三角形化测试用例 '''

# p1 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0', '2', '-1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1', '0', '1']), constant_term='-1')
# p4 = Plane(normal_vector=Vector(['2', '3', '2']), constant_term='1')
# s = LinearSystem([p1, p2, p3, p4])
# t = s.compute_triangular_form()

# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='2')
# s = LinearSystem([p1, p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == p2):
#     print('test case 1 failed')
#
# p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='2')
# s = LinearSystem([p1, p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == Plane(constant_term='1')):
#     print('test case 2 failed')

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
p4 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
s = LinearSystem([p1, p2, p3, p4])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2 and
        t[2] == Plane(normal_vector=Vector(['0', '0', '-2']), constant_term='2') and
        t[3] == Plane()):
    print('test case 3 failed')

# p1 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1', '2', '-5']), constant_term='3')
# s = LinearSystem([p1, p2, p3])
# t = s.compute_triangular_form()
# if not (t[0] == Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2') and
#         t[1] == Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1') and
#         t[2] == Plane(normal_vector=Vector(['0', '0', '-9']), constant_term='-2')):
#     print('test case 4 failed')
