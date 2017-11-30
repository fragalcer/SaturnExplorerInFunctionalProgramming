
class Robot:
    facing, x, y, map_size_y, map_size_x = None, None, None, None, None
    def __init__(self, x, y, facing, map_size_x, map_size_y):
        self.facing, self.x, self.y, self.map_size_x, self.map_size_y = facing, x, y, map_size_x, map_size_y

def rotate_left(robot):
    x, y, map_size_x, map_size_y = robot.x, robot.y, robot.map_size_x, robot.map_size_y
    if(robot.facing) == 'N':
        return Robot (x, y, 'W', map_size_x, map_size_y)
    elif (robot.facing) == 'E':
        return Robot(x, y, 'N', map_size_x, map_size_y)
    elif (robot.facing) == 'S':
        return Robot(x, y, 'E', map_size_x, map_size_y)
    elif (robot.facing) == 'W':
        return Robot(x, y, 'S', map_size_x, map_size_y)

def rotate_right(robot):
    x, y, map_size_x, map_size_y = robot.x, robot.y, robot.map_size_x, robot.map_size_y
    if (robot.facing) == 'N':
        return Robot(x, y, 'E', map_size_x, map_size_y)
    elif (robot.facing) == 'E':
        return Robot(x, y, 'S', map_size_x, map_size_y)
    elif (robot.facing) == 'S':
        return Robot(x, y, 'W', map_size_x, map_size_y)
    elif (robot.facing) == 'W':
        return Robot(x, y, 'N', map_size_x, map_size_y)

def move_robot(robot):
    x, y, map_size_x, map_size_y = robot.x, robot.y, robot.map_size_x, robot.map_size_y
    if robot.facing == 'N':
        new_x, new_y = x, y + 1
    if robot.facing == 'S':
        new_x, new_y = x, y - 1
    if robot.facing == 'E':
        new_x, new_y = x + 1, y
    if robot.facing == 'W':
        new_x, new_y = x - 1, y

    if new_x < 0 or new_y < 0 or new_x > robot.map_size_x or new_y > map_size_y:
        raise ValueError('Position of Robot is out of bounds.')
    return Robot(new_x, new_y, robot.facing, map_size_x, map_size_y)


def print_robot(robot):
    return robot.x, " ", robot.y, " ", robot.facing


def read_instruction(robot, list_of_instructions):
    print(list_of_instructions)
    print (robot.x, ' ', robot.y, ' ', robot.facing)
    if len(list_of_instructions) == 0:
        return robot

    next_instruction = list_of_instructions.pop(0)

    if next_instruction == 'L':
        return (read_instruction(rotate_left(robot), list_of_instructions))
    elif next_instruction == 'R':
        return (read_instruction(rotate_right(robot), list_of_instructions))
    elif next_instruction == 'M':
        return (read_instruction(move_robot(robot), list_of_instructions))


    # for elem in my_list:
    #     if elem == 'M':
    #         my_robot.move()
    #     elif elem == 'L':
    #         my_robot.rotate_left()
    #     elif elem == 'R':
    #         my_robot.rotate_right()
    #     print(my_robot.show_current_location())
    #
    # print(my_robot.show_current_location())

if __name__ == "__main__":
    map_size = input().split()
    width = int(map_size[0])
    height = int(map_size[1])
    map_size_x, map_size_y = width, height

    x_pos, y_pos, facing = input().split()
    instructions = input()

    my_robot = Robot(int(x_pos), int(y_pos), facing, map_size_x, map_size_y)

    my_list = list(instructions)
    print(my_list)

    print(print_robot(read_instruction(my_robot, my_list)))