import math
import numpy as np

def globalUserPred( disbursed_amount, asset_cost, loan_to_value_ratio, primary_disbursed_amount, primary_current_balance, primary_sanctioned_amount, primary_overdue_accounts, primary_active_accounts, primary_number_of_accounts, primary_installment_accounts, secondary_disbursed_amount, secondary_current_balance, secondary_sanctioned_amount, secondary_overdue_accounts, secondary_active_accounts, secondary_number_of_accouts, secondary_installment_accounts, perform_cns_score, deliquent_accounts, new_accounts, number_of_inquiries, employment_type):
    flag = 1
    mp = [806,761,736,706,681,651,631,601,571,521, 351, 300, 1]

    # RISK DESCRIPTION LIST
    vals = []

    # Risk - A to Risk - M 
    for e in mp:
        if(flag and perform_cns_score >= e):
            vals.append(1)
            flag = 0
        else:
            vals.append(0)
    
    #NO BUREAU HISTORY AVAILABLE
    if(flag == 0):
        vals.append(0)
    else:
        vals.append(1)

    # NOT SCORED
    vals.append(0) 

    # EMPLOYMENT DESCRIPTION LIST
    emp = []
    emp.append(1 if employment_type.lower() == "salaried" else 0)
    emp.append(1 if emp[0] == 0 else 0)
    
    # print(vals)
    # print(emp)
    return model(disbursed_amount, asset_cost, loan_to_value_ratio, perform_cns_score, primary_number_of_accounts, primary_active_accounts, primary_overdue_accounts, primary_current_balance, primary_sanctioned_amount, primary_disbursed_amount,secondary_number_of_accouts,secondary_active_accounts,secondary_current_balance,secondary_sanctioned_amount,secondary_disbursed_amount,primary_installment_accounts,secondary_installment_accounts,new_accounts, deliquent_accounts, number_of_inquiries,emp[0], emp[1], vals[0],vals[1],vals[2], vals[3],vals[4],vals[5],vals[6],vals[7],vals[8], vals[9],vals[10],vals[11], vals[12], vals[13], vals[14])



def model(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37):
    lst_coeff=[ 1.63815369e-05, -2.68494481e-05, -2.93865379e-05, -3.53871308e-04,
  -2.30631958e-06, -8.92467638e-07,  3.27923920e-07,  1.25823655e-07,
  -1.16446176e-07, -1.27534796e-07, -4.96254456e-08, -5.19002692e-09,
   1.90687810e-07, -6.19091101e-05,  6.13949753e-05, -1.33144403e-07,
   7.18593746e-06, -4.31774443e-07,  2.15927489e-07,  3.06578196e-07,
  -4.58988243e-07,  2.70362852e-08, -1.40008170e-07, -1.21632910e-07,
  -1.34840776e-07, -1.23054414e-07, -4.06416149e-08, -4.38196704e-08,
  -1.25153384e-08,  2.15640608e-08,  3.82419739e-08,  2.22938329e-08,
   7.60904347e-08,  9.08520530e-09,  9.49128623e-08, -3.81908585e-08,
  -3.75486554e-08]

    lst_inputs = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37]
    sum=0
    
    arr1 = np.array(lst_inputs)
    arr2 = np.array(lst_coeff)
    
    
    out_arr = np.multiply(arr1,arr2)
    sum=0
    for i in out_arr:
        sum+=i
        
    z=sum
    return 1/(1+math.exp(-z))





# TEMPORARY

    # msp = {
    # 'A-Very Low Risk': 806,
    # 'B-Very Low Risk':
    # 761,
    # 'C-Very Low Risk':
    # 736,
    # 'D-Very Low Risk':
    # 706,
    # 'E-Low Risk':
    # 681,
    # 'F-Low Risk':
    # 651,
    # 'G-Low Risk':
    # 631,
    # 'H-Medium Risk':
    # 601,
    # 'I-Medium Risk':
    # 571,
    # 'J-High Risk':
    # 521,
    # 'K-High Risk':
    # 351,
    # 'L-Very High Risk':
    # 301,
    # 'M-Very High Risk':
    # 300,
    # 'No Bureau History Available':
    # 0-0,
    # 'Not Scored':
    # Nan
    # }