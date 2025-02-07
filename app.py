import streamlit as st
import datetime
import pytz



# Set page config
st.set_page_config(page_title="Gokulnath's Portfolio", page_icon=":star2:", layout="wide")


# Custom CSS for modern design and font
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Satisfy&display=swap');

    body {
        font-family: 'Arial', sans-serif;
        background-color: #f5f5f5;
        color: yellow;
        margin: 0;
        padding-bottom: 60px;
    }
    .about-me {
        font-family: 'Frank Ruhl Libre', serif;  /* Use the same  */
        font-size: 1.2em;  /* Adjust the font size as needed */
        color: #333;  /* Set the text color */
        margin: 20px 0;  /* Add some margin */
    }
    .navbar {
        background-color: #333;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
        transition: background-color 0.3s ease;
    }
    .custom-font {
            font-family: 'Frank Ruhl Libre', serif;
        }
    .navbar a:hover {
        background-color: #555;
        color: white;
    }
    .header {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        padding: 50px;
        background: linear-gradient(90deg, rgba(0,0,0,0.8), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1517413500375-e8f8e28fa22b');
        color: white;
        background-size: cover;
        background-position: center;
    }
    .header .text-content {
        max-width: 50%;
        position:relative;
        left: 50px;
    }
    .header h1 {
        margin: 0;
        font-size: 3.5em;
        color: #FFFF00;
        font-family: 'Frank Ruhl Libre', serif;
    }
    .header p {
        font-size: 1.8em;
        font-family: 'Frank Ruhl Libre', serif;
    }
    .profile-img-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        max-width: 100px; /* Adjust size as needed */
        height: 100px; /* Adjust size as needed */
        border-radius: 50%;
        overflow: hidden;
        border: 100px solid #333; /* Optional border */
    }
    .profile-img {
        width: 100%;
        height: 250%;
            +
        object-fit: cover; /* Ensure the image covers the circle without distortion */
    }
    .section-title {
        font-size: 2.5em;
        margin: 50px 0 20px 0;
        color: #333;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
        font-family: 'Frank Ruhl Libre', serif;
    }
    .card {
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        padding: 20px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin: 20px;
        flex: 1;
    }
    .card:hover {
        transform: scale(1.1);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
    }
    .card h3 {
        margin-top: 0;
        font-family: 'Frank Ruhl Libre', serif;
    }
    .skills-container {
        display: grid;
        grid-template-columns: repeat(5, minmax(150px, 1fr));
        gap: 20px;
        justify-content: center;
        margin: 20px 0;
    }
    .skills-card {
         width: 250px;
            height: 300px;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
            color: white;
            background-size: cover;
            background-position: center;
    }
    .bmi-project {
    background-image: url("https://media-hosting.imagekit.io//e8074d2e0bcc491e/efa66f1cf1.jpg?Expires=1833526865&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=z3I4-Kbb0xWQYB~1zWSdfH57U33nYmDcg4c5oa~pVBObMnMh6k2gFxKE6ZTKNfATievv0kIImcqMs6N9OVkNLcVnM40cZzAmvqezPElwK12F0Dgp7JxU7r0tFgANVZQMjEI57rAohGzBnmBFnee1vSX-zrqu0CIf4hLmFqAeAQXNkbDchtUPxNj6OQUUjwSiuElRmka2Vpgf6K8e4PaZSJxv6geSs~R5r13Q18vHDPJdG6aiiKeDUsb9ehAgWBLH3hr48T6KFC4Hrg5AknHCVtTOaAwrKyb5ZLm8IHQbBfGfcm0q1wHy0RDcf3eJ2gKXuHsRpM8JmwCCnASr-lizgw__");
}
    .skills-card:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
    }
    .skills-card img {
        width: 60px;
        height: 60px;
        margin-bottom: 10px;
    }
    .skills-card h4 {
        margin: 10px 0 0 0;
        font-size: 1.2em;
        color: #333;
        font-family: 'Frank Ruhl Libre', serif;
    }
    .skills-card p {
        font-size: 0.9em;
        color: #666;
        font-family: 'Frank Ruhl Libre', serif;
    }
            .section-title {
        font-family: 'Frank Ruhl Libre', serif;
        font-size: 2em;
        color: #2c3e50;
        margin: 20px 0;
    }
    .custom-font {
            font-family: 'Frank Ruhl Libre', serif;
            color: black;  /* Set text color to black */
            text-align: center; /* Center text */
        }
    .education-item {
            font-size: 15px; /* Font size for each item */
            margin: 10px ; /* Increase vertical spacing between items */ /* Optional: add padding for better appearance */
        }
    h4 {
            font-family: 'Frank Ruhl Libre', serif; /* Ensure h4 also uses the custom font */
            color: black;  /* Set h4 color to black */

        }
    .footer {
        text-align: center;
        padding: 3px;
        background-color: #333;
        color: white;
        position: fixed;
        width: 100%;
        bottom: 0;
        left:0;
        z-index: 1000;
    }
    .contact-info {
        text-align: center;
        margin: 30px 0;
    }
    .contact-info img {
        width: 40px;
        height: 40px;
        margin: 0 10px;
        cursor: pointer;
    }
    .secondary-navbar {
        background-color: #444;
        overflow: hidden;
        margin: 20px auto;
        border-radius: 5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        display: flex;
        justify-content: center;
        width: fit-content;
    }
    .secondary-navbar a {
        display: block;
        color: white;
        text-align: center;
        padding: 10px 20px;
        text-decoration: none;
        transition: background-color 0.3s ease;
    }
    .secondary-navbar a:hover {
        background-color: #555;
        color: white;
    }
    .secondary-navbar a.active {
        background-color: #666;
        color: white;
    }
    .greeting {
        font-family: "Satisfy", cursive;
        font-weight: 400;
        font-style: normal;
        font-size: 4em;
        text-align: center;
    }        
    </style>
    """, unsafe_allow_html=True)
# Navigation Bar
st.markdown("""
    <div class="navbar">
        <a href="#about-me">About Me</a>
        <a href="#skills">Skills</a>
        <a href="#education">Education</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </div>
            <br>
            <br>
""", unsafe_allow_html=True)

# Download Resume Button
with open("Gokulnath S - Resume.pdf", "rb") as resume_file:  # Update the path to your resume file
    st.download_button(
        label="Download My Resume",
        data=resume_file,
        file_name="Gokulnath_Resume.pdf",  # Name of the downloaded file
        mime="application/pdf"  # MIME type for PDF files
    )

# Create two columns for text and image
col1, col2 = st.columns([2, 1])  # Adjust column width as needed
with col1:
    st.markdown("""
                <br>
                <br>
                <br>
                <br>
        <div class="text-content">
            <marquee><h1>Gokulnath's Portfolio</h1></marquee>
            <p>AI Engineer | Python Developer | Tech Enthusiast</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("profile-pic (5).png", width=400,use_column_width=False)
    

# Define the time zone (e.g., "Asia/Kolkata" for India)
local_timezone = pytz.timezone("Asia/Kolkata")

# Get current time in the specified time zone
now = datetime.datetime.now(local_timezone)
hour = now.hour

# Determine greeting based on the hour
if 5 <= hour < 12:  # Morning: 5 AM - 12 PM
    greeting = "Good Morning!"
elif 12 <= hour < 17:  # Afternoon: 12 PM - 5 PM
    greeting = "Good Afternoon!"
elif 17 <= hour < 21:  # Evening: 5 PM - 9 PM
    greeting = "Good Evening!"
else:  # Night: 9 PM - 5 AM
    greeting = "Good Night!"

# Display greeting with your custom styles
st.markdown(f"""
    <h2 class="greeting">
        {greeting} Welcome to my portfolio...
    </h2>
""", unsafe_allow_html=True)


# About Me Section
st.markdown("<div class='section-title' id='about-me'>About Me</div>", unsafe_allow_html=True)
st.markdown("<div class='about-me'> I am an <b>AI enthusiast</b> with a strong background in <b>Python, Machine learning,</b> and <b>Deep learning</b>. I have hands-on experience developing intelligent systems and enjoy <b>solving complex problems</b> by turning data into useful insights. I work well in <b>team environments</b> and am always eager to learn more in the fast-growing AI and DL fields. My projects focus on <b>model optimization, data exploration,</b> and <b>neural networks</b>. I believe AI has the power to change industries and am excited to contribute to <b>meaningful projects</b>. Outside of work, I enjoy <b>coding challenges</b> and connecting with the tech community.</div>", unsafe_allow_html=True)

# Skills Section
st.markdown("<div class='section-title' id='skills'>Skills</div>", unsafe_allow_html=True)
st.markdown("""
    <div class="skills-container">
        <div class="skills-card">
            <img src="https://img.icons8.com/ios-filled/50/000000/machine-learning.png" alt="Machine Learning"/>
            <h4>Machine Learning</h4>
            <p>Supervised & Unsupervised Learning, Deep Learning, NLP, Reinforcement Learning</p>
        </div>
        <div class="skills-card">
            <img src="https://img.icons8.com/ios-filled/50/000000/graph.png" alt="Data Visualization"/>
            <h4>Data Handling & Visualization</h4>
            <p>SQL, Pandas, NumPy, Power BI, Matplotlib, Seaborn, Git, GitHub, Excel, Google Sheets</p>
        </div>
        <div class="skills-card">
            <img src="https://img.icons8.com/ios-filled/50/000000/web.png" alt="Web Development"/>
            <h4>Tools & Technologies</h4>
            <p>Streamlit, Google Gemini AI, TensorFlow, PyTorch, Scikit-learn, OpenAI API, LangChain,HTML, CSS, React, Django, Deployment Tools (Docker, Heroku)</p>
        </div>
        <div class="skills-card">
            <img src="https://img.icons8.com/ios-filled/50/000000/statistics.png" alt="Statistics"/>
            <h4>AI & Data Science</h4>
            <p>Predictive Analytics, Statistical Modeling, Feature Engineering, Data Preprocessing, Explainable AI</p>
        </div>
        <div class="skills-card">
            <img src="https://img.icons8.com/ios-filled/50/000000/python.png" alt="Programming Languages"/>
            <h4>Programming & Libraries</h4>
            <p>Python, OpenCV, BeautifulSoup, Selenium, FastAPI, Flask, NLTK, SpaCy</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# About Me Section
st.markdown("<div class='section-title' id='education'>Education</div>", unsafe_allow_html=True)

# Create four columns for the education section
col1, col2, col3, col4 = st.columns(4)

# Content for each column
content1 = """<div class='education-item custom-font'><h4>Python AI</h4>Qtree Technologies,<br> 
Gandhipuram,<br> Coimbatore - 641012</div>"""

content2 = """<div class='education-item custom-font'><h4>B.E.ECE</h4>73%<br>KSR IET College,<br>
K.S.R.Kalvi Nagar,<br> Tiruchengode - 637 215</div>"""

content3 = """<div class='education-item custom-font'><h4>HSC</h4>60%<br>G.H.S.School<br>
Mylambadi,<br> Bhavani,<br> Erode - 638 314</div>"""

content4 = """<div class='education-item custom-font'><h4>SSLC</h4>80%<br>G.H.S.School<br>
Mylambadi,<br> Bhavani,<br> Erode - 638 314</div>"""

# Display the content in each column with the custom font
with col1:
    st.markdown(content1, unsafe_allow_html=True)

with col2:
    st.markdown(content2, unsafe_allow_html=True)

with col3:
    st.markdown(content3, unsafe_allow_html=True)

with col4:
    st.markdown(content4, unsafe_allow_html=True)

    
# Projects Section
st.markdown("<div class='section-title' id='projects'>Projects</div>", unsafe_allow_html=True)

# Combined Project Cards with Images and Links
st.markdown("""
    <div class="skills-container">
        <div class="skills-card bmi-project">
            <h4 style="color: #FFCC00; text-shadow: 2px 2px 4px #000000;">BMI Calculator & Health Stats Visualizer</h4>
            <p style="color: black;">This Streamlit app predicts customer churn using a Random Forest model, with data preprocessing, training, and a prediction interface for user inputs.</p>
            <a href="https://document-genie-using-rag-framwork-aupgjwt9u6avwadhvlhdux.streamlit.app/" target="_blank" style="color: skyblue;text-shadow: 2px 2px 4px #000000; text-decoration:none;">View Project</a>
        </div>
        <div class="skills-card bmi-project">
            <h4 style="color: #FFCC00; text-shadow: 2px 2px 4px #000000;">AI-Resume Analyzer</h4>
            <p style="color: black; ">This Streamlit app analyzes resumes using Google Gemini AI, extracting text and comparing it with job descriptions to provide skill improvement suggestions.</p>
            <a href="https://document-genie-using-rag-framwork-aupgjwt9u6avwadhvlhdux.streamlit.app/" target="_blank" style="color: skyblue;text-shadow: 2px 2px 4px #000000; text-decoration:none;">View Project</a>
        </div>
        <div class="skills-card bmi-project">
            <h4 style="color: #FFCC00; text-shadow: 2px 2px 4px #000000;">Document Genie using RAG Framwork</h4>
            <p style="color: black; ">This Streamlit app, Document Genie, uses Google's Gemini-PRO with the RAG framework to analyze PDFs. It extracts text and provides precise, context-aware answers</p>
            <a href="https://document-genie-using-rag-framwork-aupgjwt9u6avwadhvlhdux.streamlit.app/" target="_blank" style="color: skyblue;text-shadow: 2px 2px 4px #000000; text-decoration:none;">View Project</a>
        </div>
        <div class="skills-card bmi-project">
            <h4 style="color: #FFCC00; text-shadow: 2px 2px 4px #000000;">Spotify Track/Playlist Info Finder</h4>
            <p style="color: black; ">This Streamlit app fetches Spotify track/playlist details, visualizes artist popularity with a pie chart, and allows users to download data in CSV or Excel format.</p>
            <a href="https://spotify-dataproject-sfxhvaq8gwrhhpje6py4ge.streamlit.app/" target="_blank" style="color: skyblue;text-shadow: 2px 2px 4px #000000; text-decoration:none;">View Project</a>
        </div>
        <div class="skills-card bmi-project">
            <h4 style="color: #FFCC00; text-shadow: 2px 2px 4px #000000;">Personal Finance Manager</h4>
            <p style="color: black;">This Personal Finance Manager App built with Streamlit allows users to track expenses, set budgets, and analyze financial data in an interactive way.</p>
            <a href="https://personalfinance-wkmio3s6qvwifa3zi4qjwf.streamlit.app/" target="_blank" style="color: skyblue;text-shadow: 2px 2px 4px #000000; text-decoration:none;">View Project</a>
        </div>
        <div class="skills-card bmi-project">
            <h4 style="color: #FFCC00; text-shadow: 2px 2px 4px #000000;">Customer Churn Prediction App</h4>
            <p style="color: black;">This Customer Churn Prediction App uses Random Forest Classifier to predict whether a customer is likely to churn based on key attributes.</p>
            <a href="https://customer-churn-prediction-app-nlg6hhw4mkgvq8gwu2uchb.streamlit.app/" target="_blank" style="color: skyblue;text-shadow: 2px 2px 4px #000000; text-decoration:none;">View Project</a>
        </div>
        <div class="skills-card bmi-project">
            <h4 style="color: #FFCC00; text-shadow: 2px 2px 4px #000000;">Wine Quality Prediction App</h4>
            <p style="color: black;">This Wine Quality Prediction App built with Streamlit allows users to enter various wine attributes and predict whether the wine is of good or bad quality using a pre-trained machine learning model.</p>
            <a href="https://wineprediction-nwwk4efidbvfdjmyylypng.streamlit.app/" target="_blank" style="color: skyblue;text-shadow: 2px 2px 4px #000000; text-decoration:none;">View Project</a>
        </div>
        <div class="skills-card bmi-project">
            <h4 style="color: #FFCC00; text-shadow: 2px 2px 4px #000000;">BMI Calculator & Health Stats Visualizer</h4>
            <p style="color: black; ">This Streamlit app is a stylish BMI Calculator & Health Stats Visualizer that computes BMI, categorizes it, and provides health recommendations with a bar chart.</p>
            <a href="https://calculator-jpl3lfgg9rlbjrxbd5e5k7.streamlit.app/" target="_blank" style="color: skyblue;text-shadow: 2px 2px 4px #000000; text-decoration:none;">View Project</a>
        </div>
        <div class="skills-card bmi-project">
            <h4 style="color: #FFCC00; text-shadow: 2px 2px 4px #000000;">Quiz Game</h4>
            <p style="color: black; ">This Streamlit app is an interactive Virat Kohli Quiz Game where users answer multiple-choice questions about the cricket legend. It provides immediate feedback on each answer and calculates the final score.</p>
            <a href="https://quizgame-x5ceijnhwxbdbzxuembqq4.streamlit.app/" target="_blank" style="color: skyblue;text-shadow: 2px 2px 4px #000000; text-decoration:none;">View Project</a>
        </div>
        <div class="skills-card bmi-project">
            <h4 style="color: #FFCC00; text-shadow: 2px 2px 4px #000000;">Weather App</h4>
            <p style="color: black; ">This Streamlit app fetches real-time weather data from OpenWeatherMap, displaying temperature, conditions, humidity, wind speed, and local time in a stylish format.</p>
            <a href="https://weatherapp-brczgqpy9nmpvgy8h3xujy.streamlit.app/" target="_blank" style="color: skyblue;text-shadow: 2px 2px 4px #000000; text-decoration:none;">View Project</a>
        </div>
    </div>
""", unsafe_allow_html=True)


# Contact Section
st.markdown("<div class='section-title' id='contact'>Contact</div>", unsafe_allow_html=True)
st.markdown("""
    <div class="contact-info">
        <a href="https://www.linkedin.com/in/gokulnath-s-287038318/" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" alt="LinkedIn"/>
        </a>
        <a href="https://mail.google.com/mail/?view=cm&fs=1&to=gokulsgn7@gmail.com" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/mail.png" alt="Email"/>
        </a>
        <a href="https://x.com/gokul_sgn" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/twitter.png" alt="Twitter"/>
        </a>
        <a href="https://www.instagram.com/gokul_sgn/?__pwa=1" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/instagram.png" alt="Instagram"/>
        </a>
        <a href="https://wa.me/917708943199" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/whatsapp.png" alt="WhatsApp"/>
        </a>
        <a href="https://github.com/Gokulsgn" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/000000/github.png" alt="GitHub"/>
        </a>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>&copy; 2024 Gokul. All rights reserved.</p>
    </div>
""", unsafe_allow_html=True)

