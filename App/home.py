import streamlit as st
from PIL import Image

with open("App/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
import streamlit as st

import streamlit as st

st.write('''
# **Dewi Adelia Priyono** :fairy:
''') 
st.write('''
#### *Hi I'm Adel :wave:*
''')  
st.write("I am a computer science undergraduate student at UGM with experience in the tech, reinsurance, and consulting sectors. I have a strong foundation in data mining, big data processing, and data pipelining, with hands-on experience in Python and SQL, as well as working with Apache Hadoop and Apache Spark. Additionally, I have some experience with cloud computing tools such as Oracle, Google Cloud and AWS. I am continually seeking opportunities to broaden my horizons and enhance my skills before embarking on my professional career upon graduation.")

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #5D4A69;">
  <a class="navbar-brand" target="_blank">Dewi Adelia Priyono</a>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experience">Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#documentation">Documentation</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelor Degree in Computer Science**, *Universitas Gadjah Mada*, Indonesia','*2022-Present*')
st.markdown('''
- GPA: `3.76`
- Elective Courses:  `Genetic Algorithm, Big Data Analytics, Big Data Architecture, DataCenter Development, Digital Image Processing`
- Competitions: `UGM Gemastik Data Mining Delegate 2023, UGM Satria Data Big Data Challenge Delegate 2023, DataQuest Universitas Airlangga 2023, DSW Telkomsel 2023`
- Awards: `Talent Scouting Academy Digital Talent Scholarship (TSA DTS) - Oracle Cloud by KOMINFO`    
''')


#####################
st.markdown('''
## Experience
''')

txt('**Head, Big Data Division KOMASTAGAMA**, UGM',
'*Present*')
st.markdown('''
- Spearheaded the design and implementation of a comprehensive division learning plan, fostering skill development and knowledge sharing among a diverse community of 60+ members. 
- Led a dedicated internal team of 5 members in the routine evaluation of machine learning and data models, ensuring alignment with project objectives and quality standards.
- Collaborated with esteemed lecturers to conduct cutting-edge research on emerging trends in data processing tools and methodologies.
''')

txt('**Research Leader,  180 Degrees Consulting UGM**, UGM',
'*2023-2024*')
st.markdown('''
- Led cross-functional teams of 7 professionals to optimize product development processes through comprehensive data analysis.
- Evaluated over 5 business cases and collaborated on 2 industry projects with NGOs and startup companies.
- Delivered data-driven strategic blueprints and impact analyses, providing stakeholders with valuable insights to guide strategic decision-making processes.
''')

txt('**Staff, Data Mining and Artificial Intelligence**, KOMATIKUGM, UGM',
'2023-2024')
st.markdown('''
- Built and deployed predictive models and algorithms across diverse datasets, driving improved data
 accuracy and effectiveness
- Conducted research for novel AI technologies, leveraging various datasets to fuel cutting-edge solutions.
- Captained a research team called “Byte Benders” to 5+ Data and AI competitions on national and
 international level in 2023
''')

txt('**Regional Leader**, Generation Girl, Yogyakarta',
'2022-2023')
st.markdown('''
- Led Generation Girl Jogja's operational team, ensuring smooth execution of programs and collaborating
  with local partners like SkinGame and Innovative Academy UGM to deliver impactful STEM resources.
- Designed and piloted Electives, a work-ready program in partnership with Gojek, empowering 240+
 STEM-focused girls annually through bootcamps, webinars, and competitions.
-  Championed STEM inclusion by launching impactful initiatives, attracting 20-30 girls monthly to
 Generation Girl Jogjakarta for the past 1 year.
''')

#####################
st.markdown('''
## Documentation
''')
# Creating three columns for the images and titles
col1, col2, col3, col4= st.columns(4)
col5, col6, col7, col8= st.columns(4)

with col1:
    st.image("dokum/1.jpg", use_column_width=True)
with col2:
    st.image("dokum/2.jpg", use_column_width=True)
with col3:
    st.image("dokum/3.jpg", use_column_width=True)
with col4:
    st.image("dokum/4.jpg", use_column_width=True)
with col5:
    st.image("dokum/5.jpg", use_column_width=True)
with col6:
    st.image("dokum/6.jpg", use_column_width=True)
with col7:
    st.image("dokum/7.jpg", use_column_width=True)
with col8:
    st.image("dokum/8.jpg", use_column_width=True)


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `C++`, `Java`')
txt3('Data processing/wrangling', '`Sparks`,`SQL`, `pandas`, `numpy`, `Hadoop`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`HTML`, `CSS`')
txt3('Model deployment', '`streamlit`')
txt3('Cloud environment', '`Oracle`, `AWS`, `Google Cloud`')

#####################
st.markdown('''
## Projects''')

# Creating three columns for the images and titles
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.image("image/LSTM.jpg", use_column_width=True)
    st.markdown("[Stock Analysis](https://github.com/adeliiee22/Projects/tree/main/Stocks%20Analysis%20LSTM)", unsafe_allow_html=True)

with col2:
    st.image("image/telecom.jpg", use_column_width=True)
    st.markdown("[Churn](https://github.com/adeliiee22/Projects/tree/main/Telecom%20Churn)", unsafe_allow_html=True)

with col3:
    st.image("image/Chest.jpg", use_column_width=True)
    st.markdown("[Chest Cancer Detection](https://github.com/adeliiee22/Projects/tree/main/Chest%20Cancer%20Detection/Notebook)", unsafe_allow_html=True)

with col4:
    st.image("image/perpus.jpg", use_column_width=True)
    st.markdown("[Perpus UIN WebApp](http://158.178.244.40/)", unsafe_allow_html=True)


#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/priyonoadelia/')
txt2('Email', 'priyonoadelia@gmail.com')
