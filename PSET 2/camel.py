def main():
    camelCase=input("camelCase: ")
    snake(camelCase)

def snake(txt):
    for n in range(len(txt)):
        if txt[n].isupper():
            txt=txt.replace(txt[n],"_"+txt[n].lower())
    print(txt)

main()