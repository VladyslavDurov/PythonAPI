
#variant_1
mygenerator = (x**2 for x in range(3,5))

#variant_2
def createGenerator():
    for item in range(2,5):
        yield item**3

for item in mygenerator:
    print(item)

print(20*'+')

for x in createGenerator():
    print(x)

print(20*'+')

generator = createGenerator()
print(next(generator))
print(next(generator))
print(next(generator))
