import hashlib
def md5_hash(text:str):
    md5=hashlib.md5()
    md5.update(text.encode('utf-8'))
    return md5.hexdigest()

for i in range(int(input())):
    if md5_hash(input())==md5_hash(input()):
        print('Yes')
    else:
        print('No')