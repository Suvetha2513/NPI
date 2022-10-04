import random
num = ""
num1 ="12"
length1 = 1
res1 = "".join(random.sample(num1,length1))
if res1 == "1":
    num = "23456789"
elif res1 =="2":
    num = "13456789"


stand = "80840"
length = 8
tempres = "".join(random.sample(num,length))
res = res1 + tempres
fres = stand + res
print("-------------------------------------------------------------------------------")
print("\nThe random number generated is : ",res)
print("\n-------------------------------------------------------------------------------")



def digits_ci(n):
    return [int(d) for d in str(n)]
    
checksum = 0
digit = digits_ci(fres)
even_digits = digit[-1::-2]
odd_digits = digit[-2::-2]
checksum += sum(odd_digits)

for i in even_digits:
    checksum += sum(digits_ci(i*2))

higher_zero = checksum%10
higher_end = 10-higher_zero
nhigher_end = str(higher_end)
card_issuer = fres + nhigher_end



def digits_npi(n):
    return [int(e) for e in str(n)]
    
digits = digits_npi(res)
even_digits1 = digits[-1::-2]
odd_digits1 = digits[-2::-2]
checksum1 = 24
checksum1 += sum(odd_digits1)

for j in even_digits1:
    checksum1 += sum(digits_npi(j*2))

higher_zero1 = checksum1%10
higher_end1 = 10-higher_zero1
nhigher_end1 = str(higher_end1)
NPI_checkdigit = res + nhigher_end1

print("\n Card issuer identifier with check digit : ",card_issuer)
print("\n -------------------------------------------------------------------------------")
print("\n NPI with check digit : ",NPI_checkdigit)
print("\n -------------------------------------------------------------------------------")