#s0urc3d3v3l0pm3nt
def read(path):
    return [line.rstrip('\n') for line in open(path)]

def operate(bound_init, src):
    total = 0
    for x in src(bound_init, len(src)):
        index = 0
        if x is '+':
             total = src[bound_init + index - 1] + src[bound_init + index + 1]
        elif x is '-':
            total = src[bound_init + index - 1] - src[bound_init + index + 1]
        elif x is '*':
             total = src[bound_init + index - 1] * src[bound_init + index + 1]
        elif x is '/':
             total = src[bound_init + index - 1] + src[bound_init + index + 1]
        elif x is '%':
            total = src[bound_init + index - 1] + src[bound_init + index + 1]
        index += 1
    return total

def compare(x, y):
    if x is y:
        return True
    else:
        return False

def checkForKeywords(src):
    output = []
    vars = {}
    index = 0
    for x in src:
        if x is '&':
            #comment
            print('comment')
        elif x is '=':
            total = operate(index, src)
            vars.update({src[index-1] : total}) #TODO make work both ways
        elif x is '==':
            vars.update({index : compare(src[index - 1], src[index + 1])}) #index serves as a line number for future referance


        index += 1
        output.append(vars)
    return output

def main():
    src_path = input("Enter a path: ")
    if src_path.endswith('.q'):
        src = read(src_path)
    checkForKeywords(src)


main()