import os
def getNums(fname):
    filename= os.path.join( os.getcwd(), fname)
    file = open(filename, 'r')
    count=0
    arr=[]
    for line in file:
        count += 1
        arr.append(line.strip())
    file.close()
    return (arr)