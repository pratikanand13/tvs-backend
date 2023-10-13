import math
import numpy as np

def localUserPred(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24):
    lst_coeff=[-9.13324529e-09,-1.70311317e-07, -2.84805379e-06, -1.79837335e-07,
  -2.20264865e-04,-2.81065236e-05, -3.10083192e-06, -3.50235031e-08,
  -3.14120668e-06, -1.12014684e-05, -2.53340950e-07, -2.39913613e-07,
   1.15322575e-07, -5.61189701e-05, -1.86786778e-07, -1.68814286e-07,
  -7.39477586e-08, -1.29740134e-05, -2.06972603e-09,  8.39772489e-08,
  -1.12167129e-08, -2.90218129e-08, -4.54505799e-10,  4.01715072e-08]

    lst_inputs = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24]
    sum=0
    
    arr1 = np.array(lst_inputs)
    arr2 = np.array(lst_coeff)
    
    
    out_arr = np.multiply(arr1,arr2)
    sum=0
    for i in out_arr:
        sum+=i
        
    z=sum
    return 1/(1+math.exp(-z))
