import pandas as pd
def create_data():
    data = [['dark theme','#0D1528','white','#0D1528','gray64','gray10','#03E4D9','white','#0D1528']]
    df = pd.DataFrame(data,columns=['name','displaybg','displayfg','displayfbg','displayffg','buttonactivebg','HOBbg','HOBfg','HeadButtonActiveBg'])
    df.to_csv('resources/theme.csv',index=False)
    
def change_theme(theme_name):
    b = "/ "
    b = b[0]
    a = b + theme_name
    df = pd.read_csv('resources/Themes' + a + '/theme.csv')
    df.to_csv('resources/theme.csv',index=False)

def create_locus_csv():
    df = pd.DataFrame(['340x550+450+100'],columns=['position'])
    df.to_csv('resources/locus.csv',index=False)

def update_locus(position):
    df = pd.DataFrame([position],columns=['position'])
    df.to_csv('resources/locus.csv',index=False)
