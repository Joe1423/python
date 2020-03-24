def count_words(filename):
    """Count the number of words in a file."""

    try:
        with open(filename) as texto:
            content = texto.read()
    except FileNotFoundError:
        #If you want python to ignore this error silently you can use the keyword 'pass' and python will do nothing in this block
        print("El archivo " + filename + " no existe.")
    else:
        words = content.split()
        num_words = len(words)
        print("The file " + filename + " contains " + str(num_words) + " words.")

files = ['/home/jnmdz/git/git-tutorial.txt', 'nothing.txt']

for file in files:
    count_words(file)

