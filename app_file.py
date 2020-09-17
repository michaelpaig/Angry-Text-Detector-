

import streamlit as st
from PIL import Image
from tensorflow import keras
from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle


st.title('Angry Text Detector')

seq_len = 100  
max_vocab = 1500

model = load_model('finalfinal2')

with open('tokenizer4.pkl', 'rb') as handle4:
    tokenizer = pickle.load(handle4)


user_input = st.text_area("Enter your text here:",'')
if st.button('run me!'):
	seq = tokenizer.texts_to_sequences([user_input])
	padded = pad_sequences(seq, maxlen=seq_len)
	pred = model.predict(padded)
	st.text('Anger probability is:')
	st.write(pred[0][0])