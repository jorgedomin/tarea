a= [19,16,13]
x=[12,10,18]
z=[22,20,28]
def bubble_sort(list1):
    for i in range(0,len(a)-1):
        for j in range(len(a)-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1], a[j]
    return list1
def bubble_sort(x):
    for i in range(0,len(x)-1):
        for j in range(len(x)-1):
            if(x[j]>x[j+1]):
                x[j],x[j+1] = x[j+1], x[j]
    return x
def bubble_sort(z):
    for i in range(0,len(z)-1):
        for j in range(len(z)-1):
            if(z[j]>z[j+1]):
                z[j],z[j+1] = z[j+1], z[j]
    return z
print("original list: ", a, x,z)
print("list after sorting: ", bubble_sort(a),bubble_sort(x), bubble_sort(z))
