domain = [1,2,3,4,5]

#map is a high order function, this means a function that takes a function as an argument
our_range = map(lambda num: num*2, domain)
print(list(our_range))