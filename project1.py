# ROBO SPEAKER

import os


if __name__ == '__main__':
    print("Welcome to Robo Speaker")
    x = input("Enter some lines: ")
    command = f"say {x}"
    os.system(command)