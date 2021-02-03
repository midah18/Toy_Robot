
def moving_square(size):
    """
    it moves in a square
    """
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")
    return size


def move_rectangle(length, width):
    """
    it moves in a rectangle
    """
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_circle():
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


def square_dancing(size):
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        moving_square(size)


def move_crop_circle(length):
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle()


def move():
    '''
    its_dancing(), it is what it is
    '''
    moving_square(10)
    move_rectangle(20, 10)
    move_circle()
    square_dancing(20)
    move_crop_circle(20)


if __name__ == "__main__":
    move()