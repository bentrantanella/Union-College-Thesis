import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import csv
from scipy.stats import ttest_rel

if __name__ == '__main__':
    datafile = open('FinalExperiment.csv')
    datareader = csv.reader(datafile)
    
    header = []
    header = next(datareader)
    
    U1000_1 = []
    U1000_10 = []
    U1000_20 = []
    U5000_1 = []
    U5000_10 = []
    U5000_20 = []
    
    L1000_1 = []
    L1000_10 = []
    L1000_20 = []
    L5000_1 = []
    L5000_10 = []
    L5000_20 = []
    
    P1000_1 = []
    P1000_10 = []
    P1000_20 = []
    P5000_1 = []
    P5000_10 = []
    P5000_20 = []
    
    B1000_1 = []
    B1000_10 = []
    B1000_20 = []
    B5000_1 = []
    B5000_10 = []
    B5000_20 = []
    
    for row in datareader:
        #BUCKET QUEUE
        if row[0] == 'Bucket Queue':
            if row[1] == '1000' and row[2] == '0.01':
                U1000_1.append(row)
            elif row[1] == '1000' and row[2] == '0.1':
                U1000_10.append(row)
            elif row[1] == '1000' and row[2] == '0.2':
                U1000_20.append(row)
            elif row[1] == '5000' and row[2] == '0.01':
                U5000_1.append(row)
            elif row[1] == '5000' and row[2] == '0.1':
                U5000_10.append(row)
            elif row[1] == '5000' and row[2] == '0.2':
                U5000_20.append(row)
        
        #LL PRIORITY QUEUE
        elif row[0] == 'LL Priority Queue':
            if row[1] == '1000' and row[2] == '0.01':
                L1000_1.append(row)
            elif row[1] == '1000' and row[2] == '0.1':
                L1000_10.append(row)
            elif row[1] == '1000' and row[2] == '0.2':
                L1000_20.append(row)
            elif row[1] == '5000' and row[2] == '0.01':
                L5000_1.append(row)
            elif row[1] == '5000' and row[2] == '0.1':
                L5000_10.append(row)
            elif row[1] == '5000' and row[2] == '0.2':
                L5000_20.append(row)
            
        #PRIORITY QUEUE
        elif row[0] == 'Priority Queue':
            if row[1] == '1000' and row[2] == '0.01':
                P1000_1.append(row)
            elif row[1] == '1000' and row[2] == '0.1':
                P1000_10.append(row)
            elif row[1] == '1000' and row[2] == '0.2':
                P1000_20.append(row)
            elif row[1] == '5000' and row[2] == '0.01':
                P5000_1.append(row)
            elif row[1] == '5000' and row[2] == '0.1':
                P5000_10.append(row)
            elif row[1] == '5000' and row[2] == '0.2':
                P5000_20.append(row)
            
        #BINARY HEAP
        elif row[0] == 'Binary Heap':
            if row[1] == '1000' and row[2] == '0.01':
                B1000_1.append(row)
            elif row[1] == '1000' and row[2] == '0.1':
                B1000_10.append(row)
            elif row[1] == '1000' and row[2] == '0.2':
                B1000_20.append(row)
            elif row[1] == '5000' and row[2] == '0.01':
                B5000_1.append(row)
            elif row[1] == '5000' and row[2] == '0.1':
                B5000_10.append(row)
            elif row[1] == '5000' and row[2] == '0.2':
                B5000_20.append(row)
    
    
    #1000, 1%, USER
    UU1000_1 = [float(x[3]) for x in U1000_1]
    LU1000_1 = [float(x[3]) for x in L1000_1]
    PU1000_1 = [float(x[3]) for x in P1000_1]
    BU1000_1 = [float(x[3]) for x in B1000_1]
    
    df = pd.DataFrame({'Bucket Queue': UU1000_1, 'LL PQueue': LU1000_1, 'PQueue': PU1000_1, 'Binary Heap': BU1000_1})
    boxplot = df[['Bucket Queue', 'LL PQueue', 'PQueue', 'Binary Heap']].plot(kind='box', title='Size 1000, Density 1%', grid=True, ylabel='Time (Seconds)', ylim=(0,2))
    plt.show()
    
    
    #1000, 10%, USER
    UU1000_10 = [float(x[3]) for x in U1000_10]
    LU1000_10 = [float(x[3]) for x in L1000_10]
    PU1000_10 = [float(x[3]) for x in P1000_10]
    BU1000_10 = [float(x[3]) for x in B1000_10]
    
    df = pd.DataFrame({'Bucket Queue': UU1000_10, 'LL PQueue': LU1000_10, 'PQueue': PU1000_10, 'Binary Heap': BU1000_10})
    boxplot = df[['Bucket Queue', 'LL PQueue', 'PQueue', 'Binary Heap']].plot(kind='box', title='Size 1000, Density 10%', grid=True, ylabel='Time (Seconds)', ylim=(0,2))
    plt.show()
    
    #1000, 20%, USER
    UU1000_20 = [float(x[3]) for x in U1000_20]
    LU1000_20 = [float(x[3]) for x in L1000_20]
    PU1000_20 = [float(x[3]) for x in P1000_20]
    BU1000_20 = [float(x[3]) for x in B1000_20]
    
    df = pd.DataFrame({'Bucket Queue': UU1000_20, 'LL PQueue': LU1000_20, 'PQueue': PU1000_20, 'Binary Heap': BU1000_20})
    boxplot = df[['Bucket Queue', 'LL PQueue', 'PQueue', 'Binary Heap']].plot(kind='box', title='Size 1000, Density 20%', grid=True, ylabel='Time (Seconds)', ylim=(0,60))
    plt.show()
    
    #5000, 1%, USER
    UU5000_1 = [float(x[3]) for x in U5000_1]
    LU5000_1 = [float(x[3]) for x in L5000_1]
    PU5000_1 = [float(x[3]) for x in P5000_1]
    BU5000_1 = [float(x[3]) for x in B5000_1]
    
    df = pd.DataFrame({'Bucket Queue': UU5000_1, 'LL PQueue': LU5000_1, 'PQueue': PU5000_1, 'Binary Heap': BU5000_1})
    boxplot = df[['Bucket Queue', 'LL PQueue', 'PQueue', 'Binary Heap']].plot(kind='box', title='Size 5000, Density 1%', grid=True, ylabel='Time (Seconds)', ylim=(0,60))
    plt.show()
    
    #5000, 10%, USER
    UU5000_10 = [float(x[3]) for x in U5000_10]
    LU5000_10 = [float(x[3]) for x in L5000_10]
    PU5000_10 = [float(x[3]) for x in P5000_10]
    BU5000_10 = [float(x[3]) for x in B5000_10]
    
    df = pd.DataFrame({'Bucket Queue': UU5000_10, 'LL PQueue': LU5000_10, 'PQueue': PU5000_10, 'Binary Heap': BU5000_10})
    boxplot = df[['Bucket Queue', 'LL PQueue', 'PQueue', 'Binary Heap']].plot(kind='box', title='Size 5000, Density 10%', grid=True, ylabel='Time (Seconds)', ylim=(0,60))
    plt.show()
    
    #5000, 20%, USER
    UU5000_20 = [float(x[3]) for x in U5000_20]
    LU5000_20 = [float(x[3]) for x in L5000_20]
    PU5000_20 = [float(x[3]) for x in P5000_20]
    BU5000_20 = [float(x[3]) for x in B5000_20]
    
    df = pd.DataFrame({'Bucket Queue': UU5000_20, 'LL PQueue': LU5000_20, 'PQueue': PU5000_20, 'Binary Heap': BU5000_20})
    boxplot = df[['Bucket Queue', 'LL PQueue', 'PQueue', 'Binary Heap']].plot(kind='box', title='Size 5000, Density 20%', grid=True, ylabel='Time (Seconds)', ylim=(0,60))
    plt.show()
    
    AllU = UU1000_1 + UU1000_10 + UU1000_20 + UU5000_1 + UU5000_10 + UU5000_20
    AllP = PU1000_1 + PU1000_10 + PU1000_20 + PU5000_1 + PU5000_10 + PU5000_20
    dfU = pd.DataFrame({'Bucket Queue': AllU})
    dfP = pd.DataFrame({'PQueue': AllP})
    t, p = ttest_rel(dfU, dfP)
    print('t = ' + str(t) + ' p = ' + str(p))
    
    
    #1000, 10%, METHODS
    UA1000_10 = [float(x[4]) for x in U1000_10]
    LA1000_10 = [float(x[4]) for x in L1000_10]
    PA1000_10 = [float(x[4]) for x in P1000_10]
    BA1000_10 = [float(x[4]) for x in B1000_10]
    
    UG1000_10 = [float(x[5]) for x in U1000_10]
    LG1000_10 = [float(x[5]) for x in L1000_10]
    PG1000_10 = [float(x[5]) for x in P1000_10]
    BG1000_10 = [float(x[5]) for x in B1000_10]
    
    UP1000_10 = [float(x[6]) for x in U1000_10]
    LP1000_10 = [float(x[6]) for x in L1000_10]
    PP1000_10 = [float(x[6]) for x in P1000_10]
    BP1000_10 = [float(x[6]) for x in B1000_10]
    
    UA_avg = sum(UA1000_10) / len(UA1000_10)
    LA_avg = sum(LA1000_10) / len(LA1000_10)
    PA_avg = sum(PA1000_10) / len(PA1000_10)
    BA_avg = sum(BA1000_10) / len(BA1000_10)
    
    UG_avg = sum(UG1000_10) / len(UG1000_10)
    LG_avg = sum(LG1000_10) / len(LG1000_10)
    PG_avg = sum(PG1000_10) / len(PG1000_10)
    BG_avg = sum(BG1000_10) / len(BG1000_10)
    
    UP_avg = sum(UP1000_10) / len(UP1000_10)
    LP_avg = sum(LP1000_10) / len(LP1000_10)
    PP_avg = sum(PP1000_10) / len(PP1000_10)
    BP_avg = sum(BP1000_10) / len(BP1000_10)
    
    
    L_avg = [LA_avg, LG_avg, LP_avg]
    B_avg = [BA_avg, BG_avg, BP_avg]
    
    df = pd.DataFrame({'Time': L_avg}, index=['Add', 'getNext', 'Update'])
    plot = df.plot.pie(y='Time', figsize=(5,5), title='LL PQueue, 1000 10%')
    plt.show()
    
    df = pd.DataFrame({'Time': B_avg}, index=['Add', 'getNext', 'Update'])
    plot = df.plot.pie(y='Time', figsize=(5,5), title='Binary Heap, 1000 10%')
    plt.show()

    
    #5000, 10%, METHODS
    UA5000_10 = [float(x[4]) for x in U5000_10]
    LA5000_10 = [float(x[4]) for x in L5000_10]
    PA5000_10 = [float(x[4]) for x in P5000_10]
    BA5000_10 = [float(x[4]) for x in B5000_10]
    
    UG5000_10 = [float(x[5]) for x in U5000_10]
    LG5000_10 = [float(x[5]) for x in L5000_10]
    PG5000_10 = [float(x[5]) for x in P5000_10]
    BG5000_10 = [float(x[5]) for x in B5000_10]
    
    UP5000_10 = [float(x[6]) for x in U5000_10]
    LP5000_10 = [float(x[6]) for x in L5000_10]
    PP5000_10 = [float(x[6]) for x in P5000_10]
    BP5000_10 = [float(x[6]) for x in B5000_10]
    
    UA_avg = sum(UA5000_10) / len(UA5000_10)
    LA_avg = sum(LA5000_10) / len(LA5000_10)
    PA_avg = sum(PA5000_10) / len(PA5000_10)
    BA_avg = sum(BA5000_10) / len(BA5000_10)
    
    UG_avg = sum(UG5000_10) / len(UG5000_10)
    LG_avg = sum(LG5000_10) / len(LG5000_10)
    PG_avg = sum(PG5000_10) / len(PG5000_10)
    BG_avg = sum(BG5000_10) / len(BG5000_10)
    
    UP_avg = sum(UP5000_10) / len(UP5000_10)
    LP_avg = sum(LP5000_10) / len(LP5000_10)
    PP_avg = sum(PP5000_10) / len(PP5000_10)
    BP_avg = sum(BP5000_10) / len(BP5000_10)
    
    
    L_avg = [LA_avg, LG_avg, LP_avg]
    B_avg = [BA_avg, BG_avg, BP_avg]
    
    df = pd.DataFrame({'Time': L_avg}, index=['Add', 'getNext', 'Update'])
    plot = df.plot.pie(y='Time', figsize=(5,5), title='LL PQueue, 5000 10%')
    plt.show()
    
    df = pd.DataFrame({'Time': B_avg}, index=['Add', 'getNext', 'Update'])
    plot = df.plot.pie(y='Time', figsize=(5,5), title='Binary Heap, 5000 10%')
    plt.show()
    
    
    
    datafile.close()