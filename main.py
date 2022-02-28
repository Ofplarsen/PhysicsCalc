import SVT
import rectilinear_motion


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ans = rectilinear_motion.RectilinearMotion.solve_method(v0=0, v=45, x=1.5, a=675)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
