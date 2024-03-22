def dis(t):
      ls=list(str(t))
      for i in range(4):
            for j in range(i+1):
                  if ls[i]==ls[j]:
                        return False
      return True



def p(n):
      ans=False 
      while(ans==False):
            n=n+1
            ans=dis(n)
      return n 

# Comment
s=int(input())
print(p(s))
