#Derrell Dunn
#Math 5364
#HOMEWORK #8

def gcd(a, b):
    if b==0:
      return a
    return gcd(b, a%b)


def gcd_iterations(a, b):
    global divcnt
    if b==0:
      return divcnt
    divcnt +=1
    return gcd_iterations(b, a % b)


def gcd_avgnum(a, b, summer):
    for x in range(1, a+1):
        for y in range(1, b+1):
            # print gcd_iterations(a,b)
            summer.append(gcd_iterations(x, y))

    return summer


def gcd_prime_finder(a, b, summer):
    global number_primes
    for x in range(1, a+1):
        for y in range(1, b+1):
            # print gcd_iterations(a,b)
            summer.append(gcd(x, y))

    return summer.count(1)

def compute_avg_num_div(source_array):
   return  sum(source_array)/source_array.__len__()

def clear_array(source_array):
    del source_array[:]
    return source_array

#initialize some global items
divcnt = 0 # keep division count here
number_primes = 0 # keep track of number of relative primes
summer = [] #empty array for passing integegers around

print 'The GCD between 20 and 2 is {}.' .format(gcd(20, 2))

print 'The number of iterations needed to find the GCD of 1908 and 684 is {}.' .format( gcd_iterations(1908, 684))

print ""
gcd_avgnum(100, 100, summer)
print 'The average number of divisions for [1,100] * [1,100] is {}.' .format(compute_avg_num_div(summer))
clear_array(summer)

print ""
gcd_avgnum(200, 200, summer)
print 'The average number of divisions for [1,200] * [1,200] is {}.' .format(compute_avg_num_div(summer))
clear_array(summer)

print ""
gcd_avgnum(400, 400, summer)
print 'The average number of divisions for [1,400] * [1,400] is {}.' .format(compute_avg_num_div(summer))
clear_array(summer)

print""
gcd_avgnum(800, 800, summer)
print 'The average number of divisions for [1,800] * [1,800] is {}.' .format(compute_avg_num_div(summer))
clear_array(summer)

print ""
gcd_avgnum(1600, 1600, summer)
print 'The average number of divisions for [1,1600] * [1,1600] is {}.' .format(compute_avg_num_div(summer))
clear_array(summer)

print 'The number of relative primes are {}.' .format( gcd_prime_finder(100, 100, summer))
print 'The percentage of relative primes are {}%.' .format((gcd_prime_finder(100, 100, summer)/float(summer.__len__()))*100.0)
