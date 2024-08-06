l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]


l3 = []
for i in l:
    if type(i) == list or type(i) == tuple or type(i) == set:
        product = 1
        for j in i:
            if type(j) == int:
                product = product * j
        l3.append(product)
    elif type(i) == dict:
        product = 1
        v = list(i.values())
        k = list(i.keys())
        v.extend(k)

        for j in v:
            if type(j) == int:
                product = product * j

        l3.append(product)
print(l3)

