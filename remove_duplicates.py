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

    #sort and rewite back to orignal file
    data[1].sort(reverse=True)
    data[1]=[data[1][i] for i in range(len(data[1])) if i%2==0]
    with open(fname, "w") as fout:
        json.dump(data, fout)
