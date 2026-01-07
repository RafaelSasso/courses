import random

def main():
    count = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        p = x + y
        right = False

        for _ in range(3):
            a = int(input(f'{x} + {y} = '))
            if(a==p):
                right = True
                count+=1
                break
            else:
                print('EEE')

        if(not right):
            print(f'{x} + {y} = {p}')

    print(f'Score: {count}')


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if(1>level or level>3):
                raise ValueError
            break
        except ValueError:
            pass

    return level

def generate_integer(level):
    count = 0
    if level == 1:
        n = random.randint(0,9)
    else:
        low = 10 ** (level - 1)
        high = (10 ** level) - 1
        n = random.randint(low,high)

    return n

if __name__ == "__main__":
    main()
