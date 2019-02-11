from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x1 < x0):
	x = x1
	y = y1
	x1= x0
	y1 = y0
	a = y1 - y
	b = -1 * (x1 - x)
    else:
        x = x0
	y = y0
	a = y1 - y
	b = -1 * (x1 - x)

    

    # octant I
    if ( a >= 0 and -1*b >=a ):
        d = 2*a + b
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y+=1
                d+= 2*b
            x+=1
            d+= 2*a
    
    # octant II
    elif ( a > 0 and -1*b <a):
        d = 2*b + a
        while y <= y1:
            plot(screen, color, x, y)
            if d < 0:
                x+=1
                d+= 2*a
            y+=1
            d+= 2*b 
    
    # octant VIII
    elif ( a < 0 and b <=a ):
        d = 2*a - b
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0:
                y-=1
                d-= 2*b
            x+=1
            d+= 2*a
    
    # octant VII
    elif (a < 0 and b >a):
        d = a - 2*b
        while y >= y1:
            plot(screen, color, x, y)
            if d > 0:
                x+=1
                d+= 2*a
            y-=1
            d-= 2*b 
    
    
    
    
