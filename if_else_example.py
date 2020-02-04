def main() :
    password=input("please enter you password")
    if password=="student":
        student()
    elif password=="teacher":
        teacher()
    else:
        print("incorrect password")

def student():
    print("hello S")

def teacher():
    print("hello T")

main()
