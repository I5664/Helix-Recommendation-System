import streamlit as st
import pandas as pd
st.title("Recommender System")

product = pd.read_pickle("./products.pkl")
reconstructed_matrix = pd.read_pickle("./matrix.pkl")

def get_recommendation(user_recommendations, value):
    # value = 419139, 1362762, 1167082, 1166671
    recommended_products = list(user_recommendations[user_recommendations.index == (value)])[0]
    st.write('Recommended Products')
    for i in recommended_products:
        # st.text_input(f'<p style="background-size:200px 100px;background-color:#7FFFD4;font-size:24px;border-radius:2%;">{"•     "+i}</p>')
        st.success("* "+i)

def get_recommendation_matrix(reconstructed_matrix, userID):
    print(reconstructed_matrix)
    products = reconstructed_matrix.columns
    user_recommend = list(reconstructed_matrix.loc[[userID]].values[0])
    user_recommend_reference = user_recommend.copy()
    user_recommend.sort(reverse=True)
    temp = []
    for i, recommendation in enumerate(user_recommend[:3]):
        temp.append(products[user_recommend_reference.index(recommendation)])
    st.write('Recommended Products')
    for i in temp:
        # st.write(f'<p style="background-size:200px 100px;background-color:#7FFFD4;font-size:24px;border-radius:2%;">{"•     "+i}</p>', unsafe_allow_html=True)
        st.success("* "+i)


approach = st.selectbox("Select Recommender", ("Cluster Based Recommendation", "Collaborative Filtering"))
cust_code = (st.number_input(label = "Enter the Customer code", step=1))

if approach=="Cluster Based Recommendation":
    if st.button("Predict"):
        get_recommendation(product, cust_code)
elif approach=="Collaborative Filtering":
    if st.button("Predict"):
        get_recommendation_matrix(reconstructed_matrix, cust_code)

    