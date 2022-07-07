import streamlit as st
import pyperclip

lorem = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum'''

st.title('Removing New Line Characters for Dad')

left_column, right_column = st.columns(2)

with left_column:
    st.text_area("Input Text", value=lorem, height=512, key="text")

edited_text = st.session_state.text.replace("\n", "")

with right_column:
    st.write("Output Text")
    st.write(edited_text)
    if st.button('Copy to Clipboard'):
        pyperclip.copy(edited_text)
