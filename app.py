from pathlib import Path

import streamlit as st
from PIL import Image


#----------Path Settings----------
current_dir = Path(__file__).parent if "__file__"in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "NicoleLai_Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


#----------General Settings----------
PAGE_TITLE = "Digital CV | Nicole Lai"
PAGE_ICON = ":wave:"
NAME = "Nicole Lai"
DESCRIPTION = """
Fresh Gradute of Bachelor Degree in Computer Science of Software Engineering
"""

EMAIL = "lsihua411@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/nicole-laish/",
    "GitHub": "https://github.com/nlsh0411"
}

PROJECTS = {
    "GoScooter_Mobile": "https://github.com/nlsh0411/GoScoot_Mobile"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# st.title("Hello There!!!")

#----------Load CSS, PDF & PROFILE PIC---------- 
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


#----------Resuming Details Section----------
col1, col2 = st.columns(2, gap="small")
#Profile Picture Column
with col1:
    st.image(profile_pic, width=230)

#Resume Details + Download Resume Button
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


#----------Social Media Section(horizontal)----------
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA)) #Count the Num of Link Provided Above
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#----------Eeperience & Qualification Section----------
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("---")
st.write(
    """
- ✔️ Final Project Development in Website & Mobile Application 
- ✔️ 3 months Assistant PMO Intern Expereince in Silverlake Digitale Sdn Bhd
- ✔️ 6 months Mobile Developer Intern Expereince in Maxwell Cloud Technology Sdn Bhd
- ✔️ Strong hands on experience and knowledge in JavaScript and React Framework
- ✔️ Good understanding of Software Development especially Mobile
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


#----------Skills----------
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: HTML | CSS | JavaScript | Kotlin | Java
- 👩‍💻 Framework: React | Next.js
- 🗄️ Databases: MySQL | SQL | Firebase | Supabase
"""
)


#----------Work History----------
st.write('\n')
st.subheader("Work History")
st.write("---")

#Job 1
st.write("- 🚧", "**Mobile Developer Intern | Maxwell Cloud Technology Sdn Bhd**")
st.write("- 🗓️","02/2024 - 08/2024")
st.write(
    """
- ► Used React Redux to Develop the Mobile Application
"""
)

#Job 2
st.write('\n')
st.write("- 🚧", "**Assitant PMO Intern | Silverlake Digitale Sdn Bhd**")
st.write("- 🗓️", "10/2021 – 01/2022")
st.write(
    """
- ► Capture logs from a website at 12pm and 4pm, and promptly share it with the specifies WhatsApp group
- ► Prepare 3 end-of-day reports at 8pm, focusing on logging activities. Included tables and images to track the daily log volume and integrate information received from email with team members
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"-🗎 [{project}]({link})")