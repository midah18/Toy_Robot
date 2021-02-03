def name_the_robot():
    """
    name of the robot is asked
    name is stored and returned
    """
    name_of_robot = input("What do you want to name your robot? ")
    print(name_of_robot + ": Hello kiddo!")
    return name_of_robot


def get_command_input(name):
    """
    print statement asking user what the robot will do next appears
    user input coverted into casefold and returned
    """
    user_input =  input(f"{name}: What must I do next? ")
    new_input = user_input.casefold()
    return new_input, user_input


def moving_forward(input_from_user, name, direction, x, y):
    """
    since the robot moves on a cartesian plane, x is for x-axis and y is for y-axis
    the instruction(command) and steps(value) is stored in a tuple named same
    same will then determine the direction and number of steps the robot should move
    """
    oldy = y
    oldx = x
    instruction = input_from_user.split()[0]
    steps = int(input_from_user.split()[1])
    same = (instruction, steps) 
    if direction == 1:
        y = oldy + int(steps)
        if y in range(-200, 200):
            print(" > {} moved forward by {} steps.".format(name, steps))
    elif direction == 0 or direction == 4:
        x = oldx - int(steps)
        if x in range(-100,100):
            print(" > {} moved forward by {} steps.".format(name, steps))
    elif direction == 2 or direction == -2:
        x = oldx + int(steps)
        if x in range(-100, 100):
            print(" > {} moved forward by {} steps.".format(name, steps))
    elif direction == -1 or direction == 3:
        y = oldy - int(steps)
        if y in range(-200, 200):
            print(" > {} moved forward by {} steps.".format(name, steps))
    return x, y, direction, instruction, oldx, oldy


def moving_backward(input_from_user, name, direction, x, y):
    """
    since the robot moves on a cartesian plane, x is for x-axis and y is for y-axis
    the instruction(command) and steps(value) is stored in a tuple named same
    same will then determine the direction and number of steps the robot should move
    """
    oldy = y
    oldx = x
    instruction = input_from_user.split()[0]
    steps = int(input_from_user.split()[1])
    same = (instruction, steps)
    if direction == 1:
        y = y - int(steps)
        print(" > {} moved back by {} steps.".format(name, steps))
    elif direction == 0 or direction == 4:
        x = x + int(steps)
        print(" > {} moved back by {} steps.".format(name, steps))
    elif direction == 2 or direction == -2:
        x = x - int(steps)
        print(" > {} moved back by {} steps.".format(name, steps))
    elif direction == -1 or direction == 3:
        y = y + int(steps)
        print(" > {} moved back by {} steps".format(name, steps))
    return x, y, direction, instruction, oldx, oldy


def keep_track_of_position(x, y, steps, name, direction, oldx, oldy):
    """
    this function soley focuses on the position of the robot
    current position is stored and a print statement will be printed
    otherwise
    (since the robot is allowed to move within certain parameters)
    if the robots future position is outside the boundries, it does not move and
    will notify the user
    """
    if x > -101 and x < 101 and y > -201 and y < 201:
        print(" > {} now at position ({},{}).".format(name, x, y))  
    else:
        print("{}: Sorry, I cannot go outside my safe zone.".format(name))
        print(f" > {name} now at position ({oldx},{oldy}).")
        return oldx, oldy, direction
    return x, y, direction


def keep_track_of_sprint(input_from_user, x, y, name, direction, steps):
    """
    the value will decrease by one until it reaches one
    it will take one less step forward
    """
    if steps > 0:
        input_from_user = f"sprint {steps}"
        x, y, direction, instruction, oldx, oldy = moving_forward(input_from_user, name, direction, x, y)
        steps = steps - 1
        return keep_track_of_sprint(input_from_user, x, y, name, direction, steps)
    else:
        return x,y


def direction_left(direction, name, x, y):
    """
    anti-clockwise 
    """
    direction = direction - 1
    if direction < -2:
        direction = 1
    print(f" > {name} turned left.")
    print(" > {} now at position ({},{}).".format(name, x, y))
    return direction


def direction_right(direction, name, x, y):
    """
    clockwise
    x - position on the x-axis
    y - position on the y-axis
    """
    direction = direction + 1
    if direction > 4:
        direction = 1
    print(f" > {name} turned right.")
    print(" > {} now at position ({},{}).".format(name, x, y))
    return direction


def need_help():
    """
    when "help" is the command, the below statements are printed
    """
    print("I can understand these commands:")
    print("OFF  - Shut down robot")
    print("HELP - provide information about commands")
    print("FORWARD - in the direction that one is facing or travelling")
    print("BACK - in the direction that one is not facing or travelling")
    print("SPRINT - accelerates in the direction that one is not facing or travelling")
    print("LEFT - turns left")
    print("RIGHT - turns right")


def off_command(name):
    """
    when "off" is the user input, this function runs
    returns false to prevent it from running
    """
    print(f"{name}: Shutting down..")
    return False


def invalid_command(user_input, name):
    """
    as long as user input is not a valid command, the below will be printed
    """
    print(f"{name}: Sorry, I did not understand '{user_input}'.")
    robot_start


def robot_start():
    """
    This is where the robot starts running
    a certain set of commands is laid
    if user input has that particular command, it will be redirected to the function that
    soley deals with that certain command
    """
    x = 0
    y = 0
    direction = 1

    commands = ["off", "help", "forward", "back", "right", "up", "left", "down", "sprint"]
    robot_on = True
    """
    as long as it is true, robot will continue running
    """
    name = name_the_robot()
    while robot_on:
        """
        user input is split and searches for specific command
        """
        input_from_user, new_input = get_command_input(name)
        cmd = input_from_user.split(" ")

        if "help" in input_from_user:
            need_help()
        elif "off" in input_from_user:
            robot_on = off_command(name)
        elif "forward" == cmd[0] and cmd[1].isdigit():
            x, y, direction, instruction, oldx, oldy = moving_forward(input_from_user, name, direction, x, y )
            x, y, direction = keep_track_of_position(x, y, int(cmd[1]), name, direction, oldx, oldy)
        elif "back" == cmd[0] and cmd[1].isdigit():
            x, y , direction, instruction, oldx, oldy= moving_backward(input_from_user, name, direction, x, y )
            x, y, direction = keep_track_of_position(x, y, int(cmd[1]), name, direction, oldx, oldy)
        elif input_from_user == "left":
            direction = direction_left(direction, name, x, y)
        elif input_from_user == "right":
            direction = direction_right(direction, name, x, y)
        elif "sprint" in cmd and cmd[1].isdigit():
            x, y = keep_track_of_sprint(input_from_user, x, y, name, direction, int(cmd[1]))
            print(" > {} now at position ({},{}).".format(name, x, y))
        else:
            invalid_command(new_input, name)


if __name__ == "__main__":
    robot_start()
