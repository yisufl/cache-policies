import sys
import random

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'w') as file:
            
            k = random.randint(1, 50)
            m = random.randint(50, 500)

            file.write(f"{k} {m}\n")

            rm = [str(random.randint(0, 50)) for i in range(m)]

            file.write(' '.join(rm))

            file.close()

    return 0




if __name__ == "__main__":
    main()