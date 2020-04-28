def isPrime(num):
    if num == 0 or num == 1:
        return False

    noPrimeFlag = False
    for i in range(2, int(num**(1/2))+1):
        if(num % i == 0):
            noPrimeFlag = True
            break
    
    return not noPrimeFlag 