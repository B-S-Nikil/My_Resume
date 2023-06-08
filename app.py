import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="My Resume",
    page_icon=":tada:",
    layout="wide"
)

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lottie_url = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_wdhfjhyc.json")

# Display the animation in the top right corner

left_column, right_column = st.columns(2)

with st.container():
    with left_column:
        st.title("Nikil B S")
        st.subheader("Computer Science Engineering Graduate")
        st.write("bsnikil2000@gmail.com")
        st.write("7406050759")
        st.write("K S layout, Bengaluru - 560078")
        st.write("[GitHub](https://github.com/B-S-Nikil) | [LinkedIn](https://www.linkedin.com/in/nikil-b-s)")
    with right_column:
        col_animation, _ = st.columns([1, 5])
        st_lottie(lottie_url, width=300, height=300)

st.write("---")

st.header("About")
st.write("As a recent CSE graduate, I am highly motivated and passionate about exploring new technologies and their applications in solving real-world problems.")

st.write("---")

with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("My Skills")
        st.write("- Python\n- Web Applications\n- Cloud Computing Basics\n- Linux\n- Data Analysis\n- Cybersecurity")

    with right_column:
        st.header("Certifications")
        st.write("- Python for Data Analysis: Numpy and Pandas\n"
                 "- Complete SQL Bootcamp\n"
                 "- Linux Fundamentals\n"
                 "- Ethical Hacking Essential")

st.write("---")

st.header("Education")
st.subheader("K S Institute of Technology")
st.write("Bachelor of Engineering")
st.write("GPA: 7.50")

st.subheader("Deeksha Integrated SGPTA PU College")
st.write("12th Grade")
st.write("Percentage: 68%")

st.subheader("Samved School")
st.write("10th Grade")
st.write("Percentage: 88.64%")

st.write("---")

st.header("Projects")

st.subheader("Pharmacy Management System")
st.write("Created a web app that keeps track of pharmacy transactions. Medicines sold, remaining stocks, new items added, etc.")
st.write("Team size: 1")
st.write("Skills: Python (tkinter), dbsqlite")
st.write("GitHub Link: [Pharmacy Management System](https://github.com/B-S-Nikil/Pharmacy-Management-PY)")

st.write("---")

st.subheader("Chronic Kidney Disease (CKD)")
st.write("Developed a machine learning model to predict chronic kidney disease based on clinical data.")
st.write("Team size: 4")
st.write("Skills: Machine Learning")
st.write("GitHub Link: [Chronic Kidney Disease](https://github.com/2021-CS-28/Chronic-Kidney-Disease)")

st.write("---")

st.subheader("2D Boat Simulation")
st.write("Created an OpenGL application that simulates the movement of a boat for user interaction.")
st.write("Team size: 1")
st.write("Skills: C++ (OpenGL)")

st.write("---")

st.subheader("Weather App (Android App)")
st.write("Developed an Android application that retrieves weather details using a 3rd party weather API.")
st.write("Team size: 4")
st.write("Skills: Android Studios (Java, XML)")


with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/bsnikil2000@gmail.com"" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()