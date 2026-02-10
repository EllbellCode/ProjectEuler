# Among the first 343 thousand square numbers, what is the sum of all the odd squares?

# First, odd square numbers are only ever have odd square roots.

# So we iterate over the odd numbers and keep a track of how many odd numbers we have gone through

sum = 0


for i in range(343000):

    if i % 2 == 1:

        sum += i**2

print(sum)

