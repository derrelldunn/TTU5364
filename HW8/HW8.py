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


divcnt = 0
number_primes = 0
summer = []

print gcd(20, 2)

print gcd_iterations(1908, 684)

print ""
print "100---------------------------------------"
gcd_avgnum(100, 100, summer)
print compute_avg_num_div(summer)
clear_array(summer)
print ""
print "200----------------------------------------"
gcd_avgnum(200, 200, summer)
print compute_avg_num_div(summer)
clear_array(summer)
print ""
print "400-----------------------------------------"
gcd_avgnum(400, 400, summer)
print compute_avg_num_div(summer)
clear_array(summer)
print""
print "800 reps------------------------------------"
gcd_avgnum(800, 800, summer)
print compute_avg_num_div(summer)
clear_array(summer)
print ""
print "1600 reps-----------------------------------"
gcd_avgnum(1600, 1600, summer)
print compute_avg_num_div(summer)
clear_array(summer)

print gcd_prime_finder(100, 100, summer)

