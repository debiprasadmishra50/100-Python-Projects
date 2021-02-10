import time
def print_sending():
    for num in range(0, 5):
        print("\rSending.", end="")
        time.sleep(0.5)
        print("\rSending..", end="")
        time.sleep(0.5)
        print("\rSending...", end="")
        time.sleep(0.5)
        print("\rSending....", end="")
        time.sleep(0.5)
        print("\rSending.....", end="")
        time.sleep(0.5)
print_sending()
