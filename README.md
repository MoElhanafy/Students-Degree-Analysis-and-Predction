🎓 Students Degree Analysis and Predction
This Streamlit application provides insightful analysis of a dataset containing information about students' lifestyles, study habits, and GPA. It answers various analytical questions and visualizes relationships between key attributes, helping users understand patterns and trends in student behaviors.

📝 Overview
The app allows users to:

Analyze: Explore how students spend their time and how lifestyle factors impact their GPA, stress levels, and study habits.
Visualize: Interactive visualizations (using Seaborn, Matplotlib, and Plotly) to display insights.
Predict: Understand trends, relationships, and general behavior among students.

🚀 Features
Analyzing Mode: Provides answers to key analytical questions such as:

Where do most students spend their time?
What is the relationship between sleep hours, social hours, and GPA?
How does studying affect stress and GPA?
Distribution of GPA and study habits.
Interactive Visualizations:

Pie charts, histograms, scatterplots, and regression plots to uncover patterns.
Insights are displayed alongside visuals for easier understanding.
Customizable Sidebar: Allows users to select specific questions to analyze.

📊 Technologies Used
Python: Core programming language.
Streamlit: For interactive web-based UI.
Pandas: Data manipulation and analysis.
NumPy: Numeric calculations.
Seaborn & Matplotlib: Static data visualizations.
Plotly Express: Interactive charts.
🔧 Setup Instructions
To run this app locally:

Clone the repository:

git clone <repository-url>
cd students-degree-analysis
Install the dependencies:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run app.py
Open the browser at:

http://localhost:8501
📁 Folder Structure
📂 students-degree-analysis
│-- app.py                  # Main Streamlit application
│-- student_lifestyle_dataset.csv  # Dataset file
│-- moduleV2.py             # Custom module (if applicable)
│-- requirements.txt        # Python dependencies
└── README.md               # Project documentation
📊 Dataset
The dataset file (student_lifestyle_dataset.csv) should include:
Student ID: Unique identifier.
Study_Hours_Per_Day: Average study hours.
Sleep_Hours_Per_Day: Average sleep hours.
Social_Hours_Per_Day: Socializing hours per day.
Physical_Activity_Hours_Per_Day: Hours spent in physical activities.
GPA: Students' GPA.
Stress_Level: Stress levels reported by students.
💡 Usage
Use the Sidebar to select a mode and corresponding question.
View insights and interact with visualizations to analyze relationships between GPA, stress levels, study hours, and other variables.
Great for students, educators, and analysts to identify key trends.
🙌 Contributions
Contributions, feedback, and suggestions are welcome! Please open an issue or submit a pull request.

📄 License
This project is licensed under the MIT License.

🧑‍💻 Author
[Mohamed Elhanafy,Mohamed Ibn Saad]
LinkedIn:www.linkedin.com/in/elhanafy0
