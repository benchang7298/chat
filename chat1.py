
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())   
    return lines        


def convert(lines):
    person = None
    allen_c = 0
    allen_strick = 0
    allen_p = 0
    viki_c = 0
    viki_strick = 0
    viki_p = 0
    for line in lines:  # extract the data one by one column and put in line
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
               allen_strick += 1 
            elif s[2] == '圖片':
                allen_p += 1   
            else:
               for m in s[2:]:  #collect all the data after [2:~~]
                   allen_c += len(m) 
        elif name == 'Viki':
            if s[2] == '貼圖':
               viki_strick += 1
            elif s[2] == '圖片':
                viki_p += 1     
            else:   
                for m in (s[2:]):
                    viki_c += len(m)
    print('Allen total speak: ', allen_c, 'words','and send',allen_strick, 'strickers',allen_p, 'pictures')
    print('Viki total speak: ', viki_c, 'words', 'and send', viki_strick, 'strickers', viki_p, 'prctures')


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)
main()