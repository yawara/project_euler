function phi(n)
    rtv = 1
    for (p, k) in factor(n)
        rtv *= p^(k-1) * ( p - 1 )  
    end
    return rtv
end

function digits(n)
    rtv = { i => 0 for i in 0:9 }
    
    tmp = n
    while true
        rtv[tmp%10] += 1
        tmp = div(tmp, 10)
        if tmp == 0
            return rtv
        end
    end
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
