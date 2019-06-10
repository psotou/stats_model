import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

desv = input('Ingresar desviaciones (ejemplo, 10% = 0.1) separadas por comas:').split(',') #0.216403,0.161056,0.33,0.001
mad = input('Ingresar indicador madurez (ejemplo, 4/1.9) separados por comas:').split(',') #2.353,1.818,4,1

l, ll = [], []
for i in range(len(desv)):
    a = float(desv[i])
    b = float(mad[i])
    l.append(a)
    ll.append(b)

df = pd.DataFrame({'Desv': l, 'Mad': ll})

def modelo_propuesto(df):
    df['cons'] = 1
    reg = sm.OLS(endog=df.Desv, exog=df[['cons', 'Mad']], missing='drop').fit()
    b = reg.params
    r2 = reg.rsquared
    p = reg.pvalues
    
    m = np.linspace(1.0, 4.0, 31)
    l = []
    for i in range(len(m)):
        y = b[0] + b[1]*4/m[i]
        y = np.float(y)
        l.append(y)

    y = np.asarray(l).reshape(len(m), 1)

    fig = plt.figure()
    plt.plot(m, y, "r-")
    plt.axis([1, 4, 0.01, 0.4])
    plt.grid(True)
    plt.title('Relación Madurez BIM y Desviación Costos Finales')
    plt.xlabel('Madurez BIM', fontsize=12)
    plt.ylabel('Desviación Costos', fontsize=12)
    
    return b, r2, p, fig, reg

b, r2, p, fig, reg = modelo_propuesto(df) #run reg.summary() to see more details

fig.show()