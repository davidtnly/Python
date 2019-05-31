# def announce_location(country):
# #     return country
# #
# #
# # instructor_location = announce_location('canada')
# #
# # print(instructor_location)
# #
# # instructor_location  # does nothing

x = None
print(x)

digits = '0123456789'
result = 100

for digit in digits:
    result = result - int(digit)

print(result)


digits = '0123456789'
result = 0

for digit in digits:
    result = digit

print(result)

digits = '0123456789'
result = ''

for digit in digits:
    result = result + digit * 2

print(result)

digits = '0123456789'
result = ''

for digit in digits:
    result = result + digit * 2

print(result)


def secret(s):
    i = 0
    result = ''

    while s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result

def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result

letters = ['b', 'd', 'a']
letters.sort()
print(letters)

treats = [['apple', 'pie'], ['vanilla', 'ice-cream'], ['chocolate', 'cake']]
print(treats[-3][-1])

c = 0
for i in range(2, 5):
    for j in range(4, 9):
        print(i, j)
        c += 1
        print(c)

d = {'a': 1, 'c': 3, 'b': 2}
not('e'in d)


tup = (1,2,3)

def f(x):
    y = x * 3
    return y - x

start = 'L'
middle = 8
end = 'R'