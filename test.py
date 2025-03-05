import hashlib

def hash_file(fileName1,fileName2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()
    
    with open(fileName1,"rb") as file:
        chunk = 0
        while chunk != b'':
            chuck = file.read(1024)
            h1.update(chunk)
    

    with open(fileName2,"rb") as file:
        chunk = 0
        while chunk != b'':
            chuck = file.read(1024)
            h2.update(chunk)
    
    return h1.hexdigest(),h2.hexdigest()

msg1,msg2 = hash_file("matching1.pdf","matching2.pdf")

if msg1 == msg2:
    print("The tow files are identical")
else: 
    print("The two files are not identical")
