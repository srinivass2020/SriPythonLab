customersNamelist=["Sri","Mad","Sat","Gau"]

sriTouple=("Sri",35,"Pittsburgh")
madTouple=("Mad",30,"Pittsburgh")
satTouple=("Sat",40,"Pittsburgh")
gauTouple=("Gau",45,"Pittsburgh")

custfdbkdict = {"Sri":"Sri is Good Employee","Mad":"Madhuri is Nice"}

custfdbkdict1= dict(Sat="Satha is Bad Employee",Gau="Gaurang is Excellent")

customersDetailList=[sriTouple,madTouple,satTouple,gauTouple]

custfdbkdict.update(custfdbkdict1);

name,age,city = sriTouple

sriToupleList = [name,age,city]

print(f"All Customer Details : {customersDetailList}");
print("All Customer Details : ", customersDetailList);

print("Sri Touple List : ",sriToupleList)

print("Sri customer feedback : ",custfdbkdict["Sri"])
print("Sat customer feedback : ",custfdbkdict["Sat"])


sriToupleList.append(custfdbkdict["Sri"])

print("Sri extended touple list",sriToupleList)



