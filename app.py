import db
import streamlit as st
import re
import pickle
import spacy
import re
from rapidfuzz import process
import requests

st.set_page_config(page_title="Py Chatbot")

def give_words(prompt):
    doc = nlp(prompt)
    sid = None
    subject = None
    action = None

    match = re.search(r'\bS\d{6}\b', prompt, re.IGNORECASE)
    if match:
        sid = match.group(0).upper()

    score_words = ['score', 'marks', 'grade', 'result', 'got', 'scored']
    topper_words = ['highest', 'top', 'best', 'topper']
    predict_words = ['pass', 'fail', 'predict', 'outcome', 'will']
    performance_words = ['performance', 'analysis', 'review', 'how']
    greet_words = ['hi', 'hii', 'hello', 'whatsupp']
    points = [0,0,0,0,0]
    labels = ['get_score','get_topper','performance_comment','predict_result','greet']

    for token in doc:
        t = token.lemma_.lower()
        if process.extractOne(t, ['math', 'science', 'english'])[1]>90:
            subject = process.extractOne(t, ['math', 'science', 'english'])[0]
        if process.extractOne(t, score_words)[1]>90:
            points[0] += 1
        elif process.extractOne(t, topper_words)[1]>90:
            points[1] += 1
        elif process.extractOne(t, performance_words)[1]>90:
            points[2] += 1
        elif process.extractOne(t, predict_words)[1]>90:
            points[3] += 1
        elif process.extractOne(t, greet_words)[1]>90:
            points[4] += 1
        m = 0
        for i in range(5):
            if m<=points[i]:
                m = points[i]
                action = labels[i]
        
        if m==0: action=None

    # st.write(points)

    return action, sid, subject




nlp = spacy.load('en_core_web_sm')

with open('stu_log_model.pickle', 'rb') as file:
    logmodel = pickle.load(file)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_history.append(('bot', 'Hi bro, How can I help you?'))


prom = None
prom = st.chat_input('Enter ID number')
# type = st.radio("What do you want", ['Quering', 'Prediction'])


def start(action):
    bot = ''
    if action == 'predict_result' and sid:
        res_df = db.get_details(sid)
        a = res_df[['math_score', 'science_score', 'english_score', 'attendence']].to_numpy()
        res = logmodel.predict(a)
        res = 'PASS' if res == 1 else 'FAIL'
        bot = f"{sid} is predicted to '{res}'"

    elif action == 'get_score' and sid:
        res_df = db.get_scores(sid)
        bot = res_df.to_markdown(index=False)

    elif action == 'get_topper' and subject:
        res_df = db.get_top(subject)
        bot = f"Topper in {subject.capitalize()} is {res_df['name'].values[0]} with score {res_df[subject + '_score'].values[0]}"
    
    elif action=='performance_comment' and sid:
        res_df = db.get_details(sid)
        bad = []; good = []
        subs = ['math', 'science', 'english']
        if not res_df.empty:
            for i in subs:
                if res_df[i+'_score'].values[0]>60:
                    good.append(i)
                else:
                    bad.append(i)
        if good:
            bot += f"{sid} is good at: {', '.join(good)}.\n"
        if bad:
            bot += f"{sid} needs improvement in: {', '.join(bad)}."
    
    elif action=='greet':
        bot = "Hi bro, How can i help you?"
    else:
        bot += "Sorry, I couldn't understand."
    
    st.session_state.chat_history.append(('bot', bot))

if prom:
    action, sid, subject = give_words(prom)
    st.session_state.chat_history.append(('You', prom))
    start(action)


for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

# give me result of S210894