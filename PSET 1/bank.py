def main():
    greeting=input("Greeting: ")
    hello(greeting)

def hello(greeting):
    greeting=greeting.lower().strip()

    if greeting=="hello":
        print("$0")

    elif greeting[0:1]=="h" and greeting!="hello":
        print("$20")

    elif greeting[0:1]!="h":
        print("$100")

main()