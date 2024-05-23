question=input("What is the Answer to the Great Question of Life, the Universe, and Everything ")
question=question.strip().lower()
question=question.replace(" ","-")

if question.find("forty-two")>=0 or question.find("42")>=0:
    print("Yes")
else:
    print("No")