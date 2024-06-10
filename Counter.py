import time

def countdown(minutes):
    for minute in range(minutes, 0, -1):
        for second in range(60, 0, -1):
            print(f"{minute - 1:02}:{second - 1:02}", end="\r")
            time.sleep(1)

def start_presentations(total_presenters):
    presenter_number = 1
    while presenter_number <= total_presenters:
        print(f"\nPresenter {presenter_number}, your time starts now!")
        countdown(1)  # 1 minute countdown
        print(f"\nPresenter {presenter_number}, your time is up!")
        presenter_number += 1

if __name__ == "__main__":
    total_presenters = 10
    start_presentations(total_presenters)
