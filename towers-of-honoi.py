def print_move(start, end):
    print (start, '->', end)

def towers(n, start, end):
    # if there is only one disk (move from start to end)
    if n == 1:
        print_move(start, end)
    else: 
    # the other tower is 6 - [start + end]
        other = 6 - (start + end)
    # pass in the next disk, and move it.
        towers(n - 1, start, other)
        print_move(start, end)
    # pass in the next disk, and move it.
        towers(n - 1, other, end)

towers(3,1,3)