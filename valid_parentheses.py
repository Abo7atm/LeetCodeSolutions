# sudo code -- again
# for char in string
#   if char is opening
#       count opening
#       add closing to expected stack
#           
def is_valid(s: str) -> bool:
    nxt = []
    for i in s:
        if ord(i) in [40, 91, 123]: # chr(124) = '|'
            nxt.insert(0, chr(ord(i)+1))
        else:
            if len(nxt) == 0:
                return False
            a = nxt.pop(0)
            print(a)
            if a != i:
                print('false 2')
                return False
    if len(nxt) == 0:
        return True
    return False

if __name__=='__main__':
    while True:
        s = input('enter set of paran: (x to exit) ')
        if s == 'x':
            break
        print(is_valid(s))
