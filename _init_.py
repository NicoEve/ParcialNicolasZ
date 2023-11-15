from Binarios import get_ascii, get_binary, get_results

menu = int(input('Menu\n=====\n1. Character\n2. Word\n'))

if menu == 1:
    char = input('Enter a character: ')
    word = char
elif menu == 2:
    word = input('Enter a word: ')
else:
    print('Invalid choice. Exiting.')
    exit()

print('Results\n========')

results = get_results(word)
for result in results:
    print(result)