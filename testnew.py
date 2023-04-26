# from cgitb import html
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import requests, webbrowser
from bs4 import BeautifulSoup, Doctype
import csv

st.write("""
### Questionnaire
""")


with st.expander("Question: 1"):
    age = st.slider('How old are you ?', 0, 130, 25)
    st.write("I'm ", age, 'years old')
with st.expander("Question: 2"):
    gender = st.radio(
     "What is your Gender ?",
     ('Male', 'Female', 'Prefer Not To Say'))

    if gender == 'Male':
     st.write('You selected Male.')
    if gender == 'Female':
     st.write('You selected Female.')
    if gender == 'Prefer Not To Say':
     st.write("You selected Prefer Not To say.")
with st.expander("Question: 3"):
    alco = st.radio(
     "Are you Alcoholic ?",
     ('Yes', 'No'))

    if alco == 'Yes':
     st.write('Yes, I am Alcohol Consumer.')
    if alco == 'No':
     st.write('No, I am not Alcohol Consumer')

with st.expander("Question: 4"):
    como = st.radio(
     "Do you have any Co-Morbidity ?",
     ('Yes', 'No'))

    if como == 'Yes':
        title = st.text_input('Co-Morbidity Name', '')
        st.write('The Disease name is', title)
    if como == 'No':
     st.write('No, I didn`t have any Co-Morbidity.')
with st.expander("Question: 5"):
    covid = st.radio(
     "Are you COVID-19 positive earlier ?",
     ('No', 'Yes'))

    if covid == 'Yes':
        covidtime = st.slider('How many months ago ?', 0, 12,0)
        st.write("I'm COVID-19 Positive ", covidtime, 'months ago.')
    if covid == 'No':
     st.write('I didn`t have covid-19 virus.')

st.write("""
### Symptoms Checker
""")
def predict_disease_from_symptom(symptom_list):

    symptoms = {'abdominal pain': 0,'abnormal menstruation': 0,'acidity': 0,'acute liver failure': 0,'altered sensorium': 0,'anxiety': 0,'back pain': 0,'belly pain': 0,'blackheads': 0,'bladder discomfort': 0,
'blister': 0,'blood in sputum': 0,'bloody stool': 0,'blurred and distorted vision': 0,'breathlessness': 0,'brittle nails': 0,'bruising': 0,'burning micturition': 0,'chest pain': 0,'chills': 0,
'cold hands and feets': 0,'coma': 0,'congestion': 0,'constipation': 0,'continuous feel of urine': 0,'continuous sneezing': 0,'cough': 0,'cramps': 0,'dark urine': 0,'dehydration': 0,
'depression': 0,'diarrhoea': 0,'dischromic  patches': 0,'distention of abdomen': 0,'dizziness': 0,'drying and tingling lips': 0,'enlarged thyroid': 0,'excessive hunger': 0,'extra marital contacts': 0,'family history': 0,
'fast heart rate': 0,'fatigue': 0,'fluid overload': 0,'foul smell of urine': 0,'headache': 0,'high fever': 0,'hip joint pain': 0,'history of alcohol consumption': 0,'increased appetite': 0,'indigestion': 0,
'inflammatory nails': 0,'internal itching': 0,'irregular sugar level': 0,'irritability': 0,'irritation in anus': 0,'joint pain': 0,'knee pain': 0,'lack of concentration': 0,'lethargy': 0,'loss of appetite': 0,
'loss of balance': 0,'loss of smell': 0,'malaise': 0,'mild fever': 0,'mood swings': 0,'movement stiffness': 0,'mucoid sputum': 0,'muscle pain': 0,'muscle wasting': 0,'muscle weakness': 0,
'nausea': 0,'neck pain': 0,'nodal skin eruptions': 0,'obesity': 0,'pain behind the eyes': 0,'pain during bowel movements': 0,'pain in anal region': 0,'painful walking': 0,'palpitations': 0,'passage of gases': 0,
'patches in throat': 0,'phlegm': 0,'polyuria': 0,'prominent veins on calf': 0,'puffy face and eyes': 0,'pus filled pimples': 0,'receiving blood transfusion': 0,'receiving unsterile injections': 0,'red sore around nose': 0,'red spots over body': 0,
'redness of eyes': 0,'restlessness': 0,'runny nose': 0,'rusty sputum': 0,'scurring': 0,'shivering': 0,'silver like dusting': 0,'sinus pressure': 0,'skin peeling': 0,'skin rash': 0,
'slurred speech': 0,'small dents in nails': 0,'spinning movements': 0,'spotting  urination': 0,'stiff neck': 0,'stomach bleeding': 0,'stomach pain': 0,'sunken eyes': 0,'sweating': 0,'swelled lymph nodes': 0,
'swelling joints': 0,'swelling of stomach': 0,'swollen blood vessels': 0,'swollen extremeties': 0,'swollen legs': 0,'throat irritation': 0,'toxic look (typhos)': 0,'ulcers on tongue': 0,'unsteadiness': 0,'visual disturbances': 0,
'vomiting': 0,'watering from eyes': 0,'weakness in limbs': 0,'weakness of one body side': 0,'weight gain': 0,'weight loss': 0,'yellow crust ooze': 0,'yellow urine': 0,'yellowing of eyes': 0,'yellowish skin': 0,
'itching': 0}

    for s in symptom_list:
        symptoms[s] = 1
    df_test = pd.DataFrame(columns=list(symptoms.keys()))
    df_test.loc[0] = np.array(list(symptoms.values()))
    df_test
    clf = load(str("random_forest.joblib"))
    result = clf.predict(df_test)
    del df_test
    st.title("Know about your Disease : ")
    return f"{result[0]}"



options=st.multiselect(
        'Please select your symptoms : ',
        ['abdominal pain','abnormal menstruation','acidity','acute liver failure','altered sensorium','anxiety','back pain','belly pain','blackheads','bladder discomfort',
'blister','blood in sputum','bloody stool','blurred and distorted vision','breathlessness','brittle nails','bruising','burning micturition','chest pain','chills',
'cold hands and feets','coma','congestion','constipation','continuous feel of urine','continuous sneezing','cough','cramps','dark urine','dehydration',
'depression','diarrhoea','dischromic  patches','distention of abdomen','dizziness','drying and tingling lips','enlarged thyroid','excessive hunger','extra marital contacts','family history',
'fast heart rate','fatigue','fluid overload','foul smell of urine','headache','high fever','hip joint pain','history of alcohol consumption','increased appetite','indigestion',
'inflammatory nails','internal itching','irregular sugar level','irritability','irritation in anus','joint pain','knee pain','lack of concentration','lethargy','loss of appetite',
'loss of balance','loss of smell','malaise','mild fever','mood swings','movement stiffness','mucoid sputum','muscle pain','muscle wasting','muscle weakness',
'nausea','neck pain','nodal skin eruptions','obesity','pain behind the eyes','pain during bowel movements','pain in anal region','painful walking','palpitations','passage of gases',
'patches in throat','phlegm','polyuria','prominent veins on calf','puffy face and eyes','pus filled pimples','receiving blood transfusion','receiving unsterile injections','red sore around nose','red spots over body',
'redness of eyes','restlessness','runny nose','rusty sputum','scurring','shivering','silver like dusting','sinus pressure','skin peeling','skin rash',
'slurred speech','small dents in nails','spinning movements','spotting  urination','stiff neck','stomach bleeding','stomach pain','sunken eyes','sweating','swelled lymph nodes',
'swelling joints','swelling of stomach','swollen blood vessels','swollen extremeties','swollen legs','throat irritation','toxic look (typhos)','ulcers on tongue','unsteadiness','visual disturbances',
'vomiting','watering from eyes','weakness in limbs','weakness of one body side','weight gain','weight loss','yellow crust ooze','yellow urine','yellowing of eyes','yellowish skin',
'itching'])


ans=predict_disease_from_symptom(options)


with st.expander("Look for the Disease : "):
    st.header(ans)

with st.expander("See About Disease "):
    with open('symptom_Description.csv', 'r+') as f:
        myDataList = f.readlines()
        namelist = []
        desc=[]
        for line in myDataList:
            entry = line.split(',')
            namelist.append(entry[0])
            if ans in namelist:
                namelist.append(entry[1])
                desc.append(entry[1])
                lst_repl = [i.replace('"', '') for i in desc]
                strr=str(lst_repl)
                
                strrr=strr.replace('[','')
                strrrr=strrr.replace(']','')
                strrrrr=strrrr.replace('\'','')
                st.write(" • "+strrrrr)
                break
    google_search = requests.get ("https://www.google.com/search?q="+ ans)
    soup = BeautifulSoup(google_search.text, 'html.parser')
    search_res=soup.select('.Ap5OSd .AP7Wnd')
    lensearch=len(search_res)
    i=0
    while(i<lensearch):
        st.write(" • "+search_res[i].string)
        i+=1;

with st.expander("See About Medical Test  "):
    print ("gooogling.....")
    google_search = requests.get ("https://www.google.com/search?q="+ ans +" medical test")
    soup = BeautifulSoup(google_search.text, 'html.parser')
    search_res=soup.select('.rQMQod')

    lensearch=len(search_res)
    i=0
    while(i<lensearch):
        st.write(search_res[i].string)
        i+=1;
        break;

with st.expander("See About Precautions  "):
    with open('symptom_precaution.csv', 'r+') as f:
        myDataList = f.readlines()
        namelist = []
        desc=[]
        for line in myDataList:
            entry = line.split(',')
            namelist.append(entry[0])
            if ans in namelist:
                desc.append(entry[1])
                desc.append(entry[2])
                desc.append(entry[3])
                desc.append(entry[4])

                lst_repl = [i.replace('"', '') for i in desc]
                strr=str(lst_repl)
                for x in range(len(desc)):
                    st.write(" • "+desc[x])
                    print(desc[x])
                break

