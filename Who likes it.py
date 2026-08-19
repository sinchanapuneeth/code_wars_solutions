def likes(names):
    #defined once, so that it doesn't compute it every time
    n = len(names)
    if n == 0:
        return ("no one likes this")
    elif n == 1:
        return("{} likes this".format(names[0]))
    elif n == 2:
        return("{} and {} like this".format(names[0], names[1]))
    elif n == 3:
        return(("{}, {} and {} like this".format(names[0], names[1], names[2])))
    #changed to else to remove checking if n is greater or equal since it can be done using previous statement's inductions
    else:
        #shifted here so it is only calculated if needed
        x = len(names) - 2
        return("{}, {} and {} others like this".format(names[0], names[1],x)) 

#while the original and this code's time complexity and space complexity is still O(1), this is more readable and is a teeny tiny bit more optimized
#python naturally saves length of lists so time complexity for calculating n  is O(1) and it only has to look up the first two indexes so still O(n)
#as for space, it only creates these fixed number of results so it is a constant hence O(1)
# :)
