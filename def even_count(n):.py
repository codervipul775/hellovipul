def even_count(n):
    
    if n<2:
        return 0
        
    else:
        return n//2
n=int(input())
result=even_count(n)
print(result)