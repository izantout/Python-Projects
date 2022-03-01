def binary_add(a, u):
    a = a.replace(" ","")
    u = u.replace(" ","")
    counter = 0
    result2 = ''
    c = 0
    result = ''
    k = max(len(a), len(u))
    carry = c
    a_i = 0
    u_i = 0
    s_k = 0
    s_i = 0
    
    if len(a) > len(u):
        u = '0' * (len(a)-len(u)) + u
    if len(u) > len(a):
        a = '0' * (len(u)-len(a)) + a
        
    for i in range (k-1,-1,-1):
        
        if a[i] == '1':
            a_i = 1
        elif a[i] == '0':
                a_i = 0
            
        if u[i] == '1':
            u_i = 1
        elif u[i] == '0':
            u_i = 0
            
        s_i = (a_i + u_i + c) % 2  
        c = (a_i + u_i + c) // 2
        result = str(s_i) + result
        
    s_k = c
    result = str(s_k) + result
    print(result)
    result = result[::-1]
    
    result = ' '.join(result[i:i+4] for i in range(0,len(result),4))
    
    result = result[::-1]
    
    while result[0] == "0" or result[0] == ' ':
        result = result[1:]
    return result
