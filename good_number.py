def primes_sqrt_range(n):
    primes = []
    # opps = 0
    for i in range(2, int(n**0.5)+1):
        p = False
        for j in range(2, int(i**0.5)+1):
            # opps += 1
            if i%j == 0:
                p = True
                break
        if p == False:
            primes.append(i)
    # print('Opperations= ', opps)
    return primes

if __name__ == "__main__":
    n = 100_000
    primes = primes_sqrt_range(n)
    q = int(input())
    while(q):
        q -= 1
        a, b = map(int, input().split())
        perf_count = 0

        for i in range(a, b+1):
            dig_count = len(str(i))
            p_count = 0

            if i == 1: # special case
                perf_count += 1
            
            for p in primes: 
                if i%p == 0:
                    p_count += 1
                if p > i: # exit check, further optimization, the factors should be smaller than the number itself
                    # print(p, i)
                    break
            
            if p_count == dig_count:
                perf_count += 1
            
        print(perf_count)
