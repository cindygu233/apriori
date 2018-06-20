f=open("category.txt","r")
file=f.read()
c_list=file.split("\n")
c_list=c_list[0:len(c_list)-1]


db=[]
for c in c_list:
    db.append(c.split(";"))



##GET THE LENGTH-1 FREQUENT ITEMSET
c=[]
f_0={}
pattern={}
for d in db:
    for dd in d:
        if dd in f_0:
            f_0[dd]=f_0[dd]+1
        else:
            f_0[dd]=1

for ff in f_0:
    if f_0[ff]>=0.01*len(c_list):
        c.append([ff])

        

for i in range(len(c)):
    pattern[';'.join(c[i])]=f_0[';'.join(c[i])]
    
    
## USE APRIORI TO GET ALL THE FREQUENT ITEMSET
while(len(c_k)>0):
    c_new=[]
    for ii in range(len(c_k)):
        for jj in range(ii+1,len(c_k)):
            i=c_k[ii]
            i.sort()
            j=c_k[jj]
            j.sort()
            if i != j:
                com=list(set(i+j))
                freq={}
                n=0
                for d in db:
                    if set(com)<=set(d):
                        n=n+1
                if n>0.01*len(c_list):
                    c_new.append(com)
                    print(c_new)
                    freq[';'.join(com)]=n
                    pattern.update(freq)
                    #if n in pattern:
                     #   for iii in com:
                      #      if iii in pattern[n]:
                       #         pattern[n]=pattern[n]
                        #    else:
                         #       pattern[n]=pattern[n]+";"+iii
                    #else:
                     #   pattern.update({n:";".join(com)})
    c_k=c_new             
    
    
foo=open("patterns.txt","w")

for category,support in pattern.items():
    foo.write(str(support)+":"+str(category)+"\n")


foo.close()   
