array = [list(range(7)) for i in range(6)]

'''
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]

array[0][0]
array[1][0], array[0][1]
2,0 1,1 0,2

array[len-1][0], array[len-2][1], ... array[0][len]
array[len-1][1], array[len-2][2], ... array[0][len+1]

array[5][2], array[4][3], ... array[1][6]
array[5][3], array[4][4], ... array[2][6]
54-36, 55-46, 56
array[len-1][diff+1], array[len-2][diff+2], ... array[diff+1][len[0]+1]
array[len-1][diff+2], array[len-2][diff+3], ... array[diff+2][len[0]+1]
array[-1][diff+1]... array[diff+1][-1]
array[len-1][len[0]-1]
'''
'''
       [0]
      [0, 1]
    [0, 1, 2]
   [0, 1, 2, 3]
 [0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
 [2, 3, 4, 5, 6]
   [3, 4, 5, 6]
    [4, 5, 6]
      [5, 6]
       [6]'''
def right_45(array):
    ab = abs(len(array)-len(array[0]))
    m = min(len(array), len(array[0]))
    head = [[array[r][c] for r,c in zip(range(row-1, -1, -1), range(row))] for row in range(1, m+1)]
    wide_or_square = len(array) <= len(array[0])
    tall = not wide_or_square
    return head + [[array[r][c] for r,c in zip(range(m-1+row*tall, row*tall-1, -1), range(row*wide_or_square, m+row*wide_or_square+1))
         ] for row in range(1, ab+wide_or_square)
    ] + [[array[r][c] for r,c in zip(range(len(array)-1, ab*tall+row-1, -1), range(ab*wide_or_square+row, len(array[0])+wide_or_square))
         ] for row in range(wide_or_square, m)
    ]
