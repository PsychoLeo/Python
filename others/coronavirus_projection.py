import matplotlib.pyplot as plt

cases = [9, 15, 30, 40, 56, 66, 84, 102, 131, 159, 173, 186, 190, 221, 248, 278, 330, 354, 382, 461, 481, 526, 587, 608, 697, 781, 896, 999, 1124, 1212, 1385, 1715, 2055, 2429, 2764, 3323, 4288, 5364, 6780, 8555, 10288, 12742, 14901, 17867, 21393]
# cases of the coronavirus not including china
moy_l = []

for i in (1, len(cases)-1) :
    rapport = cases[i]/cases[i-1]
    moy_l.append (rapport)

moy = sum(moy_l)/len(moy_l)

def evolution (q, evolution_projection_limit):
    pass   
    
def evolution_less (q, limit_date) :
    sol = int(cases [-1]*q**(limit_date - 6))
    print ('There will approximatively be %s cases of coronavirus outside China on the %s/03/2020 (following the projection).' % (sol, limit_date))
                
                

if __name__ == '__main__' :
    limit_date = int(input("Enter the day of march to which you want to do the projection : "))
    evolution_less (moy, limit_date)
    # date = int(input("Enter the date to which you want to get the coronavirus' evolution : "))
    # evolution (moy, date)