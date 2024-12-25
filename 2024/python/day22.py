from helper import read_data

PRUNE = 16777216


def calculate(secret: int) -> int:
    result = secret * 64
    secret ^= result
    secret %= PRUNE

    result = int(secret / 32)
    secret ^= result
    secret %= PRUNE

    result = secret * 2048
    secret ^= result
    secret %= PRUNE

    return secret


def main():
    data = read_data("day22.txt")
    result = 0
    for initial_secret in map(int, data.rstrip().split("\n")):
        num = initial_secret
        for _ in range(2000):
            num = calculate(num)
        result += num
    print(result)


if __name__ == "__main__":
    main()
