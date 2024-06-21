from pathlib import Path 

import streamlit as st
from PIL import Image


#----PATH SETTINGS----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Emmanuel's Resume (1).pdf"
profile_pic = current_dir / "assets" / "pfpic.png"


#----GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Emmanuel Warega"
PAGE_ICON = ":wave:"
NAME = "Emmanuel Warega"
DESCRIPTION = """
WebBuilder, App builder and Junior Data Analyst.
"""
EMAIL = "emmezwarega@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello there!")



#---LOADING THE CSS, PDF & PROFIL PIC----
with open(css_file) as f:
	st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
	PDFbyte = pdf_file.read()
	profile_pic = Image.open(profile_pic)


#----HERO SECTION ---

col1, col2 = st.columns(2, gap="small")
with col1:
	st.image(profile_pic, width=280)

with col2:
	st.title(NAME)
	st.write(DESCRIPTION)
	st.download_button(
		label= "📄 Download Resume",
		data=PDFbyte,
		file_name=resume_file.name,
		mime = "application/octet-stream",
)
	st.write("📬", EMAIL)


#----SOCIAL LINKS---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
	cols[index].write(f"[{platform}]({link})")


	#----EXPERIENCE & QUALIFICATIONS----
st.write("#")
st.subheader("Experience and Qualifications")
st.write(
	"""
	- ✅ Good understanding on webapp building using python and dart languages.
	- ✅ Upcoming data analytical knowledge and skills in python.
	- ✅ A strong team player. 
	- ✅ A powerful zeal to learn and accomplish tasks effectively.
	"""
	)

	#----SKILLS----
st.write("#")
st.subheader("Hard Skills")
st.write(
"""
	-💻 Programming: Python, SQL, Dart.

	-📈 Data Visualization: MS Excel.

	-Database: MySQLite, Firebase.
"""
)
