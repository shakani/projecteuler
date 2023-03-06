import numpy as np

test = np.array([[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]])

# parse data file
data = np.zeros((80,80))
with open("p081-data.txt", 'r') as f:
    for i in range(80):
        data[i] = list(map(int, f.readline().strip('\n').split(',')))

def get_diag(mat, i): # gets i-th diagonal of matrix
    if i < len(mat):
        return [mat[i-j][j] for j in range(i+1)]
    else:
        return [mat[len(mat)-1-j][i-len(mat)+1+j] for j in range(len(mat)-1 - (i%len(mat)))]

def min_shape(arr): # takes arr of length N and returns arr of length (N-1) where elements are the pairwise minima of arr
    return [min(arr[i], arr[i+1]) for i in range(len(arr)-1)]

def max_shape(arr): # similar to min_shape, but takes arr of length N and returns arr of length (N+1) where pairwise min of boundaries is trivial
    return [arr[0]] + min_shape(arr) + [arr[-1]]

def add_diags(d1, d2): # adds d1 to d2 in the right way
    if len(d1) > len(d2): # d1 is longer; cast to min shape
        return [min_shape(d1)[i] + d2[i] for i in range(len(d2))]
    else: # d1 is shorter; cast to max shape
        return [max_shape(d1)[i] + d2[i] for i in range(len(d2))]

'''
For M as an N x N matrix, computes minimal path sum from M_11 to M_NN by computing minimal path sum to middle diagonal.
Middle diagonal is taken to be matrix elements M_XY where X+Y = N+1.
Minimal distance minimizes distance from M_11 to middle diagonal + M_NN to middle diagonal. 

Time complexity looks like O(N) for loop in the path_sum.
Space complexity is O(N) < O(N^2) for reading in the matrix, so we're good here. 

Probably worse than this if my intermediate methods above aren't optimized. 

'''
def path_sum(arr): # computes min distance to middle diagonal from M_11 
    ans_A, ans_B = get_diag(arr, 0), get_diag(arr, 2*len(arr)-2)
    for i in range(len(arr)-1):
        a = get_diag(arr, i+1)
        b = get_diag(arr, 2*len(arr)-3 - i)
        ans_A, ans_B = add_diags(ans_A, a), add_diags(ans_B, b)

    ans = [ans_A[i] + ans_B[i] - get_diag(arr, len(arr)-1)[i] for i in range(len(ans_A))]
    return int(min(ans))

print(path_sum(data))
