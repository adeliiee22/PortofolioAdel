import streamlit as st

# Load custom CSS
with open("App/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Education and Awards", "Work Experience", "Organization", "Projects", "Contact"])

if page == "Home":
    # Home Page
    st.write('''
    # **[Dewi Adelia Priyono](https://www.linkedin.com/in/priyonoadelia/)** :fairy:
    ''')
    st.write('''
    #### *Hi I'm Adel :wave:*
    ''')  
    st.write("A computer science student at UGM with experience in tech, reinsurance, and consulting. Skilled in data mining, big data processing, and data pipelining using Python, SQL, Hadoop, and Spark. Experienced with cloud computing and database tools like Oracle, Firebase, and AWS. Eager to expand my knowledge and skills before starting my professional career.")

    # Creating three columns for the images and titles
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)

    with col1:
        st.image("App/dokum/1.jpg", use_column_width=True)
    with col2:
        st.image("App/dokum/2.jpg", use_column_width=True)
    with col3:
        st.image("App/dokum/3.jpg", use_column_width=True)
    with col4:
        st.image("App/dokum/4.jpg", use_column_width=True)
    with col5:
        st.image("App/dokum/5.jpg", use_column_width=True)
    with col6:
        st.image("App/dokum/6.jpg", use_column_width=True)
    with col7:
        st.image("App/dokum/7.jpg", use_column_width=True)
    with col8:
        st.image("App/dokum/8.jpg", use_column_width=True)  

elif page == "Education and Awards":
    # Education Page
    st.markdown('## Education')

    # Degree information
    st.markdown("""
    <div style="display: flex; justify-content: space-between;">
        <span><strong>Bachelor Degree in Computer Science</strong>, UGM, Indonesia</span>
        <span>2022-Present</span>
    </div>
    """, unsafe_allow_html=True)

    # GPA
    st.markdown("- GPA: `3.57`")

    # Create columns for Elective Courses
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Elective Courses:**")
        st.markdown("""
        - Genetic Algorithm  
        - Big Data Analytics  
        - Big Data Architecture  
        """)

    with col2:
        st.markdown("**  **")
        st.markdown(""" 
        - DataCenter Development  
        - Digital Image Processing
        """)

    st.markdown('## Awards')

    # Awards section
    st.markdown("""
    - Runner Up Internal Case Competition 180DC UGM 2023  
    - 1st Place APWINC Digital Hackathon 2024  
    - Best Participant Talent Scouting Academy Digital Talent Scholarship (TSA DTS) - Oracle Cloud 2024 by KOMINFO  
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("App/Award/1.jpg", use_column_width=True)
    with col2:
        st.image("App/Award/2.jpg", use_column_width=True)
    with col3:
        st.image("App/Award/3.jpg", use_column_width=True)



elif page == "Work Experience":
    # Work Experience Page
    st.markdown('## Work Experience')

    def txt(a, b):
        col1, col2 = st.columns([4,1])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)

    txt('**Data Engineer Intern**, Ucoal Resources', '*Jul 2024 - Sep 2024*')
    st.markdown('''
    - Built a robust data pipeline from MongoDB for 50k+ records, including extraction, cleaning, and preparation, to support comprehensive product and data analysis.
    - Established data connections between a cloud database and Jupyter Notebook using PySpark, and implemented time series prediction models to analyze coal production trends.
    - Created data transformation formulas in Excel for Power BI dashboards, and handled fraud detection in the hauling system for day-to-day monitoring of coal production.
    ''')

    txt('**Data Annotator**, KUPU ID', '*Apr 2024 - Jun 2024*')
    st.markdown('''
    - Led a comprehensive data labeling and verification project for ChatGPT-4, focusing on 500+ video and image datasets.
    - Verified data quality, completeness, and reliability to enhance model accuracy and performance.
    - Conducted thorough validation processes to improve data integrity and annotation consistency.
    ''')

elif page == "Organization":
    # Organization Page
    st.markdown('## Organization')

    def txt(a, b):
        col1, col2 = st.columns([4,1])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)

    txt('**Head, Big Data Division KOMASTAGAMA**, UGM', '*Jan 2024 - July 2024*')
    st.markdown('''
    - Spearheaded the design and implementation of a comprehensive division learning plan, fostering skill development and knowledge sharing among a diverse community of 60+ members. 
    - Led a dedicated internal team of 5 members in the routine evaluation of machine learning and data models, ensuring alignment with project objectives and quality standards.
    - Collaborated with esteemed lecturers to conduct cutting-edge research on emerging trends in data processing tools and methodologies.
    ''')

    txt('**Research Leader, 180 Degrees Consulting UGM**, UGM', '*Aug 2023 - Jun 2024*')
    st.markdown('''
    - Led cross-functional teams of 7 professionals to optimize product development processes through comprehensive data analysis.
    - Evaluated over 5 business cases and collaborated on 2 industry projects with NGOs and startup companies.
    - Delivered data-driven strategic blueprints and impact analyses, providing stakeholders with valuable insights to guide strategic decision-making processes.
    ''')

    txt('**Staff, Data Mining and Artificial Intelligence**, KOMATIK, UGM', '*Feb 2023 - Apr 2024*')
    st.markdown('''
    - Built and deployed predictive models and algorithms across diverse datasets, driving improved data accuracy and effectiveness.
    - Conducted research for novel AI technologies, leveraging various datasets to fuel cutting-edge solutions.
    - Captained a research team called “Byte Benders” to 5+ Data and AI competitions on national and international level in 2023.
    ''')

    txt('**Regional Leader**, Generation Girl, Yogyakarta', '*Jun 2022 - Jun 2023*')
    st.markdown('''
    - Led Generation Girl Jogja's operational team, ensuring smooth execution of programs and collaborating with local partners like SkinGame and Innovative Academy UGM to deliver impactful STEM resources.
    - Designed and piloted Electives, a work-ready program in partnership with Gojek, empowering 240+ STEM-focused girls annually through bootcamps, webinars, and competitions.
    - Championed STEM inclusion by launching impactful initiatives, attracting 20-30 girls monthly to Generation Girl Jogjakarta for the past 1 year.
    ''')

elif page == "Projects":
    # Projects Page
    st.markdown('## Projects')

    # Creating columns for the project images and titles
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)

    with col1:
      st.image("App/image/LSTM.jpg", use_column_width=True)
      st.markdown("[Stock Analysis](https://github.com/adeliiee22/Projects/tree/main/Stocks%20Analysis%20LSTM)", unsafe_allow_html=True)
      st.markdown("""
      - Utilized the Long Short-Term Memory (LSTM) technique to predict stock price trends, training the model with data sourced from Yahoo Finance to ensure accurate forecasts.
      - Achieved a Mean Absolute Percentage Error (MAPE) of 4.62%, using the LSTM model. Significantly outperforming the 50-day and 200-day moving averages, which had MAPEs of 10.87%, and 16.73%, respectively.
      """)


    with col2:
        st.image("App/image/telecom.jpg", use_column_width=True)
        st.markdown("[Churn](https://github.com/adeliiee22/Projects/tree/main/Telecom%20Churn)", unsafe_allow_html=True)
        st.markdown("""
        - Developed a predictive model using logistic regression in PySpark to analyze and predict customer churn for a telecommunications company.
        - Achieved an Area Under the Receiver Operating Characteristic (ROC) curve of 0.728 and attained an accuracy of 64.83% in correctly predicting customer churn, demonstrating the model's effectiveness in real-world scenarios..
        """)

    with col3:
        st.image("App/image/Chest.jpg", use_column_width=True)
        st.markdown("[Chest Cancer Detection](https://github.com/adeliiee22/Projects/tree/main/Chest%20Cancer%20Detection/Notebook)", unsafe_allow_html=True)
        st.markdown("""
        - Utilized the Kaggle Chest CT-Scan Dataset to detect chest cancer from CT scan images using Functional API and Transfer Learning techniques.
        - Employed MobileNetV2 as the base model to enhance learning efficiency and accuracy in identifying cancerous tissues.
        - Achieved a categorical accuracy of 90.55% with a training loss of 0.3026, and validated the model with a loss of 0.4703, demonstrating high predictive accuracy and model robustness.
        """)

    with col4:
        st.image("App/image/Perpus.jpg", use_column_width=True)
        st.markdown("[Perpus UIN WebApp](http://158.178.244.40/)", unsafe_allow_html=True)
        st.markdown("""
        - Developed a library management web application using the Laravel framework, hosted on an always-free VM instance on Oracle Cloud to ensure cost-effective scalability.
        - Integrated the application with Oracle Autonomous Database, leveraging its advanced features for reliable data management and high availability.
        """)

    with col5:
        st.image("App/image/Fraud.jpg", use_column_width=True)
        st.markdown("[Credit Card Fraud Detection](https://github.com/adeliiee22/Projects/tree/main/Credit%20card%20fraud%20detection/Notebook)", unsafe_allow_html=True)
        st.markdown("""
        - Created a credit card fraud detection implementation using PySpark, leveraging StandardScaler and VectorAssembler to preprocess data for machine learning.
        - Achieved a high Area Under ROC (0.973) and an accuracy of 99.92%, demonstrating strong performance in distinguishing between fraud and non-fraud transactions.
        """)

    with col6:
        st.image("App/image/EHR.jpg", use_column_width=True)
        st.markdown("[REKMED EHR Mobile App](https://github.com/adeliiee22/EHR-REKMED)", unsafe_allow_html=True)
        st.markdown("""
        - Engineered effective methods for storing and managing medical data by creating a fully functional mobile app using the Flutter framework, emphasizing on product development.
        - Utilized Firebase for authentication, Firestore for database management, and real-time data synchronization to provide secure and efficient handling of medical information within the app.
        """)

    with col7:
        st.image("App/image/Frequent.jpg", use_column_width=True)
        st.markdown("[Frequent Sequence Mining](https://github.com/adeliiee22/Projects/tree/main/Frequent%20Sequence%20Mining)", unsafe_allow_html=True)
        st.markdown("""
        - Utilized PySpark to generate all frequent itemsets from a dataset with a minimum support threshold of 70%, ensuring comprehensive identification of frequent patterns.
        - Applied the Apriori algorithm in PySpark on mushroom data, identifying association rules with confidence levels ranging from 95% to 100%.
        """)

elif page == "Contact":
    # Contact Page
    st.markdown('## Contact')

    def txt2(a, b):
        col1, col2 = st.columns([1,4])
        with col1:
            st.markdown(f'**{a}:**')
        with col2:
            st.markdown(b)

    txt2("LinkedIn", "[Dewi Adelia Priyono](https://www.linkedin.com/in/priyonoadelia/)")
    txt2("Email", "dewiadeliapriyono@mail.ugm.ac.id")
