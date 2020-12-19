def parse_input(i):
    r, c, password = tuple(i.split())
    l, r = map(int, r.split('-'))
    c = c[0]
    return (l, r, c, password)

def isValid(left, right, char, password):
    charMap = {}
    for c in password:
        charMap[c] = charMap.get(c, 0) + 1
    if charMap.get(char) == None:
        return False
    elif charMap.get(char) > right:
        return False
    elif charMap.get(char) < left:
        return False
    else:
        return True
def isValidPart2(left, right, char, password):
    if password[left-1] == password[right-1] == char:
        return False
    elif password[left-1] != char and password[right-1] != char:
        return False
    elif password[left-1] == char:
        return True
    elif password[right-1] == char:
        return True

if __name__ == '__main__':
    count_valid = 0
    while True:
        try:
            inp = input()
            if isValidPart2(*parse_input(inp)):
                count_valid += 1
        except EOFError:
            break
    print(count_valid)
