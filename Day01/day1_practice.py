print("Harish Kumar Dubey")
print("10 Years of Experience")
print("Mahindra & Mahindra Finance")
print("₹60–80+ LPA AI Architect/Applied AI Engineer")

def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

print(simple_interest(30000,8,2))

num = int(input("Enter a number: "))

if num <= 1:
    print("The number is not prime.")
else: 
    is_prime = True
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

