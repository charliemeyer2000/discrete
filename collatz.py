def collatz(n):
    
    print(n)
    if n == 1:
        return n
    if n % 2 == 0:
        
        return collatz(n // 2)
    else:
        
        return collatz(3 * n + 1)
def prime_factorization(n):
    for i in range(2, n):
        if n % i == 0:
            print(i)
            return prime_factorization(n // i)
    print(n)
    return n


    

    
if __name__ == "__main__":
        print(pi_sort([6, 5, 9]))
    