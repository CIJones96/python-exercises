def check(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

if __name__ == "__main__":
    print(check(4))
    print(check(7))
    print(check(0))