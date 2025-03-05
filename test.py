import hashlib

def hash_file(fileName1,fileName2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()
    
    with open(fileName1,"rb") as file:
        chunk = 0
        while chunk != b'':
            chuck = file.read(1024)
            h1.update(chunk)
    

    