def print_line():
    for num in range(0, 10):
        print("\r|", end="")
        time.sleep(0.15)
        print("\r/", end="")
        time.sleep(0.15)
        print("\r-", end="")
        time.sleep(0.15)
        print("\r\\", end="")
        time.sleep(0.15)
        
print_line()
