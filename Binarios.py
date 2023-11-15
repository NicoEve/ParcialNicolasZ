def get_ascii(character):
    return ord(character)

def get_binary(character):
    return bin(get_ascii(character))[2:].zfill(8)

def get_results(word):
    results = []
    for char in word:
        ascii_value = get_ascii(char)
        binary_representation = get_binary(char)
        result = f"ASCII character value of '{char}' is {ascii_value}. Binary representation is {binary_representation}"
        results.append(result)
    return results
