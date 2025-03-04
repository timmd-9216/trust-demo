import streamlit as st
from src import utils

st.set_page_config(page_title="Home", layout="wide")

# filepath = f'data/label_studio_annotations.json'
# annotations = import_utils.import_label_studio_annotations(filepath, "entities")

filepath = utils.set_data_path()
#corpus = utils.import_corpus_pickle(filepath)
corpus = utils.import_corpus_json(filepath)

title_choices = {article["index"]:article["titulo"] for article in corpus}

st.title("Trust")

with st.container(border=True):
    dw_article = st.selectbox('Seleccionar un artículo', (title_choices.keys()), format_func=lambda x: f'{x} - {title_choices.get(x)}')
    
# Get article by index.
#article = corpus.get_article(dw_article)
article = [art for art in corpus if art["index"] == dw_article][0]

col1, col2 = st.columns([3, 1])

with col1: 
    
    #text = article.cuerpo
    text = article["cuerpo"]
    html = utils.plot_text(text)   

    #st.header(article.titulo)
    st.header(article["titulo"])
    st.markdown(html, unsafe_allow_html=True)

with col2:
    with st.container(border=True):
        #st.metric(label="Medio", value=article.medio)
        st.metric(label="Medio", value=article["medio"])
    with st.container(border=True):
        #st.metric(label="Fecha", value=article.fecha)
        st.metric(label="Fecha", value=article["fecha"])
    with st.container(border=True):
        #st.metric(label="Autor", value=article.autor)
        st.metric(label="Autor", value=article["autor"])
    #with st.container(border=True):
    #    st.metric(label="Número de Palabras", value=article.nlp_annotations.doc["stanza"].num_words)

