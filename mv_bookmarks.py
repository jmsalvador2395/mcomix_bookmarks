import json
import os


if __name__ == '__main__':
    #file strings
    fname='bookmarks.json'
    bak='.bak'

    #read in original json
    fin=open(fname)
    data=json.loads(fin.read())
    fin.close()

    #save backup
    with open(fname+bak, 'w') as fout:
        json.dump(data, fout)

    #uncomment and edit directories to run again
    """
    #replace /mnt/ directory with new directory
    for bm in data[1]:
        bm[1]='/home/john/mnt/.h/'+bm[1][5:]

    #write out to bookmarks.json
    with open(fname, "w") as fout:
        json.dump(data, fout)
    """
