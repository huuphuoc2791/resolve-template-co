
def solve(queries, n):
    a = [i+1 for i in range(n)]
    r = []
    for q in queries:
        idx = a.index(q)
        r.append(idx)
        a.insert(0,a.pop(idx))
    return r
  
