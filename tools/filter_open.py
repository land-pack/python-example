def main():
    cache = []
    stack = []
    flag = False
    with open("test.txt", "r") as fd:
        
        lines = fd.readlines()
        for line in lines:
            if not line.isspace():
                stack.append(line)
                if 'open' in line:
                    print("true")
                    flag = True   
            else:
                print(line)
                if flag:
                    cache.append(stack)
                    flag = False
                stack = []

    print(cache)

if __name__ == '__main__':
    main()
