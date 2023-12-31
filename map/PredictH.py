import pandas
import numpy as np, pandas as pd

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import math
from statsmodels.tsa.stattools import acf, pacf
import statsmodels.tsa.stattools as ts
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima.model import ARIMA
from openpyxl import load_workbook



import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt

import statsmodels.api as sm
import scipy.stats as scs
#from arch import arch_model

import matplotlib.pyplot as plt
import matplotlib.pyplot as pltt
import matplotlib as mpl

######################Import Data##################################
data = pd.read_excel(r'static/exels/operation.xlsx')
Ell  = pd.read_excel(r'static/exels/operation.xlsx',1)
Dis  = pd.read_excel(r'static/exels/operation.xlsx',2)
#######################Input Variables#############################

## این قسمت برای خواندن متغییرها از فایل اکسل میباشد در صورت نیاز اضافه خواهد شد
"""wb = load_workbook("static/exels/operation.xlsx")
sh =wb['Sheet1']  
wb.close()
"""

C=0.9
A=413
Stin=356
pkhours=18
NWL=1220
MWL=1150
Smax=1450
Smin=99
PPC=55.2
Hd=8
Nu=2
epsilon=0.7
Lpenestak=100
ks=0.00005
l_v=1000000
Hloss=3
Htail=3
V=0.000001
K=1.4
p=3
q=2
d=2


##################################################################
Qd=PPC*1000/Hd/9.81/epsilon
Dint=1.12*Qd*0.45/Hd*0.12
Dpen=1.12*(Qd/Nu)*0.45/Hd*0.12
Aint=3.14*(Dint**2)/4
Apen=3.14*(Dpen**2)/4
Vin=Qd/Aint;
Vpen=Qd/Apen/Nu;
Hloss_in=(Vin**2)/(2*9.81);
Hloss_pen=(Vpen**2)/(2*9.81);
Re=Dpen*Vpen*100000;
f=0.25/(math.log10((epsilon/1000/3.7/Dpen)+(5.7/(Re**0.9))))**2
Qmin=0.4*Qd/Nu
Npkours=24-pkhours
Volume=Ell.Volume
El=Ell.El
AA=Ell.Area
df=data.Rain
y=df
price=df
lnprice=np.log(price)
lnprice
plt.plot(lnprice)
#plt.show()
acf_1 =  acf(lnprice)[1:20]
plt.plot(acf_1)
#plt.show()
test_df = pandas.DataFrame([acf_1]).T
test_df.columns = ['Pandas Autocorrelation']
test_df.index += 1
test_df.plot(kind='bar')
pacf_1 =  pacf(lnprice)[1:20]
plt.plot(pacf_1)
#plt.show()
# test_df = pandas.DataFrame([pacf_1]).T
# test_df.columns = ['Pandas Partial Autocorrelation']
# test_df.index += 1
# test_df.plot(kind='bar')
# result = ts.adfuller(lnprice, 1)
# result
lnprice_diff=lnprice-lnprice.shift()
diff=lnprice_diff.dropna()
acf_1_diff =  acf(diff)[1:100]
test_df = pandas.DataFrame([acf_1_diff]).T
test_df.columns = ['First Difference Autocorrelation']
test_df.index += 1
test_df.plot(kind='bar')
pacf_1_diff =  pacf(diff)[1:20]
plt.plot(pacf_1_diff)
#plt.show()
price_matrix=data
model = ARIMA(df, order=(p,d,q))  # Replace p, d, q with appropriate values
model_fit = model.fit()

predictions=model_fit.predict(step=120, typ='levels')
predictions

plt.plot(predictions)



def tsplot(y, lags=None, figsize=(10, 8), style='bmh'):
    if not isinstance(y, pd.Series):
        y = pd.Series(y)
    with plt.style.context(style):    
        fig = plt.figure(figsize=figsize)
        #mpl.rcParams['font.family'] = 'Ubuntu Mono'
        layout = (3, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))
        qq_ax = plt.subplot2grid(layout, (2, 0))
        pp_ax = plt.subplot2grid(layout, (2, 1))
        
        y.plot(ax=ts_ax)
        ts_ax.set_title('Time Series Analysis Plots')
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax, alpha=0.5)
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax, alpha=0.5)
        sm.qqplot(y, line='s', ax=qq_ax)
        qq_ax.set_title('QQ Plot')        
        scs.probplot(y, sparams=(y.mean(), y.std()), plot=pp_ax)

        plt.tight_layout()
    return

 # Replace p, d, q with appropriate values
model = ARIMA(y, order=(p,q,d))  # Replace p, d, q with appropriate values
model_fit = model.fit()
# tsplot(y, lags=19)
# model_fit = model.fit()
# tsplot(y.diff(), lags=19)
# Make predictions
steps=120
forecast = model_fit.predict(steps=steps)
forecasts=[]
i=1
for i in range (steps):
    
    if forecast[i]<=0:
        forecasts.append(0)
    else:
        forecasts.append(forecast[i])
g=[]
for i in range (steps):
    g.append(data.g[i])
b=[]
for i in range (steps):
    b.append(data.b[i])
Fc = list(map(float, forecasts))

Q=[]
for i in range (steps):
 Q.append(((0.278*C*A*(Fc[i])*3600*30*18)/100000000)+16)
    
    
tsplot(forecast, lags=1)

# pltt.show()



n=1
Qt=[]
ST_i=[]
Def_i=[]
EXP_i=[]
Rtot_i=[]
Rpt_i=[]
Ppkt_i=[]
Epk=[]
Roff_i=[]
Qoff_i=[]
Htail_i=[]
Htailof_i=[]
Hnetof_i=[]
Pof_i=[]
Eof_i=[]
Etot_i=[]
HHH=[]
for i in range(120):
    
    if i==0:
        st=Stin
    else:
        st=ST_i[i-1]
    Qt=Q[i]*3600*30*24/1000000
   
    Rti=Qt*pkhours*3600/100000
    HHH.append(Rti)
    Elt=np.interp(st, Volume, El)
    Elti=Elt
    Hg=Elti-El[0]
    Hgi=Hg
    Hnetavg=(Hgi+Hg)/2-Htail-Hloss
    Qpi=PPC*1000/9.81/epsilon/1000000
    At=np.interp(st,Volume,AA)
    Ati=At
    et=(Ati+At)/2000*data.evt[i]
    sti=st+Qt-Rti-et-183*0.25
    
    if sti>Smax:
        stii=Smax
    if sti<Smin:
        stii=Smin
    else:
       stii=sti
       
    if sti<Smin:
        Def=Smin-sti
    else:
        Def=0
    
    if sti>Smax:
        Exp=sti-Smax
    else:
        Exp=0
        
    j=1
    s=[]
    s.append(0)
    s.append(5)
    
    while abs(s[j]-s[j-1]):
        Elt=np.interp(sti, Volume, El)
        Elti=Elt
        Hg=Elti-El[0]
        Hgi=Hg
        Hnetavg=(Hgi+Hg)/2-Htail-Hloss
        Qpi=PPC*1000/9.81/epsilon/1000000
        Vint=Qpi/Aint
        Vpen=Qpi/Nu/Apen
        Hint=Vint**2/(2*9.81);
        Hpen=Vpen**2/(2*9.81)
        Re=Vpen*l_v*Dpen
        f=0.25/((math.log10(ks/3.7/Dpen+5.74/(Re**0.9)))**2)
        k3=f*Lpenestak/Dpen
        Hloss=K*Hint+k3*Hpen
        Rti=Qt*pkhours*3600/100000
        At=np.interp(sti,Volume,AA)
        Ati=At
        et=(Ati+At)/2000*data.evt[i]
        sti=st+Qt-Rti-et-183*0.25
        if sti<Smin:
           Def=Smin-sti;
        else:
          Def=0
    
        if sti>Smax:
           Exp=sti-Smax;
        else:
            Exp=0
        if sti>Smax:
           sti=Smax
        elif sti<Smin:
            sti=Smin
        else:
            sti=sti
    
        
        Rtot=Rti+Exp-Def;
        Rpt=Rtot-Exp
        Qpt=Rpt*1000000/(pkhours*3600)
        
        if Qpt<Qmin:
            Ppkt=0
        else:
            Ppkt=9.81/1000*Qpt*Hnetavg*epsilon;
        
        Epk=Ppkt*pkhours;
        Roff=Exp;
        Qoff=Roff*1000000/3600/Npkours
        Htail=np.interp(Qpt,Dis.Discharge ,Dis.Height );
        Htailof=np.interp(Qoff,Dis.Discharge ,Dis.Height );
        Hnetof=Hnetavg-Htail+Htailof
        
        if Qoff<Qmin:
            Pof=0
        else:
            Pof=min(PPC,9.81/1000*Qoff*Qoff*epsilon);
        
        Eof=Pof*Npkours;
        Etot=Eof+Epk;
        j=j+1
        s.append(sti);
    Rpt_i.append(Rpt)
    ST_i.append(sti);
    Def_i.append(Def);
    EXP_i.append(Exp);
    Rtot_i.append(Rtot);
    Rpt_i.append(Rpt);
    Ppkt_i.append(Ppkt);
    # Epk.append(Ppkt[i]*pkhours);
    Roff_i.append(Roff);
    Qoff_i.append(Qoff);
    Htail_i.append(Htail);
    Htailof_i.append(Htailof);
    Hnetof_i.append(Hnetof);
    Pof_i.append(Pof);
    Eof_i.append(Eof);
    Etot_i.append(Etot);



def plot():
 pltt.plot(forecasts)
 pltt.savefig('static/img/plot1.png',format= 'png' , dpi=800,bbox_inches='tight')
 pltt.plot(g)
 pltt.savefig('static/img/plot2.png',format= 'png' , dpi=800,bbox_inches='tight')
 pltt.plot(b)
 pltt.savefig('static/img/plot3.png',format= 'png' , dpi=800,bbox_inches='tight')
 #pltt.show()
 plt.plot(Etot_i)
 plt.savefig('static/img/plot4.png',format= 'png' , dpi=800,bbox_inches='tight')
 #plt.show()
 plt.plot(ST_i)
 plt.savefig('static/img/plot5.png',format= 'png' , dpi=800,bbox_inches='tight')
 #plt.show

            

    
        

