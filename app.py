# =========================
# IMPORT REQUIRED LIBRARIES
# =========================

import streamlit as st
# streamlit -> Framework to build interactive web apps quickly

import langchain_helper
# langchain_helper -> Custom module containing AI helper functions (e.g., generate_restaurant_name_and_items)


# =========================
# STREAMLIT PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="2026 Restaurant Generator",
    page_icon=":)",
    layout="centered"
)
# Set page title, icon, and layout for the Streamlit app


# =========================
# PAGE HEADER
# =========================

st.title(":) AI Restaurant Idea Generator")
# Main title of the app

st.markdown("""
Select a cuisine from the sidebar, and our AI will dream up a  
**unique restaurant name** and a **signature menu** for you!
""")
# Short instructions for users


# =========================
# SIDEBAR FOR CUISINE SELECTION
# =========================

st.sidebar.title("Choose:")
# Sidebar section title

cuisine = st.sidebar.selectbox(
    "Cuisines",
    ("Indian", "Thai", "Continental", "English", "Japanese")
)
# Dropdown for cuisine selection


# =========================
# GENERATE RESTAURANT NAME & MENU
# =========================

with st.spinner(f":D Our 5STAR 4K ULTRA PRO MAX Chef is creating a {cuisine} idea"):
    # Show spinner while AI generates restaurant info
    try:
        response = langchain_helper.generate_restaurant_name_and_items(cuisine)
        # Call helper function to generate restaurant name and menu

        st.divider()
        st.markdown("### :) Recommended Name:")
        st.success(response["restaurant_name"])
        # Display AI-generated restaurant name

        st.markdown("### B) Signature Menu:")
        menu_items = response["menu_item"].split(",")
        # Split menu items into a list

        for item in menu_items:
            st.write(item.strip())
            # Display each menu item

    except Exception as e:
        st.error(":( Something went wrong! Please check your API or model configs.")
        st.exception(e)
        # Handle any errors during AI generation


# =========================
# PAGE FOOTER
# =========================

st.divider()
st.caption("Made with Love <3")
# Footer with a personal touch
