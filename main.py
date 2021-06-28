import plotly_express as px
import pandas as pd
import streamlit as st
from PIL import Image





image1=Image.open('C:/Users/Administrator/Documents/GitHub/main/1612705199068.jpg')
st.image(image1, width=800)



st.title(' KITOPI CONTRACTs DASHBOARD (KCD)')



List_aree= ['None','Riyadh', 'Jeddah']
List_P= ['None','Kitchens', 'Accommodation']
List_kitchens_Ruh= ['None', 'Qurtuba', 'Olaya', 'Malqa', 'Manar', 'Laban', 'Sawaidi']
List_Acc_Ruh= ['None','Head Office', 'Al Wadi', 'AlMalqa', 'Olaya', 'Sawaidi', 'Qurtuba 1', 'Qurtuba 2']
List_kitchens_Jed= ['None','Al Nakeel', 'Al Zahra', 'Falasten', 'Al Safa', ]
List_Acc_Jed=['None', 'Soundlines(Al Alazizya)']
List_P_Jed=['None', 'Kitchens', 'Accommodations']

image=Image.open('C:/Users/Administrator/Documents/GitHub/main/download.jpg')
st.sidebar.image(image, width=300)


######### CONDITINST ########
ex= 'C:/Users/Fawaz Almutairi/Desktop/Contractss.xlsx'
Due= pd.read_excel(ex, usecols='A:D', header=0, sheet_name=1, index_col=0)
st.sidebar.warning('Next payment')
st.sidebar.table(Due)


st.sidebar.write('Created by: Fawaz Almutairi')



###Var####


sel1=st.checkbox('Search Separately (Manual)')
if sel1:
    searche = st.selectbox('Select Area', options=List_aree)

    if searche == 'Riyadh':
        st.subheader('Riyadh Contracts')
        col1, col2 = st.beta_columns(2)
        Search = st.selectbox(label='Select Type', options=List_P)

        if Search == 'Kitchens':
            kitchens2 = st.selectbox(label='Select Kitchen', options=List_kitchens_Ruh)

            if kitchens2 == 'Olaya':
                st.subheader('Contract amount 1,200,000 SAR')
                st.subheader('period of 05 year from 8/1/2021 - 7/31/2024')
                st.subheader(' Total 09 installments')
                st.success('Valid Contract')
                st.info('Owner Name:Mohamed Abdulrahman AlAliq   Phone: 0555405759')
                st.subheader('Balance')
                source7 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df7 = pd.read_excel(source7, sheet_name=12, usecols='A:F', index_col=0)
                df77 = pd.DataFrame(df7)
                st.write('Payment progress')
                st.progress(44)
                st.table(df77)

            if kitchens2 == 'Sawaidi':
                st.subheader('Contract amount 34,000 SAR')
                st.subheader('period of 01 year from 10/18/2020 - 10/6/2021')
                st.subheader(' Total 01 installments')
                st.success('Valid Contract')
                st.subheader('Balance')
                st.info('Owner Name:Badrya Suliman Mohamed AlSaif  Phone: 0505258620 ')
                source5 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df5 = pd.read_excel(source5, usecols='A:F', sheet_name=7, header=0, index_col=0)
                st.write('Payment progress')
                st.progress(100)
                st.table(df5)

            if kitchens2 == 'Qurtuba':
                st.subheader('Contract amount 2,167,750 SAR')
                st.subheader('period of 05 year from 9/1/2020 - 8/31/2025')
                st.subheader('Total 08 installments')
                st.success('Valid Contract')
                st.info('Owner Name: Nasir Saif Nasir AlQahtani  Phone: 0542417970')
                st.subheader('Balance')
                source1 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df2 = pd.read_excel(source1, usecols='A:F', sheet_name=10, header=0, index_col=0)
                st.write('Payment progress')
                st.progress(25)
                st.table(df2)

            if kitchens2 == 'Laban':
                st.subheader('Contract amount 650,000 SAR')
                st.subheader('period of 04 from 1/1/2020 - 12/31/2024')
                st.subheader('Total 05 installments')
                st.success('Valid Contract')
                st.info('Owner Name : Abdullah Mohamed AlShehri  Phone: 0560059491')
                st.subheader('Balance')
                source2 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df2 = pd.read_excel(source2, usecols='A:F', sheet_name=9, header=0, index_col=0)
                st.write('Payment progress')
                st.progress(20)
                st.table(df2)

            if kitchens2 == 'Manar':
                st.subheader('Contract amount 115,000 SAR')
                st.subheader('period of 01 year from 9/16/2020 - 9/15/2021')
                st.subheader(' Total 02 installments')
                st.success('Valid Contract')
                st.info('Owner Name: Easa Salem Zaid AlTamimi    Phone:0556174000')
                st.subheader('Balance')
                source3 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df3 = pd.read_excel(source3, sheet_name=8, usecols='A:F', header=0, index_col=0)
                st.write('Payment progress')
                st.progress(100)
                st.table(df3)

            if kitchens2 == 'Malqa':
                st.subheader('Contract amount 143,150 SAR')
                st.subheader('period of 01 year from 12/1/2020 - 11/30/2021 ')
                st.subheader('Total 02 installments ')
                st.success('Valid Contract')
                st.info('Owner Name: Muklid Fingal Sultan AlOtaibi   Phone: 0566667742    ')
                st.subheader('Balance')
                source4 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df4 = pd.read_excel(source4, usecols='A:F', sheet_name=6, header=0, index_col=0)
                st.write('Payment progress')
                st.progress(100)
                st.table(df4)
        elif Search == 'Accommodation':
            Acc = st.selectbox(label='Select Accommodation', options=List_Acc_Ruh)

            if Acc == 'Head Office':
                st.subheader('Contract amount 514,560 SAR')
                st.subheader('period of 01 year from 1/1/2021 - 12/31/2022')
                st.subheader(' Total 04 installments')
                st.success('Valid Contract')
                st.info('Owner Name: Abdulmalik Mohamed almasri   Phone: 0505456116')
                st.subheader('Balance')
                source6 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df6 = pd.read_excel(source6, sheet_name=5, usecols='A:F', header=0, index_col=0)
                st.write('Payment progress')
                st.progress(25)
                st.table(df6)


    elif searche == 'Jeddah':
        st.subheader('Jeddah Contracts')
        Search1 = st.selectbox('Select Type', options=List_P_Jed)
        if Search1 == 'Kitchens':
            Kitchens4 = st.selectbox(label='Select Kitchen', options=List_kitchens_Jed)
            if Kitchens4 == 'Al Nakeel':
                st.subheader('Contract amount 920,000 SAR')
                st.subheader('period of 04 year from 11/15/2020 - 11/14/2024')
                st.subheader(' Total 16 installments')
                st.success('Valid Contract')
                st.info('Owner Name:Abdulrahman Abdualziz AlSudays  Phone: 0553666469')
                st.subheader('Balance')
                source20 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df20 = pd.read_excel(source20, sheet_name=13, usecols='A:F', header=0, index_col=0)
                st.write('Payment progress')
                st.progress(19)
                st.table(df20)

            if Kitchens4 == 'Al Zahra':
                st.subheader('Contract amount 1,842,300 SAR')
                st.subheader('period of 06 year from 12/01/2020 - 11/30/2024')
                st.subheader(' Total 06 installments')
                st.success('Valid Contract')
                st.info('Owner Name: Akram Wahid Ali Saddiqi  Phone: 0505614548')
                st.subheader('Balance')
                source21 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df21 = pd.read_excel(source21, sheet_name=14, usecols='A:F', header=0, index_col=0)
                st.write('Payment progress')
                st.progress(17)
                st.table(df21)

            if Kitchens4 == 'Falasten':
                st.subheader('Contract amount 450,000 SAR')
                st.subheader('period of 06 year from 07/01/2020 - 06/30/2026')
                st.subheader(' Total 12 installments')
                st.success('Valid Contract')
                st.info('Owner Name: Mohhammed Foad AlKhatib  Phone: Not found')
                st.subheader('Balance')
                source22 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df22 = pd.read_excel(source22, sheet_name=16, usecols='A:F', header=0, index_col=0)
                st.write('Payment progress')
                st.progress(17)
                st.table(df22)

            if Kitchens4 == 'Al Safa':
                st.subheader('Contract amount 240,000 SAR')
                st.subheader('period of 05 year from 06/01/2020 - 06/30/2025')
                st.subheader(' Total 20 installments')
                st.success('Valid Contract')
                st.info('Owner Name: Slem Atiq Al Sarfy  Phone: 0563083330')
                st.subheader('Balance')
                source23 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df23 = pd.read_excel(source23, sheet_name=15, usecols='A:F', header=0, index_col=0)
                st.write('Payment progress')
                st.progress(20)
                st.table(df23)

        elif Search1 == 'Accommodations':
            Acc_jed = st.selectbox(label='Select Accommodation', options=List_Acc_Jed)
            if Acc_jed == 'Soundlines(Al Alazizya)':
                st.subheader('Contract amount 360,000 SAR')
                st.subheader('period of 02 year from 02/01/2021 - 08/1/2022')
                st.subheader(' Total 4 installments')
                st.success('Valid Contract')
                st.info('Owner Name: Soundlines for contracting Co.  Telephone: 0112291125')
                st.subheader('Balance')
                source24 = 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
                df24 = pd.read_excel(source24, sheet_name=11, usecols='A:F', header=0, index_col=0)
                st.write('Payment progress')
                st.progress(25)
                st.table(df24)

    st.stop()










sel= st.checkbox('Summary')
if sel:
    st.info('Riyadh')
    ruh = summary1 = pd.read_excel('C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx', usecols='A:G', header=0,
                                   sheet_name=0, index_col=0)
    st.table(ruh)
    jed = summary2 = pd.read_excel('C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx', usecols='K:P', header=0,
                                   sheet_name=0, index_col=0)
    st.info('Jeddah')
    st.table(jed)
    st.stop()



total= st.checkbox('Total Balance All KSA contracts')
if total:
    st.subheader('Total Balance Until Today')
    ex= 'C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
    s= pd.read_excel(ex, usecols='B:E', header=0, sheet_name=18)
    st.table(s)
    st.stop()





all_inst= st.checkbox('Installments Chart')
details= st.checkbox('Statistic Contracts Info!')







if all_inst:
    excel='C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx'
    da1= pd.read_excel(excel, usecols='A:D', header=0, sheet_name=2)
    da2 = pd.read_excel(excel, usecols='A:D', header=0, sheet_name=3)


    st.header('Riyadh Installment Chart')
    fig= px.scatter(data_frame=da1, x='Due date', y='Installment', color='name', hover_name='status', width=1000, height=750, size='Installment')
    st.write(fig)
    st.header('Jeddah Installment Chart')
    fig2=px.scatter(data_frame=da2, x='Due date', y='Installment', color='name', hover_name='status', width=1000, height=750, size='Installment')
    st.write(fig2)



details_file = pd.read_excel('C:/Users/Administrator/Documents/GitHub/main/Contractss.xlsx',sheet_name=4 ,usecols='A:E',
                                     header=0)
for x in details_file:
    if details:
        st.subheader('Rental info.')
        st.table(details_file)
        stats=details_file.describe()
        st.subheader('Statistics info.')
        st.table(stats)
        st.subheader('1m. Price Vs. Kitchen')
        plot1 = px.scatter(data_frame=details_file, x='Kitchen', y='1m. Price', size='1m. Price')
        st.write(plot1)
        st.stop()


####FRONT#####

    st.stop()
