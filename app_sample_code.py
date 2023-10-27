
# Import Streamlit
import streamlit as st

# Main function for the app
def main():
    # Load logo and display it
    st.image("assets/logo.png", width=300)
    
    # Display friendly message and search box
    st.write("Bonjour! Comment puis-je vous aider aujourd'hui?")
    user_input = st.text_input("Entrez votre recherche ici...")
    
    # Placeholder for displaying results
    if user_input:
        st.write("Les résultats pour votre recherche seront affichés ici.")
        
# Run the app
if __name__ == "__main__":
    main()
