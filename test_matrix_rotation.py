from matrix_rotation import rotate_array as rot
arrays = [([list(range(x)) for i in range(y)], orient) for x,y,orient in [(5,8,False), (5,5,False), (8,5,True)]]
for array, orient in arrays:
    print('\n\n\n')
    for line in array:
        print(*line)
    for angle in range(45, 360, 45):
        print('\n')
        for line in rot(array, angle, orient):
            print(*line)