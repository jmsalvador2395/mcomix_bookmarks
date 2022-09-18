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

    in_str='/home/john/mnt/.h/mnt/.h/'
    in_len=len(in_str)
    out_str='/home/john/mnt/.h/'
    for bm in range(len(data[1])):
        if data[1][bm][1][:in_len] == in_str:
            print(f'updated: {data[1][bm][1]}')
            print(f'{out_str}{data[1][bm][1][in_len:]}')
            data[1][bm][1]=f'{out_str}{data[1][bm][1][in_len:]}'

    #check for and remove duplicates
    dup=False
    for i in range(1, len(data[1])):
        if data[1][i][1] == data[1][i-1][1]:
            print('found duplicates')
            dup=True
            break
        else:
            print(data[1][i-1][1])
            print(data[1][i][1])
            print()

    if dup:
        indeces=[]
        for i in range(1, len(data[1])):
            if data[1][i][1] == data[1][i-1][1]:
                indeces.append(i)
        print(indeces)

        for i in indeces[::-1]:
            data[1].pop(i)

    """
    #deletes entries whose directories begin with {query}
    query='/home/johnt/'
    len_query=len(query)
    indeces=[]
    for i in range(len(data[1])):
        if data[1][i][1][:len_query] == query:
            indeces.append(i)

    for i in indeces[::-1]:
        data[1].pop(i)
    """

    """
    #write out to bookmarks.json
    with open(fname, "w") as fout:
        json.dump(data, fout)
    """
