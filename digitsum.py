adad = 0
counter = 0
number = int(input())

def majmoo(n):
    while n > 0:
        adad2 = 0
        while n > 0:
            adad2 += n % 10
            n //= 10
        print(adad2)

        


while counter < 222 ** 222:
    majmoo(number)
    counter += 1
    number = int(input())
