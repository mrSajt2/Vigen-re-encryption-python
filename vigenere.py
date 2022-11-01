abc = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"

def encode(data, key):
    data, key = data.upper(), key.upper()
    encoded_data = ""
    while True:
        if len(data) > len(key):
            key = key + key
        else:
            break
    for i in range(len(data)):
        offset = abc.index(key[i])
        while True:
            if (abc.index(data[i]) + offset) > len(abc):
                offset -= len(abc)
            else:
                encoded_data += abc[abc.index(data[i]) + offset]
                break
    return encoded_data

def decode(data, key):
    data, key = data.upper(), key.upper()
    decoded_data = ""
    while True:
        if len(data) > len(key):
            key = key + key
        else:
            break
    for i in range(len(data)):
        offset = abc.index(key[i])
        while True:
            if offset - abc.index(data[i]) < 0:
                offset += len(abc)
            else:
                decoded_data += abc[abc.index(data[i]) - offset]
                print(decoded_data)
                break
    return decoded_data