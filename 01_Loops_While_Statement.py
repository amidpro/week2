line = None

while line != 'done':
    line = input('Type "done" to complete ')
    line = line.lower()
    print('>', line, '<')

# Output - 'Type "done" to complete ': (type done) - prints out > done < (can type in anything, prints out > "str" <