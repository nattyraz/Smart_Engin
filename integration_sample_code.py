
# Import Streamlit and custom NLP module
import streamlit as st
import traitement_langage_naturel as nlp  # Make sure to place traitement_langage_naturel.py in the same directory or adjust the import

# Main function for the app
def main():
    # Load logo and display it
    st.image("assets/logo.png", width=300)
    
    # Display friendly message and search box
    st.write("Bonjour! Comment puis-je vous aider aujourd'hui?")
    user_input = st.text_input("Entrez votre recherche ici...")
    
    # Process the user query and display results
    if user_input:
        # Process the query using custom NLP module
        criteria = nlp.process_query(user_input)
        
        # Search in Excel based on the criteria and get results
        search_results = nlp.search_in_excel(criteria)
        
        # Display the search results
        st.write("Voici les résultats correspondant à votre recherche :")
        st.write(search_results)

# Run the app
if __name__ == "__main__":
    main()
