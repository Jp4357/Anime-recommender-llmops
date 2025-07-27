import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv


st.set_page_config(page_title="Anime Recommender", page_icon="🍥", layout="wide")
load_dotenv(override=True)


@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()


pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input(
    "Enter your anime preference eg. : light hearted anime with school setting"
)

if query:
    with st.spinner("Fetching Recommendations..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)
