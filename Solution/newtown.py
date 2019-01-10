def newtown_sqrt(x):
    obj = x
    while abs(x - obj*obj) > 1e-3:
        obj = (obj+x/obj)/2
    return obj

print(newtown_sqrt(9))