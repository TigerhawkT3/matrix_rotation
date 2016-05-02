def rotate_45(array, left=False):
    '''
    Rotates a rectangular 2D array by 45 degrees. Default rotates clockwise (right).
    Parameter:
        left (bool): Specifies counter-clockwise (left) rotation instead.
    '''
    direction = -2*left + 1
    ab = abs(len(array)-len(array[0]))
    m = min(len(array), len(array[0]))
    tall = len(array) > len(array[0])
    return [[array[r*direction-left][c*direction-left] for r,c in zip(range(row-1, -1, -1), range(row))
            ][::direction] for row in range(1, m+1)
       ] + [[array[r*direction-left][c*direction-left] for r,c in zip(range(m-1+row*tall, row*tall-1, -1),
                                                                   range(row*(not tall), m+row*(not tall)+1))
            ][::direction] for row in range(1, ab+(not tall))
       ] + [[array[r*direction-left][c*direction-left] for r,c in zip(range(len(array)-1, ab*tall+row-1, -1),
                                                                   range(ab*(not tall)+row, len(array[0])+(not tall)))
            ][::direction] for row in range((not tall), m)
       ]
