konsonanter = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,z"

ny_mening = " "

mening = input ("Skriv en mening: ")

for tecken in mening:
    if tecken in konsonanter:
        ny_mening += tecken + "o" + tecken
     
    else:
     ny_mening += tecken
print (ny_mening)   