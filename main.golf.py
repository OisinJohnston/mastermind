import random as r;C=["r","l","b","n","p"];x=r.choices(C,k=4);a=1;u=[]
while u!=x: z=len([v for i,v in enumerate(u) if x[i]==v]);u=input(f'{a}{z}{len([i for i in u if i in x])-z}{C}').split();a+=1
