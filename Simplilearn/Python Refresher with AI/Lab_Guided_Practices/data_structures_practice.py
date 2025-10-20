customersNamelist=["Sri","Mad","Sat","Gau","Ted"]
sriTouple=("Sri",35,"Pittsburgh")
madTouple=("Mad",30,"Pittsburgh")
satTouple=("Sat",40,"Pittsburgh")
gauTouple=("Gau",45,"Pittsburgh")
tedTouple=("Ted",50,"Pittsburgh")
customersDetailList=[sriTouple,madTouple,satTouple,gauTouple,tedTouple]


allCustfdbkdict = {"Sri":"The service was excellent and very professional","Mad":"I had a bad experience with customer support"}
custfdbkdict1= dict(Sat="Good quality but delivery was slow",Gau="The product was poor and not worth the price",Ted="Poor Good")
allCustfdbkdict.update(custfdbkdict1);

name,age,city = sriTouple
sriToupleList = [name,age,city]
sriToupleListWithFeedback = [name,age,city,allCustfdbkdict["Sri"]]
#sriToupleList = [sriTouple]

name,age,city = madTouple
madToupleList = [name,age,city]
madToupleListWithFeedback = [name,age,city,allCustfdbkdict["Mad"]]

name,age,city = satTouple
satToupleList = [name,age,city]
satToupleListWithFeedback = [name,age,city,allCustfdbkdict["Sat"]]

name,age,city = gauTouple
gauToupleList = [name,age,city]
gauToupleListWithFeedback = [name,age,city,allCustfdbkdict["Gau"]]

name,age,city = gauTouple
tedToupleList = [name,age,city]
tedToupleListWithFeedback = [name,age,city,allCustfdbkdict["Ted"]]

custDetailFeedbackDict = {sriTouple[0]:sriToupleListWithFeedback,
                          madTouple[0]:madToupleListWithFeedback,
                          satTouple[0]:satToupleListWithFeedback,
                          gauTouple[0]:gauToupleListWithFeedback,
                          tedTouple[0]:tedToupleListWithFeedback
                         }

print(f"Customer name list : {customersNamelist}");
print("All Customer Details : ", customersDetailList);

print("All Customer feedback : ",allCustfdbkdict)

#print("Sri customer feedback : ",allCustfdbkdict["Sri"])
#print("Sat customer feedback : ",allCustfdbkdict["Sat"])

#sriToupleList.append(allCustfdbkdict["Sri"])

#print("Sri extended touple list",sriToupleList)

#Analyzing Feedback
positive_feedback={"good","nice","excellent","awesome","outstanding","perfect","superb","brilliant","fabulous","marvelous","incredible","exceptional","wonderful","great"}
negative_feedback={"bad","poor","terrible","awful","dreadful","horrible","lousy","mediocre","subpar","unsatisfactory","unacceptable","deficient","inferior"}

feedback_classification_dict={}
for cust,feedback in allCustfdbkdict.items():
    words=set(feedback.lower().split())
    if words & positive_feedback:
        feedback_classification_dict[cust]="Positive"
    elif words & negative_feedback:
        feedback_classification_dict[cust]="Negative"
    else:
        feedback_classification_dict[cust]="Neutral"

print("*** Feedback Classification ***")
for cust,classification in feedback_classification_dict.items():
    print(f"Customer {cust} has given a {classification} feedback")

positive_feedback_customers=[]
negative_feedback_customers=[]

#Generating Summary Report
for cust,classification in feedback_classification_dict.items():
    if classification=="Positive":
        positive_feedback_customers.append(cust)
    elif classification=="Negative":
        negative_feedback_customers.append(cust)

print(f"Positive feedback customers : {positive_feedback_customers}")
print(f"Negative feedback customers : {negative_feedback_customers}")

# List comprehension/Lambda to find customers who gave positive feedback
positive_customers = [customer for customer, category in feedback_classification_dict.items() if category == "Positive"]
print("Postive Customers :", positive_customers)

#Organizing customer details with feedback
for cust in customersNamelist:
    print(f"Customer {cust} feedback is : {feedback_classification_dict[cust]}")

positive_set=set(positive_feedback_customers)
negative_set=set(negative_feedback_customers)
both_feedback_set=positive_set & negative_set


print("All Customer Feedback : ",positive_set|negative_set)
print("Both Positive and Negative Customer Feedback : ",both_feedback_set)
print("Only Negative Customer Feedback : ",both_feedback_set^negative_set)
print("Only Negative Customer Feedback : ",negative_set-both_feedback_set)

