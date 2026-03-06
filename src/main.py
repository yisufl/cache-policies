import sys
from pathlib import Path
from collections import deque

import fifo
import lru
import optff

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            k, m = map(lambda x: int(x), file.readline().split())
            requests = list(map(lambda x: int(x), file.readline().split()))

            if k < 1:
                print("cache capacity must be >= 1")
                return

            if len(requests) != m:
                print("number of requests does not match sequence")
                return
            

            fifoMisses = 0
            lruMisses = 0
            optffMisses = 0

            
            out = Path(sys.argv[1]).with_suffix(".out")

            with open(out, 'w') as fileOut:
                fifoText = f"FIFO  : {fifoMisses}\n"
                lruText = f"LRU   : {lruMisses}\n"
                optffText = f"OPTFF : {optffMisses}"

                print(fifoText, lruText, optffText, sep='')

                fileOut.write(fifoText)
                fileOut.write(lruText)
                fileOut.write(optffText)

                fileOut.close()

            file.close()

    return 0





if __name__ == "__main__":
    main()