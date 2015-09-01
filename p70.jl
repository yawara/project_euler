function phi(n)
    rtv = n
    primes = keys(factor(n))
    for p in primes;
        rtv *= ( 1 - 1/p )  
    end
    return int(rtv)
end

function digits(n)
    rtv = { i => 0 for i in 0:9 }
    for d in string(n)
        rtv[parseint(d)] += 1
    end
    return rtv
end

function answer(N)
    min_n, min_r = 0, N+1

    for n in 2:(N+1)
        phi_n = phi(n)
        if digits(phi(n)) == digits(n)
            r = n / phi_n
            if r < min_r
                min_n, min_r = n, r
            end
        end
    end
    
    return min_n, min_r
end
