"""
二阶行列式和三阶行列式可以使用对角线方法计算
"""

D1 = [
    ['a11', 'a12'],
    ['a21', 'a22']
]

def second (D):
    print('%s * %s - %s * %s' % (D[0][0], D[1][1], D[0][1], D[1][0]))

# second(D1)

"""
三阶行列式也可以用类似方法计算
"""

D2 = [
    ['a11', 'a12', 'a13'],
    ['a21', 'a22', 'a23'],
    ['a31', 'a32', 'a33']
]

def third (D):
    print("""
    %s%s%s + %s%s%s + %s%s%s
    -
    %s%s%s - %s%s%s - %s%s%s
    """ % (
        D[0][0], D[1][1], D[2][2],
        D[0][1], D[1][2], D[2][0],
        D[0][2], D[1][0], D[2][1],
        D[0][2], D[1][1], D[2][0],
        D[0][0], D[1][2], D[2][1],
        D[0][1], D[0][1], D[2][2]
    ))

# third(D2)

"""
Reverse few 逆序数的概念
排列 32514的逆序
3 -> 0
2 -> 1
5 -> 0
1 -> 3
4 -> 1
逆序数为5
"""
fews = [3, 2, 5, 5, 1, 4]

def getReverseFewNum (arr):
    totals = 0 #逆序数

    def merge (leftArr, rightArr):
        nonlocal totals
        temp = []
        i = j = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                temp.append(leftArr[i])
                i += 1
            else:
                temp.append(rightArr[j])
                totals += len(leftArr) - i # 计算逆序的关键一步
                j += 1
        
        if i == len(leftArr):
            temp += rightArr[j:]
        else:
            temp += leftArr[i:]

        return temp
    
    def merge_sort (arr):
        if len(arr) <= 1:
            return arr
        
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)

    # print(merge_sort(arr))

    return totals        

# print(getReverseFewNum(fews))


"""
创建一个NxN矩阵,计算矩阵展开式
"""
N = 4

def createD (N):
    D = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append('a%d%d' % (i + 1, j + 1))
        D.append(row)
    
    return D

# 全排列算法
def get_all_fron (length):
    all = list(range(length))
    # 返回数组
    result = []
    def _fron (arr, res_list):
        if len(arr) == 1:
            res_list.append(arr[0])
            result.append(res_list)
        else:
            for i in range(len(arr)):
                # new_res_list = res_list + arr[:1]
                new_arr = arr[:]
                new_arr.pop(i)
                _fron(new_arr, res_list + [arr[i]])

    _fron(all, [])
    return result

# print(get_all_fron(4))
# 通过全排列算法,我们就能获取到一个NxN的矩阵的计算方式了
def genDString (D):
    string = ''

    for fron in get_all_fron(len(D)):
        if getReverseFewNum(list(map(lambda x : x + 1, fron))) % 2 == 0:
            string += '+'
        else:
            string += '-'
        for i in range(len(fron)):
            string += D[i][fron[i]]
    
    print(string)
    return string




# genDString(createD(4))

# 转置行列式,将行列式翻转

D3 = [
    ['a11', 'a12', 'a13', 'a14'],
    ['a21', 'a22', 'a23', 'a24'],
    ['a31', 'a32', 'a33', 'a34'],
    ['a41', 'a42', 'a43', 'a44']
]

def getDt (D):
    l = len(D)
    Dt = []
    for i in range(l):
        row = []
        for j in range(l):
            row.append(D[j][i])
        Dt.append(row)
    print(Dt)

getDt(D3)


