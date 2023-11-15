def get_ascii(character):
    """Obtiene el valor ASCII de un carácter."""
    return ord(character)

def get_binary(character):
    """Obtiene la representación binaria de un carácter."""
    return bin(get_ascii(character))[2:].zfill(8)

def get_results(word):
    """Obtiene los resultados para cada carácter en una palabra."""
    results = []
    for char in word:
        ascii_value = get_ascii(char)
        binary_representation = get_binary(char)
        result = f"ASCII character value of '{char}' is {ascii_value}. Binary representation is {binary_representation}"
        results.append(result)
    return results
