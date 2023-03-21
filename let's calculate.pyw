#modules  imported---------------------------------------------------------------------------------------------------------
#pre-defined---------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import math
import tkinter.ttk as ttk
import mysql.connector
import matplotlib.pyplot as py
import pandas as pd
#created ------------------------------------------------------------------------------------------------------------------
from module.functions import *
from module.Currency_data_download import*
from module.Xml_and_Csv_to_Mysql_convertor import *
from module.theme_data import *
#--------------------------------------------------------------------------------------------------------------------------
#theme data----------------------------------------------------------------------------------------------------------------
try:
    loc_data = pd.read_csv('resources\locus.csv')
except:
    create_locus_csv()
    loc_data = pd.read_csv('resources\locus.csv')

geo = loc_data.iloc[0][0]
#--------------------------------------------------------------------------------------------------------------------------
#Main window---------------------------------------------------------------------------------------------------------------
window = Tk()
window.geometry(geo)
window.wait_visibility(window)
window.wm_attributes("-alpha",0.9)
window.title("Calculater")
window_icon = PhotoImage(file = 'resources\icons and photos\Calculater_icon(16x16).png')
window.iconphoto(False, window_icon)
#--------------------------------------------------------------------------------------------------------------------------
#Manage Theme -------------------------------------------------------------------------------------------------------------
try:
    thm = pd.read_csv('resources/theme.csv')
    
except:
    create_data()
    thm = pd.read_csv('resources/theme.csv')

thm = thm.iloc[0]
thm = list(thm)

a = thm[0]
b = "\ "
b = b[0]
a = b + a
#--------------------------------------------------------------------------------------------------------------------------
#images ------------------------------------------------------------------------------------------------------------------
graph_page = PhotoImage(file = 'resources\icons and photos\graph_choice.png')
graph_start = PhotoImage(file = 'resources\loading\Begain_graph.png')
plot_but_image = PhotoImage(file = 'resources\icons and photos\plot_but.png')
About_slider = PhotoImage(file = 'resources\icons and photos\slider.png')
About_page_img = PhotoImage(file="resources\icons and photos\About.png")
About_head =PhotoImage(file="resources\icons and photos\head.png")
theme_base = PhotoImage(file="resources\loading\Theme.png")
theme_head = PhotoImage(file="resources\icons and photos\Theme_head.png")
theme_back_but_image = PhotoImage(file="resources\icons and photos\Back_but_image.png")
thm1 = PhotoImage(file="resources\Themes\dark theme\Thm.png")
thm2 = PhotoImage(file="resources\Themes\light theme\Thm.png")
thm3 = PhotoImage(file="resources\Themes\Butterfly theme\Thm.png")
thm4 = PhotoImage(file="resources\Themes\Fruit theme\Thm.png")
thm5 = PhotoImage(file="resources\Themes\Forest theme\Thm.png")
thm6 = PhotoImage(file="resources\Themes\Vector theme\Thm.png")
thm7 = PhotoImage(file="resources\Themes\Wooden theme\Thm.png")
#calculater buttons---------------------------------------------------------------------------------------------------
sd_back_space_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\Back_space.png')
sd_head = PhotoImage(file = 'resources\Themes' + a + '\Standard\head.png')
sd_clear_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\clear.png')
sd_bracket_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\Bracket.png')
sd_divide_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\divide.png')
sd_multi_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\mult.png')
sd_add_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\Add.png')
sd_subtr_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\subtr.png')
sd_equal_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\equal.png')
sd_s0_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\S0.png')
sd_s1_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\S1.png')
sd_s2_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\S2.png')
sd_s3_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\S3.png')
sd_s4_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\S4.png')
sd_s5_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\S5.png')
sd_s6_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\S6.png')
sd_s7_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\S7.png')
sd_s8_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\S8.png')
sd_s9_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\S9.png')
sd_ss_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\Ss.png')
sd_point_image = PhotoImage(file = 'resources\Themes' + a + '\Standard\point.png')
sdback = PhotoImage(file = 'resources\Themes' + a + '\Standard\standard.png')
clear_hist = PhotoImage(file = 'resources\icons and photos\clear_hist.png')
hist_img = PhotoImage(file = 'resources\icons and photos\hist.png')
#---------------------------------------------------------------------------------------------------------------------
#slider button -------------------------------------------------------------------------------------------------------
slider_image = PhotoImage(file = 'resources\Themes' + a + '\Basic comp\Slider_image.png')
his_image = PhotoImage(file = 'resources\Themes' + a + '\Basic comp\History.png')
base = PhotoImage(file="resources\Themes" + a + "\Basic comp\Base.png")
Standard_img = PhotoImage(file="resources\PannelButton\Standard.png")
Scientific_img = PhotoImage(file="resources\PannelButton\Scientific.png")
Programmer_img = PhotoImage(file="resources\PannelButton\Programmer.png")
Currency_img = PhotoImage(file="resources\PannelButton\Currency.png")
Volume_img = PhotoImage(file="resources\PannelButton\Volume.png")
Length_img = PhotoImage(file="resources\PannelButton\Length.png")
Weight_and_Mass_img = PhotoImage(file="resources\PannelButton\Weight and Mass.png")
Temperature_img = PhotoImage(file="resources\PannelButton\Temperature.png")
Energy_img = PhotoImage(file="resources\PannelButton\Energy.png")
Area_img = PhotoImage(file="resources\PannelButton\Area.png")
Speed_img = PhotoImage(file="resources\PannelButton\Speed.png")
Time_img = PhotoImage(file="resources\PannelButton\Time.png")
Data_img = PhotoImage(file="resources\PannelButton\Data.png")
Power_img = PhotoImage(file="resources\PannelButton\Power.png")
Pressure_img = PhotoImage(file="resources\PannelButton\Pressure.png")
Angle_img = PhotoImage(file="resources\PannelButton\Angle.png")
cal_image = PhotoImage(file="resources\PannelButton\CAL.png")
con_image = PhotoImage(file="resources\PannelButton\conver.png")
About_img = PhotoImage(file="resources\PannelButton\About.png")
slider_close_image = PhotoImage(file="resources\Themes" + a + "\Basic comp\slider_close.png")
Theme_but_image = PhotoImage(file="resources\PannelButton\Themes.png")
#---------------------------------------------------------------------------------------------------------------------
#scientific Button----------------------------------------------------------------------------------------------------
sc_back_space_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Back_space.png')
sc_head = PhotoImage(file = 'resources\Themes' + a + '\stientific\head.png')
sc_clear_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\clear.png')
sc_bracket_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Bracket.png')
sc_divide_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\divide.png')
sc_multi_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\mult.png')
sc_add_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Add.png')
sc_subtr_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\subtr.png')
sc_equal_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\equal.png')
sc_s0_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\S0.png')
sc_s1_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\S1.png')
sc_s2_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\S2.png')
sc_s3_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\S3.png')
sc_s4_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\S4.png')
sc_s5_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\S5.png')
sc_s6_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\S6.png')
sc_s7_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\S7.png')
sc_s8_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\S8.png')
sc_s9_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\S9.png')
sc_ss_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Ss.png')
sc_point_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\point.png')
scback = PhotoImage(file = 'resources\Themes' + a + '\stientific\scientific.png')
swap_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\swap.png')
rad_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Rad.png')
deg_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Deg.png')
root_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Root.png')
cuberoot_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\cuberoot.png')
sin_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\sin.png')
cos_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\cos.png')
tan_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Tan.png')
ln_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\ln.png')
log_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\log.png')
rec_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Bix.png')
ex_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\ex.png')
x2_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\X2.png')
xy_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Xy.png')
mod_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\mod.png')
pi_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\pi.png')
e_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\e.png')
asin_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Asin.png')
acos_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Acos.png')
atan_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Atan.png')
sinh_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\sinh.png')
cosh_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\cosh.png')
tanh_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Tanh.png')
asinh_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Asinh.png')
acosh_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Acosh.png')
atanh_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\Atanh.png')
exp2_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\exp2.png')
x3_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\X3.png')
xf_image = PhotoImage(file = 'resources\Themes' + a + '\stientific\X!.png')
#PROGRAMMING BUTTONS-----------------------------------------------------------------------------------------------------
pr_back_space_image = PhotoImage(file = 'resources\Themes' + a + '\programming\Back_space.png')
pr_head = PhotoImage(file = 'resources\Themes' + a + '\programming\head.png')
pr_clear_image = PhotoImage(file = 'resources\Themes' + a + '\programming\clear.png')
A_image = PhotoImage(file = 'resources\Themes' + a + '\programming\A.png')
B_image = PhotoImage(file = 'resources\Themes' + a + '\programming\B.png')
C_image = PhotoImage(file = 'resources\Themes' + a + '\programming\C.png')
D_image = PhotoImage(file = 'resources\Themes' + a + '\programming\D.png')
E_image = PhotoImage(file = 'resources\Themes' + a + '\programming\EE_.png')
F_image = PhotoImage(file = 'resources\Themes' + a + '\programming\F.png')
prback = PhotoImage(file = 'resources\Themes' + a + '\programming\programming.png')
pr_equal_image = PhotoImage(file = 'resources\Themes' + a + '\programming\equal.png')
pr_s0_image = PhotoImage(file = 'resources\Themes' + a + '\programming\S0.png')
pr_s1_image = PhotoImage(file = 'resources\Themes' + a + '\programming\S1.png')
pr_s2_image = PhotoImage(file = 'resources\Themes' + a + '\programming\S2.png')
pr_s3_image = PhotoImage(file = 'resources\Themes' + a + '\programming\S3.png')
pr_s4_image = PhotoImage(file = 'resources\Themes' + a + '\programming\S4.png')
pr_s5_image = PhotoImage(file = 'resources\Themes' + a + '\programming\S5.png')
pr_s6_image = PhotoImage(file = 'resources\Themes' + a + '\programming\S6.png')
pr_s7_image = PhotoImage(file = 'resources\Themes' + a + '\programming\S7.png')
pr_s8_image = PhotoImage(file = 'resources\Themes' + a + '\programming\S8.png')
pr_s9_image = PhotoImage(file = 'resources\Themes' + a + '\programming\S9.png')
pr_ss_image = PhotoImage(file = 'resources\Themes' + a + '\programming\Ss.png')
Hex_image = PhotoImage(file = 'resources\Themes' + a + '\programming\H.png')
Oct_image = PhotoImage(file = 'resources\Themes' + a + '\programming\Oc.png')
Bin_image = PhotoImage(file = 'resources\Themes' + a + '\programming\Bi.png')
#convertor Buttton---------------------------------------------------------------------------------------------------------
back_space_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\Back_space.png')
head_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\head.png')
clear_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\clear.png')
equal_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\equal.png')
s0_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\S0.png')
s1_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\S1.png')
s2_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\S2.png')
s3_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\S3.png')
s4_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\S4.png')
s5_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\S5.png')
s6_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\S6.png')
s7_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\S7.png')
s8_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\S8.png')
s9_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\S9.png')
ss_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\Ss.png')
point_image = PhotoImage(file = 'resources\Themes' + a + '\convertor\point.png')
conback = PhotoImage(file = 'resources\Themes' + a + '\convertor\convertor.png')
#currency convertor Buttton---------------------------------------------------------------------------------------------------------
cr_back_space_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\Back_space.png')
cr_head = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\head.png')
cr_clear_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\clear.png')
cr_equal_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\equal.png')
cr_s0_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\S0.png')
cr_s1_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\S1.png')
cr_s2_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\S2.png')
cr_s3_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\S3.png')
cr_s4_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\S4.png')
cr_s5_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\S5.png')
cr_s6_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\S6.png')
cr_s7_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\S7.png')
cr_s8_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\S8.png')
cr_s9_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\S9.png')
cr_ss_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\Ss.png')
cr_point_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\point.png')
curback = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\currency_convertor.png')
upg_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\cur_data_upg.png')
graph_image = PhotoImage(file = 'resources\Themes' + a + '\currency convertor\graph.png')
#---------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
history_but = Button(window,image = his_image,bd=0,activebackground=thm[8])
hist = Label(window,image=hist_img)
#functing Variables----------------------------------------------------------------------------------------------------------------
opp = StringVar()
opp.set("standard")
oppf = StringVar()
oppf.set("standard")
#----------------------------------------------------------------------------------------------------------------------------------

#frames ---------------------------------------------------------------------------------------------------------------------
def slide_view():
    slide_view_frame = Frame(window,bg="#0d1528")
    #Button Functions--------------------------------------------------------------------------------------------------------------------
    def CalStand():
        opp.set("standard")
        oppf.set("standard")
        cal()
        
    def CalSci():
        opp.set("Scientific")
        oppf.set("Scientific")
        cal()

    def Calpro():
        opp.set("programming")
        oppf.set("programming")
        cal()

    def ConCurr():
        opp.set("currency")
        oppf.set("currency")
        cal()

    def ConLen():
        opp.set("length")
        oppf.set("length")
        cal()

    def ConVol():
        opp.set("volume")
        oppf.set("volume")
        cal()

    def ConTem():
        opp.set("temp")
        oppf.set("temp")
        cal()
        
    def ConWei():
        opp.set("weight")
        oppf.set("weight")
        cal()

    def ConEng():
        opp.set("energy")
        oppf.set("energy")
        cal()

    def ConAre():
        opp.set("area")
        oppf.set("area")
        cal()

    def ConSpe():
        opp.set("speed")
        oppf.set("speed")
        cal()
        
    def ConTim():
        opp.set("time")
        oppf.set("time")
        cal()

    def ConDat():
        opp.set("data")
        oppf.set("data")
        cal()

    def ConPow():
        opp.set("power")
        oppf.set("power")
        cal()

    def ConPre():
        opp.set("pressure")
        oppf.set("pressure")
        cal()
        
    def ConAng():
        opp.set("angle")
        oppf.set("angle")
        cal()

    def Abt():
        opp.set("about")
        oppf.set("about")
        cal()
    
    #------------------------------------------------------------------------------------------------------------------------------------
    
    canvas = Canvas(slide_view_frame,bg="#0d1528",bd=0,highlightthickness=0)
    astyle = ttk.Style(slide_view_frame)
    astyle.theme_use('clam')
    astyle.configure("Vertical.TScrollbar", gripcount=0,background="#00b0f0",darkcolor="#0d1528",lightcolor="#0d1528",troughcolor="#0d1528",bordercolor="#0d1528",arrowcolor="#0d1528")
    scroll_y = ttk.Scrollbar(slide_view_frame,orient="vertical", command=canvas.yview)

    frame = Frame(canvas,bg="#0d1528",bd=0)

    Calculater = Label(frame,image = cal_image,height=51,bg="#0d1528",bd=0).grid(row=0,column=0,columnspan=2)
    Standard = Button(frame, image=Standard_img,bd=0,command = CalStand,bg="#0d1528",height=238,width=115,activebackground="#0d1528").grid(row=1,column=0,rowspan=2,padx=2,pady=2)
    Scientific = Button(frame, image=Scientific_img,bd=0,command = CalSci,bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=1,column=1,padx=2,pady=2)
    Programmer = Button(frame, image=Programmer_img,bd=0,command = Calpro,bg="#0d1528",height=115,width=115,activebackground="#0d1528").grid(row=2,column=1,padx=2,pady=2)
    
    Convertor = Label(frame,image = con_image,height=51,bg="#0d1528",bd=0).grid(row=4,column=0,columnspan=2)
    Currency = Button(frame, image=Currency_img,bd=0,bg="#0d1528",height=115,width=234,activebackground="#0d1528",command=ConCurr).grid(row=5,column=0,columnspan=2,padx=2,pady=2)
    Volume = Button(frame, image=Volume_img,bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528",command=ConVol).grid(row=6,column=0,padx=2,pady=2)
    Length = Button(frame, image=Length_img,bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528",command=ConLen).grid(row=6,column=1,padx=2,pady=2)
    Weight_and_Mass = Button(frame, image=Weight_and_Mass_img,bd=0,bg="#0d1528",height=238,width=115,activebackground="#0d1528",command=ConWei).grid(row=7,column=0,rowspan=2,padx=2,pady=2)
    Temperature = Button(frame, image=Temperature_img,bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528",command=ConTem).grid(row=7,column=1,padx=2,pady=2)
    Energy = Button(frame, image=Energy_img,bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528",command=ConEng).grid(row=8,column=1,padx=2,pady=2)
    Area = Button(frame, image=Area_img,bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528",command=ConAre).grid(row=9,column=0,padx=2,pady=2)
    Speed= Button(frame, image=Speed_img,bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528",command=ConSpe).grid(row=9,column=1,padx=2,pady=2)
    Time = Button(frame, image=Time_img,bd=0,bg="#0d1528",height=115,width=234,activebackground="#0d1528",command=ConTim).grid(row=10,column=0,columnspan=2,padx=2,pady=2)
    Data = Button(frame, image=Data_img,bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528",command=ConDat).grid(row=11,column=0,padx=2,pady=2)
    Power= Button(frame, image=Power_img,bd=0,bg="#0d1528",height=238,width=115,activebackground="#0d1528",command=ConPow).grid(row=11,column=1,rowspan=2,padx=3,pady=2)
    Pressure = Button(frame, image=Pressure_img,bd=0,bg="#0d1528",height=238,width=115,activebackground="#0d1528",command=ConPre).grid(row=12,column=0,rowspan=2,padx=2,pady=2)
    Angle = Button(frame, image=Angle_img,bd=0,bg="#0d1528",height=115,width=115,activebackground="#0d1528",command=ConAng).grid(row=13,column=1,padx=2,pady=2)

    canvas.create_window(0, 0, anchor='nw', window=frame)

    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=scroll_y.set)
                         
    scroll_y.set(0.2,0.3)

    About = Button(slide_view_frame,image=About_img,bd=0,bg="#0d1528",activebackground="#0d1528",command=Abt)

    theme_but = Button(slide_view_frame,image=Theme_but_image,bd=0,bg="#0d1528",activebackground="#0d1528",command=theme_start)

    if oppf.get()== "currency":
        About.place(x=0,y=517,width=215,height=38)
        theme_but.place(x=218,y=515,width=38,height=38)
        canvas.place(x=0,y=9,height=503,width=244)
        scroll_y.place(x=244,y=9,height=503)
        slide_view_frame.place(x=0,y=40,height=555,width=260)

    elif oppf.get()== "programming":
        About.place(x=0,y=432,width=215,height=38)
        theme_but.place(x=218,y=430,width=38,height=38)
        canvas.place(x=0,y=9,height=418,width=244)
        scroll_y.place(x=244,y=9,height=418)
        slide_view_frame.place(x=0,y=40,height=470,width=260)
        
    else:
        About.place(x=0,y=472,width=215,height=38)
        theme_but.place(x=218,y=470,width=38,height=38)
        canvas.place(x=0,y=9,height=458,width=244)
        scroll_y.place(x=244,y=9,height=458)
        slide_view_frame.place(x=0,y=40,height=510,width=260)

    #----  ----  ----  ----   ----    ----    ----    ----    ----    ----    ----    ----    ----#
# Req ------------------------------------------------------------------------
n = StringVar()
n.set("Rad")
def sin(x):
    if n.get() == "Deg":
        res = round(math.sin(x),15)
    elif n.get() == "Rad" :
        res = round(math.sin(math.radians(x)),15)
    return res

def cos(x):
    if n.get() == "Deg":
        res = round(math.cos(x),15)
    elif n.get() == "Rad" :
        res = round(math.cos(math.radians(x)),15)
    return res

def tan(x):
    if n.get() == "Deg":
        if x%(math.pi/2)==0 and (x//(math.pi/2))%2!=0 :
            res = "Not Exist"
        else:
            res = round(math.tan(x),15)
    elif n.get() == "Rad" :
        if x%(90)==0 and (x//(90))%2!=0 :
            res = "Not Exist"
        else:
            res = round(math.tan(math.radians(x)),15)
    return res

def sinh(x):
    if n.get() == "Deg":
        res = round(math.sinh(x),15)
    elif n.get() == "Rad" :
        res = round(math.sinh(math.radians(x)),15)
    return res

def cosh(x):
    if n.get() == "Deg":
        res = round(math.cosh(x),15)
    elif n.get() == "Rad" :
        res = round(math.cosh(math.radians(x)),15)
    return res

def tanh(x):
    if n.get() == "Deg":
        res = round(math.tanh(x),15)
    elif n.get() == "Rad" :
        res = round(math.tanh(math.radians(x)),15)
    return res

def asin(x):
    if n.get() == "Deg":
        res = round(math.asin(x),15)
    elif n.get() == "Rad" :
        res = round(math.degrees(math.asin(x)),15)
    return res

def acos(x):
    if n.get() == "Deg":
        res = round(math.cos(x),15)
    elif n.get() == "Rad" :
        res = round(math.degrees(math.cos(x)),15)
    return res

def atan(x):
    if n.get() == "Deg":
        res = round(math.tan(x),15)
    elif n.get() == "Rad" :
        res = round(math.degrees(math.tan(x)),15)
    return res

def asinh(x):
    if n.get() == "Deg":
        res = round(math.sinh(x),15)
    elif n.get() == "Rad" :
        res = round(math.degrees(math.sinh(x)),15)
    return res

def acosh(x):
    if n.get() == "Deg":
        res = round(math.cosh(x),15)
    elif n.get() == "Rad" :
        res = round(math.degrees(math.cosh(x)),15)
    return res

def atanh(x):
    if n.get() == "Deg":
        res = round(math.tanh(x),15)
    elif n.get() == "Rad" :
        res = round(math.degrees(math.tanh(x)),15)
    return res

def fac(x):
    res = math.factorial(x)
    return res

def sqr(x):
    res = round(x**(1/2),15)
    return res

def cur(x):
    res = round(x**(1/3),15)
    return res

def abs(x):
    if x < 0 :
        res = round(x*(-1),15)
    else:
        res = round(x,15)
    return res

# ----------------------------------------------------------------------------
def standard_calculater():
    standard_frame = Frame(window)
    backlabel = Label(standard_frame,image = sdback)
    backlabel.place(height=510,width=340)

    fxn_list=["÷","ᵡ"]
    replacement_list=["/","*"]

    displayf = StringVar()
    displayf_view = Label(standard_frame, font=('Bookman Old Style',12), justify='right', textvariable = displayf,bg=thm[3],fg=thm[4])
    displayf_view.place(width=313,height=25, y=32,x=13)
     
    display = StringVar()
    display_view = Entry(standard_frame, font=('Bookman Old Style',30),bg=thm[1], justify='right',bd=0, textvariable = display,fg=thm[2])
    display_view.place(width=294,height=50,x=23, y=78)

    sd_his = StringVar()
    sd_his.set("OFF")

    hist.place(x=340,height=40,width=360)
    #History open---------------------------------------------  
    def sd_history_open():
        if sd_his.get() == "OFF":
            sd_his.set("ON")
            window.maxsize(700,550)
            window.minsize(700,550)
        elif sd_his.get() == "ON":
            sd_his.set("OFF")
            window.maxsize(340,550)
            window.minsize(340,550)
    #------------------------------------------------------------
    history_but.configure(command=sd_history_open)
    history_but.place(x=280,y=0,width=60,height=40)
    #History window-------------------------------------------------------------
    def history():
        sd_canvas = Canvas(standard_frame,bg="#0d1528",bd=0,highlightthickness=0)
        sd_style = ttk.Style(standard_frame)
        sd_style.theme_use('clam')
        sd_style.configure("Vertical.TScrollbar", gripcount=0,background="#00b0f0",darkcolor="#0d1528",lightcolor="#0d1528",troughcolor="#0d1528",bordercolor="#0d1528",arrowcolor="#0d1528")
        sd_scroll_y = ttk.Scrollbar(standard_frame,orient="vertical", command=sd_canvas.yview)

        sd_frame = Frame(sd_canvas,bg="#0d1528",bd=0)
        mycursor.execute("SELECT * FROM standard_history")
        myresult = mycursor.fetchall()
        q = []
        s = []
        for x in myresult:
            alpha = x[1]
            for i,j in zip(fxn_list,replacement_list):
                alp = alpha.replace(j,i)
            Button(sd_frame,bg="#0d1528",fg="white",font=('Bookman Old Style',10),width=43,bd=0,text=alp,activebackground="#0d1528",command = lambda a=alp : display.set(display.get() + a)).pack()
            Button(sd_frame,bg="#0d1528",fg="cyan",font=('Bookman Old Style',20),width=20,bd=0,text=x[2],activebackground="#0d1528",command = lambda a=x[2] : display.set(display.get() + a)).pack()

        sd_canvas.create_window(0, 0, anchor='nw', window=sd_frame)

        sd_canvas.update_idletasks()

        sd_canvas.configure(scrollregion=sd_canvas.bbox('all'),yscrollcommand=sd_scroll_y.set)

        def clear_his():
            mycursor.execute("DELETE FROM standard_history ")
            mydb.commit()
            List = sd_frame.pack_slaves()
            for I in List:
                I.destroy()

        clear_hist_but = Button(standard_frame,bg="#0D1528",activebackground="#0D1528",bd=0,image=clear_hist,command=clear_his)
        clear_hist_but.place(x=340,y=465,height=45,width=360)
                             
        sd_canvas.place(x=340,y=0,height=465,width=360)
        sd_scroll_y.place(x=682,y=0,height=465)
        sd_scroll_y.set(0.2,0.3)
    history()
    #---------------------------------------------------------------------------

    #button Functions ----------------------------------------------------------------------------------------------------------
    def bracket():
        bracket_fxn(standard_frame,display)

    def equal():
        if displayf.get() != "":
            equal_fxn(standard_frame,display,fxn_list,replacement_list,displayf)
            ques = displayf.get()
            for i,j in zip(fxn_list,replacement_list):
                ques_ = ques.replace(i,j)
            sol_ = display.get()
            val = (ques_,sol_)
            mycursor.execute(sdi, val)
            mydb.commit()
            history()        

    def clear():
        claer_fxn(standard_frame,display,displayf)
                
    def back_space():
        back_space_fxn(standard_frame,display)
                
    def divide():
        divide_fxn(standard_frame,display,displayf,14)
        
    def multi():
        multi_fxn(standard_frame,display,displayf,14)
                
    def add():
        add_fxn(standard_frame,display,displayf,14)
                
    def subtract():
        subtract_fxn(standard_frame,display,displayf,14)
                
    def seven():
        seven_fxn(standard_frame,display,14)
                
    def eaight():
        eaight_fxn(standard_frame,display,14)
                
    def nine():
        nine_fxn(standard_frame,display,14)
                
    def four():
        four_fxn(standard_frame,display,14)
                
    def five():
        five_fxn(standard_frame,display,14)
                
    def six():
        six_fxn(standard_frame,display,14)
                
    def one():
        one_fxn(standard_frame,display,14)
                
    def two():
        two_fxn(standard_frame,display,14)
                
    def three():
        three_fxn(standard_frame,display,14)
                
    def ss():
        ss_fxn(standard_frame,display)
                   
    def zero():
        zero_fxn(standard_frame,display,14)
                  
    def point():
        point_fxn(standard_frame,display,14)

    #-------------------------------------------------------------------------------------------------------------------------
        
    clear_but=Button(standard_frame,image = sd_clear_image,bd=0,command=clear,activebackground=thm[5])
    clear_but.place(y=160,x=0 ,width=85,height=70)
    bracket_but=Button(standard_frame,image = sd_bracket_image,bd=0,command=bracket,activebackground=thm[5])
    bracket_but.place(y=160,x=85 ,width=85,height=70)
    back_space_but=Button(standard_frame,image = sd_back_space_image,bd=0,command=back_space,activebackground=thm[5])
    back_space_but.place(y=160,x=170 ,width=85,height=70)
    divide_but=Button(standard_frame,image = sd_divide_image,bd=0,command=divide,activebackground=thm[5])
    divide_but.place(y=160,x=255 ,width=85,height=70)
        
    seven_but=Button(standard_frame,image = sd_s7_image,bd=0,command=seven,activebackground=thm[5])
    seven_but.place(y=230,x=0 ,width=85,height=70)
    eaight_but=Button(standard_frame,image = sd_s8_image,bd=0,command=eaight,activebackground=thm[5])
    eaight_but.place(y=230,x=85 ,width=85,height=70)
    nine_but=Button(standard_frame,image = sd_s9_image,bd=0,command=nine,activebackground=thm[5])
    nine_but.place(y=230,x=170 ,width=85,height=70)
    multi_but=Button(standard_frame,image = sd_multi_image,bd=0,command=multi,activebackground=thm[5])
    multi_but.place(y=230,x=255 ,width=85,height=70)
    
    four_but=Button(standard_frame,image = sd_s4_image,bd=0,command=four,activebackground=thm[5])
    four_but.place(y=300,x=0 ,width=85,height=70)
    five_but=Button(standard_frame,image = sd_s5_image,bd=0,command=five,activebackground=thm[5])
    five_but.place(y=300,x=85 ,width=85,height=70)
    six_but=Button(standard_frame,image = sd_s6_image,bd=0,command=six,activebackground=thm[5])
    six_but.place(y=300,x=170 ,width=85,height=70)
    add_but=Button(standard_frame,image = sd_add_image,bd=0,command=add,activebackground=thm[5])
    add_but.place(y=300,x=255 ,width=85,height=70)
    
    one_but=Button(standard_frame,image = sd_s1_image,bd=0,command=one,activebackground=thm[5])
    one_but.place(y=370,x=0 ,width=85,height=70)
    two_but=Button(standard_frame,image = sd_s2_image,bd=0,command=two,activebackground=thm[5])
    two_but.place(y=370,x=85 ,width=85,height=70)
    three_but=Button(standard_frame,image = sd_s3_image,bd=0,command=three,activebackground=thm[5])
    three_but.place(y=370,x=170 ,width=85,height=70)
    subtract_but=Button(standard_frame,image = sd_subtr_image,bd=0,command=subtract,activebackground=thm[5])
    subtract_but.place(y=370,x=255 ,width=85,height=70)
    
    ss_but=Button(standard_frame,image = sd_ss_image,bd=0,command=ss,activebackground=thm[5])
    ss_but.place(y=440,x=0 ,width=85,height=70)
    zero_but=Button(standard_frame,image = sd_s0_image,bd=0,command=zero,activebackground=thm[5])
    zero_but.place(y=440,x=85 ,width=85,height=70)
    point_but=Button(standard_frame,image = sd_point_image,bd=0,command=point,activebackground=thm[5])
    point_but.place(y=440,x=170 ,width=85,height=70)
    equal_but=Button(standard_frame,image = sd_equal_image,bd=0,command=equal,activebackground=thm[5])
    equal_but.place(y=440,x=255 ,width=85,height=70)

    standard_frame.place(x=0,y=40,height=510,width=700)

    #----  ----  ----  ----   ----    ----    ----    ----    ----    ----    ----    ----    ----#

def Scientific_Calculater():
    scientific_frame = Frame(window)
    backlabel = Label(scientific_frame,image=scback)
    backlabel.place(height=510,width=595)

    fxn_list=["÷","^","ᵡ","e","ᴨ","³√(","√("]
    replacement_list=["/","**","*","2.718281828459045","3.141592653589793","cur(","sqr("]

    switchvar = StringVar()
    switchvar.set("s1")
     
    displayf = StringVar()
    displayf_view = Label(scientific_frame, font=('Bookman Old Style',12), textvariable = displayf,bd=0,bg=thm[3],fg=thm[4])
    displayf_view.place(width=568,height=25,x=13, y=32)
     
    display = StringVar()
    display_view = Entry(scientific_frame, font=('Bookman Old Style',30), justify='right', textvariable = display,bd=0,bg=thm[1],fg=thm[2])
    display_view.place(width=549,height=50,x=23,y=78)

    sc_his = StringVar()
    sc_his.set("OFF")

    hist.place(x=595,height=40,width=360)
    #History open----------------------------------------------
        
    def sc_history_open():
        if sc_his.get() == "OFF":
            sc_his.set("ON")
            window.maxsize(955,550)
            window.minsize(955,550)
        elif sc_his.get() == "ON":
            sc_his.set("OFF")
            window.maxsize(595,550)
            window.minsize(595,550)
    #------------------------------------------------------------
    history_but.configure(command=sc_history_open)
    history_but.place(x=535,y=0)
    #History window-------------------------------------------------------------
    def history():
        sc_canvas = Canvas(scientific_frame,bg="#0D1528",bd=0,highlightthickness=0)
        sc_style = ttk.Style(scientific_frame)
        sc_style.theme_use('clam')
        sc_style.configure("Vertical.TScrollbar", gripcount=0,background="#00b0f0",darkcolor="#0d1528",lightcolor="#0d1528",troughcolor="#0d1528",bordercolor="#0d1528",arrowcolor="#0d1528")
        sc_scroll_y = ttk.Scrollbar(scientific_frame,orient="vertical", command=sc_canvas.yview)

        sc_frame = Frame(sc_canvas,bg="#0D1528",bd=0)

        mycursor.execute("SELECT * FROM scientific_history")
        myresult = mycursor.fetchall()
        for x in myresult:
            alpha = x[1]
            for i,j in zip(fxn_list,replacement_list):
                alpha = alpha.replace(j,i)
            alp = alpha
            Button(sc_frame,bg="#0D1528",fg="white",font=('Bookman Old Style',10),width=43,bd=0,text=alp,activebackground="#0D1528",command = lambda a=alp : display.set(display.get() + a)).pack()
            Button(sc_frame,bg="#0D1528",fg="cyan",font=('Bookman Old Style',20),width=20,bd=0,text=x[2],activebackground="#0D1528",command = lambda a=x[2] : display.set(display.get() + a)).pack()

        sc_canvas.create_window(0, 0, anchor='nw', window=sc_frame)

        sc_canvas.update_idletasks()

        sc_canvas.configure(scrollregion=sc_canvas.bbox('all'),yscrollcommand=sc_scroll_y.set)
        def clear_his():
            mycursor.execute("DELETE FROM scientific_history ")
            mydb.commit()
            List = sc_frame.pack_slaves()
            for I in List:
                I.destroy()

        clear_hist_but = Button(scientific_frame,bg="#0D1528",activebackground="#0D1528",bd=0,image=clear_hist,command=clear_his)
        clear_hist_but.place(x=595,y=465,height=45,width=360)
                             
        sc_canvas.place(x=595,y=0,height=465,width=345)
        sc_scroll_y.place(x=939,y=0,height=465)
        sc_scroll_y.set(0.2,0.3)

    history()
    #---------------------------------------------------------------------------
        
    #----------------------------------------------------------------------

    
    #button Functions ----------------------------------------------------------------------------------------------------------
    def bracket():
        bracket_fxn(scientific_frame,display)

    def equal():
        icale = display.get()
        icalf = displayf.get()
        ical = icalf + icale
        displayf.set(ical)
        if ical == "":
                None
        else:
                for a,b in zip(fxn_list,replacement_list):
                        ical = ical.replace(a,b)
                       
                try:
                    result = eval(ical)
                except:
                    result = "Error"
                display.set(result)
        ques = displayf.get()
        for i,j in zip(fxn_list,replacement_list):
            ques = ques.replace(i,j)
        ques_ = ques
        sol_ = display.get()
        val = (ques_,sol_)
        mycursor.execute(sci, val)
        mydb.commit()
        history()

    def clear():
        claer_fxn(scientific_frame,display,displayf)
                
    def back_space():
        back_space_fxn(scientific_frame,display)
                
    def divide():
        divide_fxn(scientific_frame,display,displayf,25)
        
    def multi():
        multi_fxn(scientific_frame,display,displayf,25)
                
    def add():
        add_fxn(scientific_frame,display,displayf,25)
                
    def subtract():
        subtract_fxn(scientific_frame,display,displayf,25)
                
    def seven():
        seven_fxn(scientific_frame,display,25)
                
    def eaight():
        eaight_fxn(scientific_frame,display,25)
                
    def nine():
        nine_fxn(scientific_frame,display,25)
                
    def four():
        four_fxn(scientific_frame,display,25)
                
    def five():
        five_fxn(scientific_frame,display,25)
                
    def six():
        six_fxn(scientific_frame,display,25)
                
    def one():
        one_fxn(scientific_frame,display,25)
                
    def two():
        two_fxn(scientific_frame,display,25)
                
    def three():
        three_fxn(scientific_frame,display,25)
                
    def ss():
        ss_fxn(scientific_frame,display)
                   
    def zero():
        zero_fxn(scientific_frame,display,25)
                  
    def point():
        point_fxn(scientific_frame,display,25)

    def root():   
        root_fxn(window,display,25)
        
    def sine():    
        sine_fxn(window,display,25)
        
    def cosine():    
        cosine_fxn(window,display,25)
        
    def tangent():   
        tangent_fxn(window,display,25)
        
    def log_e():     
        log_e_fxn(window,display,25)
        
    def log_10():   
        log_10_fxn(window,display,25)
        
    def reciprocal():   
        reciprocal_fxn(window,display)
        
    def exponencial():   
        exponencial_fxn(window,display,25)
        
    def square():    
        square_but_fxn(window,display,25)

    def x_y():    
        x_y_fxn(window,display,25)

    def modulus():     
        modulus_fxn(window,display)

    def pie():    
        pie_fxn(window,display,25)

    def nepions(): 
        nepions_fxn(window,display,25)

    def cuberoot():     
        cuberoot_fxn(window,display,25)

    def sin_itf():     
        sin_itf_fxn(window,display,25)

    def cos_itf():    
        cos_itf_fxn(window,display,25)

    def tan_itf():    
        tan_itf_fxn(window,display,25)

    def hyperbolic_sin():   
        hyperbolic_sin_fxn(window,display,25)

    def hyperbolic_cos():    
        hyperbolic_cos_fxn(window,display,25)

    def hyperbolic_tan(): 
        hyperbolic_tan_fxn(window,display,25)

    def hyperbolic_sin_itf():     
        hyperbolic_sin_itf_fxn(window,display,25)

    def hyperbolic_cos_itf():   
        hyperbolic_cos_itf_fxn(window,display,25)

    def hyperbolic_tan_itf():   
        hyperbolic_tan_itf_fxn(window,display,25)

    def two_x():     
        two_x_fxn(window,display,25)

    def cube():    
        cube_fxn(window,display,25)

    def factorial_x():    
        factorial_x_fxn(window,display,25)

    def scientific_button():
        if switchvar.get() == "s1":
            #1
            cuberoot_but.place(x=-85,y=160,width=85,height=70)
            #2
            sin_itf_but.place(x=-255,y=230,width=85,height=70)
            cos_itf_but.place(x=-170,y=230,width=85,height=70)
            tan_itf_but.place(x=-85,y=230,width=85,height=70)
            #3
            hyperbolic_sin_but.place(x=-255,y=300,width=85,height=70)
            hyperbolic_cos_but.place(x=-170,y=300,width=85,height=70)
            hyperbolic_tan_but.place(x=-85,y=300,width=85,height=70)
            #4
            hyperbolic_sin_itf_but.place(x=-255,y=370,width=85,height=70)
            hyperbolic_cos_itf_but.place(x=-170,y=370,width=85,height=70)
            hyperbolic_tan_itf_but.place(x=-85,y=370,width=85,height=70)
            #5
            two_x_but.place(x=-255,y=440,width=85,height=70)
            cube_but.place(x=-170,y=440,width=85,height=70)
            factorial_x_but.place(x=-85,y=440,width=85,height=70)
            #1
            root_but.place(x=170,y=160,width=85,height=70)
            #2
            sine_but.place(x=0,y=230,width=85,height=70)
            cosine_but.place(x=85,y=230,width=85,height=70)
            tangent_but.place(x=170,y=230,width=85,height=70)
            #3
            log_e_but.place(x=0,y=300,width=85,height=70)
            log_10_but.place(x=85,y=300,width=85,height=70)
            reciprocal_but.place(x=170,y=300,width=85,height=70)
            #4
            exponencial_but.place(x=0,y=370,width=85,height=70)
            square_but.place(x=85,y=370,width=85,height=70)
            x_y_but.place(x=170,y=370,width=85,height=70)
            #5
            modulus_but.place(x=0,y=440,width=85,height=70)
            pie_but.place(x=85,y=440,width=85,height=70)
            nepions_const_but.place(x=170,y=440,width=85,height=70)

        elif switchvar.get() == "s2":
            #1
            root_but.place(x=-85,y=160,width=85,height=70)
            #2
            sine_but.place(x=-255,y=230,width=85,height=70)
            cosine_but.place(x=-170,y=230,width=85,height=70)
            tangent_but.place(x=-85,y=230,width=85,height=70)
            #3
            log_e_but.place(x=-255,y=300,width=85,height=70)
            log_10_but.place(x=-170,y=300,width=85,height=70)
            reciprocal_but.place(x=-85,y=300,width=85,height=70)
            #4
            exponencial_but.place(x=-255,y=370,width=85,height=70)
            square_but.place(x=-170,y=370,width=85,height=70)
            x_y_but.place(x=-85,y=370,width=85,height=70)
            #5
            modulus_but.place(x=-255,y=440,width=85,height=70)
            pie_but.place(x=-170,y=440,width=85,height=70)
            nepions_const_but.place(x=-85,y=440,width=85,height=70)
            #1
            cuberoot_but.place(x=170,y=160,width=85,height=70)
            #2
            sin_itf_but.place(x=0,y=230,width=85,height=70)
            cos_itf_but.place(x=85,y=230,width=85,height=70)
            tan_itf_but.place(x=170,y=230,width=85,height=70)
            #3
            hyperbolic_sin_but.place(x=0,y=300,width=85,height=70)
            hyperbolic_cos_but.place(x=85,y=300,width=85,height=70)
            hyperbolic_tan_but.place(x=170,y=300,width=85,height=70)
            #4
            hyperbolic_sin_itf_but.place(x=0,y=370,width=85,height=70)
            hyperbolic_cos_itf_but.place(x=85,y=370,width=85,height=70)
            hyperbolic_tan_itf_but.place(x=170,y=370,width=85,height=70)
            #5
            two_x_but.place(x=0,y=440,width=85,height=65)
            cube_but.place(x=85,y=440,width=85,height=65)
            factorial_x_but.place(x=170,y=440,width=85,height=65)

    def switch():
        if switchvar.get() == "s1":
            switchvar.set("s2")
        elif switchvar.get() == "s2":
            switchvar.set("s1")
        scientific_button()

    
    #-------------------------------------------------------------------------------------------------------------------------
    clear_but=Button(scientific_frame,image = sc_clear_image,bd=0,command=clear,activebackground=thm[5])
    clear_but.place(y=160,x=255 ,width=85,height=70)
    bracket_but=Button(scientific_frame,image = sc_bracket_image,bd=0,command=bracket,activebackground=thm[5])
    bracket_but.place(y=160,x=340 ,width=85,height=70)
    back_space_but=Button(scientific_frame,image = sc_back_space_image,bd=0,command=back_space,activebackground=thm[5])
    back_space_but.place(y=160,x=425 ,width=85,height=70)
    divide_but=Button(scientific_frame,image = sc_divide_image,bd=0,command=divide,activebackground=thm[5])
    divide_but.place(y=160,x=510 ,width=85,height=70)

    seven_but=Button(scientific_frame,image = sc_s7_image,bd=0,command=seven,activebackground=thm[5])
    seven_but.place(y=230,x=255 ,width=85,height=70)
    eaight_but=Button(scientific_frame,image = sc_s8_image,bd=0,command=eaight,activebackground=thm[5])
    eaight_but.place(y=230,x=340 ,width=85,height=70)
    nine_but=Button(scientific_frame,image = sc_s9_image,bd=0,command=nine,activebackground=thm[5])
    nine_but.place(y=230,x=425 ,width=85,height=70)
    multi_but=Button(scientific_frame,image = sc_multi_image,bd=0,command=multi,activebackground=thm[5])
    multi_but.place(y=230,x=510 ,width=85,height=70)
    
    four_but=Button(scientific_frame,image = sc_s4_image,bd=0,command=four,activebackground=thm[5])
    four_but.place(y=300,x=255 ,width=85,height=70)
    five_but=Button(scientific_frame,image = sc_s5_image,bd=0,command=five,activebackground=thm[5])
    five_but.place(y=300,x=340 ,width=85,height=70)
    six_but=Button(scientific_frame,image = sc_s6_image,bd=0,command=six,activebackground=thm[5])
    six_but.place(y=300,x=425 ,width=85,height=70)
    add_but=Button(scientific_frame,image = sc_add_image,bd=0,command=add,activebackground=thm[5])
    add_but.place(y=300,x=510 ,width=85,height=70)
    
    one_but=Button(scientific_frame,image = sc_s1_image,bd=0,command=one,activebackground=thm[5])
    one_but.place(y=370,x=255 ,width=85,height=70)
    two_but=Button(scientific_frame,image = sc_s2_image,bd=0,command=two,activebackground=thm[5])
    two_but.place(y=370,x=340 ,width=85,height=70)
    three_but=Button(scientific_frame,image = sc_s3_image,bd=0,command=three,activebackground=thm[5])
    three_but.place(y=370,x=425 ,width=85,height=70)
    subtract_but=Button(scientific_frame,image = sc_subtr_image,bd=0,command=subtract,activebackground=thm[5])
    subtract_but.place(y=370,x=510 ,width=85,height=70)
    
    ss_but=Button(scientific_frame,image = sc_ss_image,bd=0,command=ss,activebackground=thm[5])
    ss_but.place(y=440,x=255 ,width=85,height=70)
    zero_but=Button(scientific_frame,image = sc_s0_image,bd=0,command=zero,activebackground=thm[5])
    zero_but.place(y=440,x=340 ,width=85,height=70)
    point_but=Button(scientific_frame,image = sc_point_image,bd=0,command=point,activebackground=thm[5])
    point_but.place(y=440,x=425 ,width=85,height=70)
    equal_but=Button(scientific_frame,image = sc_equal_image,bd=0,command=equal,activebackground=thm[5])
    equal_but.place(y=440,x=510 ,width=85,height=70)
    
    #1
    root_but=Button(scientific_frame,image = root_image,bd=0,command=root,activebackground=thm[5])
    #2
    sine_but=Button(scientific_frame,image = sin_image,bd=0,command=sine,activebackground=thm[5])
    cosine_but=Button(scientific_frame,image = cos_image,bd=0,command=cosine,activebackground=thm[5])
    tangent_but=Button(scientific_frame,image = tan_image,bd=0,command=tangent,activebackground=thm[5])
    #3
    log_e_but=Button(scientific_frame,image = ln_image,bd=0,command=log_e,activebackground=thm[5])
    log_10_but=Button(scientific_frame,image = log_image,bd=0,command=log_10,activebackground=thm[5])
    reciprocal_but=Button(scientific_frame,image = rec_image,bd=0,command=reciprocal,activebackground=thm[5])
    #4
    exponencial_but=Button(scientific_frame,image = ex_image,bd=0,command=exponencial,activebackground=thm[5])
    square_but=Button(scientific_frame,image = x2_image,bd=0,command=square,activebackground=thm[5])
    x_y_but=Button(scientific_frame,image = xy_image,bd=0,command=x_y,activebackground=thm[5])
    #5
    modulus_but=Button(scientific_frame,image = mod_image,bd=0,command=modulus,activebackground=thm[5])
    pie_but=Button(scientific_frame,image = pi_image,bd=0,command=pie,activebackground=thm[5])
    nepions_const_but=Button(scientific_frame,image = e_image,bd=0,command=nepions,activebackground=thm[5])
    #1
    cuberoot_but=Button(scientific_frame,image = cuberoot_image,bd=0,command=cuberoot,activebackground=thm[5])
    #2
    sin_itf_but=Button(scientific_frame,image = asin_image,bd=0,command=sin_itf,activebackground=thm[5])
    cos_itf_but=Button(scientific_frame,image = acos_image,bd=0,command=cos_itf,activebackground=thm[5])
    tan_itf_but=Button(scientific_frame,image = atan_image,bd=0,command=tan_itf,activebackground=thm[5])
    #3
    hyperbolic_sin_but=Button(scientific_frame,image = sinh_image,bd=0,command=hyperbolic_sin,activebackground=thm[5])
    hyperbolic_cos_but=Button(scientific_frame,image = cosh_image,bd=0,command=hyperbolic_cos,activebackground=thm[5])
    hyperbolic_tan_but=Button(scientific_frame,image = tanh_image,bd=0,command=hyperbolic_tan,activebackground=thm[5])
    #4
    hyperbolic_sin_itf_but=Button(scientific_frame,image = asinh_image,bd=0,command=hyperbolic_sin_itf,activebackground=thm[5])
    hyperbolic_cos_itf_but=Button(scientific_frame,image = acosh_image,bd=0,command=hyperbolic_cos_itf,activebackground=thm[5])
    hyperbolic_tan_itf_but=Button(scientific_frame,image = atanh_image,bd=0,command=hyperbolic_tan_itf,activebackground=thm[5])
    #5
    two_x_but=Button(scientific_frame,image = exp2_image,bd=0,command=two_x,activebackground=thm[5])
    cube_but=Button(scientific_frame,image = x3_image,bd=0,command=cube,activebackground=thm[5])
    factorial_x_but=Button(scientific_frame,image = xf_image,bd=0,command=factorial_x,activebackground=thm[5])
    
    def rad_deg():
        if n.get() == "Rad":
            rad_deg_but.configure(image = deg_image)
            n.set("Deg")
        elif n.get() == "Deg":
            rad_deg_but.configure(image = rad_image)
            n.set("Rad")

    rad_deg_but = Button(scientific_frame,image=rad_image,activebackground=thm[5],bd=0,command=rad_deg)
    rad_deg_but.place(y=160 ,x=85 ,width=85 ,height=70)
   
    change_but=Button(scientific_frame,image=swap_image,activebackground=thm[5],bd=0,command=switch)
    change_but.place(y=160 ,x=0 ,width=85 ,height=70)
    scientific_button()

    scientific_frame.place(x=0,y=40,height=510,width=955)

    #----  ----  ----  ----   ----    ----    ----    ----    ----    ----    ----    ----    ----#

def programming_calculater():
    programming_frame = Frame(window)
    backlabel = Label(programming_frame,image=prback)
    backlabel.place(height=470,width=425)
    
    dece = StringVar()
    hexa = StringVar()
    octa = StringVar()
    bine = StringVar()
    Decbox = Entry(programming_frame,font=("Comic Sans MS",20),textvariable = dece,bd=0,bg=thm[1],fg=thm[2])
    Hexbox = Entry(programming_frame,font=("Comic Sans MS",12),textvariable = hexa,bd=0,bg=thm[6],fg=thm[7])
    Octbox = Entry(programming_frame,font=("Comic Sans MS",12),textvariable = octa,bd=0,bg=thm[6],fg=thm[7])
    Binbox = Entry(programming_frame,font=("Comic Sans MS",12),textvariable = bine,bd=0,bg=thm[6],fg=thm[7])

    hexlab = Label(programming_frame,image = Hex_image)
    octlab = Label(programming_frame,image = Oct_image)
    binlab = Label(programming_frame,image = Bin_image)

    act = StringVar()
    act.set("dec")

    def opperation(txt):
        try:
            if act.get() == "dec":
                    lmt(dece)
                    dece.set(dece.get() + txt)
                    h = str(hex(int(dece.get())))
                    hexa.set(h.replace("0x",""))
                    o = str(oct(int(dece.get())))
                    octa.set(o.replace("0o",""))
                    b = str(bin(int(dece.get())))
                    bine.set(b.replace("0b",""))

            elif act.get() == "hex":
                    lmt(hexa)
                    hexa.set(hexa.get() + txt)
                    di = int(hexa.get(),16)
                    d = str(di)
                    dece.set(d)
                    o = str(oct(di))
                    octa.set(o.replace("0o",""))
                    b = str(bin(di))
                    bine.set(b.replace("0b",""))

            elif act.get() == "oct":
                    lmt(octa)
                    octa.set(octa.get() + txt)
                    di = int(octa.get(),8)
                    d = str(di)
                    dece.set(d)
                    h = str(hex(di))
                    hexa.set(h.replace("0x",""))
                    b = str(bin(di))
                    bine.set(b.replace("0b",""))

            elif act.get() == "bin":
                    lmt(bine)
                    bine.set(bine.get() + txt)
                    di = int(bine.get(),2)
                    d = str(di)
                    dece.set(d)
                    h = str(hex(di))
                    hexa.set(h.replace("0x",""))
                    o = str(oct(di))
                    octa.set(o.replace("0b",""))
        except:
            None
                     
    def lmt(display):
        alp = display.get()
        if len(alp) >= 14 :
            display.set(alp[0:len(alp)-1])

    def clear_fxn():
        l1 = [dece,hexa,octa,bine]
        for display in l1:
            display.set("")

    def back_space_fxn():
        apd = str(dece.get())
        aph = str(hexa.get())
        apo = str(octa.get())
        apb = str(bine.get())
        if len(apd) > 0 and len(aph) > 0 and len(apo) > 0 and len(apb) > 0 :
            if act.get() == "dec":
                dece.set(apd[0:len(apd)-1])
                if dece.get() != "":
                    h = str(hex(int(dece.get())))
                    hexa.set(h.replace("0x",""))
                    o = str(oct(int(dece.get())))
                    octa.set(o.replace("0o",""))
                    b = str(bin(int(dece.get())))
                    bine.set(b.replace("0b",""))
                else:
                    clear_fxn()
            elif act.get() == "hex":
                hexa.set(aph[0:len(aph)-1])
                if hexa.get() != "":
                    di = int(hexa.get(),16)
                    d = str(di)
                    dece.set(d)
                    o = str(oct(di))
                    octa.set(o.replace("0o",""))
                    b = str(bin(di))
                    bine.set(b.replace("0b",""))
                else:
                    clear_fxn()

            elif act.get() == "oct":
                octa.set(apo[0:len(apo)-1])
                if octa.get() != "":
                    di = int(octa.get(),8)
                    d = str(di)
                    dece.set(d)
                    h = str(hex(di))
                    hexa.set(h.replace("0x",""))
                    b = str(bin(di))
                    bine.set(b.replace("0b",""))
                else:
                    clear_fxn()

            elif act.get() == "bin":
                bine.set(apb[0:len(apb)-1])
                if bine.get() != "":
                    di = int(bine.get(),2)
                    d = str(di)
                    dece.set(d)
                    h = str(hex(di))
                    hexa.set(h.replace("0x",""))
                    o = str(oct(di))
                    octa.set(o.replace("0o",""))
                else:
                        clear_fxn()
    def seven():
        opperation("7")
                
    def eaight():
        opperation("8")
                
    def nine():
        opperation("9")
                
    def four():
        opperation("4")
                
    def five():
        opperation("5")
                
    def six():
        opperation("6")
                
    def one():
        opperation("1")
                
    def two():
        opperation("2")
                
    def three():
        opperation("3")
                
    def ss():
        l1 = [dece,hexa,octa,bine]
        for display in l1:
            apx = display.get()
            if apx == "" :
                display.set("-" + apx)  
            elif apx[0] == "-" :
                display.set(apx[1:])
            else :
                display.set("-" + apx)
                   
    def zero():
        opperation("0")
        
        
    def A_fxn():
        opperation("A")

    def B_fxn():
        opperation("B")

    def C_fxn():
        opperation("C")

    def D_fxn():
        opperation("D")

    def E_fxn():
        opperation("E")

    def F_fxn():
        opperation("F")

    def equal_fxn():
        opperation("")

    clear_but=Button(programming_frame,image = pr_clear_image,bd=0,command=clear_fxn,activebackground=thm[5],bg=thm[5])
    back_space_but=Button(programming_frame,image = pr_back_space_image,bd=0,command=back_space_fxn,activebackground=thm[5],bg=thm[5])
    seven_but=Button(programming_frame,image = pr_s7_image,bd=0,command=seven,activebackground=thm[5],bg=thm[5])
    eaight_but=Button(programming_frame,image = pr_s8_image,bd=0,command=eaight,activebackground=thm[5],bg=thm[5])
    nine_but=Button(programming_frame,image = pr_s9_image,bd=0,command=nine,activebackground=thm[5],bg=thm[5])
    four_but=Button(programming_frame,image = pr_s4_image,bd=0,command=four,activebackground=thm[5],bg=thm[5])
    five_but=Button(programming_frame,image = pr_s5_image,bd=0,command=five,activebackground=thm[5],bg=thm[5])
    six_but=Button(programming_frame,image = pr_s6_image,bd=0,command=six,activebackground=thm[5],bg=thm[5])
    one_but=Button(programming_frame,image = pr_s1_image,bd=0,command=one,activebackground=thm[5],bg=thm[5])
    two_but=Button(programming_frame,image = pr_s2_image,bd=0,command=two,activebackground=thm[5],bg=thm[5])
    three_but=Button(programming_frame,image = pr_s3_image,bd=0,command=three,activebackground=thm[5],bg=thm[5])
    ss_but=Button(programming_frame,image = pr_ss_image,bd=0,command=ss,activebackground=thm[5],bg=thm[5])
    zero_but=Button(programming_frame,image = pr_s0_image,bd=0,command=zero,activebackground=thm[5],bg=thm[5])
    equal_but=Button(programming_frame,image = pr_equal_image,bd=0,command=equal_fxn,activebackground=thm[5],bg=thm[5])
    A_but=Button(programming_frame,image = A_image,bd=0,command=A_fxn,activebackground=thm[5],bg=thm[5])
    B_but=Button(programming_frame,image = B_image,bd=0,command=B_fxn,activebackground=thm[5],bg=thm[5])
    C_but=Button(programming_frame,image = C_image,bd=0,command=C_fxn,activebackground=thm[5],bg=thm[5])
    D_but=Button(programming_frame,image = D_image,bd=0,command=D_fxn,activebackground=thm[5],bg=thm[5])
    E_but=Button(programming_frame,image = E_image,bd=0,command=E_fxn,activebackground=thm[5],bg=thm[5])
    F_but=Button(programming_frame,image = F_image,bd=0,command=F_fxn,activebackground=thm[5],bg=thm[5])
    
    clear_but.place(y=190,x=0 ,width=85,height=70)
    back_space_but.place(y=190,x=85 ,width=85,height=70)
    seven_but.place(y=190,x=170 ,width=85,height=70)
    eaight_but.place(y=190,x=255 ,width=85,height=70)
    nine_but.place(y=190,x=340 ,width=85,height=70)
    
    A_but.place(y=260,x=0 ,width=85,height=70)
    B_but.place(y=260,x=85 ,width=85,height=70)
    four_but.place(y=260,x=170 ,width=85,height=70)
    five_but.place(y=260,x=255 ,width=85,height=70)
    six_but.place(y=260,x=340 ,width=85,height=70)
    
    C_but.place(y=330,x=0 ,width=85,height=70)
    D_but.place(y=330,x=85 ,width=85,height=70)
    one_but.place(y=330,x=170 ,width=85,height=70)
    two_but.place(y=330,x=255 ,width=85,height=70)
    three_but.place(y=330,x=340 ,width=85,height=70)
    
    E_but.place(y=400,x=0 ,width=85,height=70)
    F_but.place(y=400,x=85 ,width=85,height=70)   
    ss_but.place(y=400,x=170 ,width=85,height=70)
    zero_but.place(y=400,x=255 ,width=85,height=70)
    equal_but.place(y=400 ,x=340 ,width=85,height=70)


    A_but['state']='disabled'
    B_but['state']='disabled'
    C_but['state']='disabled'
    D_but['state']='disabled'
    E_but['state']='disabled'
    F_but['state']='disabled'
    nine_but['state']='normal'
    eaight_but['state']='normal'
    seven_but['state']='normal'
    six_but['state']='normal'
    five_but['state']='normal'
    four_but['state']='normal'
    three_but['state']='normal'
    two_but['state']='normal'

    def decf(event):
        act.set("dec")
        A_but['state']='disabled'
        B_but['state']='disabled'
        C_but['state']='disabled'
        D_but['state']='disabled'
        E_but['state']='disabled'
        F_but['state']='disabled'
        nine_but['state']='normal'
        eaight_but['state']='normal'
        seven_but['state']='normal'
        six_but['state']='normal'
        five_but['state']='normal'
        four_but['state']='normal'
        three_but['state']='normal'
        two_but['state']='normal'
        
    def hexf(event):
        act.set("hex")
        A_but['state']='normal'
        B_but['state']='normal'
        C_but['state']='normal'
        D_but['state']='normal'
        E_but['state']='normal'
        F_but['state']='normal'
        nine_but['state']='normal'
        eaight_but['state']='normal'
        seven_but['state']='normal'
        six_but['state']='normal'
        five_but['state']='normal'
        four_but['state']='normal'
        three_but['state']='normal'
        two_but['state']='normal'

    def octf(event):
        act.set("oct")
        A_but['state']='disabled'
        B_but['state']='disabled'
        C_but['state']='disabled'
        D_but['state']='disabled'
        E_but['state']='disabled'
        F_but['state']='disabled'
        nine_but['state']='disabled'
        eaight_but['state']='disabled'
        seven_but['state']='normal'
        six_but['state']='normal'
        five_but['state']='normal'
        four_but['state']='normal'
        three_but['state']='normal'
        two_but['state']='normal'
        
    def binf(event):
        act.set("bin")
        A_but['state']='disabled'
        B_but['state']='disabled'
        C_but['state']='disabled'
        D_but['state']='disabled'
        E_but['state']='disabled'
        F_but['state']='disabled'
        nine_but['state']='disabled'
        eaight_but['state']='disabled'
        seven_but['state']='disabled'
        six_but['state']='disabled'
        five_but['state']='disabled'
        four_but['state']='disabled'
        three_but['state']='disabled'
        two_but['state']='disabled'
      


    Decbox.bind("<FocusIn>",decf)
    Hexbox.bind("<FocusIn>",hexf)
    Octbox.bind("<FocusIn>",octf)
    Binbox.bind("<FocusIn>",binf)

    hexlab.place(x=3,y=82,width=45,height=25)
    octlab.place(x=3,y=114,width=45,height=25)
    binlab.place(x=3,y=146,width=45,height=25)

    Decbox.place(x=23,y=20,height=50,width=379)
    Hexbox.place(x=64,y=82,width=347,height=25)
    Octbox.place(x=64,y=114,width=347,height=25)
    Binbox.place(x=64,y=146,width=347,height=25)

    programming_frame.place(x=0,y=40,height=470,width=425)

    # -----     -----   -----   -----   ------  ------  -----   #
combo1 = StringVar()
combo2 = StringVar()
       
#----------------------------------------------------------------------------------------------------------------------------------
def convertor_currency():
    currency_frame = Frame(window)
    backlabel = Label(currency_frame,image = curback)
    backlabel.place(height=555,width=340)
    cstyle = ttk.Style()
    cstyle.theme_use('vista') 
    mycursor_cur.execute("SELECT Target FROM data")
    myresult = mycursor_cur.fetchall()
    l1=[]
    for x in myresult:
        l1.append(x[0])

    def upgrade_data():
        try:
            download_update()
            modulating()
            upgrade_currencydata()
            messagebox.showinfo("Info", "Database Updated Successfuly")
        except:
            messagebox.showwarning("Error", "Can't Connect to Internet, Please! try again")

    def ploting(x,y):
        py.bar(x,y)
        py.xlabel("Currency")
        py.ylabel("Exchange Rate")
        py.title("Daily Foreign Exchange Rates for U.S. Dollar (USD)")
        py.show()

    def data_graph():
        choise = Toplevel()
        choise.maxsize(340,550)
        choise.minsize(340,550)
        view = Label(choise,image=graph_start)
        view.place(height=550,width=340)
        def end():
            view.config(image=graph_page)   
            char1 = StringVar()
            char2 = StringVar()
            char3 = StringVar()
            char4 = StringVar()
            char5 = StringVar()
            char1.set("--Select--")
            char2.set("--Select--")
            char3.set("--Select--")
            char4.set("--Select--")
            char5.set("--Select--")
            char1box = ttk.Combobox(choise,width=15,textvariable=char1)
            char2box = ttk.Combobox(choise,width=15,textvariable=char2)
            char3box = ttk.Combobox(choise,width=15,textvariable=char3)
            char4box = ttk.Combobox(choise,width=15,textvariable=char4)
            char5box = ttk.Combobox(choise,width=15,textvariable=char5)
            char1box['values']=l1
            char2box['values']=l1
            char3box['values']=l1
            char4box['values']=l1
            char5box['values']=l1
            char1box.place(x=20,y=120)
            char2box.place(x=20,y=213)
            char3box.place(x=20,y=310)
            char4box.place(x=20,y=393)
            char5box.place(x=20,y=485)
            def start_plot():
                if char1.get() != "--Select--" and char2.get() != "--Select--" and char3.get() != "--Select--" and char4.get() != "--Select--" and char5.get() != "--Select--" :
                    x = [char1.get(),char2.get(),char3.get(),char4.get(),char5.get()]
                    y=[]
                    for i in x:
                        mycursor_cur.execute("SELECT InverseRate FROM data WHERE Target = '" + i + "'")
                        myresult = mycursor_cur.fetchall()
                        apx = myresult[0]
                        apx = apx[0]
                        apx = eval(apx)
                        y.append(apx)
                    choise.destroy()
                    ploting(x,y)
                else:
                    messagebox.showinfo("Note", "All 5 Are Mandatery")

            ploting_but = Button(choise,image=plot_but_image,command=start_plot,bd=0,activebackground="#2DC2BC")
            ploting_but.place(x=268,y=479,width=72,height=71)
        choise.after(1000,end)
        
    display1 = StringVar()
    display2 = StringVar()
    combo1.set("U.S. Dollar")
    combo2.set("U.S. Dollar")
    act = StringVar()
    act.set("1")

    display1_view = Entry(currency_frame,font=("Comic Sans MS",20),textvariable = display1,bg=thm[1],bd=0,fg=thm[2])
    display2_view = Entry(currency_frame,font=("Comic Sans MS",20),textvariable = display2,bg=thm[1],bd=0,fg=thm[2])
    combobox1 = ttk.Combobox(currency_frame,width=15,textvariable=combo1)
    combobox2 = ttk.Combobox(currency_frame,width=15,textvariable=combo2)
    upgrade_button = Button(currency_frame,image=upg_image,command=upgrade_data,bd=0,activebackground=thm[1])
    upgrade_button.place(x=22,y=232,height=26,width=156)
    graph_button = Button(currency_frame,image=graph_image,command=data_graph,bd=0,activebackground=thm[1])
    graph_button.place(x=300,y=231,height=27,width=27)
    combobox1['values']=l1
    combobox2['values']=l1
    combobox1['state'] = "readonly"
    combobox2['state'] = "readonly"
    
    def foc1(event):
        act.set("1")

    def foc2(event):
        act.set("2")

    display1_view.bind("<FocusIn>",foc1)
    display2_view.bind("<FocusIn>",foc2)
        
    def currency(txt):
        try:
            if act.get() == "2":
                    display2.set(display2.get() + txt)
                    base = combo2.get()
                    tar = combo1.get()
                    mycursor_cur.execute("SELECT InverseRate FROM data WHERE Target='" + base +"'" )
                    b = mycursor_cur.fetchall()
                    mycursor_cur.execute("SELECT ExchangeRate FROM data WHERE Target='" + tar +"'" )
                    a = mycursor_cur.fetchall()
                    a = a[0]
                    a = a[0]
                    b = b[0]
                    b = b[0]
                    display1.set(str(eval("(" + display2.get() + ")*(" + a + ")*(" + b + ")")))

            elif act.get() == "1":
                    display1.set(display1.get() + txt)
                    base = combo1.get()
                    tar = combo2.get()
                    mycursor_cur.execute("SELECT InverseRate FROM data WHERE Target='" + base +"'" )
                    b = mycursor_cur.fetchall()
                    mycursor_cur.execute("SELECT ExchangeRate FROM data WHERE Target='" + tar +"'" )
                    a = mycursor_cur.fetchall()
                    a = a[0]
                    a = a[0]
                    b = b[0]
                    b = b[0]
                    display2.set(str(eval("(" + display1.get() + ")*(" + a + ")*(" + b + ")")))
        except:
            None
                  
    display1_view.place(x=23,y=15,width=294)
    display2_view.place(x=23,y=125,width=294)
    combobox1.place(x=21,y=77)
    combobox2.place(x=21,y=187)
        
    def equal():
        currency("")        

    def clear():
        display2.set("")
        display1.set("")

                
    def back_space():
        if act.get()=="2":
            apx = display2.get()
            display2.set(apx[0:len(apx)-1])
        else:
            apx = display1.get()
            display1.set(apx[0:len(apx)-1])
        currency("")
                
    def seven():
        currency("7")
                
    def eaight():
        currency("8")
                
    def nine():
        currency("9")
                
    def four():
        currency("4")
                
    def five():
        currency("5")
                
    def six():
        currency("6")
                
    def one():
        currency("1")
                
    def two():
        currency("2")
                
    def three():
        currency("3")
                   
    def zero():
        currency("0")
                  
    def point():
        currency(".")

    def ss():
        display1.set("-" + display1.get())
        display2.set("-" + display2.get())

    clear_but=Button(currency_frame,image = cr_clear_image,bd=0,command=clear,activebackground=thm[5])
    clear_but.place(y=485,x=0 ,width=85,height=70)
    
    back_space_but=Button(currency_frame,image = cr_back_space_image,bd=0,command=back_space,activebackground=thm[5])
    back_space_but.place(y=275,x=255 ,width=85,height=70)
    
    seven_but=Button(currency_frame,image = cr_s7_image,bd=0,command=seven,activebackground=thm[5])
    seven_but.place(y=275,x=0 ,width=85,height=70)
    
    eaight_but=Button(currency_frame,image = cr_s8_image,bd=0,command=eaight,activebackground=thm[5])
    eaight_but.place(y=275,x=85 ,width=85,height=70)
    
    nine_but=Button(currency_frame,image = cr_s9_image,bd=0,command=nine,activebackground=thm[5])
    nine_but.place(y=275,x=170 ,width=85,height=70)
    
    ss_but=Button(currency_frame,image = cr_ss_image,bd=0,command=ss,activebackground=thm[5])
    ss_but.place(y=345,x=255 ,width=85,height=70)
    
    four_but=Button(currency_frame,image = cr_s4_image,bd=0,command=four,activebackground=thm[5])
    four_but.place(y=345,x=0 ,width=85,height=70)
    
    five_but=Button(currency_frame,image = cr_s5_image,bd=0,command=five,activebackground=thm[5])
    five_but.place(y=345,x=85 ,width=85,height=70)
    
    six_but=Button(currency_frame,image = cr_s6_image,bd=0,command=six,activebackground=thm[5])
    six_but.place(y=345,x=170 ,width=85,height=70)
    
    one_but=Button(currency_frame,image = cr_s1_image,bd=0,command=one,activebackground=thm[5])
    one_but.place(y=415,x=0 ,width=85,height=70)
    
    two_but=Button(currency_frame,image = cr_s2_image,bd=0,command=two,activebackground=thm[5])
    two_but.place(y=415,x=85 ,width=85,height=70)
    
    three_but=Button(currency_frame,image = cr_s3_image,bd=0,command=three,activebackground=thm[5])
    three_but.place(y=415,x=170 ,width=85,height=70)
    
    zero_but=Button(currency_frame,image = cr_s0_image,bd=0,command=zero,activebackground=thm[5])
    zero_but.place(y=485,x=85 ,width=85,height=70)
    
    point_but=Button(currency_frame,image = cr_point_image,bd=0,command=point,activebackground=thm[5])
    point_but.place(y=485,x=170 ,width=85,height=70)
    
    equal_but=Button(currency_frame,image = cr_equal_image,bd=0,command=equal,activebackground=thm[5])
    equal_but.place(y=485,x=255 ,width=85,height=70)
    
    currency_frame.place(y=40,height=555,width=340)
#--------------------------------------------------------------------------------------------------------------
def convertor():
    convertor_frame = Frame(window)
    backlabel = Label(convertor_frame,image = conback)
    backlabel.place(height=510,width=340)
    cstyle = ttk.Style()
    cstyle.theme_use('vista')
    convertor_typ = opp.get()
    
    if convertor_typ == "length":
        mycursor_con.execute("SELECT Unit FROM length")
        myresult = mycursor_con.fetchall()
        l1=[]
        for x in myresult:
            l1.append(x[0])
        combo1.set("Meters")
        combo2.set("Meters")
        
    elif convertor_typ == "volume":
        mycursor_con.execute("SELECT Unit FROM volume")
        myresult = mycursor_con.fetchall()
        l1=[]
        for x in myresult:
            l1.append(x[0])
        combo1.set("Meter cube")
        combo2.set("Meter cube")
        
    elif convertor_typ == "temp":
        l1=["Celsius","Kelvin","Fahrenheit"]
        combo1.set("Kelvin")
        combo2.set("Kelvin")
        
    elif convertor_typ == "weight":
        mycursor_con.execute("SELECT Unit FROM weight")
        myresult = mycursor_con.fetchall()
        l1=[]
        for x in myresult:
            l1.append(x[0])
        combo1.set("Kilogram")
        combo2.set("Kilogram")
        
    elif convertor_typ == "energy":
        mycursor_con.execute("SELECT Unit FROM energy")
        myresult = mycursor_con.fetchall()
        l1=[]
        for x in myresult:
            l1.append(x[0])
        combo1.set("joule")
        combo2.set("joule")
        
    elif convertor_typ == "area":
        mycursor_con.execute("SELECT Unit FROM area")
        myresult = mycursor_con.fetchall()
        l1=[]
        for x in myresult:
            l1.append(x[0])
        combo1.set("Meter square")
        combo2.set("Meter square")
        
    elif convertor_typ == "speed":
        mycursor_con.execute("SELECT Unit FROM speed")
        myresult = mycursor_con.fetchall()
        l1=[]
        for x in myresult:
            l1.append(x[0])
        combo1.set("Meter/second")
        combo2.set("Meter/second")
                   
    elif convertor_typ == "time":
        mycursor_con.execute("SELECT Unit FROM time")
        myresult = mycursor_con.fetchall()
        l1=[]
        for x in myresult:
            l1.append(x[0])
        combo1.set("second")
        combo2.set("second")
        
    elif convertor_typ == "data":
        mycursor_con.execute("SELECT Unit FROM data")
        myresult = mycursor_con.fetchall()
        l1=[]
        for x in myresult:
            l1.append(x[0])
        combo1.set("byte")
        combo2.set("byte")
        
    elif convertor_typ == "power":
        mycursor_con.execute("SELECT Unit FROM power")
        myresult = mycursor_con.fetchall()
        l1=[]
        for x in myresult:
            l1.append(x[0])
        combo1.set("watt")
        combo2.set("watt")
        
    elif convertor_typ == "pressure":
        mycursor_con.execute("SELECT Unit FROM pressure")
        myresult = mycursor_con.fetchall()
        l1=[]
        for x in myresult:
            l1.append(x[0])
        combo1.set("Pascal")
        combo2.set("Pascal")
        
    elif convertor_typ == "angle":
        l1=["Degrees","Radians","Gradians"]
        combo1.set("Radians")
        combo2.set("Radians")
        
    display1 = StringVar()
    display2 = StringVar()
    act = StringVar()
    act.set("1")

    display1_view = Entry(convertor_frame,font=("Comic Sans MS",20),textvariable = display1,bg=thm[1],bd=0,fg=thm[2])
    display2_view = Entry(convertor_frame,font=("Comic Sans MS",20),textvariable = display2,bg=thm[1],bd=0,fg=thm[2])
    combobox1 = ttk.Combobox(convertor_frame,width=15,textvariable=combo1)
    combobox2 = ttk.Combobox(convertor_frame,width=15,textvariable=combo2)
    combobox1['values']=l1
    combobox2['values']=l1
    combobox1['state'] = "readonly"
    combobox2['state'] = "readonly"
    
    def foc1(event):
        act.set("1")

    def foc2(event):
        act.set("2")

    display1_view.bind("<FocusIn>",foc1)
    display2_view.bind("<FocusIn>",foc2)

        
    def convert_data(txt):
        if convertor_typ == "angle":
            try:
                if act.get() == "2":
                        display2.set(display2.get() + txt)
                        base = combo2.get()
                        tar = combo1.get()
                        apx = display2.get()
                        if base == "Radians" and tar == "Degrees":
                            x = (eval(apx)*180)/math.pi 
                        elif base == "Radians" and tar == "Gradians":
                            x = (eval(apx)*200)/math.pi
                        elif base == "Degrees" and tar == "Radians":
                            x = (eval(apx)*math.pi)/180 
                        elif base == "Degrees" and tar == "Gradians":
                            x = (eval(apx)*200)/180
                        elif base == "Gradians" and tar == "Degrees":
                            x = (eval(apx)*180)/200 
                        elif base == "Gradians" and tar == "Radians":
                            x = (eval(apx)*math.pi)/200
                        else:
                            x = eval(apx)
                        display1.set(str(round(x,15)))

                elif act.get() == "1":
                        display1.set(display1.get() + txt)
                        base = combo1.get()
                        tar = combo2.get()
                        apx = display1.get()
                        if base == "Radians" and tar == "Degrees":
                            x = (eval(apx)*180)/math.pi
                        elif base == "Radians" and tar == "Gradians":
                            x = (eval(apx)*200)/math.pi
                        elif base == "Degrees" and tar == "Radians":
                            x = (eval(apx)*math.pi)/180 
                        elif base == "Degrees" and tar == "Gradians":
                            x = (eval(apx)*200)/180
                        elif base == "Gradians" and tar == "Degrees":
                            x = (eval(apx)*180)/200 
                        elif base == "Gradians" and tar == "Radians":
                            x = (eval(apx)*math.pi)/200
                        else:
                            x = eval(apx)
                        display2.set(str(round(x,15)))
            except:
                None

        elif convertor_typ == "temp":
            try:
                if act.get() == "2":
                        display2.set(display2.get() + txt)
                        base = combo2.get()
                        tar = combo1.get()
                        apx = display2.get()
                        if base == "Celsius" and tar == "Kelvin" :
                            x = apx + "+ 273"
                        elif base == "Celsius" and tar == "Fahrenheit" :
                            x = "((9/5)*(" + apx + ")) + 32"
                        elif base == "Kelvin" and tar == "Celsius" :
                            x = apx + "- 273"
                        elif base == "Kelvin" and tar == "Fahrenheit" :
                            x = "((9/5)*(" + apx + "- 273)) + 32"
                        elif base == "Fahrenheit" and tar == "Celsius" :
                            x = "(5/9)*(" + apx + " - 32)"
                        elif base == "Fahrenheit" and tar == "Kelvin" :
                            x = "((5/9)*(" + apx + " - 32)) + 273"
                        else:
                            x = apx
                        display1.set(str(eval(x)))


                elif act.get() == "1":
                        display1.set(display1.get() + txt)
                        base = combo1.get()
                        tar = combo2.get()
                        apx = display1.get()
                        if base == "Celsius" and tar == "Kelvin" :
                            x = apx + "+ 273"
                        elif base == "Celsius" and tar == "Fahrenheit" :
                            x = "((9/5)*(" + apx + ")) + 32"
                        elif base == "Kelvin" and tar == "Celsius" :
                            x = apx + "- 273"
                        elif base == "Kelvin" and tar == "Fahrenheit" :
                            x = "((9/5)*(" + apx + "- 273)) + 32"
                        elif base == "Fahrenheit" and tar == "Celsius" :
                            x = "(5/9)*(" + apx + " - 32)"
                        elif base == "Fahrenheit" and tar == "Kelvin" :
                            x = "((5/9)*(" + apx + " - 32)) + 273"
                        else:
                            x = apx
                        display2.set(str(eval(x)))
            except:
                None
            
        else:
            try:
                if act.get() == "2":
                        display2.set(display2.get() + txt)
                        base = combo2.get()
                        tar = combo1.get()
                        sq1="SELECT Value FROM " + convertor_typ + " WHERE Unit= '" + base +"'"
                        sq2="SELECT Value FROM " + convertor_typ + " WHERE Unit= '" + tar +"'"
                        mycursor_con.execute(sq1)
                        b = mycursor_con.fetchall()
                        mycursor_con.execute(sq2)
                        a = mycursor_con.fetchall()
                        a = a[0]
                        a = a[0]
                        b = b[0]
                        b = b[0]
                        display1.set(str(eval("(" + display2.get() + ")*(" + a + ")/(" + b + ")")))

                elif act.get() == "1":
                        display1.set(display1.get() + txt)
                        base = combo1.get()
                        tar = combo2.get()
                        sq1="SELECT Value FROM " + convertor_typ + " WHERE Unit= '" + base +"'"
                        sq2="SELECT Value FROM " + convertor_typ + " WHERE Unit= '" + tar +"'"
                        mycursor_con.execute(sq1)
                        b = mycursor_con.fetchall()
                        mycursor_con.execute(sq2)
                        a = mycursor_con.fetchall()
                        a = a[0]
                        a = a[0]
                        b = b[0]
                        b = b[0]
                        display2.set(str(eval("(" + display1.get() + ")*(" + a + ")/(" + b + ")")))
            except:
                None
                  
    display1_view.place(x=23,y=15,width=294)
    display2_view.place(x=23,y=125,width=294)
    combobox1.place(x=21,y=77)
    combobox2.place(x=21,y=187)
        
    def equal():
        convert_data("")        

    def clear():
        display2.set("")
        display1.set("")

                
    def back_space():
        if act.get()=="2":
            apx = display2.get()
            display2.set(apx[0:len(apx)-1])
        else:
            apx = display1.get()
            display1.set(apx[0:len(apx)-1])
        convert_data("")
                
    def seven():
        convert_data("7")
                
    def eaight():
        convert_data("8")
                
    def nine():
        convert_data("9")
                
    def four():
        convert_data("4")
                
    def five():
        convert_data("5")
                
    def six():
        convert_data("6")
                
    def one():
        convert_data("1")
                
    def two():
        convert_data("2")
                
    def three():
        convert_data("3")
                   
    def zero():
        convert_data("0")
                  
    def point():
        convert_data(".")

    def ss():
        display1.set("-" + display1.get())
        display2.set("-" + display2.get())

    clear_but=Button(convertor_frame,image = clear_image,bd=0,command=clear,activebackground=thm[5])
    clear_but.place(y=440,x=0 ,width=85,height=70)
    
    back_space_but=Button(convertor_frame,image = back_space_image,bd=0,command=back_space,activebackground=thm[5])
    back_space_but.place(y=230,x=255 ,width=85,height=70)
    
    seven_but=Button(convertor_frame,image = s7_image,bd=0,command=seven,activebackground=thm[5])
    seven_but.place(y=230,x=0 ,width=85,height=70)
    
    eaight_but=Button(convertor_frame,image = s8_image,bd=0,command=eaight,activebackground=thm[5])
    eaight_but.place(y=230,x=85 ,width=85,height=70)
    
    nine_but=Button(convertor_frame,image = s9_image,bd=0,command=nine,activebackground=thm[5])
    nine_but.place(y=230,x=170 ,width=85,height=70)
    
    ss_but=Button(convertor_frame,image = ss_image,bd=0,command=ss,activebackground=thm[5])
    ss_but.place(y=300,x=255 ,width=85,height=70)
    
    four_but=Button(convertor_frame,image = s4_image,bd=0,command=four,activebackground=thm[5])
    four_but.place(y=300,x=0 ,width=85,height=70)
    
    five_but=Button(convertor_frame,image = s5_image,bd=0,command=five,activebackground=thm[5])
    five_but.place(y=300,x=85 ,width=85,height=70)
    
    six_but=Button(convertor_frame,image = s6_image,bd=0,command=six,activebackground=thm[5])
    six_but.place(y=300,x=170 ,width=85,height=70)
    
    one_but=Button(convertor_frame,image = s1_image,bd=0,command=one,activebackground=thm[5])
    one_but.place(y=370,x=0 ,width=85,height=70)
    
    two_but=Button(convertor_frame,image = s2_image,bd=0,command=two,activebackground=thm[5])
    two_but.place(y=370,x=85 ,width=85,height=70)
    
    three_but=Button(convertor_frame,image = s3_image,bd=0,command=three,activebackground=thm[5])
    three_but.place(y=370,x=170 ,width=85,height=70)
    
    zero_but=Button(convertor_frame,image = s0_image,bd=0,command=zero,activebackground=thm[5])
    zero_but.place(y=440,x=85 ,width=85,height=70)
    
    point_but=Button(convertor_frame,image = point_image,bd=0,command=point,activebackground=thm[5])
    point_but.place(y=440,x=170 ,width=85,height=70)
    
    equal_but=Button(convertor_frame,image = equal_image,bd=0,command=equal,activebackground=thm[5])
    equal_but.place(y=440,x=255 ,width=85,height=70)
    
    convertor_frame.place(y=40,height=510,width=340)
#----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------
def About():
    About_frame = Frame(window)
    Back = Label(About_frame,image=About_page_img)
    Back.place(height=510,width=340)
    About_frame.place(y=40,height=510,width=340)


#launch Oppeartins-----------------------------------------------------------------------------------------------------------------
def main_calculater(window):

    if opp.get() == "pannel":
        slider.config(image=slider_close_image)
    else:
        slider.config(image=slider_image)

    if opp.get() != "pannel" and opp.get() != "standard" and opp.get() != "Scientific":
        history_but.place(x=1050,y=0)
        hist.place(x=-1000)
    else:
        None
    
    if opp.get() == "pannel":
        window.wm_attributes("-alpha",0.9)
        slide_view()
        
    elif opp.get() == "standard":
        head.config(image = sd_head)
        head.place(x=40,height=40,width=240)
        window.wm_attributes("-alpha",0.9)
        window.maxsize(340,550)
        window.minsize(340,550)
        standard_calculater()

    elif opp.get() == "Scientific":
        head.config(image = sc_head)
        head.place(x=40,height=40,width=495)
        window.wm_attributes("-alpha",0.9)
        window.maxsize(595,550)
        window.minsize(595,550)
        Scientific_Calculater()

    elif opp.get() == "programming":
        head.config(image = pr_head)
        head.place(x=40,height=40,width=385)
        window.wm_attributes("-alpha",0.9)
        window.maxsize(425,510)
        window.minsize(425,510)
        programming_calculater()

    elif opp.get() == "currency":
        head.config(image = cr_head)
        head.place(x=40,height=40,width=300)
        window.wm_attributes("-alpha",0.9)
        window.maxsize(340,595)
        window.minsize(340,595)
        convertor_currency()

    elif opp.get() == "about":
        slider.config(image=About_slider)
        head.config(image = About_head)
        head.place(x=40,height=40,width=300)
        window.wm_attributes("-alpha",0.9)
        window.maxsize(340,550)
        window.minsize(340,550)
        About()

    elif opp.get() != '' :
        head.config(image = head_image)
        head.place(x=40,height=40,width=300)
        window.wm_attributes("-alpha",0.9)
        window.maxsize(340,550)
        window.minsize(340,550)
        convertor()
        
def cal():
    window.maxsize(340,550)
    window.minsize(340,550)
    view = Label(window,image=base)
    view.place(height=550,width=340,bordermode="outside")
    def end():
        view.place(height=0,width=0)   
        main_calculater(window)
    window.after(1000,end)
    
def pannel():
    if opp.get() != "pannel":
        opp.set("pannel")
    elif opp.get() == "pannel":
        opp.set(oppf.get())
    main_calculater(window)
    
slider = Button(window ,image = slider_image, bd=0,command=pannel,activebackground=thm[8])
slider.place(width=40,height=40)
head = Label(window,image = sd_head)
head.place(height=40,width=340)
cal()
#history----------------------------------------------------------------------------------------
try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="1234",
      database="History"
    )
    mycursor = mydb.cursor()
#--------    
except:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="1234"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE History")
    mycursor.execute("USE History")
    mycursor.execute("CREATE TABLE standard_history(id INT AUTO_INCREMENT PRIMARY KEY, ques VARCHAR(255), sol VARCHAR(255))")
    mycursor.execute("CREATE TABLE scientific_history(id INT AUTO_INCREMENT PRIMARY KEY, ques VARCHAR(255), sol VARCHAR(255))")
    mydb.commit()
    
#--------
sdi = "INSERT INTO standard_history(ques, sol) VALUES (%s, %s)"
sci = "INSERT INTO scientific_history(ques, sol) VALUES (%s, %s)"   
#-----------------------------------------------------------------------------------------------
#Data-----------------------------------------------------------------------------------------
try:
    mydb_cur = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="currencydata"
    )
    mycursor_cur = mydb_cur.cursor()
except:
    mydb_cur = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="1234"
    )
    convert_xml_currency()
    mycursor_cur = mydb_cur.cursor()
    mycursor_cur.execute("USE currencydata")

try:
    mydb_con = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="data"
    )
    mycursor_con = mydb_con.cursor()
except:
    mydb_con = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="1234"
    )
    convert_csv_data()
    mycursor_con = mydb_con.cursor()
    mycursor_con.execute("USE data")

#themes-------------------------------------------------------------------------------------------------------------------------------------------
def theme_window():
    theme_frame = Frame(window,bg="white")
    #theme fxn ---------------------------------------------------------------------------------
    def back():
        opp.set(oppf.get())
        theme_frame.destroy()
        cal()

    def changes_apply():
        x = str(window.winfo_x())
        y = str(window.winfo_y())
        loc = '340x550+' + x + '+' + y
        update_locus(loc)
        def end():
            window.destroy()
        import os
        os.startfile("change_theme.pyw")
        window.after(3000,end)
        
    def thm1_fxn():
        change_theme("dark theme")
        changes_apply()

    def thm2_fxn():
        change_theme("light theme")
        changes_apply()

    def thm3_fxn():
        change_theme("Butterfly theme")
        changes_apply()

    def thm4_fxn():
        change_theme("Fruit theme")
        changes_apply()

    def thm5_fxn():
        change_theme("Forest theme")
        changes_apply()

    def thm6_fxn():
        change_theme("Vector theme")
        changes_apply()

    def thm7_fxn():
        change_theme("Wooden theme")
        changes_apply()
    #-------------------------------------------------------------------------------------------
    style = ttk.Style(theme_frame)
    style.theme_use('vista') 
    label = Label(theme_frame,bd=0,image=theme_head)
    back_but = Button(theme_frame,image=theme_back_but_image,activebackground="white",command=back,bd=0)
    canvas = Canvas(theme_frame,bg="white",bd=0,highlightthickness=0)
    scroll_y = ttk.Scrollbar(theme_frame,orient="vertical", command=canvas.yview)

    frame = Frame(canvas,bg="white",bd=0)

    thm1_but = Button(frame,image=thm1,bd=0,command=thm1_fxn).grid(row=0,column=0,padx=5,pady=10)
    thm2_but = Button(frame,image=thm2,bd=0,command=thm2_fxn).grid(row=0,column=1,padx=5,pady=10)
    thm3_but = Button(frame,image=thm3,bd=0,command=thm3_fxn).grid(row=0,column=2,padx=5,pady=10)
    thm4_but = Button(frame,image=thm4,bd=0,command=thm4_fxn).grid(row=1,column=0,padx=5,pady=10)
    thm5_but = Button(frame,image=thm5,bd=0,command=thm5_fxn).grid(row=1,column=1,padx=5,pady=10)
    thm6_but = Button(frame,image=thm6,bd=0,command=thm6_fxn).grid(row=1,column=2,padx=5,pady=10)
    thm7_but = Button(frame,image=thm7,bd=0,command=thm7_fxn).grid(row=2,column=0,padx=5,pady=10)

    canvas.create_window(0, 0, anchor='nw', window=frame)

    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=scroll_y.set)
                         
    scroll_y.set(0.2,0.3)

    label.place(x=0,y=0,height=150,width=340)
    back_but.place(x=0,y=0,height=40,width=40)
    canvas.place(x=0,y=150,height=400,width=325)
    scroll_y.place(x=325,y=150,height=400)
    theme_frame.place(x=0,y=0,height=550,width=340)

def theme_start():
    window.maxsize(340,550)
    window.minsize(340,550)
    view = Label(window,image=theme_base)
    view.place(height=550,width=340,bordermode="outside")
    def end():
        view.place(height=0,width=0)   
        theme_window()
    window.after(1000,end)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------

window.mainloop()
