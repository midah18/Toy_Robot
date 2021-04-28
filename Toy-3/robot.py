"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 2 exercise.
"""


# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', "replay", "replay silent", "silent", "reversed", "replay reversed","replay reversed silent","-"]

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100
history_appended = []
silent = False
reverse = False

def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split("-", 1)
    if '-' in command:
        return args[0], args[1]
    
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """
    command = command.lower()
    (command_name, arg) = split_command_input(command)
    arg1 = ''
    arg2 = ''
    
    if '-' in arg:
        (arg1,arg2) =split_command_input(arg)
    
    try:
        arg1, arg2 = split_command_input(arg)
    except ValueError:
        pass
    
    if '-' in command and is_int(arg1) and is_int(arg2):
        return True
    
    elif ("replay" == command_name and (is_int(arg1) and 
        (arg2 == 'silent' or arg2 == 'reversed'))):
        return True
        
    elif "silent" in command:
        command_name = command
        arg1 = ""
        return (command_name.lower() in valid_commands and 
                (len(arg1) == 0 or is_int(arg1)))
        
    elif "reversed" in command.lower():
        command_name = command
        arg1 = ""
        return (command_name.lower() in valid_commands and (len(arg1) == 0 
            or is_int(arg1)))
        
    else:
        (command_name, arg1) = split_command_input(command)

    return (command_name.lower() in valid_commands and (len(arg1) == 0 or
             is_int(arg1)))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - filters out all non-movement commands and prints them out  
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    global new_x, new_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    global silent
    global reverse
    (command_name, arg) = split_command_input(command)

    if "silent" in command:
        silent = True
        
    if "reversed" in command:
        reverse = True

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))
    # elif "replay" in command and command[1].isdigit() or command[-1].isdigit:
    #     (do_next, command_output) = replay_extra(history_appended, robot_name, command)
    elif "replay" == command_name:
        (do_next, command_output) = replay(history_appended, robot_name, command)

        
    if silent == False:
        print(command_output)
        show_position(robot_name)
        
    return do_next


def history(command, history_appended):
    if "replay" not in command and "history" not in command and "help" not in command:
        history_appended.append(command)
        return history_appended
    
    
def replay(history_appended, robot_name, command):
    global silent,reverse
    n = 0
    (command_name, arg) = split_command_input(command)
    
    try:
        arg1, arg2 = split_command_input(arg)
    except ValueError:
        pass
    
    if '-' in command and reverse == True:
        f = int(arg[0])
        m = int(arg[-1])-1
        for i in range(m,f,-1):
            handle_command(robot_name, history_appended[i])
            n += 1 
    
    elif "-" in command:
        f = int(arg[0])+1
        m = int(arg[-1])
        for i in range(f, m):
            handle_command(robot_name, history_appended[i])
            n += 1 
            
    elif "replay" == command_name and (is_int(arg1) and arg2 == 'reversed'):
        arg = int(arg1) * (1)
        for i in range(arg-1,-1,-1):
            handle_command(robot_name, history_appended[i])
            n += 1 
        
            
    elif "replay" == command_name and (is_int(arg1) and arg2 == 'silent'):
        arg = int(arg1) * (-1)
        for i in range(arg,0):
            handle_command(robot_name, history_appended[i])
            n += 1 
    
    elif len(arg) == 1:
        arg = int(arg) * (-1)
        for i in range(arg,0):
            handle_command(robot_name, history_appended[i])
            n += 1 
    
    elif reverse == True:
        for i in reversed(history_appended):
            handle_command(robot_name, i)
            n += 1
            
    else:
        for i in history_appended:
            handle_command(robot_name, i)
            n += 1
     
    
    x = "commands."
    silent = False
    reverse = False
    
    if "silent" in command and "reversed" in command:
        return True, ' > '+robot_name+' replayed ' +str(n) +' commands in reverse silently.'
    elif "silent" in command:
        return True, ' > '+robot_name+' replayed ' +str(n) +' commands silently.'
    elif "reversed" in command:
        return True, ' > '+robot_name+' replayed ' +str(n) +' commands in reverse.'      
    else:
        return True, ' > '+robot_name+' replayed ' +str(n) + " " + (x)     
   
        
def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, history_appended
    position_x = 0
    position_y = 0
    current_direction_index = 0



    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    
    command = get_command(robot_name)
    history(command, history_appended)
    while handle_command(robot_name, command):
        command = get_command(robot_name)
        history(command, history_appended)
        


    output(robot_name, "Shutting down..")
    history_appended = []


if __name__ == "__main__":
    robot_start()
