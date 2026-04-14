import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Infinity Defeater", page_icon="♾️")

st.title("♾️ Cantor's Diagonal Defeater")
st.write("### Can you list every decimal? I bet you can't.")

# Sidebar for controls
st.sidebar.header("Challenge Settings")
num_rows = st.sidebar.slider("How many numbers in your 'infinite' list?", 5, 20, 5)

# --- Data Scientist Mind: Automation ---
if st.sidebar.button("🔀 Randomize My List"):
    # Generate random decimals for the current number of rows
    st.session_state.user_nums = [f"0.{random.randint(1000000000, 9999999999)}" for _ in range(20)]

# Initialize list in session state if it doesn't exist
if 'user_nums' not in st.session_state:
    st.session_state.user_nums = [f"0.{i*1111111111}"[:12] for i in range(1, 21)]

# Create inputs dynamically using the session state
updated_list = []
for i in range(num_rows):
    val = st.text_input(f"Decimal {i+1}", value=st.session_state.user_nums[i], key=f"input_{i}")
    updated_list.append(val)

if st.button("EXECUTE DIAGONAL DEFEAT"):
    new_num_digits = []
    diagonal_info = []
    
    for i in range(len(updated_list)):
        try:
            # Logic: If input is short, treat missing digits as '0'
            current_digit = updated_list[i][i+2] if len(updated_list[i]) > i+2 else "0"
            
            # The Mutation Logic
            replacement = "5" if current_digit != "5" else "4"
            new_num_digits.append(replacement)
            diagonal_info.append(current_digit)
        except Exception:
            new_num_digits.append("9")
            diagonal_info.append("?")
            
    final_missing_num = "0." + "".join(new_num_digits)
    st.success(f"### DEFEATED! You missed: {final_missing_num}")
    
    # Show the proof table
    explanation_df = pd.DataFrame({
        "Your List": updated_list,
        "Digit at Diagonal": diagonal_info,
        "My Replacement": new_num_digits
    })
    st.table(explanation_df)
    st.balloons()
   
