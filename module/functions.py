# functional module
import math

def opperation(txt,display,a):
        lmt(display,a)
        display.set(display.get() + txt)

def lmt(display,a):
        alp = display.get()
        if len(alp) >= a :
                display.set(alp[0:len(alp)-1])

def claer_fxn(window,display,displayf):
    display.set("")
    displayf.set("")

def bracket_fxn(window,display):
    spx =[" ÷ "," ᵡ "," + "," - ","(","sin","cos","tan","asin","acos","atan","sinh","cosh","tanh","asinh","acosh","atanh",]
    if display.get() == "" :
            display.set("(")
    else :
        apx = display.get()
        if apx[-1:-4:-1] in spx:
                display.set(apx + "(")
        else:
                display.set(apx + ")")
        

def back_space_fxn(window,display):
        apx = str(display.get())
        if len(apx) > 0 :
                display.set(apx[0:len(apx)-1])
        
def divide_fxn(window,display,displayf,a):
        spx =[" ÷ "," ᵡ "," + "," - "]
        apxe = display.get()
        apxf = displayf.get()
        apx = apxf + apxe
        displayf.set(apx)
        display.set("")
        if apx == "" :
              None
        elif apx[-3:0] in spx:
                displayf.set(apx[0:len(apx)-1] + " ÷ ")
        else:
                opperation(" ÷ ",display,a)
        
def multi_fxn(window,display,displayf,a):
        spx =[" ÷ "," ᵡ "," + "," - "]
        apxe = display.get()
        apxf = displayf.get()
        apx = apxf + apxe
        displayf.set(apx)
        display.set("")
        if apx == "" :
              None
        elif apx[-3:0] in spx:
                displayf.set(apx[0:len(apx)-1] + " ᵡ ")
        else:
                opperation(" ᵡ ",display,a)
        
def add_fxn(window,display,displayf,a):
        spx =[" ÷ "," ᵡ "," + "," - "]
        apxe = display.get()
        apxf = displayf.get()
        apx = apxf + apxe
        displayf.set(apx)
        display.set("")
        if apx == "" :
              None
        elif apx[-3:0] in spx:
                displayf.set(apx[0:len(apx)-1] + " + ")
        else:
                opperation(" + ",display,a)
        
def subtract_fxn(window,display,displayf,a):
        spx =[" ÷ "," ᵡ "," + "," - "]
        apxe = display.get()
        apxf = displayf.get()
        apx = apxf + apxe
        displayf.set(apx)
        display.set("")
        if apx == "" :
              None
        elif apx[-3:0] in spx:
                displayf.set(apx[0:len(apx)-1] + " - ")
        else:
                opperation(" - ",display,a)

def equal_fxn(window,display,fxn_list,replacement_list,displayf):
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
                        
        
def seven_fxn(window,display,a):
        opperation("7",display,a)
        
def eaight_fxn(window,display,a):
        opperation("8",display,a)
        
def nine_fxn(window,display,a):
        opperation("9",display,a)
        
def four_fxn(window,display,a):
        opperation("4",display,a)
        
def five_fxn(window,display,a):
        opperation("5",display,a)
        
def six_fxn(window,display,a):
        opperation("6",display,a)
        
def one_fxn(window,display,a):
        opperation("1",display,a)
        
def two_fxn(window,display,a):
        opperation("2",display,a)
        
def three_fxn(window,display,a):
        opperation("3",display,a)
        
def ss_fxn(window,display):
        apx = display.get()
        if apx == "" :
              display.set("-" + apx)  
        elif apx[0] == "-" :
                display.set(apx[1:])
        else :
                display.set("-" + apx)
        
def zero_fxn(window,display,a):
        opperation("0",display,a)
        
def point_fxn(window,display,a):
        opperation(".",display,a)

def opperation2(txt,display,a):
        spx =[" ÷ "," ᵡ "," + "," - "]
        lmt(display,a)
        apx = display.get()
        if apx == "":
                display.set(apx + txt)
        elif apx[-1] == "(":  
                display.set(apx + txt)
        elif apx in spx:
                display.set(apx + txt)
        else:
                display.set(apx + "ᵡ" + txt)

def root_fxn(window,display,a):
        opperation2("√(",display,a)
        
def sine_fxn(window,display,a):
        opperation2("sin(",display,a)
        
def cosine_fxn(window,display,a):
        opperation2("cos(",display,a)
        
def tangent_fxn(window,display,a):
        opperation2("tan(",display,a)
        
def log_e_fxn(window,display,a):
        opperation2("ln(",display,a)
        
def log_10_fxn(window,display,a):
        opperation2("log(",display,a)
        
def reciprocal_fxn(window,display):
        display.set(display.get() + "1÷(")
        
def exponencial_fxn(window,display,a):
        display.set(display.get() + "e^(")
        
def square_but_fxn(window,display,a):
        display.set(display.get() + "^(2)")
        
def x_y_fxn(window,display,a):
        display.set(display.get() + "^")
        
def modulus_fxn(window,display):
         display.set("abs(" + display.get())
        
def pie_fxn(window,display,a):
        opperation2("ᴨ",display,a)
        
def nepions_fxn(window,display,a):
        opperation2("e",display,a)
        
def cuberoot_fxn(window,display,a):
        opperation2("³√(",display,a)
        
def sin_itf_fxn(window,display,a):
        opperation2("asin(",display,a)
        
def cos_itf_fxn(window,display,a):
        opperation2("acos(",display,a)
        
def tan_itf_fxn(window,display,a):
        opperation2("atan(",display,a)
        
def hyperbolic_sin_fxn(window,display,a):
        opperation2("sinh(",display,a)
        
def hyperbolic_cos_fxn(window,display,a):
        opperation2("cosh(",display,a)
        
def hyperbolic_tan_fxn(window,display,a):
        opperation2("tanh(",display,a)
        
def hyperbolic_sin_itf_fxn(window,display,a):
        opperation2("asinh(",display,a)
        
def hyperbolic_cos_itf_fxn(window,display,a):
        opperation2("acosh(",display,a)
        
def hyperbolic_tan_itf_fxn(window,display,a):
        opperation2("atanh(",display,a)
        
def two_x_fxn(window,display,a):
        display.set("2^(" + display.get() + ")")
        
def cube_fxn(window,display,a):
        display.set(display.get() + "^(3)")
        
def factorial_x_fxn(window,display,a):
        display.set("fac(" + display.get())

def log(x):
        res = math.log10(x)
        return res

def ln(x):
        res = math.log(x)
        return res
    

