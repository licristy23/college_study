import math

def first_time(n):
    return 100 * n**2

def second_time(n):
    return 2**n

def find_smallest_n():
    n = 1
    while True:
        time_1 = first_time(n)
        time_2 = second_time(n)

        if time_1 <= time_2:
            return n
        n += 1

def main():
    smallest_n = find_smallest_n()
    print(f"O menor valor de n é: {smallest_n}")

if __name__ == "__main__":
    main()
