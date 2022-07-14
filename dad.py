import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

st.title('아빠를 위한 줄바꿈 캐릭터 없애기')

left_column, right_column = st.columns(2)

with left_column:
    st.text_area("입력 텍스트", height=512, key="text")

edited_text = st.session_state.text.replace("\n\n", "#뜀#").replace("\n", "").replace("#뜀#", "\n")

with right_column:
    st.write("출력 텍스트")
    st.write(edited_text)

    copy_button = Button(label="복사하기")
    copy_button.js_on_event("button_click", CustomJS(args=dict(edited_text=edited_text), code="""
        navigator.clipboard.writeText(edited_text);
        """))

    no_event = streamlit_bokeh_events(
        copy_button,
        events="GET_TEXT",
        key="get_text",
        refresh_on_update=True,
        override_height=75,
        debounce_time=0)
