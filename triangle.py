def equilateral(sides):
    a, b, c = sides
    
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    if not (a + b >= c and b + c >= a and a + c >= b):
        return False
    
    return a == b == c

def isosceles(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if not (a + b >= c and b + c >= a and a + c >= b):
        return False
    
    if a == b or a == c or c == b:
        return True
    else:
        return False

def scalene(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    if not (a + b >= c and b + c >= a and a + c >= b):
        return False
    
    if a != b and b != c and a!= c:
        return True
    else:
        return False

print(scalene([3, 4, 3]))