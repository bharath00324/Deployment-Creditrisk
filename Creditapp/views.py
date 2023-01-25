from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np


# use get_key()  to get value of it
def get_key(k):
	for key, value in Cat_dict.items():
		if  k==key :
			return value
Cat_dict = {"Non-Existed Customer": 1, "Existed Customer": 2, "Income and expenses verified": 1, "Income unverified": 2, "Income verified": 3, "Income unverified, cross-referenced by phone": 4, "Not set": 5, "Estonian": 1, " Finnish": 2, "Spanish": 3, "Russian": 4, "English": 5, "Slovakian": 6, "others": 6, "German": 8, "Male": 1, "Women": 2, "Undefined": 3, "EE": 1, "FI": 2, "ES": 3, "SK": 4, "Not set category": 1, "Other": 6, "Home improvement": 3, "Loan consolidation": 4, "Vehicle": 5, "Business": 6, "Travel ": 7, "Health": 8, "Education": 11, "Real estate": 10, "Purchase of machinery equipment": 11, "Other business": 12, "Accounts receivable financing": 13, "Working capital financing": 14, "Acquisition of stocks": 15, "Acquisition of real estate": 16, "Construction finance": 17, "Secondary education": 1, "Higher education": 2, "Vocational education": 3, "Basic educattion": 4, "Primary education": 5, "Not present": 1, "Single": 2, "Married": 3, "Cohabitant": 4, "Divoreced": 5, "Widow": 6, "0thers": 1, "Fully employed": 2, "Entrepreneur": 3, "Retiree": 6, "Self employed": 5, "Partially employed": 6, "MoreThan5Years": 1, "UpTo1Year": 2, "UpTo5Years": 3, "UpTo2Years": 4, "UpTo3Years": 5, "UpTo4Years": 7, "TrialPeriod": 9, "Not_specified": 1, "Retail and wholesale ": 3, "Construction": 4, "Processing ": 5, "Transport and warehousing": 6, "Healthcare and social help": 7, "Hospitality and catering": 8, "Info and telecom ": 9, "Civil service & military": 10, "Finance and insurance": 12, "Agriculture, forestry and fishing": 13, "Administrative": 14, "Energy": 15, "Art and entertainment": 16, "Research": 17, "Real-estate": 18, "Utilities": 19, "Mining": 20, "Owner": 1, "Tenants, pre furnished property": 2, "Living with parents": 3, "Mortgage": 4, "Tenanats unfurnished property": 5, "Joint ownership": 7, "Joint tenant": 8, "Council house": 9, "Owner with encumbance": 10, "Homeless": 11, "Not specified": 12, "F": 1, "HR": 2, "E": 3, "D": 4, "C": 5, "B": 6, "A": 7, "AA": 8, "false": 1, "true": 2, "M": 1, "M1": 2, "M5": 3, "M2": 4, "M3": 5, "M4": 6, "M6": 7, "M8": 8, "M9": 9, "M7": 10, "M10": 11}






# Create your views here.
def home(request):
    return render(request,"home.html")


def result(request):
    
    
    if request.method == "POST":
     
        
        BidsportfolioManager =int(request.POST.get("BidsportfolioManager"))
        BidsApi =int(request.POST.get("BidsApi"))
        BidsManual =int(request.POST.get("BidsManual"))
        Age =int(request.POST.get("Age"))
        AppliedAmount =int(request.POST.get("AppliedAmount"))
        Interest =int(request.POST.get("Interest"))
        IncomeTotal =int(request.POST.get("IncomeTotal"))
        ExistingLiabilities =int(request.POST.get("ExistingLiabilities"))
        RefinanceLiabilities =int(request.POST.get("RefinanceLiabilities"))
        DebtToIncome =int(request.POST.get("DebtToIncome"))
        FreeCash =int(request.POST.get("FreeCash"))
        InterestAndPenaltyPaymentsMade =int(request.POST.get("InterestAndPenaltyPaymentsMade"))
        PreviousEarlyRepaymentsCountBeforeLoan =int(request.POST.get("PreviousEarlyRepaymentsCountBeforeLoan"))
        NewCreditCustomer = request.POST.get("NewCreditCustomer")
        NewCreditCustomer = get_key(NewCreditCustomer)
        VerificationType = request.POST.get("VerificationType")
        VerificationType =  get_key(VerificationType)
        LanguageCode = request.POST.get("LanguageCode")
        LanguageCode = get_key(LanguageCode)
        Country = request.POST.get("Country")
        Country = get_key(Country)
        UseOfLoan = request.POST.get("UseOfLoan")
        UseOfLoan = get_key(UseOfLoan)
        Education = request.POST.get("Education")
        Education = get_key(Education)
        MaritalStatus = request.POST.get("MaritalStatus")
        MaritalStatus = get_key(MaritalStatus)
        EmploymentStatus = request.POST.get("EmploymentStatus")
        EmploymentStatus = get_key(EmploymentStatus)
        EmploymentDurationCurrentEmployer = request.POST.get("EmploymentDurationCurrentEmployer")
        EmploymentDurationCurrentEmployer = get_key(EmploymentDurationCurrentEmployer)
        OccupationArea = request.POST.get("OccupationArea")
        OccupationArea = get_key(OccupationArea)
        Rating = request.POST.get("Rating")
        Rating = get_key(Rating)
        CreditScoreEsMicroL = request.POST.get("CreditScoreEsMicroL")
        CreditScoreEsMicroL = get_key(CreditScoreEsMicroL)
        MonthlyPayment = int(request.POST.get("MonthlyPayment"))
        Gender = request.POST.get("Gender")
        Gender = get_key(Gender)
        HomeOwnershipType = request.POST.get("HomeOwnershipType")
        HomeOwnershipType = get_key(HomeOwnershipType)
        Restructured = request.POST.get("Restructured")
        Restructured = get_key(Restructured)
        PrincipalPaymentsMade=int(request.POST.get("PrincipalPaymentsMade"))





        model=pickle.load(open("rfc.pkl","rb")) 
        prediction = model.predict([[BidsportfolioManager,BidsApi,BidsManual,Age,AppliedAmount,Interest,MonthlyPayment,IncomeTotal,ExistingLiabilities,
                                     RefinanceLiabilities,DebtToIncome,FreeCash,InterestAndPenaltyPaymentsMade,
                                     PreviousEarlyRepaymentsCountBeforeLoan,NewCreditCustomer,VerificationType,
                                     LanguageCode,Gender,Country,UseOfLoan,Education,MaritalStatus,EmploymentStatus,EmploymentDurationCurrentEmployer,OccupationArea,
                                     HomeOwnershipType,Rating,CreditScoreEsMicroL,Restructured,PrincipalPaymentsMade]]) 
        result = prediction
        if(result==0):
            return render(request,'home.html',{ 'prediction_text':f'Unfortunatly, The loan has been declined'})
        else:
            model1=pickle.load(open("ridge.pkl","rb"))
            predict1 = model1.predict([[BidsportfolioManager,BidsApi,BidsManual,Age,AppliedAmount,Interest,MonthlyPayment,IncomeTotal,ExistingLiabilities,
                                     RefinanceLiabilities,DebtToIncome,FreeCash,InterestAndPenaltyPaymentsMade,
                                     PreviousEarlyRepaymentsCountBeforeLoan,NewCreditCustomer,VerificationType,
                                     LanguageCode,Gender,Country,UseOfLoan,Education,MaritalStatus,EmploymentStatus,EmploymentDurationCurrentEmployer,OccupationArea,
                                     HomeOwnershipType,Rating,CreditScoreEsMicroL,Restructured,PrincipalPaymentsMade]])
            result = predict1
            result = {'EMI': predict1[0][0],'ELA': predict1[0][1],'ROI': predict1[0][2]}
            return render(request,'home.html',{ 'prediction_text':f'Congratulations, the loan has been approved {result}'})
            
        
            


    
        
        




        

        
    

