hab={"name":"dhoni","age":33,"team":"CSK","born_year":1989}
l=dict(sorted(hab.items()))
print(l)
print(hab.items())

print(dict(l))

a=[1,2,3,9,5,6,"uyad","ujdajd"]
print(sorted(a))
import json
a='{"abc":1,"cde":2}'
d=json.loads(a)
e=json.dumps(d)
print(type(d))
print(type(e))

#
def solution(sequence):
    z=[]
    #p=sequence[:]
    i=0
    j=1
    while j!=len(sequence):
        if sequence[i]>sequence[j]:
            z.extend([i,j])
        i=i+1
        j=j+1
    # return z
    q=0
    # print(len(sequence))
    for i in z:
        p=sequence[:]
        p.pop(i)
        if p==sorted(p) and len(p)==len(set(p)):
            q=1
            #return True
            break
    if q==1 or len(sequence)==2:
        return True
    else:
        return False

def solution(matrix):
    c = 0
    p = len(matrix)
    d = len(matrix[0])
    # print(p,d)
    for i in range(0, p):
        for j in range(0, d):
            # if matrix[i][d-1]==0:
            #     for i in range(0,p):
            #         matrix[i][d-1]=0
            # #print(matrix[i][j])
            if i == 0:
                if matrix[0][j] != 0:
                    c = c + matrix[0][j]
            else:
                if matrix[i][j] != 0 and matrix[i - 1][j] != 0 and matrix[0][j] != 0:
                    c = c + matrix[i][j]
    return c


