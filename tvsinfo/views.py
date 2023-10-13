from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import JsonResponse
from .utils.globalUserPred import *
from .utils.localUserPred import *

baseInterest = 6

def getInterestRate(score):
    maxBias = 10
    stp = 1 / 90
    bias = ((score - 40) ** 2) * stp
    return baseInterest + bias


    
class pageone(APIView):
    def post(self, request):
            Bouncedinfirst = int(request.data.get('bounced_while_repaying'))
            nob12m = int(request.data.get('twelve_month_bounce_history'))
            MaxMob = int(request.data.get('maximum_mob'))
            bouncedwhilerepaying = int(request.data.get('bounced_while_repaying'))
            Emi = int(request.data.get('emi'))
            Loan_Amount = int(request.data.get('loan_amount'))
            Tenure = int(request.data.get('tenure'))
            advance_EMI = int(request.data.get('advance_emi_paid'))
            Roi = int(request.data.get('roi'))
            Customer_agewtk = int(request.data.get('age'))
            Noofloans = int(request.data.get('total_loans_taken'))
            Noosc  = int(request.data.get('total_secured_loans'))
            Noousc  = int(request.data.get('total_unsecured_loans'))
            maxamtsanc = int(request.data.get('maximum_loan_sanctioned'))
            no30d6 = int(request.data.get('thirty_days'))
            no60d6 = int(request.data.get('sixty_days'))
            no90d3 = int(request.data.get('ninety_days'))
            age = int(request.data.get('age_of_vehicle'))
            Dealercodes = int(request.data.get('dealer_code'))
            Tier_WOE = int(request.data.get('tier'))
            
            Gender_WOE = (request.data.get('gender'))
            Et_WOE = (request.data.get('employment_type'))
            Rt_WOE = (request.data.get('resident_type'))
            Productcodes = (request.data.get('product_code'))
            

            result = 100 * localUserPred(Bouncedinfirst,nob12m,MaxMob,bouncedwhilerepaying,Emi,Loan_Amount,Tenure,advance_EMI,Roi,Customer_agewtk,Noofloans,Noosc,Noousc,maxamtsanc,no30d6,no60d6,no90d3,age,Dealercodes,Productcodes,Gender_WOE,Et_WOE,Rt_WOE,Tier_WOE)
            
            context_data = {'result': result , 'interestRate': baseInterest if result <= 40 else (getInterestRate(result) if result <= 70 else 0)}
            return JsonResponse(context_data)
    
class Check(APIView):
    def post(self, request):
       disbursed_amount= int(request.data.get('disbursed_amount')) / 80
       asset_cost=int(request.data.get('asset_cost')) / 80
       loan_to_value_ratio=int(request.data.get('loan_to_value_ratio'))
       primary_disbursed_amount=int(request.data.get('primary_disbursed_amount')) / 80
       primary_current_balance= int(request.data.get('primary_current_balance')) / 80
       primary_sanctioned_amount=int(request.data.get('primary_sanctioned_amount')) / 80
       primary_overdue_accounts=int(request.data.get('primary_overdue_accounts')) 
       primary_active_accounts=int(request.data.get('primary_active_accounts'))
       primary_number_of_accounts=int(request.data.get('primary_number_of_accounts'))
       primary_installment_amount=int(request.data.get('primary_installment_amount')) / 80
       secondary_disbursed_amount=int(request.data.get('secondary_disbursed_amount')) / 80
       secondary_current_balance=int(request.data.get('secondary_current_balance')) / 80
       secondary_sanctioned_amount=int(request.data.get('secondary_sanctioned_amount')) / 80
       secondary_overdue_accounts=int(request.data.get('secondary_overdue_accounts'))
       secondary_active_accounts=int(request.data.get('secondary_active_accounts'))
       secondary_number_of_accouts=int(request.data.get('secondary_number_of_accounts')) 
       secondary_installment_amount=int(request.data.get('secondary_installment_amount')) / 80
       perform_cns_score=int(request.data.get('perform_cns_score'))
       deliquent_accounts=int(request.data.get('deliquent_accounts'))
       new_accounts=int(request.data.get('new_accounts'))
       employment_type=request.data.get('employment_type')
       number_of_inquiries=int(request.data.get('number_of_inquiries'))

       result = 100 * globalUserPred( disbursed_amount, asset_cost, loan_to_value_ratio, primary_disbursed_amount, primary_current_balance, primary_sanctioned_amount, primary_overdue_accounts, primary_active_accounts, primary_number_of_accounts, primary_installment_amount, secondary_disbursed_amount, secondary_current_balance, secondary_sanctioned_amount, secondary_overdue_accounts, secondary_active_accounts, secondary_number_of_accouts, secondary_installment_amount, perform_cns_score, deliquent_accounts, new_accounts, number_of_inquiries, employment_type)
       context_data = {'result': result , 'interestRate': baseInterest if result <= 40 else (getInterestRate(result) if result <= 70 else 0)}
       return JsonResponse(context_data)