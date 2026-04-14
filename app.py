import streamlit as st
import pandas as pd

st.set_page_config(page_title="Infinity Defeater", page_icon="♾️")

st.title("♾️ Cantor's Diagonal Defeater")
st.write("### Can you list every decimal? I bet you can't.")

# Sidebar for controls
st.sidebar.header("Challenge Settings")
num_rows = st.sidebar.slider("How many numbers in your 'infinite' list?", 5, 20, 5)

# Create inputs dynamically
updated_list = []
for i in range(num_rows):
    # Default values that are long enough for the diagonal
    default_val = f"0.{str(i+1)*10}"[:12] 
    val = st.text_input(f"Decimal {i+1}", value=default_val, key=f"input_{i}")
    updated_list.append(val)

if st.button("EXECUTE DIAGONAL DEFEAT"):
    new_num_digits = []
    diagonal_info = []
    
    for i in range(len(updated_list)):
        # Extract digit (i+2 because of '0.')
        try:
            # If the user input is too short, we'll assume the digit is '0'
            current_digit = updated_list[i][i+2] if len(updated_list[i]) > i+2 else "0"
            
            replacement = "5" if current_digit != "5" else "4"
            new_num_digits.append(replacement)
            diagonal_info.append(current_digit)
        except Exception:
            new_num_digits.append("9")
            diagonal_info.append("?")
            
    final_missing_num = "0." + "".join(new_num_digits)
    st.success(f"### DEFEATED! You missed: {final_missing_num}")
    
    # Data Scientist Fix: Ensuring all arrays are the same length for the table
    explanation_df = pd.DataFrame({
        "Your List": updated_list,
        "Digit at Diagonal": diagonal_info,
        "My Replacement": new_num_digits
    })
    st.table(explanation_df)
    
    st.balloons()
   
