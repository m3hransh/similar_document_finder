def odd_half_state(n):
    if n % 2 == 0:
        n += 1
    magic_square = [[0 for j in range(n)] for i in range(n)]
    v = 1
    i = n // 2
    j = 0
    while v <= (n * n):
        magic_square[i][j] = v
        k = i + 1
        if k >= n: k = 0
        l = j - 1
        if l < 0: l = n - 1
        if magic_square[k][l] != 0:
            k = i
            l = j + 1
        i = k
        j = l
        v = v + 1
       
 
    return magic_square, n

def singly_even_state(n):
    if n % 2 == 1:
        n += 1
    while n % 4 == 0:
        n += 2
 
    magic_square = [[0 for j in range(n)] for i in range(n)]
    z = n // 2
    b = z * z
    c = 2 * b
    d = 3 * b
    o = odd_half_state(z)
 
    for j in range(0, z):
        for i in range(0, z):
            a = o[0][i][j]
            magic_square[i][j] = a
            magic_square[i + z][j + z] = a + b
            magic_square[i + z][j] = a + c
            magic_square[i][j + z] = a + d
 
    lc = z // 2
    rc = lc
    for j in range(0, z):
        for i in range(0, n):
            if i < lc or i > n - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = magic_square[i][j]
                    magic_square[i][j] = magic_square[i][j + z]
                    magic_square[i][j + z] = t
    for a in range(0, n): 
            for b in range(0, n): 
                print('%2d ' % (magic_square[a][b]),end = " ") 
                
                
                if b == n - 1:  
                    print()    
    return magic_square, n



 

def Even_state(n): 
   
	    magic_cube = [[(n*y)+x+1 for x in range(n)]for y in range(n)] 

	
	    for i in range(0,n//4): 
        for j in range(0,n//4): 
            magic_cube[i][j] = (n*n + 1) - magic_cube[i][j];            
		     
	
	    for i in range(0,n//4): 
	    for j in range(3 * (n//4),n): 
	        magic_cube[i][j] = (n*n + 1) - magic_cube[i][j]; 

	    for i in range(3 * (n//4),n): 
	    for j in range(0,n//4): 
	        magic_cube[i][j] = (n*n + 1) - magic_cube[i][j]; 
	
	    for i in range(3 * (n//4),n): 
	    for j in range(3 * (n//4),n): 
	        magic_cube[i][j] = (n*n + 1) - magic_cube[i][j]; 
			
	    for i in range(n//4,3 * (n//4)): 
	    for j in range(n//4,3 * (n//4)): 
	        magic_cube[i][j] = (n*n + 1) - magic_cube[i][j]
	
    
    for a in range(0, n):
        for b in range(0, n): 
            print('%2d ' % (magic_cube[a][b]),end = " ") 
            if b == n - 1:  
                print() 
    
        




def magic_cube_generator(n):
    if n % 2 ==1:
        magic_cube = [[0 for x in range(n)] for y in range(n)]
        postion_of_number_i = int(n/2)
        position_of_number_j =int(n-1) 

        number_selected = 1
        while number_selected <= n**2:
            if postion_of_number_i == -1 and position_of_number_j == n :
                postion_of_number_i = 0
                position_of_number_j = n-2
            else:
                if position_of_number_j == n:
                    position_of_number_j = 0
                if postion_of_number_i < 0:
                    postion_of_number_i = n-1
            
            if magic_cube[postion_of_number_i][position_of_number_j]:
                position_of_number_j = position_of_number_j - 2
                postion_of_number_i = postion_of_number_i + 1
                continue
            else:
                magic_cube[postion_of_number_i][position_of_number_j] = number_selected
                number_selected = number_selected + 1

            position_of_number_j = position_of_number_j + 1
            postion_of_number_i = postion_of_number_i - 1
        

        print ("sum of row & column",  
                n * (n * n + 1) / 2, "\n") 
        
        for a in range(0, n): 
            for b in range(0, n): 
                print('%2d ' % (magic_cube[a][b]),end = " ") 
                
                
                if b == n - 1:  
                    print()
    elif n%4 == 0:
        Even_state(n)
    elif n%4 == 2:
        singly_even_state(n)            
       

     




 
        

        
	
		
			 

n = 4   
magic_cube_generator(n)


