# =========================
# IMPORT REQUIRED LIBRARIES
# =========================

import os
# os -> Provides functions for interacting with the operating system (e.g., environment variables)

from dotenv import load_dotenv
# load_dotenv -> Loads environment variables from a .env file (e.g., API keys)

from langchain_google_genai import ChatGoogleGenerativeAI
# ChatGoogleGenerativeAI -> LangChain wrapper for Google Generative AI (Gemini)

from langchain_core.prompts import PromptTemplate
# PromptTemplate -> Used to create prompt templates for LLM input

from langchain_core.output_parsers import StrOutputParser
# StrOutputParser -> Parses LLM output into a clean string


# =====================
# LOAD ENVIRONMENT VARIABLES
# =====================

load_dotenv()
# Load environment variables from .env file


# =====================
# INITIALIZE GOOGLE AI LLM
# =====================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)
# llm -> ChatGoogleGenerativeAI instance
# model -> specifies the AI model to use
# temperature -> controls randomness/creativity of AI responses


# =====================
# DEFINE FUNCTION TO GENERATE RESTAURANT NAME AND MENU
# =====================

def generate_restaurant_name_and_items(cuisine):
    """
    Generates a fancy restaurant name and 5 signature menu items based on cuisine.
    
    Args:
        cuisine (str): Type of cuisine (e.g., 'Indian', 'Thai').
        
    Returns:
        dict: Contains 'restaurant_name' and 'menu_item' (comma-separated string).
    """
    
    # Create prompt for restaurant name
    name_prompt = PromptTemplate.from_template(
        "Suggest one fancy name for a {cuisine} restaurant"
    )
    
    # Create prompt for menu items
    menu_prompt = PromptTemplate.from_template(
        "List 5 menu items for {restaurant_name}. Return as a comma-separated string"
    )

    # Build chains: prompt -> LLM -> string parser
    name_chain = name_prompt | llm | StrOutputParser()
    menu_chain = menu_prompt | llm | StrOutputParser()

    # Generate restaurant name
    restaurant_name = name_chain.invoke({"cuisine": cuisine}).strip()
    
    # Generate menu items
    menu_items = menu_chain.invoke({"restaurant_name": restaurant_name}).strip()

    return {
        "restaurant_name": restaurant_name,
        "menu_item": menu_items
    }


# =====================
# TEST AI CONNECTION
# =====================

if __name__ == "__main__":
    print("--- 2026 Environment Check (Conda + Python 3.11) ---")
    try:
        res = llm.invoke("Are you there?")
        print(f"Success! AI says: {res.content}")
    except Exception as e:
        print(f"Error: {e}")
