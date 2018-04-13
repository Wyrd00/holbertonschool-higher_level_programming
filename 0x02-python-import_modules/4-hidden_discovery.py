#!/usr/bin/python3
if __name__ == "__main__":
        import hidden_4
        result = dir(hidden_4)
        for i in range(0, len(result)):
                if result[i][0] != '_':
                        print("{}".format(result[i]))
