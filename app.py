# Import required libraries
import streamlit as st
import openai
import pandas as pd
import os

# Initialize OpenAI API (Replace "your_openai_api_key" with your actual API key)
openai.api_key = "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"

# Function to process natural language query
def process_query(query):
    response = openai.Completion.create(engine="text-davinci-002", prompt=query, max_tokens=50)
    processed_query = response.choices[0].text.strip()
    return processed_query

# Function to search in Excel based on the criteria
def search_in_excel(query, excel_path):
    df = pd.read_excel(excel_path)
    results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    return results

# Main function for the app
def main():
    st.image("assets/header-logo.png", width=300)
    st.write("Bonjour! Comment puis-je vous aider aujourd'hui?")
    user_input = st.text_input("Entrez votre recherche ici...")
    
    # Update this variable with the latest Excel file name
    latest_excel_file = "path_to_latest_excel_file.xlsx"
    
    if user_input:
        processed_query = process_query(user_input)
        search_results = search_in_excel(processed_query, latest_excel_file)
        
        st.write("Voici les résultats correspondant à votre recherche :")
        st.write(search_results)

# Run the app
if __name__ == "__main__":
    main()


