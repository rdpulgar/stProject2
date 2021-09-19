# ! pip install spanish_sentiment_analysis
from sentiment_analysis_spanish import sentiment_analysis

import streamlit as st

sentiment = sentiment_analysis.SentimentAnalysisSpanish()

st.title('Coke.ai')
st.title('Análisis de sentimiento ...')

write_here = "Texto aqui..."
text = st.text_area("Incluya un texto ..", write_here)
if st.button("Analizar"):
    if text != write_here:
        result = sentiment.sentiment(text)
        st.success('Sentimiento de ['+ text + ']')
        st.success('%.5f' % result)
    else:
        st.error("Ingresa un texto y presiona el boton Analizar ..")
else:
    st.info(
        "Ingresa un texto y presiona el boton Analizar .."
    )