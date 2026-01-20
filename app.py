import streamlit as st
import langchain_helper

st.set_page_config(
    page_title="2026 Restaurant Generator",
    page_icon=":)",
    layout="centered"
)

st.title(":) AI Restaurant Idea Generator")
st.markdown("""
Select a cuisine from the sidebar, and our AI will dream up a  
**unique restaurant name** and a **signature menu** for you!
""")

st.sidebar.title("Choose:")

cuisine = st.sidebar.selectbox(
    "Cuisines",
    ("Indian", "Thai", "Continental", "English", "Japanese")
)

with st.spinner(f":D Our 5STAR 4K ULTRA PRO MAX Chef is creating a {cuisine} idea"):
    try:
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)

        st.divider()
        st.markdown("### :) Recommended Name:")
        st.success(response["restaurant_name"])

        st.markdown("### B) Signature Menu:")
        menu_items = response["menu_item"].split(",")

        for item in menu_items:
            st.write(item.strip())

    except Exception as e:
        st.error(":( Something went wrong! Please check your API or model configs.")
        st.exception(e)

st.divider()
st.caption("Made with Love <3")