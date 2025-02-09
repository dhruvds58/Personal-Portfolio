import streamlit as st
from streamlit_option_menu import option_menu
from assistants import create_chat_header

# Set Page Configuration
st.set_page_config(page_title="Dhruv Shah Portfolio", page_icon=":briefcase:", layout="wide")

create_chat_header()

# Load CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Work Samples", "Experience"],
    icons=["house", "briefcase", "book"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "10px",
            "background-color": "#121212",
            "border-bottom": "2px solid #333",
            "position": "sticky",
            "top": "0",
            "z-index": "1000",
        },
        "icon": {"color": "#00bfae", "font-size": "22px", "transition": "0.3s"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "color": "#00bfae",
            "text-transform": "uppercase",
            "padding": "15px",
            "border-radius": "5px",
            "transition": "all 0.3s ease-in-out",
        },
        "nav-link:hover": {
            "background-color": "#00bfae",
            "color": "#ffffff",
            "box-shadow": "0px 4px 10px rgba(0, 191, 174, 0.5)",
        },
        "nav-link-selected": {
            "background-color": "#00bfae",
            "color": "#ffffff",
            "font-weight": "bold",
        },
    },
)


# Home Page
# Home Page
if selected == "Home":
    st.markdown(
        """
        <div class="home-container">
            <img src="https://storage.googleapis.com/streamlit-portfolio/Dhruv01.png" class="profile-pic">
            <div class="intro-text">
                <h1>Hi, I'm Dhruv!</h1>
                <p>
                    I have recently earned my Master's in Business Analytics from Boston University and am actively seeking a full-time opportunity as a Data Analyst or Business Intelligence Analyst.
                </p>
                <p>
                    Let me take your data on a journey from raw CSV to "wow, I actually understand what's happening here!"
                </p>
                <p>
                    Curious to know what I’ve worked on? Explore my Work Samples and Professional Experiences sections to see how I bring data to life.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Skills Section
    st.markdown("<div class='section-title'>Skills</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="kpi-container">
            <div class="kpi-card">
                <img src="https://storage.googleapis.com/streamlit-portfolio/pythonlogo.png" alt="Python">
            </div>
            <div class="kpi-card">
                <img src="https://storage.googleapis.com/streamlit-portfolio/sqllogo.png" alt="SQL">
            </div>
            <div class="kpi-card">
                <img src="https://storage.googleapis.com/streamlit-portfolio/powerbilogo.png" alt="Power BI">
            </div>
            <div class="kpi-card">
                <img src="https://storage.googleapis.com/streamlit-portfolio/excellogo.png" alt="Excel">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Work Samples Page
elif selected == "Work Samples":
    st.markdown('<div id="work-samples"></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="work-sample">
            <div class="project-card">
                <a href="https://github.com/dhruvds58/BA882-Strava-Team4" target="_blank">
                    <img src="https://storage.googleapis.com/streamlit-portfolio/Stravaprojectphoto.jpg" alt="Strava">
                    <h5>Data Pipeline Project with Strava API</h5>
                </a>
                <p>Date: Sep 2024 - Dec 2024<br>Skills Utilized: ETL, BigQuery, Superset, Streamlit</p>
            </div>
            <div class="project-card">
                <a href="https://github.com/dhruvds58/Power-BI-Dashboard-for-an-E-Commerce-Website" target="_blank">
                    <img src="https://storage.googleapis.com/streamlit-portfolio/TheLookProjectPhoto.png" alt="E-Commerce">
                    <h5>Power BI Project on “TheLook E-Commerce Dataset Analysis”</h5>
                </a>
                <p>Date: Jul 2024 - Aug 2024<br>Skills Utilized: Power BI, Data Analysis, DAX</p>
            </div>
            <div class="project-card">
                <a href="https://github.com/dhruvds58/Stack-Overflow-Platform-Analysis" target="_blank">
                    <img src="https://storage.googleapis.com/streamlit-portfolio/stackoverflowprojectphoto.png" alt="Stack Overflow">
                    <h5>Stack Overflow Platform Analysis (2008-2022)</h5>
                </a>
                <p>Date: Mar 2024 - May 2024<br>Skills Utilized: PySpark, BigQuery</p>
            </div>
            <div class="project-card">
                <a href="https://github.com/dhruvds58/ISS-Board-of-Directors-Analysis" target="_blank">
                    <img src="https://storage.googleapis.com/streamlit-portfolio/operationsprojectphoto.jpg" alt="Operations">
                    <h5>Operations Project: Board of Directors' Impact on Corporate Performance</h5>
                </a>
                <p>Date: Mar 2024 - May 2024<br>Skills Utilized: Advanced Analytics</p>
            </div>
            <div class="project-card">
                <a href="https://github.com/dhruvds58/boston-housing-experiment" target="_blank">
                    <img src="https://storage.googleapis.com/streamlit-portfolio/bostonhousingprojectphoto.jpeg" alt="Boston Housing">
                    <h5>Business Experimentation Project on Boston Housing</h5>
                </a>
                <p>Date: Feb 2024 - Mar 2024<br>Skills Utilized: Qualtrics, Regression</p>
            </div>
            <div class="project-card">
                <a href="https://github.com/dhruvds58/amazon-book-review-ml-project" target="_blank">
                    <img src="https://storage.googleapis.com/streamlit-portfolio/Amazonbooksprojectphoto.jpg" alt="Amazon Books">
                    <h5>Natural Language Processing on Amazon Books Reviews Dataset</h5>
                </a>
                <p>Date: Feb 2024 - Mar 2024<br>Skills Utilized: NLP, Clustering</p>
            </div>
            <div class="project-card">
                <a href="https://github.com/dhruvds58/Soccer-Player-Analysis" target="_blank">
                    <img src="https://storage.googleapis.com/streamlit-portfolio/soccerprojectphoto.jpg" alt="Soccer Analysis">
                    <h5>Python Project on “Soccer Player Analytics”</h5>
                </a>
                <p>Date: Dec 2023 - Jan 2024<br>Skills Utilized: Python, Data Cleaning, Data Vizualisation</p>
            </div>
            <div class="project-card">
                <a href="https://github.com/dhruvds58/Airbnb-Price-Prediction" target="_blank">
                    <img src="https://storage.googleapis.com/streamlit-portfolio/airbnbprojectphoto.jpg" alt="Airbnb Prediction">
                    <h5>Airbnb Price Prediction</h5>
                </a>
                <p>Date: Nov 2023 - Dec 2023<br>Skills Utilized: Supervised Machine Learning</p>
            </div>
            <div class="project-card">
                <a href="https://github.com/dhruvds58/Steam-Library-Analysis" target="_blank">
                    <img src="https://storage.googleapis.com/streamlit-portfolio/steamprojectphoto.png" alt="Steam Library">
                    <h5>Steam Library Analysis</h5>
                </a>
                <p>Date: Nov 2023 - Dec 2023<br>Skills Utilized: SQL, Tableau</p>
            </div>
            <div class="project-card">
                <a href="https://github.com/dhruvds58/Global-Gift-Giving-Behavior-Analysis" target="_blank">
                    <img src="https://storage.googleapis.com/streamlit-portfolio/giftprojectphoto.jpg" alt="Gift Behavior">
                    <h5>Analytics Project on “Global Gift Giving Behavior”</h5>
                </a>
                <p>Date: Sep 2023 - Oct 2023<br>Skills Utilized: Python, EDA</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
# Experience Page
elif selected == "Experience":
    st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="experience-container">
            <div class="experience-card">
                <img src="https://storage.googleapis.com/streamlit-portfolio/sparkphoto.png" alt="BU Spark!">
                <h5>Data Science Technical Project Management Intern</h5>
                <p><strong>Date:</strong> September 2024 - December 2024<br>
                <strong>Company:</strong> BU Spark!<br>
                <strong>Responsibilities:</strong><br>
                - Oversaw technical components for three teams, totaling 15 students, across multiple projects, ensuring client satisfaction and providing technical guidance. Conducted code reviews, answered technical questions, and managed goals.<br>
                - Helped team process and analyze over 250,000 data points using Python, integrating geospatial, demographic, and property violation data, resulting in a comprehensive analysis of off-campus student housing violations across Boston.<br>
                - Managed project workflows using Notion boards and agile sprints; organized tasks in a backlog, and took detailed internal and client meeting notes, ensuring clarity and alignment across all project phases.</p>
            </div>
            <div class="experience-card">
                <img src="https://storage.googleapis.com/streamlit-portfolio/taphoto.png" alt="Graduate Teaching Assistant">
                <h5>Graduate Teaching Assistant - OM726 (Creating Value through Operations and Technology)</h5>
                <p><strong>Date:</strong> July 2024 - August 2024<br>
                <strong>Company:</strong> Questrom School of Business, Boston University<br>
                <strong>Responsibilities:</strong><br>
                - Graded assignments and led office hours.<br>
                - Simplified complex quantitative concepts like Z-tables for MBA students.</p>
            </div>
            <div class="experience-card">
                <img src="https://storage.googleapis.com/streamlit-portfolio/rajbearingphoto.png" alt="Business Associate">
                <h5>Business Associate</h5>
                <p><strong>Date:</strong> August 2021 - July 2023<br>
                <strong>Company:</strong> Raj Bearing<br>
                <strong>Responsibilities:</strong><br>
                - Leveraged Google Ads, Email Marketing, and Website Development to expand digital reach, resulting in a 20% increase in inquiries. Conducted A/B testing in email marketing campaigns to refine content and design, optimizing engagement.<br>
                - Created and maintained an Excel-based inventory tracking sheet to monitor stock levels and ensure accurate record-keeping for ball bearings, v-belts, and pipes.<br>
                - Utilized Google Analytics to monitor website traffic and analyze user behavior, leading to recommendations for website design enhancements and a subsequent 30% increase in traffic.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )



# Footer Section with Contact Information
# Footer Section with Updated Contact Information
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class='contact-section'>
        <div class="contact-title">Contact Me</div>
        <div class='contact-links'>
            <div class='contact-item'>
                <a href="mailto:dhruvds@bu.edu">
                    <img class="contact-icon" src="https://storage.googleapis.com/streamlit-portfolio/email-icon.png" alt="Email">
                    <span>Email</span>
                </a>
            </div>
            <div class='contact-item'>
                <a href="https://github.com/dhruvds58">
                    <img class="contact-icon" src="https://storage.googleapis.com/streamlit-portfolio/github-icon.png" alt="GitHub">
                    <span>GitHub</span>
                </a>
            </div>
            <div class='contact-item'>
                <a href="https://storage.googleapis.com/streamlit-portfolio/DhruvDA_Resume.docx.pdf" target="_blank">
                    <img class="contact-icon" src="https://storage.googleapis.com/streamlit-portfolio/resume-icon.png" alt="Resume">
                    <span>Resume</span>
                </a>
            </div>
            <div class='contact-item'>
                <a href="https://www.linkedin.com/in/dhruv-shah8/">
                    <img class="contact-icon" src="https://storage.googleapis.com/streamlit-portfolio/linkedin-icon.png" alt="LinkedIn">
                    <span>LinkedIn</span>
                </a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
