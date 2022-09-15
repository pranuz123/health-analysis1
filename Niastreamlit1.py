#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import streamlit as st
# Page config
#st.set_page_config(page_title="NIA HEALTH ANALYSIS", layout="wide")

# Load config
#config, instructions, readme = load_config(
   # "config_streamlit.toml", "config_instructions.toml", "config_readme.toml"

st.title("NIA Health")  # add a title
    
uploaded_file = st.file_uploader("Upload File")

if uploaded_file is not None:
    df1=pd.read_csv(uploaded_file, encoding='latin1', on_bad_lines='skip',
                 lineterminator='\n')
    df1=pd.read_excel(uploaded_file)
else:
    st.warning('you need to upload a csv or excel file')

filename=uploaded_file.name

TPAS = ('Mednet','NextCare', 'Dhofar', 'Vipul', 'InHouse')

file_path = '/Users/praneethchoda/Downloads/Paramount :Important/NIA_Health_Automation/Claims Consolidation_HS.2021_FINAL.xlsx'

Nia_Hlth_Data = pd.read_excel(filename, sheet_name = ['Mednet','NextCare', 'Dhofar', 'Vipul', 'InHouse'])

Mednet = Nia_Hlth_Data.get('Mednet')
NextCare = Nia_Hlth_Data.get('NextCare')
Dhofar = Nia_Hlth_Data.get('Dhofar')
Vipul = Nia_Hlth_Data.get('Vipul')
InHouse = Nia_Hlth_Data.get('InHouse')

st.write(Mednet)  # visualize my dataframe in the Streamlit app


Mednet_heads = pd.DataFrame(Mednet.columns, columns = ['Mednet'])
NextCare_heads = pd.DataFrame(NextCare.columns, columns = ['NextCare'])
Dhofar_heads = pd.DataFrame(Dhofar.columns, columns = ['Dhofar'])
Vipul_heads = pd.DataFrame(Vipul.columns, columns = ['Vipul'])
InHouse_heads = pd.DataFrame(InHouse.columns, columns = ['InHouse'])
#print(len(InHouse_heads))

standard_heads = pd.DataFrame(['Policy Number', 'Admission Date','Claim Number','data upto','Data Flag','Paid Amt',
                  'OS Amt', 'Policy Type','Category','Loss Year','Concatenate','key','PremBand'], columns = ['standard'])

Appended_data = pd.concat([Mednet,NextCare,Dhofar,Vipul,InHouse],ignore_index=True)

data_heads = pd.concat([Mednet_heads, NextCare_heads,Dhofar_heads,Vipul_heads,InHouse_heads, standard_heads], axis=1)

std_Mednet_heads = np.zeros(len(Mednet_heads))

Mednet_heads_r = list(Mednet_heads.loc[:,'Mednet'])
NextCare_heads_r = list(NextCare_heads.loc[:,'NextCare'])
Dhofar_heads_r = list(Dhofar_heads.loc[:,'Dhofar'])
Vipul_heads_r = list(Vipul_heads.loc[:,'Vipul'])
InHouse_heads_r = list(InHouse_heads.loc[:,'InHouse'])

for hh in range(len(Mednet_heads_r)):
    if Mednet_heads_r[hh] == "PolicyNo" or Mednet_heads_r[hh] == "Policy No":
        Mednet_heads_r[hh] = 'Policy Number'
    elif Mednet_heads_r[hh] == "AdmissionDate" or Mednet_heads_r[hh] == "Admissiondt":
        Mednet_heads_r[hh] = 'Admission Date'
    
for hh in range(len(NextCare_heads_r)):
    if NextCare_heads_r[hh] == "PolicyNo" or NextCare_heads_r[hh] == "Policy No" or NextCare_heads_r[hh] == "Policy":
        NextCare_heads_r[hh] = 'Policy Number'
    elif NextCare_heads_r[hh] == "AdmissionDate" or NextCare_heads_r[hh] == "Admissiondt" or NextCare_heads_r[hh] == "admission date":
        NextCare_heads_r[hh] = 'Admission Date' 

for hh in range(len(Dhofar_heads_r)):
    if Dhofar_heads_r[hh] == "PolicyNo" or Dhofar_heads_r[hh] =="Policy No" or Dhofar_heads_r[hh] == "Policy":
        Dhofar_heads_r[hh] = 'Policy Number'
    elif Dhofar_heads_r[hh] == "AdmissionDate" or Dhofar_heads_r[hh] =="Admissiondt" or Dhofar_heads_r[hh] == "admission date":
        Dhofar_heads_r[hh] = 'Admission Date'        
        
for hh in range(len(Vipul_heads_r)):
    if Vipul_heads_r[hh] == "PolicyNo" or Vipul_heads_r[hh] =="Policy No" or Vipul_heads_r[hh] =="Policy":
        Vipul_heads_r[hh] = 'Policy Number'
    elif Vipul_heads_r[hh] == "AdmissionDate" or Vipul_heads_r[hh] =="Admissiondt" or Vipul_heads_r[hh] =="admission date":
        Vipul_heads_r[hh] = 'Admission Date'          
    elif Vipul_heads_r[hh] == "Claim year" or Vipul_heads_r[hh] =="Claim Year" or Vipul_heads_r[hh] =="Clm yr":
        Vipul_heads_r[hh] = 'Loss Year'
    elif Vipul_heads_r[hh] == "Approved amt" or Vipul_heads_r[hh] =="Paid amt" or Vipul_heads_r[hh] =="Paid":
        Vipul_heads_r[hh] = 'Paid Amt'
    elif Vipul_heads_r[hh] == "Prem_Band_Revised" or Vipul_heads_r[hh] =="PremBand_Revised" or Vipul_heads_r[hh] =="Revised_PremBand":
        Vipul_heads_r[hh] = 'PremBand'

for hh in range(len(InHouse_heads_r)):
    if InHouse_heads_r[hh] == "PolicyNo" or InHouse_heads_r[hh] =="Policy No" or InHouse_heads_r[hh] =="Policy":
        InHouse_heads_r[hh] = 'Policy Number'
    elif InHouse_heads_r[hh] == "AdmissionDate" or InHouse_heads_r[hh] =="Admissiondt" or InHouse_heads_r[hh] =="Year":
        InHouse_heads_r[hh] = 'Admission Date'          
    elif InHouse_heads_r[hh] == "Claim year" or InHouse_heads_r[hh] =="Claim Year" or InHouse_heads_r[hh] =="Clm yr":
        InHouse_heads_r[hh] = 'Loss Year'
    elif InHouse_heads_r[hh] == "Approved Amount" or InHouse_heads_r[hh] =="Paid amt" or InHouse_heads_r[hh] =="Paid":
        InHouse_heads_r[hh] = 'Paid Amt'
    elif InHouse_heads_r[hh] == "Prem Band" or InHouse_heads_r[hh] =="PremBand_Revised" or InHouse_heads_r[hh] =="Revised_PremBand":
        InHouse_heads_r[hh] = 'PremBand'
        


NextCare_heads_r = pd.DataFrame(NextCare_heads_r)
Dhofar_heads_r = pd.DataFrame(Dhofar_heads_r)
Vipul_heads_r = pd.DataFrame(Vipul_heads_r)
InHouse_heads_r = pd.DataFrame(InHouse_heads_r)        
        
#data_heads_r = pd.concat([Mednet_heads_r, NextCare_heads_r,Dhofar_heads_r,Vipul_heads_r,
                          #InHouse_heads_r], axis=1)   


Mednet_r = Mednet
NextCare_r = NextCare
Dhofar_r = Dhofar
Vipul_r = Vipul
InHouse_r = InHouse

Mednet_r.columns = pd.DataFrame(Mednet_heads_r)
NextCare_r.columns = pd.DataFrame(NextCare_heads_r)
Dhofar_r.columns = pd.DataFrame(Dhofar_heads_r)
Vipul_r.columns = pd.DataFrame(Vipul_heads_r)
InHouse_r.columns = pd.DataFrame(InHouse_heads_r)

Appended_data_r = pd.concat([Mednet_r,NextCare_r,Dhofar_r,Vipul_r,InHouse_r],ignore_index=True)

print(Appended_data_r)
len(Appended_data_r.columns)

Appended_data_r.to_excel("Appended TPA Data.xlsx")







