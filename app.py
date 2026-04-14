import streamlit as st
import pandas as pd

st.set_page_config(page_title="Infinity Defeater", page_icon="♾️")

st.title("♾️ Cantor's Diagonal Defeater")
st.write("### Can you list every decimal? I bet you can't.")

# Sidebar for controls
st.sidebar.header("Challenge Settings")
num_rows = st.sidebar.slider("How many numbers in your 'infinite' list?", 5, 20, 5)

# Initialize list in session state
if 'user_nums' not in st.session_state:
    st.session_state.user_nums = [f"0.{i*11111:05d}"[:7] for i in range(1, 21)]

# Create inputs
updated_list = []
cols = st.columns(1)
for i in range(num_rows):
    val = st.text_input(f"Decimal {i+1}", value=st.session_state.user_nums[i], key=f"input_{i}")
    updated_list.append(val)

if st.button("EXECUTE DIAGONAL DEFEAT"):
    new_num = "0."
    diagonal_info = []
    
    for i in range(len(updated_list)):
        # Extract digit (i+2 because of '0.')
        try:
            current_digit = updated_list[i][i+2]
            replacement = "5" if current_digit != "5" else "4"
            new_num += replacement
            diagonal_info.append(current_digit)
        except IndexError:
            new_num += "9" # Safety for short inputs
            
    st.success(f"### DEFEATED! You missed: {new_num}")
    
    # Data Scientist Flex: Show the logic
    explanation_df = pd.DataFrame({
        "Your List": updated_list,
        "Digit at Diagonal": diagonal_info,
        "My Replacement": list(new_num[2:])
    })
    st.table(explanation_df)
    
    st.balloons()
