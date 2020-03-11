def fatu(x):
   for b in range(x):
        yield b**2


for c in fatu(5):
    print(c)

