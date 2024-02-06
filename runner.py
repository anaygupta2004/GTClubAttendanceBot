from multiprocessing import Process
from attendance_bot import AttendanceBot


def process_name(name):
    bot = AttendanceBot()
    bot.formSequence(name)


def read_names_from_file(file_path):
    with open(file_path, "r") as f:
        names = [line.strip() for line in f if line.strip()]
    return names


if __name__ == "__main__":
    text_file_path = "/app/names_list.txt"
    names = read_names_from_file(text_file_path)

    processes = []
    for name in names:
        p = Process(target=process_name, args=(name,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
