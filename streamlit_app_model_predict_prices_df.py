# Importando as bibliotecas
import os
import pandas as pd
import numpy as np
import streamlit as st
import joblib

#Write Title
st.title("Title")

#Write Text 
st.write("Text")

#Text Field
st.text_input("placeholder text","default value")

#load model, set cache to prevent reloading
model = tf.keras.models.load_model('model.h5')
return model

with st.spinner("Loading Model...."):
    model=load_model()

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="myGeocoder", timeout=2)
location8 = "Sudoeste"
location8 = geolocator.geocode(location8 + ", Brasília-DF, Brasil")
latitude = float(location8.latitude)
longitude = float(location8.longitude)
latitude, longitude

quartos = (5 - house_df['quartos'].min()) / (house_df['quartos'].max() - house_df['quartos'].min())
print('Quartos =', quartos, ' / Max =', house_df['quartos'].max())
garagem = (0 - house_df['garagem'].min()) / (house_df['garagem'].max() - house_df['garagem'].min())
print('Garagem =', garagem, ' / Max =', house_df['garagem'].max())
banheiro = (1 - house_df['banheiro'].min()) / (house_df['banheiro'].max() - house_df['banheiro'].min())
print('Banheiro =', banheiro, ' / Max =', house_df['banheiro'].max())
area = (247 - house_df['area'].min()) / (house_df['area'].max() - house_df['area'].min())
print('Area =', area, ' / Max =', house_df['area'].max())
suite = (0 - house_df['suite'].min()) / (house_df['suite'].max() - house_df['suite'].min())
print('Suite =', suite, ' / Max =', house_df['suite'].max())
academia = (0 - house_df['academia'].min()) / (house_df['academia'].max() - house_df['academia'].min())
print('Academia =', academia, ' / Max =', house_df['academia'].max())
varanda = (0 - house_df['varanda'].min()) / (house_df['varanda'].max() - house_df['varanda'].min())
print('Varanda =', varanda, ' / Max =', house_df['varanda'].max())
transporte = (0 - house_df['transporte'].min()) / (house_df['transporte'].max() - house_df['transporte'].min())
print('Transporte =', transporte, ' / Max =', house_df['transporte'].max())
salao = (0 - house_df['salao'].min()) / (house_df['salao'].max() - house_df['salao'].min())
print('Salao =', salao, ' / Max =', house_df['salao'].max())
planejado = (0 - house_df['planejado'].min()) / (house_df['planejado'].max() - house_df['planejado'].min())
print('Planejado =', planejado, ' / Max =', house_df['planejado'].max())
latitude2 = (latitude - house_df['latitude'].min()) / (house_df['latitude'].max() - house_df['latitude'].min())
print('Latitude =', latitude2, ' / Max =', house_df['latitude'].max())
longitude2 = (longitude - house_df['longitude'].min()) / (house_df['longitude'].max() - house_df['longitude'].min())
print('Longitude =', longitude2, ' / Max =', house_df['longitude'].max())

X_test_1 = np.array([[ quartos, garagem, banheiro, area, suite, academia, varanda, transporte, salao, planejado, latitude2, longitude2 ]])

y_predict_8 = model.predict(X_test_1)

y_predict_8 = scaler.inverse_transform(y_predict_8)
y_predict_8
