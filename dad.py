import streamlit as st
import pyperclip

st.title('아빠를 위한 줄바꿈 캐릭터 없애기')

left_column, right_column = st.columns(2)

with left_column:
    st.text_area("입력 텍스트", height=512, key="text")

edited_text = st.session_state.text.replace("\n", "")

with right_column:
    st.write("출력 텍스트")
    st.write(edited_text)
    if st.button('복사하기'):
        pyperclip.copy(edited_text)