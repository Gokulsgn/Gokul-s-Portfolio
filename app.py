import streamlit as st
import datetime

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
        font-family: 'Frank Ruhl Libre', serif;  /* Use the same font */
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
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 20px;
        justify-content: center;
        margin: 20px 0;
    }
    .skills-card {
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        padding: 20px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
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
with open("C:/Users/gokul/OneDrive/Documents/GOKULNATH_S.pdf", "rb") as resume_file:  # Update the path to your resume file
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
    st.image("C:/Users/gokul/Downloads/profile-pic (3).jpg", width=400,use_column_width=False)
    

# Time-based greeting
now = datetime.datetime.now()
hour = now.hour
if 6 <= hour < 12:
    greeting = "Good Morning!"
elif 12 <= hour < 18:
    greeting = "Good Afternoon!"
else:
    greeting = "Good Evening!"

# Greeting text with stylish font
st.markdown(f"""
            <br>
            <br>
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
            <p>Supervised & Unsupervised Learning, Deep Learning, NLP</p>
        </div>
        <div class="skills-card">
            <img src="https://img.icons8.com/ios-filled/50/000000/graph.png" alt="Data Visualization"/>
            <h4>Data Visualization</h4>
            <p>Matplotlib, Seaborn, Plotly</p>
        </div>
        <div class="skills-card">
            <img src="https://img.icons8.com/ios-filled/50/000000/web.png" alt="Web Development"/>
            <h4>Web Development</h4>
            <p>Flask, Django, Deployment Tools (Docker, Heroku)</p>
        </div>
        <div class="skills-card">
            <img src="https://img.icons8.com/ios-filled/50/000000/statistics.png" alt="Statistics"/>
            <h4>Mathematics & Statistics</h4>
            <p>Probability, Linear Algebra, Calculus</p>
        </div>
        <div class="skills-card">
            <img src="https://img.icons8.com/ios-filled/50/000000/code.png" alt="Programming Languages"/>
            <h4>Programming Languages</h4>
            <p>Python, JavaScript, SQL</p>
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

# Secondary Navigation Bar for Project Categories
st.markdown("""
    <div class="secondary-navbar">
        <a href="#python-mini-projects">Python Mini Projects</a>
        <a href="#ml-projects" class="active">Machine Learning</a>
        <a href="#DL-projects">Deep Learning</a>
    </div>
""", unsafe_allow_html=True)


# Skills Section
st.markdown("<div class='section-title' id='python-mini-projects'>Python Projects</div>", unsafe_allow_html=True)
st.markdown("""
    <div class="skills-container">
        <div class="skills-card">
            <h4>BMI Calculator & Health Stats Visualizer</h4>
            <p>Created an interactive quiz game designed to test users' knowledge about cricketer Virat Kohli through a series of engaging multiple-choice questions. Developed a question bank covering various aspects of Kohli's career, achievements, and personal milestones to ensure diverse quiz content. Designed the game interface with Streamlit, allowing users to start the quiz, select answers, and track their scores in real-time. Incorporated functionality to provide immediate feedback on answers, enhancing user engagement and learning. Implemented a scoring system that tracks correct answers and displays the final score at the end of the quiz. Added a timer feature to increase challenge and excitement during the quiz. Documented the project with detailed explanations of the quiz structure and design decisions. Shared the game on GitHub, encouraging cricket fans to contribute more questions and improvements for future iterations.<p>
        </div>
        <div class="skills-card">
            <h4>Virat Kohli Quiz Game</h4>
            <p>Created an interactive quiz game designed to test users' knowledge about cricketer Virat Kohli through a series of engaging multiple-choice questions. Developed a question bank covering various aspects of Kohli's career, achievements, and personal milestones to ensure diverse quiz content. Designed the game interface with Streamlit, allowing users to start the quiz, select answers, and track their scores in real-time. Incorporated functionality to provide immediate feedback on answers, enhancing user engagement and learning. Implemented a scoring system that tracks correct answers and displays the final score at the end of the quiz. Added a timer feature to increase challenge and excitement during the quiz. Documented the project with detailed explanations of the quiz structure and design decisions. Shared the game on GitHub, encouraging cricket fans to contribute more questions and improvements for future iterations.<p>
        </div>
        <div class="skills-card">
            <h4>Weather App</h4>
            <p>Built a comprehensive weather application that provides real-time updates based on user-entered locations, displaying current weather conditions, forecasts, and additional climate data. Integrated a reliable weather API to fetch up-to-date information, including temperature, humidity, wind speed, and forecasts for upcoming days. Designed an intuitive user interface using Streamlit, allowing users to easily input their location for accurate weather updates. Implemented data visualization features to present weather trends graphically, such as temperature variations over a week. Included options for users to save favorite locations for quick access to weather updates. Enhanced user experience by providing background information on weather conditions and tips for severe weather preparedness. Documented the development process, focusing on API integration and data visualization techniques. Shared the project on GitHub, encouraging feedback for future improvements and enhancements.<p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Skills Section
st.markdown("<div class='section-title' id='ml-projects'>Machine Learning Projects</div>", unsafe_allow_html=True)
st.markdown("""
    <div class="skills-container">
        <div class="skills-card">
            <h4>Iris Flower Classification</h4>
            <p>Developed a classification model to identify iris flower species using the Iris dataset, focusing on petal and sepal dimensions. Implemented K-Nearest Neighbors (KNN) and Decision Trees to evaluate their effectiveness in species prediction. Preprocessed the dataset by addressing missing values and standardizing feature scales for optimal performance. Trained both models and compared their accuracy and computational efficiency. Visualized classification results using confusion matrices and performance metrics for detailed insights. Created a user-friendly Streamlit app that allows users to input dimensions and receive predictions. Included educational content to explain the features and methods used in classification. Documented the project comprehensively and shared it on GitHub for community collaboration and feedback.</p>
        </div>
        <div class="skills-card">
            <h4>House Price Prediction</h4>
            <p>Designed a predictive model using linear regression to estimate house prices based on key features such as size, location, and number of rooms. Collected and preprocessed a dataset with comprehensive housing features, handling missing values and encoding categorical variables for effective analysis. Trained the model and evaluated its performance using metrics like Mean Absolute Error (MAE) and R-squared values. Developed an interactive Streamlit application that allows users to input house features and receive real-time price predictions. Visualized the results through scatter plots to analyze the distribution of predicted prices. Incorporated explanations of the model's predictions to enhance user understanding. Documented the process, emphasizing feature selection and engineering in regression analysis. Shared the project on GitHub for collaboration and feedback from the developer community.</p>
        </div>
        <div class="skills-card">
            <h4>Customer Segmentation with K-Means</h4>
            <p>Implemented K-Means clustering to segment customers based on purchasing behavior and preferences. Collected and preprocessed transactional data, identifying key features such as purchase frequency and average spending. Applied K-Means clustering and determined the optimal number of clusters using the elbow method and silhouette scores. Developed visualizations to illustrate customer distribution and behavior patterns before and after clustering. Created a user-friendly Streamlit application that allows businesses to input customer data and view segmentation results interactively. Provided insights into how each segment can be targeted effectively for marketing campaigns. Documented the project, highlighting the significance of customer segmentation in enhancing business strategies. Shared the code on GitHub for peer review and potential collaboration.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Skills Section
st.markdown("<div class='section-title' id='DL-projects'>Deep Learning Projects</div>", unsafe_allow_html=True)
st.markdown("""
    <div class="skills-container">
        <div class="skills-card">
            <h4>Image Classification (CIFAR-10)</h4>
            <p>Developed a Convolutional Neural Network (CNN) model to classify images into 10 categories, including airplanes, cars, and various animals, using the CIFAR-10 dataset. Preprocessed the dataset through normalization and data augmentation techniques to improve model robustness. Built and trained the CNN architecture with multiple layers, including convolutional, pooling, and fully connected layers. Evaluated model performance using metrics such as accuracy and loss, achieving high classification accuracy on the test set. Visualized model performance through confusion matrices and classification reports for detailed insights. Created a Streamlit application to allow users to upload images for real-time classification. Documented the project comprehensively, explaining the design choices and methodologies used. Shared the project on GitHub to promote collaboration and receive community feedback.<p>
        </div>
        <div class="skills-card">
            <h4>Sentiment Analysis with RNN</h4>
            <p>Designed a sentiment analysis model to analyze movie reviews and classify them as positive or negative using Recurrent Neural Networks (RNNs) or Long Short-Term Memory (LSTM) networks. Collected and preprocessed a dataset of movie reviews, performing text cleaning and tokenization for effective input representation. Built the RNN architecture, utilizing embedding layers and LSTM cells to capture contextual information in the text. Trained the model on labeled data, using accuracy and loss metrics to evaluate performance. Employed techniques like dropout for regularization and to prevent overfitting during training. Visualized training and validation loss and accuracy to monitor model performance. Developed a user-friendly Streamlit application for users to input movie reviews and receive sentiment predictions. Documented the project, emphasizing the importance of NLP techniques and deep learning in sentiment analysis, and shared it on GitHub for further exploration.<p>
        </div>
        <div class="skills-card">
            <h4>Predicting Loan Approval with ANN</h4>
            <p>Developed an Artificial Neural Network (ANN) model to predict loan approval based on applicant features such as income, credit score, and employment history. Collected and preprocessed a dataset containing relevant features, handling missing values and normalizing data for effective training. Built the ANN architecture, including input, hidden, and output layers, using activation functions like ReLU and sigmoid for non-linearity. Trained the model on labeled data, utilizing techniques like backpropagation and dropout for optimization and regularization. Evaluated model performance using classification metrics, including accuracy, precision, and recall. Created a Streamlit application that allows users to input their details and receive real-time predictions on loan approval. Documented the project comprehensively, explaining the model’s structure, training process, and evaluation methods. Shared the project on GitHub to encourage collaboration and feedback from the data science community<p>
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

