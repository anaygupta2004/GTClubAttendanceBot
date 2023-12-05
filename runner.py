from multiprocessing import Process
from attendance_bot import AttendanceBot

def read_names():
    names = []
    with open("names_list.txt") as f:
        name = f.readline().rstrip()

        while name:
            names.append(name)
            name = f.readline().rstrip()
    return names

if __name__ == "__main__":
    names = read_names()
    for name in names:
        bot = AttendanceBot()
        bot.formSequence(name)