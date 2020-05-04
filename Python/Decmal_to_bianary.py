def dec2bin(x):
    list=[]
    while x>0:
        list.append(x%2)
        x=x/2
        x=int(x)
    return [y for y in reversed(list)]
def dorydumb(dec):
    
    z=dec2bin(dec)
    one=(0)
    zero=(0)
    for hi in z:
        if hi==0:
            zero=zero+1
        elif hi==1:
            one=one+1
    if one<zero:
        return "sad"
    elif one>zero:
        return "happy"
    else: 
        return "neutral"
print(dorydumb(123456789))
        
    
