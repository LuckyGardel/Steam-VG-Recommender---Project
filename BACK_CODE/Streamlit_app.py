import streamlit as st
from PIL import Image
import streamlit.components.v1 as stc
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Recommendation func
def recommend(name):
    
    df = pd.read_csv("data_concat.csv")
    recommendations = pd.DataFrame(df.nlargest(11,name)['name'])
    recommendations = recommendations[recommendations['name']!=name]
    price = pd.DataFrame(df.nlargest(11,name)['cost_price'])
    url = pd.DataFrame(df.nlargest(11,name)['url'])
    result = pd.concat([recommendations,price[1:11],url[1:11]], axis = 1)
    
    return result

# Main page func
def main():
    
    st.title("Steam Game Based Recommendation App")
    
    menu = ["Recommend","About"]
    choice = st.sidebar.selectbox("Menu",menu)
        
        
    if (choice == "Recommend"):
        st.image('store_home_share.jpg')
        name = st.text_input("Please Type the name of a game you like in lower caps to obtain your recommendations:")

        if st.button("Recommend"):
            if name is not None:
                print('Wait a minute and you will see our recommendations. Enjoy! ')
                try:
                    results = recommend(name)
                except: 
                    results = "Sorry, we can not find a suitable match. Try a different game!"
                
                st.write(results)
                
                
                
    else:
        st.subheader("About")
        st.text("Built with StreamLit & Pandas-Python, this App is designed to recommend 10 similar")  
        st.text("games to the one that the user inputs in the search tab.")
        st.text("The coding work was done by @LuckyGardel (https://github.com/LuckyGardel).")
main()


