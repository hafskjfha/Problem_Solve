from re import findall,sub
import os
def main():
    html=os.read(0, 1<<20).decode().splitlines()[0][4:-6]
    encode=str.encode
    print=os.write
    for i in findall(r'<div title="(.*?)">(.*?)</div>',html):
        print(1,encode(f'title : {i[0]}\n'))
        for k in findall(r'<p>(.*?)</p>',i[1]):
            k=sub(r'\s{2,}',' ',sub(r'<(.*?)>','',k)).strip()
            print(1,encode(f"{k}\n"))
    os._exit(os.EX_OK)
main()
