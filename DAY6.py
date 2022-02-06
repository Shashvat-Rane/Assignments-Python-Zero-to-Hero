
def div(a, b):
    print(a/b)

def mod_div(fun):
    def deno(a, b):
        if a < b:
            a, b = b, a
        return fun(a, b)

    return deno

# a, b = (int(i) for i in input('Enter two values: ').split())

a =int(input("Enter first nunber: "))

b =int(input("Enter second nunber: "))

div = mod_div(div)

div(a, b)

