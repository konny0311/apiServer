import os

def appendInText(filePath, text):
    with open(filePath, 'w+') as f:
        for row in f:
            row = ""
        f.write(text)
    return text
