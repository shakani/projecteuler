import numpy as np

test = np.array([[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]])

# parse data file
data = np.zeros((80,80))
with open("p081-data.txt", 'r') as f:
    for i in range(80):
        data[i] = list(map(int, f.readline().strip('\n').split(',')))

def min_shape(arr): 
    return [min(arr[i], arr[i+1]) for i in range(len(arr)-1)]

def feed_forward(arr1, arr2): # arr 2 is longer
    if len(arr1) > len(arr2):
        return feed_forward(arr2, arr1)
    else:
        return arr1 + min_shape(arr2)

def path_sum(mat):
    mat = np.fliplr(mat)
    N = int(mat.size**0.5)
    answer = np.array([0])
    for i in range(1-N, N):
        #print(np.diag(mat, i), np.diag(mat, i+1), i)
        print(feed_forward(np.diag(mat, i), np.diag(mat, i+1)))

path_sum(test)
