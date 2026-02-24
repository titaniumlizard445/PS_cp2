#PS 1st recursion notes

for x in range(1,11):
    if x % 2 == 0:
        print(x)


#example of factorial
a_number = 10
sum = 1
for x in range(1,a_number+1):
    sum *= x 
print(f"Loop thing: {sum}")

#uses the next iteration of the function in the current function
def factorial(something):
    if something == 1: return 1
    return something*factorial(something-1)

print(f"Recused: {factorial(a_number)}")

#loop
fibonnaci_numbers = [1,1]
for x in range(1,11):
    fibonnaci_numbers.append(fibonnaci_numbers[x-1] + fibonnaci_numbers[x])

print(f"Loop thing{fibonnaci_numbers}")

#recursion

fibbos = []
def rec_fibonnaci(number):
    fibbos.append(number)
    if number == 2: 
        return 1
    elif number == 1:
        return 0
    else:
        return rec_fibonnaci(number-1) + rec_fibonnaci(number-2)


print(f"Recursed: {rec_fibonnaci(21)}")

