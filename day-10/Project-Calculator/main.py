def calculator():
    import calc
    from calc import logo
    print(calc.logo)
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    operations={
        '+': add,
        '-':subtract,
        '*':multiply,
        '/':divide,}
    def calc_code():
        n1=float(input("What's the first number?: "))
        should_continue=True
        while should_continue:
            for symbol in operations:
                print(symbol)
            operator=input("Pick an operation?: ")
            n2=float(input("What is the next number?: "))
            answer=operations[operator](n1,n2)
            print(f"{n1} {operator} {n2} = {answer}")
            next=input(f"Type 'y' to continue calucating with {answer}, or type 'n' to start new calculations ")
            if next=='y':
                n1=answer
            elif next=='n':
                should_continue=False
                calc_code()
            else:
                should_continue=False
                calc_code()
    calc_code()
calculator()

