vet = [1,2,3,4,5]

def foo():
    global vet
    vet = 'abacaxi'


foo()

print(vet)