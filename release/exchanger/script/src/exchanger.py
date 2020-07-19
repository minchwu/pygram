import tkinter as tk
from  tkinter  import ttk  
import CoolProp.CoolProp as prp 
import math
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from sko.GA import GA
import numpy as np
window = tk.Tk()
window.title('echangeur')
window.geometry('1000x800')

frm = tk.Frame(window)
frm.pack()

fig = Figure(figsize=(4,3))
canvas = FigureCanvasTkAgg(fig, master=frm)  # A tk.DrawingArea.
canvas.get_tk_widget().pack(side=tk.BOTTOM)

frm_l = tk.LabelFrame(frm, text="Area Calculation & Exchanger Design", labelanchor="n",height = 1000)
frm_l.pack(side='left')
frm_r = tk.LabelFrame(frm, text="Temperature Calculation", labelanchor="n",height = 1000)
frm_r.pack(side='right')

tk.Label(frm_l,text='choose fluid(hot):').grid(row=0,column=0)
comvalue1=tk.StringVar()
comfluid1 = ttk.Combobox(frm_l,textvariable=comvalue1)
comfluid1["value"]=("water(liquid)",'water(gas)',"air","Methane(gas)","Methane(liquid)",
                    'R134a(gas)','R134a(liquid)')  
comfluid1.current(0)
comfluid1.grid(row=0, column=1,sticky='nw',rowspan = 1)

tk.Label(frm_l,text='choose fluid(cold)   :').grid(row=1,column=0)
comvalue2=tk.StringVar()
comfluid2= ttk.Combobox(frm_l,textvariable=comvalue2)
comfluid2["value"]=("water(liquid)",'water(gas)',"air","Methane(gas)","Methane(liquid)",
                    'R134a(gas)','R134a(liquid)')  
comfluid2.current(0)
comfluid2.grid(row=1, column=1,sticky='nw')

tk.Label(frm_l,text='choose exchanger   :').grid(row=2,column=0)
extypevar=tk.StringVar()
extype= ttk.Combobox(frm_l,textvariable= extypevar )
extype["value"]=("parallel-flow",'counter-flow','tube-shell')   
extype.current(0)
extype.grid(row=2, column=1,sticky='nw')


varnshell = tk.StringVar()
varnshell.set('how many shells?')
entry_nshell = tk.Entry(frm_l,textvariable = varnshell)
entry_nshell.grid(row=2, column=2)

var_entry_Tci = tk.StringVar()
entry_Tci = tk.Entry(frm_l,textvariable = var_entry_Tci)
entry_Tci.grid(row=3, column=1)
tk.Label(frm_l,text = 'Tci(℃):').grid(row=3)

var_entry_Tco = tk.StringVar()
entry_Tco = tk.Entry(frm_l,textvariable = var_entry_Tco)
entry_Tco.grid(row=4, column=1)
tk.Label(frm_l,text = 'Tco(℃):').grid(row=4)

var_entry_Thi = tk.StringVar()
entry_Thi = tk.Entry(frm_l,textvariable = var_entry_Thi)
entry_Thi.grid(row=5, column=1)
tk.Label(frm_l,text = 'Thi(℃):').grid(row=5)

var_entry_Tho = tk.StringVar()
entry_Tho = tk.Entry(frm_l,textvariable = var_entry_Tho)
entry_Tho.grid(row=6, column=1)
tk.Label(frm_l,text = 'Tho(℃):').grid(row=6)

var_entry_debith = tk.StringVar()
entry_debith = tk.Entry(frm_l,textvariable = var_entry_debith)
entry_debith.grid(row=7, column=1)
tk.Label(frm_l,text = 'mass flow rate hot(kg/s):').grid(row=7)


var_entry_debitc = tk.StringVar()
entry_debitc = tk.Entry(frm_l,textvariable = var_entry_debitc)
entry_debitc.grid(row=8, column=1)
tk.Label(frm_l,text = 'mass flow rate cold(kg/s):').grid(row=8)


def fluid(a):
    if a=='air':
        return 'air'
    elif 'water' in a:
        return 'water' 
    elif 'Methane' in a:
        return 'methane'
    else:
        return 'R134a'
    
def fluidstate(a):
    if a =='air':
        return 1
    elif 'gas' in a:
        return 1
    else:
        return 0

from scipy.optimize import minimize
import numpy as np


def NTU(effectiveness, C, extype):
    extype = extypevar.get()
    if extype == 'counter-flow':
        if C < 1:
            return 1./(C - 1.)*math.log((effectiveness - 1.)/(effectiveness*C - 1.))
        elif C == 1:
            return effectiveness/(1. - effectiveness)
    elif extype == 'parallel-flow':
        if effectiveness*(1. + C) > 1:
            tk.messagebox.showwarning('warning!','the maximum effectiveness possible is %.4s.' % (1./(C + 1.)))
            raise Exception('The specified effectiveness is not physically \
possible for this configuration')
            
        return -math.log(1. - effectiveness*(1. + C))/(1. + C)    
    elif extype == 'tube-shell':
        shells = int(varnshellr.get())
        F = ((effectiveness*C - 1.)/(effectiveness - 1.))**(1./shells)
        e1 = (F - 1.)/(F - C)
        E = (2./e1 - 1.- C)/(1. + C**2)**0.5       
        if (E - 1.)/(E + 1.) <= 0:
            max_effectiveness = (-((-C + math.sqrt(C**2 + 1) + 1)/(C + math.sqrt(C**2 + 1) - 1))**shells + 1)/(C - ((-C + math.sqrt(C**2 + 1) + 1)/(C + math.sqrt(C**2 + 1) - 1))**shells)
            raise Exception('The specified effectiveness is not physically \
possible for this configuration; the maximum effectiveness possible is %s.' % (max_effectiveness))
        NTU = -(1. + C*C)**-0.5*math.log((E - 1.)/(E + 1.))
        return shells*NTU
        
def isfloat(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        return None

def dr(Thi,Tho,Tci,Tco,extype):
    fig.clear()
    #extype = extypevar.get()
    ax = fig.add_subplot(111)
    if extype == 'parallel-flow':
        hot = [Thi,Tho]
        cold = [Tci,Tco]
    else :
        hot = [Tho,Thi]
        cold = [Tci,Tco]
    ax.set_ylabel('temperature(℃)')
    ax.plot([0,1],hot,color='r')
    ax.plot([0,1],cold,color='b')
    canvas.draw()

def UA():
    global fig,canvas,A,phoh,phoc,mh,mc
    U=1000
    p = 101325
    Tci = isfloat(var_entry_Tci.get())
    Tco = isfloat(var_entry_Tco.get())
    Thi = isfloat(var_entry_Thi.get())
    Tho = isfloat(var_entry_Tho.get())
    mh = isfloat(var_entry_debith.get())
    mc = isfloat(var_entry_debitc.get())
    extype = extypevar.get()
    fluidh = comvalue1.get()
    fluidc = comvalue2.get()
    qh = fluidstate(fluidh)
    qc = fluidstate(fluidc)   
    Cph = prp.PropsSI('C','P',p,'Q',qh,fluid(fluidh))
    Cpc = prp.PropsSI('C','P',p,'Q',qc,fluid(fluidc))
    phoh = prp.PropsSI('D','P',p,'Q',qh,fluid(fluidh))
    phoc = prp.PropsSI('D','P',p,'Q',qc,fluid(fluidc))
    if Thi is not None and Tho is not None:
        Q = mh*Cph*(Thi-Tho)
        if Tci is not None and Tco is None:
            Tco = Tci + Q/(mc*Cpc)
        elif Tco is not None and Tci is None:
            Tci = Tco - Q/(mc*Cpc)
        elif Tco is not None and Tci is not None:
            Q2 = mc*Cpc*(Tco-Tci)
            if abs((Q-Q2)/Q) > 0.01:
                tk.messagebox.showwarning('warning!','Something goes wrong, you may ajust T,Cp or mass flow')
                raise Exception('!')
        else:
            raise Exception('At least one temperature is required to be specified on the cold side.')
        
    elif Tci is not None and Tco is not None:
        Q = mc*Cpc*(Tco-Tci)
        if Thi is not None and Tho is None:
            Tho = Thi - Q/(mh*Cph)
        elif Tho is not None and Thi is None:
            Thi = Tho + Q/(mh*Cph)
        else:
            raise Exception('At least one temperature is required to be specified on the cold side.')
    else:
        tk.messagebox.showwarning('!','3 temperatures are needed')
        raise Exception('Three temperatures are required to be specified '
                    'when solving for UA')
    Cmin = min(mh*Cph,mc*Cpc)
    Cmax = max(mh*Cph,mc*Cpc)
    C = Cmin/Cmax
    effectiveness = Q/Cmin/(Thi-Tci)
    NTUU = NTU(effectiveness, C, extype)
    A = NTUU*Cmin/U   

    dr(Thi,Tho,Tci,Tco,extype)
    if extype == 'tube-shell':
        def schafferh(Dt,Dc,Db,Nt):
            global deltaPc, deltaPh, L
            m=mh
            mu=0.00053
            pho=phoh
            Pt=1.25*Dt
            #Nt=math.ceil(math.pi/4*0.9*pow(Dc,2)/pow(Pt,2))
            Nt=math.ceil(Nt)
            v=m/pho/Dc/Db/(Pt-Dt)*Pt
            De=4*(pow(Pt,2)-(math.pi/4*pow(Dt,2)))/(math.pi*Dt)
            Re=pho*v*De/mu
            fh=math.exp(0.567-0.19*math.log(Re))
            L=A/Nt/math.pi/Dt
            vc=mc/phoc/math.pi/pow(Dt,2)*4
            Rec=phoc*vc*Dt/mu
            if (Rec<50000):
                f=16/Rec
            else:
                f=pow(1.58*math.log(Rec)-3.28,-2);
            deltaPc=Nt*4*f*L/Dt*phoc/2*pow(vc,2)
            deltaPh=(Nt+1)*fh*Dc*pho/2*pow(v,2)/De
            return m/pho*deltaPh+mc/phoc*deltaPc
        gah = GA(func=schafferh, n_dim=4, size_pop=50, max_iter=800, lb=[0.001,0.01,0.01,1], ub=[0.05,0.3,0.5,50], precision=1e-7)
        #gac = GA(func=schafferc, n_dim=3, size_pop=50, max_iter=800, lb=[0.1,0.01,0.01], ub=[0.2,0.5,0.5], precision=1e-7)
        best_x, best_y = gah.run()
        #pressured = best_y[0]
        pressuredh = deltaPh
        pressuredc= deltaPc
        
        best_clendar_diameter = best_x[1]
        best_baffle_diameter = best_x[2]
        best_tube_diameter = best_x[0]
        best_length=L
        tk.messagebox.showinfo('Result','              A  = {:.2f}㎡, \n \
             the pressure drop of shell side is {:.2f} Pa\n \
             the pressure drop of tube side is {:.2f} Pa\n \
             the best length of tube is {:.2f} m\n\
             the best tube diameter is {} m\n \
             the best baffle distance is {:.2f} m\n \
             the best shell diameter is {:.2f} m'.format(A,pressuredh,pressuredc,best_length,best_tube_diameter,best_baffle_diameter,best_clendar_diameter))
    else:
        def schafferh(D,x):  
            m=mh
            mu=0.00053
            pho=phoh
            L=A/math.pi/D
            v=4*m/pho/math.pi/math.pow(D,2)
            Re=pho*v*D/mu
            if (Re<50000):
                f=16/Re
            else:
                f=math.pow(1.58*math.log(Re)-3.28,-2);
            deltaP=4*f*L/D*pho/2*pow(v,2)
            return deltaP
        def  schafferc(D,x):  
            m=mc
            mu=0.00053
            pho=phoc
            L=A/math.pi/D
            v=4*m/pho/math.pi/math.pow(D,2)
            Re=pho*v*D/mu
            if (Re<50000):
                f=16/Re
            else:
                f=pow(1.58*math.log(Re)-3.28,-2);
            deltaP=4*f*L/D*pho/2*pow(v,2)
            return deltaP
        gac = GA(func = schafferc, n_dim=2, size_pop=50, max_iter=800, lb=[0.0001,0], ub=[0.05,1], precision=1e-7)
        gah = GA(func = schafferh, n_dim=2, size_pop=50, max_iter=800, lb=[0.0001,0], ub=[0.05,1], precision=1e-7)
        best_xc, best_yc = gac.run()
        best_xh, best_yh = gah.run()
        pressuredh = best_yh[0]
        pressuredc = best_yc[0]
        best_diameterh = best_xh[0]
        #best_lengthh=A/math.pi/best_diameterh
        best_diameterc = best_xc[0]
        best_lengthc=A/math.pi/best_diameterc
        tk.messagebox.showinfo('Result','              A  = {:.2f}㎡, \n \
             the pressure drop of hot fluid is {:.2f} Pa\n \
             the pressure drop of cold fluid is {:.2f} Pa\n \
             the best diameter of hot fluid tube is {:.2f} m\n\
             the best diameter of cold fluid tube is {:.2f} m\n\
             and the  best length of tube is {:.2f}m' .format(A,pressuredh,pressuredc,best_diameterh,best_diameterc,best_lengthc))

btn_compute = tk.Button(frm_l,text='compute',command = UA).grid(row=9)

tk.Label(frm_r,text='choose fluid(hot)   :').grid(row=0,column=0)
comvalue1r=tk.StringVar()
comfluid1r = ttk.Combobox(frm_r,textvariable=comvalue1r)
comfluid1r["value"]=("water(liquid)",'water(gas)',"air","Methane(gas)","Methane(liquid)",
                    'R134a(gas)','R134a(liquid)')  
comfluid1r.current(0)
comfluid1r.grid(row=0, column=1,sticky='nw',rowspan = 1)

tk.Label(frm_r,text='choose fluid(cold)   :').grid(row=1,column=0)
comvalue2r=tk.StringVar()
comfluid2r= ttk.Combobox(frm_r,textvariable=comvalue2r)
comfluid2r["value"]=("water(liquid)",'water(gas)',"air","Methane(gas)","Methane(liquid)",
                    'R134a(gas)','R134a(liquid)')  
comfluid2r.current(0)
comfluid2r.grid(row=1, column=1,sticky='nw')

tk.Label(frm_r,text='choose exchanger   :').grid(row=2,column=0)
extypevarr=tk.StringVar()
extyper= ttk.Combobox(frm_r,textvariable= extypevarr )
extyper["value"]=("parallel-flow",'counter-flow','tube-shell')   
extyper.current(0)
extyper.grid(row=2, column=1,sticky='nw')


varnshellr = tk.StringVar()
varnshellr.set('how many shells?')
entry_nshellr = tk.Entry(frm_r,textvariable = varnshellr)
entry_nshellr.grid(row=2, column=2)

var_entry_Tcir = tk.StringVar()
entry_Tcir = tk.Entry(frm_r,textvariable = var_entry_Tcir)
entry_Tcir.grid(row=3, column=1)
tk.Label(frm_r,text = 'Tci(℃):').grid(row=3)

var_entry_Tcor = tk.StringVar()
entry_Tcor = tk.Entry(frm_r,textvariable = var_entry_Tcor)
entry_Tcor.grid(row=4, column=1)
tk.Label(frm_r,text = 'Tco(℃):').grid(row=4)

var_entry_Thir = tk.StringVar()
entry_Thir = tk.Entry(frm_r,textvariable = var_entry_Thir)
entry_Thir.grid(row=5, column=1)
tk.Label(frm_r,text = 'Thi(℃):').grid(row=5)

var_entry_Thor = tk.StringVar()
entry_Thor = tk.Entry(frm_r,textvariable = var_entry_Thor)
entry_Thor.grid(row=6, column=1)
tk.Label(frm_r,text = 'Tho(℃):').grid(row=6)

var_entry_debithr = tk.StringVar()
entry_debithr = tk.Entry(frm_r,textvariable = var_entry_debithr)
entry_debithr.grid(row=7, column=1)
tk.Label(frm_r,text = 'mass flow rate hot(kg/s):').grid(row=7)


var_entry_debitcr = tk.StringVar()
entry_debitcr = tk.Entry(frm_r,textvariable = var_entry_debitcr)
entry_debitcr.grid(row=8, column=1)
tk.Label(frm_r,text = 'mass flow rate cold(kg/s):').grid(row=8)

surface_var = tk.StringVar()
surface = tk.Entry(frm_r,textvariable = surface_var)
surface.grid(row=9, column=1)
tk.Label(frm_r,text = 'exchange surface(㎡):').grid(row=9)

diameter_var = tk.StringVar()
diameter = tk.Entry(frm_r,textvariable = diameter_var)
diameter.grid(row=10, column=1)
tk.Label(frm_r,text = 'tube diameter of hot  side and cold side (m):').grid(row=10)

diameter_var2 = tk.StringVar()
diameter2 = tk.Entry(frm_r,textvariable = diameter_var2)
diameter2.grid(row=10, column=2)
tk.Label(frm_r,text = ' :').grid(row=10)

shell_diameter_var = tk.StringVar()
shell_diameter = tk.Entry(frm_r,textvariable = shell_diameter_var)
shell_diameter.grid(row=11, column=1)
tk.Label(frm_r,text = 'shell diameter(m):').grid(row=11)


baffle_distance_var = tk.StringVar()
baffle_distance = tk.Entry(frm_r,textvariable = baffle_distance_var)
baffle_distance.grid(row=12, column=1)
tk.Label(frm_r,text = 'baffle distance(m):').grid(row=12)


def effec(NTU,C,extype):
    #extype = extypevar.get()
    if C > 1:
        raise Exception('Heat capacity rate must be less than 1 by definition.')
        
    if extype == 'counter-flow':
        if C < 1:
            return (1. - math.exp(-NTU*(1. - C)))/(1. - C*math.exp(-NTU*(1. - C)))
        elif C == 1:
            return NTU/(1. + NTU)
    elif extype == 'parallel-flow':
            return (1. - math.exp(-NTU*(1. + C)))/(1. + C)
    elif extype == 'tube-shell':
        shells = int(varnshellr.get())
        NTU = NTU/shells
        top = 1. + math.exp(-NTU*(1. + C**2)**.5)
        bottom = 1. - math.exp(-NTU*(1. + C**2)**.5)
        effectiveness = 2./(1. + C + (1. + C**2)**.5*top/bottom)
        if shells > 1:
            term = ((1. - effectiveness*C)/(1. - effectiveness))**shells
            effectiveness = (term - 1.)/(term - C)
        return effectiveness

def pdtube(m,mu,pho,D,A):
    L= A/math.pi/D
    v= 4*m/(pho*math.pi*D**2)
    Re=pho*v*D/mu
    if (Re<3000):
        f=16/Re
    else:
        f=math.pow(1.58*math.log(Re)-3.28,-2);
    deltaP=4*f*L/D*pho/2*pow(v,2)
    return deltaP

def pdtubeshell(mh,mc,mu,phoh,phoc,Dt,Dc,Db,A):
    Pt=1.25*Dt
    Nt=math.ceil(math.pi/4*0.9*pow(Dc,2)/pow(Pt,2))
    v=mh/phoh/Dc/Db/(Pt-Dt)*Pt
    De=4*(pow(Pt,2)-(math.pi/4*pow(Dt,2)))/(math.pi*Dt)
    Re=phoh*v*De/mu
    fh=math.exp(0.567-0.19*math.log(Re))
    L=A/Nt/math.pi/Dt
    vc=mc/phoc/math.pi/pow(Dt,2)*4
    Rec=phoc*vc*Dt/mu
    if (Rec<3000):
        f=16/Rec
    else:
        f=math.pow(1.58*math.log(Rec)-3.28,-2)
    deltaPc=Nt*4*f*L/Dt*phoc/2*pow(vc,2)
    deltaPh=(Nt+1)*fh*Dc*phoh/2*pow(v,2)/De
    return deltaPc,deltaPh
    
def temp():
    global fig,canvas,A,phoh,phoc,mh,mc
    mu= 0.00053
    U= 1000
    A = isfloat(surface_var.get())
    p = 101325
    fluidh = comvalue1.get()
    fluidc = comvalue2.get()
    Tci = isfloat(var_entry_Tcir.get())
    Tco = isfloat(var_entry_Tcor.get())
    Thi = isfloat(var_entry_Thir.get())
    Tho = isfloat(var_entry_Thor.get())
    mh = isfloat(var_entry_debithr.get())
    mc = isfloat(var_entry_debitcr.get())
    Dt = isfloat(diameter_var.get())
    Dt2 = isfloat(diameter_var2.get())
    Dc = isfloat(shell_diameter_var.get())
    Db = isfloat(baffle_distance_var.get())
    extype = extypevarr.get()
    qh = fluidstate(fluidh)
    qc = fluidstate(fluidc)   
    Cph = prp.PropsSI('C','P',p,'Q',qh,fluid(fluidh))
    Cpc = prp.PropsSI('C','P',p,'Q',qc,fluid(fluidc))
    phoh = prp.PropsSI('D','P',p,'Q',qh,fluid(fluidh))
    phoc = prp.PropsSI('D','P',p,'Q',qc,fluid(fluidc))
    Cmin = min(mh*Cph,mc*Cpc)
    Cmax = max(mh*Cph,mc*Cpc)
    C = Cmin/Cmax
    NTUU = U*A/Cmin
    effectiveness = effec(NTUU, C, extype)
    possible_inputs = [(Tci, Thi), (Tci, Tho), (Tco, Thi), (Tco, Tho)]
    if not any([i for i in possible_inputs if None not in i]):
        tk.messagebox.showinfo('!','One set of (Tci, Thi), (Tci, Tho), (Tco, Thi), or (Tco, Tho) are required along with UA.')
        raise Exception('One set of (Tci, Thi), (Tci, Tho), (Tco, Thi), or (Tco, Tho) are required along with UA.')
    if Thi and Tci:
        Q = effectiveness*Cmin*(Thi - Tci)
    elif Tho and Tco :
        Q = effectiveness*Cmin*Cpc*Cph*(Tco - Tho)/(effectiveness*Cmin*(Cpc+Cph) - Cph*Cpc)
    elif Thi and Tco:
        Q = Cmin*Cpc*effectiveness*(Tco-Thi)/(effectiveness*Cmin - Cpc)
    elif Tho and Tci:
        Q = Cmin*Cph*effectiveness*(Tci-Tho)/(effectiveness*Cmin - Cph)

    if Tci and not Tco:
        Tco = Tci + Q/(Cpc)
    else:
        Tci = Tco - Q/(Cpc)
    if Thi and not Tho:
        Tho = Thi - Q/(Cph)
    else:
        Thi = Tho + Q/(Cph)  
    dr(Thi,Tho,Tci,Tco,extype)
    print(extype)
    if extype=='parallel-flow' or extype=='counter-flow':
        pressuredroph=pdtube(mh,mu,phoh,Dt,A)
        pressuredropc=pdtube(mc,mu,phoc,Dt2,A)
        # tk.messagebox.showinfo('Result','Tci: {:.1f}℃ ,Tco: {:.1f}℃  ,Thi: {:.1f}℃  ,Tho: {:.1f}℃ \n \
        #         the pressure drop of hot fluid is {:.2f} Pa\n \
        #         the pressure drop of cold fluid is {:.2f} Pa' .format(Tci,Tco,Thi,Tho,pressuredroph,pressuredropc))
    else:
        (pressuredropc,pressuredroph)=pdtubeshell(mh,mc,mu,phoh,phoc,Dt,Dc,Db,A)
    tk.messagebox.showinfo('Result','Tci: {:.1f}℃ ,Tco: {:.1f}℃  ,Thi: {:.1f}℃  ,Tho: {:.1f}℃ \n \
                           the pressure drop of hot fluid is {:.2f} Pa\n \
                           the pressure drop of cold fluid is {:.2f} Pa'.format(Tci,Tco,Thi,Tho,pressuredroph,pressuredropc))

btn_compute_r = tk.Button(frm_r,text='compute',command = temp).grid(row=13)
window.mainloop()



