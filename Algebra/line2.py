# 这个项目设计来帮你熟悉 python list 和线性代数# 这个项目设
# 你不能调用任何NumPy以及相关的科学计算库来完成作业


# 本项目要求矩阵统一使用二维列表表示，如下：
import fractions
from copy import deepcopy
from helper import *

A = [[1, 2, 3],
     [2, 3, 3],
     [1, 2, 5]]

B = [[1, 2, 3, 5],
     [2, 3, 3, 5],
     [1, 2, 5, 1]]

# 向量也用二维列表表示
C = [[1],
     [2],
     [3]]

# TODO 创建一个 4*4 单位矩阵
I = [[1, 2, 3, 5],
     [2, 3, 3, 5],
     [7, 3, 8, 9],
     [1, 2, 5, 1]]


def printI(M=I):
    for i, p in enumerate(M):
        print(p)
    print('\n')


# TODO 返回矩阵的行数和列数

def shape(M):
    return len(M), len(M[0])


# TODO 每个元素四舍五入到特定小数数位
# 直接修改参数矩阵，无返回值
def matxRound(M, decPts=4):
    for i, p in enumerate(M):
        for n, p1 in enumerate(p):
            p[n] = round(p1, decPts)


# TODO 计算矩阵的转置
def transpose(M):
    m_shape = shape(M)
    # 先创一个倒置的空矩阵
    MT = [[0 for i in range(m_shape[0])] for i in range(m_shape[1])]

    # 然后进行交换 a[i][j] = b[j][i]
    for i in range(m_shape[1]):
        for j in range(m_shape[0]):
            MT[i][j] = M[j][i]

    printI(MT)
    return MT


# TODO 计算矩阵乘法 AB，如果无法相乘则raise ValueError
def matxMultiply(A, B):
    A_S = shape(A)
    B_S = shape(B)
    if A_S[1] != B_S[0]:
        raise ValueError()

    # 先创一个空矩阵 A的行数 B的列数
    MT = [[0 for i in range(B_S[1])] for i in range(A_S[0])]

    for i in range(A_S[0]):
        for j in range(B_S[1]):
            for n in range(A_S[1]):
                MT[i][j] += A[i][n] * B[n][j]
    return MT


# TODO 构造增广矩阵，假设A，b行数相同
def augmentMatrix(A, b):
    if shape(A)[0] != shape(b)[0]:
        raise ValueError()
    return [A[i] + b[i] for i, p in enumerate(A)]


'''
    2.2 初等行变换
'''


# TODO 交换两行
# 直接修改参数矩阵，无返回值
def swapRows(M, r1, r2):
    M[r1], M[r2] = M[r2], M[r1]


# TODO r1 <--- r1 * scale
# TODO 把某行加乘以若干倍
# scale为0是非法输入，要求 raise ValueError
# 直接修改参数矩阵，无返回值
def scaleRow(M, r, scale):
    if (scale == 0):
        raise ValueError()

    for i, p in enumerate(M[r]):
        M[r][i] = p * scale


# TODO r1 <--- r1 + r2*scale
# 直接修改参数矩阵，无返回值
def addScaledRow(M, r1, r2, scale):
    M_COPY = deepcopy(M)
    scaleRow(M_COPY, r2, scale)
    M[r1] = [p1 + p2 for p1, p2 in zip(M[r1], M_COPY[r2])]


# 不要修改这里！
A = generateMatrix(3, 10, singular=False)
b = np.ones(shape=(3, 1), dtype=int)  # it doesn't matter
Ab = augmentMatrix(A.tolist(), b.tolist())  # 请确保你的增广矩阵已经写好了

Ab_shape = shape(Ab)




for i in range(Ab_shape[0]):
    if(Ab[i][])

    for n in range(i+1,Ab_shape[0]):


printInMatrixFormat(Ab, padding=3, truncating=0)

print(fractions.Fraction(2, 4) + 6)
