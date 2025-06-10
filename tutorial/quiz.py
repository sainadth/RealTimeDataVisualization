import streamlit as st

st.title("Streamlit Tutorials Quiz")

st.header("Quiz 1: Title")
q1 = st.radio(
    "Which Streamlit function displays a title at the top of the app?",
    ["st.header()", "st.title()", "st.write()", "st.caption()"],
    key="q1"
)
if st.button("Check Q1", key="b1"):
    if q1 == "st.title()":
        st.success("Correct! st.title() displays the main title.")
    else:
        st.error("Incorrect. The correct answer is st.title().")

st.header("Quiz 2: DataFrame Display")
q2 = st.radio(
    "Which function shows a DataFrame as an interactive table?",
    ["st.table()", "st.dataframe()", "st.write()", "st.metric()"],
    key="q2"
)
if st.button("Check Q2", key="b2"):
    if q2 == "st.dataframe()":
        st.success("Correct! st.dataframe() is interactive.")
    else:
        st.error("Incorrect. The correct answer is st.dataframe().")

st.header("Quiz 3: Text Input")
q3 = st.radio(
    "How do you get text input from a user?",
    ["st.text()", "st.text_input()", "st.write()", "st.caption()"],
    key="q3"
)
if st.button("Check Q3", key="b3"):
    if q3 == "st.text_input()":
        st.success("Correct! st.text_input() collects user text input.")
    else:
        st.error("Incorrect. The correct answer is st.text_input().")

st.header("Quiz 4: Columns")
q4 = st.radio(
    "Which Streamlit function is used to create columns?",
    ["st.sidebar()", "st.columns()", "st.container()", "st.metric()"],
    key="q4"
)
if st.button("Check Q4", key="b4"):
    if q4 == "st.columns()":
        st.success("Correct! st.columns() creates columns for layout.")
    else:
        st.error("Incorrect. The correct answer is st.columns().")

st.header("Quiz 5: Caching")
q5 = st.radio(
    "What decorator is used to cache data loading functions in Streamlit?",
    ["@st.cache_data", "@st.cache", "@st.memo", "@st.cache_resource"],
    key="q5"
)
if st.button("Check Q5", key="b5"):
    if q5 == "@st.cache_data":
        st.success("Correct! @st.cache_data is used for caching data functions.")
    else:
        st.error("Incorrect. The correct answer is @st.cache_data.")

st.header("Quiz 6: Metrics")
q6 = st.radio(
    "Which Streamlit function is used to display a KPI or metric value?",
    ["st.metric()", "st.write()", "st.caption()", "st.table()"],
    key="q6"
)
if st.button("Check Q6", key="b6"):
    if q6 == "st.metric()":
        st.success("Correct! st.metric() displays a metric or KPI.")
    else:
        st.error("Incorrect. The correct answer is st.metric().")

st.header("Quiz 7: Container")
q7 = st.radio(
    "What is the purpose of st.container() in Streamlit?",
    [
        "To group related elements together",
        "To cache data",
        "To create columns",
        "To create a sidebar"
    ],
    key="q7"
)
if st.button("Check Q7", key="b7"):
    if q7 == "To group related elements together":
        st.success("Correct! st.container() groups related elements.")
    else:
        st.error("Incorrect. The correct answer is: To group related elements together.")

st.header("Quiz 8: Form")
q8 = st.radio(
    "What does st.form() do in a Streamlit app?",
    [
        "Creates a form that only runs code when submitted",
        "Displays a DataFrame",
        "Creates a sidebar",
        "Displays a metric"
    ],
    key="q8"
)
if st.button("Check Q8", key="b8"):
    if q8 == "Creates a form that only runs code when submitted":
        st.success("Correct! st.form() collects input and runs code on submit.")
    else:
        st.error("Incorrect. The correct answer is: Creates a form that only runs code when submitted.")

st.header("Quiz 9: Session State")
q9 = st.radio(
    "How do you store and update variables across user interactions in Streamlit?",
    [
        "Using global variables",
        "Using st.session_state",
        "Using st.write",
        "Using st.metric"
    ],
    key="q9"
)
if st.button("Check Q9", key="b9"):
    if q9 == "Using st.session_state":
        st.success("Correct! st.session_state is used for persistent variables.")
    else:
        st.error("Incorrect. The correct answer is: Using st.session_state.")

st.header("Quiz 10: Map")
q10 = st.radio(
    "Which function displays a DataFrame with latitude and longitude on a map?",
    [
        "st.map()",
        "st.write()",
        "st.table()",
        "st.metric()"
    ],
    key="q10"
)
if st.button("Check Q10", key="b10"):
    if q10 == "st.map()":
        st.success("Correct! st.map() displays geographic data on a map.")
    else:
        st.error("Incorrect. The correct answer is: st.map().")

st.header("Quiz 11: Download Button")
q11 = st.radio(
    "Which Streamlit function allows users to download data as a file?",
    ["st.download_button()", "st.button()", "st.write()", "st.metric()"],
    key="q11"
)
if st.button("Check Q11", key="b11"):
    if q11 == "st.download_button()":
        st.success("Correct! st.download_button() lets users download files.")
    else:
        st.error("Incorrect. The correct answer is st.download_button().")

st.header("Quiz 13: Area Chart")
q13 = st.radio(
    "Which function creates an area chart in Streamlit?",
    ["st.area_chart()", "st.line_chart()", "st.bar_chart()", "st.write()"],
    key="q13"
)
if st.button("Check Q13", key="b13"):
    if q13 == "st.area_chart()":
        st.success("Correct! st.area_chart() creates an area chart.")
    else:
        st.error("Incorrect. The correct answer is st.area_chart().")

st.header("Quiz 14: Plotly Chart")
q14 = st.radio(
    "How do you display a Plotly figure in Streamlit?",
    [
        "st.plotly_chart(fig)",
        "st.write(fig)",
        "st.table(fig)",
        "st.metric(fig)"
    ],
    key="q14"
)
if st.button("Check Q14", key="b14"):
    if q14 == "st.plotly_chart(fig)":
        st.success("Correct! st.plotly_chart(fig) displays Plotly figures.")
    else:
        st.error("Incorrect. The correct answer is st.plotly_chart(fig).")

st.header("Quiz 15: Text Area")
q15 = st.radio(
    "Which widget lets users enter multi-line text?",
    ["st.text_area()", "st.text_input()", "st.write()", "st.caption()"],
    key="q15"
)
if st.button("Check Q15", key="b15"):
    if q15 == "st.text_area()":
        st.success("Correct! st.text_area() is for multi-line text input.")
    else:
        st.error("Incorrect. The correct answer is st.text_area().")

st.header("Quiz 16: Number Input")
q16 = st.radio(
    "Which widget is used for numeric input?",
    ["st.number_input()", "st.text_input()", "st.slider()", "st.metric()"],
    key="q16"
)
if st.button("Check Q16", key="b16"):
    if q16 == "st.number_input()":
        st.success("Correct! st.number_input() is for numeric input.")
    else:
        st.error("Incorrect. The correct answer is st.number_input().")

st.header("Quiz 17: Markdown")
q17 = st.radio(
    "How do you display formatted text (bold, italics, links) in Streamlit?",
    ["st.markdown()", "st.write()", "st.caption()", "st.table()"],
    key="q17"
)
if st.button("Check Q17", key="b17"):
    if q17 == "st.markdown()":
        st.success("Correct! st.markdown() supports formatted text.")
    else:
        st.error("Incorrect. The correct answer is st.markdown().")

st.header("Quiz 18: LaTeX")
q18 = st.radio(
    "Which function is used to render mathematical expressions?",
    ["st.latex()", "st.write()", "st.caption()", "st.metric()"],
    key="q18"
)
if st.button("Check Q18", key="b18"):
    if q18 == "st.latex()":
        st.success("Correct! st.latex() renders math expressions.")
    else:
        st.error("Incorrect. The correct answer is st.latex().")

st.header("Quiz 19: JSON Display")
q19 = st.radio(
    "How do you display a JSON object in a pretty format?",
    ["st.json()", "st.write()", "st.table()", "st.metric()"],
    key="q19"
)
if st.button("Check Q19", key="b19"):
    if q19 == "st.json()":
        st.success("Correct! st.json() displays JSON prettily.")
    else:
        st.error("Incorrect. The correct answer is st.json().")

st.header("Quiz 20: Static Table")
q20 = st.radio(
    "Which function displays a static (non-interactive) table?",
    ["st.table()", "st.dataframe()", "st.write()", "st.metric()"],
    key="q20"
)
if st.button("Check Q20", key="b20"):
    if q20 == "st.table()":
        st.success("Correct! st.table() shows a static table.")
    else:
        st.error("Incorrect. The correct answer is st.table().")
