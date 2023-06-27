#def hello(*inp,**inputs):
    print(inp)
    print(inputs)


#hello(a=4,b=5,c=7)

def myrange(limit):
    i-0
    while i < limit:
        yield i 
        i=i+1
for i in myrange(100):
    print(i)

def inmyrange(limit):
    i=0
    result=[]

    while i< limit:
        result.append(i)
    return result 

for i in inmyrange(100):



x=[1,2,3,4,5,]
y=[2,3,4,5]
f=set(x)
g=set(y)
inter = f.intersection(g)
print(inter)

myfun = lambda x: x*x
print(myfun(3))

def ofilter_fun(x):
    if x % 2 == 1:
        return x
    return False 
sq_numbers=[x*x for x in range(100)]
old_y=[]
for i in data:
    old_y.append (myfun(i))
print(y)
print(list(y))
f_results = filter(ofilter_fun,data)
print(list(f_results))



