import re
import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard

st.title("아빠를 위한 줄바꿈 캐릭터 없애기")

left_column, right_column = st.columns(2)

with left_column:
    st.text_area("입력 텍스트", height=512, key="text")

substituted_text = re.sub("\n(\\*\n+\\*)+", "<뜀>", st.session_state.text)
replaced_text = re.sub("\\*\n+\\*", " ", substituted_text)
edited_text = replaced_text.replace("<뜀>", "\n\n")

with right_column:
    st.write("출력 텍스트")
    st.markdown(edited_text)
    st_copy_to_clipboard(
        edited_text, before_copy_label="복사하기", after_copy_label="복사완료"
    )
