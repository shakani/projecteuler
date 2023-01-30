'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

'''

# probably need BFS to solve

# Parse text file into nested list
tree = []
with open('p067_triangle.txt','r') as f:
    for line in f:
        tree.append(list(map(int, line.strip('\n').split(' '))))

class Tree(): # tree object
    def __init__(self, arr):
        self.arr = arr
        self.L = len(arr)

    def add_arr(self, row, addend): # adds some array addend to given row of tree
        for i, val in enumerate(addend):
            self.arr[row][i] += val

    def get_max_of_row(self, row): # maps row of length N to row of length (N-1) where we've taken the max of pairwise elements
        return [max(self.arr[row][j], self.arr[row][j+1]) for j in range(row)]

    def max_path_sum(self): # adds the pairwise max of rows bottom up to top of tree; guarantees max path sum is placed into head of tree
        for j in range(1, self.L)[::-1]:
            self.add_arr(j-1, self.get_max_of_row(j))
        return self.arr[0][0]

# debug with a smaller tree
#smalltree_arr = [[3], [7,4], [2,4,6], [8,5,9,3]]
#smalltree = Tree(smalltree_arr)

my_tree = Tree(tree)
print(my_tree.max_path_sum())
