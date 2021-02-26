def towerofhanoi(number, start=1, end=3):
    if number:
        towerofhanoi(number-1, start, 6-start-end)
        print(f"Disk {number} from peg {start} to peg {end}")
        towerofhanoi(number-1, 6-start-end, end)


if __name__ == '__main__':
    towerofhanoi(3)