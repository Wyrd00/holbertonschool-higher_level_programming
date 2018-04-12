#!/usr/bin/python3
if __name__ == "__main__":
        import sys
        num = 0
        total = 0
        for i in range(1, len(sys.argv)):
                num = int(sys.argv[i])
                total += num
        print(total)
