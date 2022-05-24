import json
import os


if __name__ == '__main__':
    #file strings
    fname='bookmarks.json'
    bak='.bak'

    #read in original json
    fin=open(fname)
    data1=json.loads(fin.read())
    fin.close()

    fin=open(fname+bak)
    data2=json.loads(fin.read())
    fin.close()
    print(f'data1: {len(data1[1])}, data2: {len(data2[1])}')
