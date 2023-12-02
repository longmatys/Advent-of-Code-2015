import hashlib

if __name__ == '__main__':
    start_code = 'bgvyzdsv'
    counter = 0
    while True:
        # Convert the input string to bytes, as hashlib works with bytes
        input_bytes = f"{start_code}{counter}".encode('utf-8')

        # Calculate the MD5 hash
        md5_hash = hashlib.md5(input_bytes).hexdigest()
        if md5_hash[:6] == '0'*6:
            print(f"Nasel jsem {counter}: {md5_hash}")
            break
        counter+=1
        #print(md5_hash)