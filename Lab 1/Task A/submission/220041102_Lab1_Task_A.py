l,w,a,b= map(int,input().split())
ans=(l*w-0.5*a*b-.5*3.14159*(a*a+b*b)/4)
print(f"{ans:.2f}")