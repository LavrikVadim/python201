import matplotlib.pyplot as plt

def generate(n:int):
    a= [i for i in range(n)]
    b = [i ** 2 for i in range(n)]

    return a,b

a,b=generate(15)

print(a)
print(b)

plt.plot(a,b)
plt.show()
