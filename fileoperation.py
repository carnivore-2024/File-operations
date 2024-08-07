names = ""
output = ""

with open(names, 'r') as file:
    text = file.read()
    wordCount = len(text.split())
    print(text)
    print("Word count: ", wordCount)