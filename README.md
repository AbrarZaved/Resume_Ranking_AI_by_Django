

# **Resume Ranking AI by Django** 🎯📄  

**AI-powered Resume Ranking System built with Django**  

## **📌 Overview**  
Resume Ranking AI is a Django-based web application that uses **Natural Language Processing (NLP) and Machine Learning (ML)** to analyze and rank resumes based on job descriptions. It helps recruiters efficiently filter and prioritize resumes based on skills, experience, and qualifications.  

## **🚀 Features**  
✅ **AI-Powered Resume Screening** – Automatically ranks resumes based on relevance to the job description.  
✅ **Skill Matching** – Extracts and compares candidate skills with job requirements.  
✅ **Experience & Qualification Analysis** – Evaluates work experience and education.  
✅ **Customizable Ranking Criteria** – Adjust weights for different parameters.  
✅ **PDF & DOCX Parsing** – Supports multiple resume formats.  
✅ **Admin Dashboard** – Manage resumes, job descriptions, and ranking criteria.  
✅ **REST API Support** – Integrate with external HR systems.  

## **🛠️ Tech Stack**  
- **Backend:** Django, Django REST Framework  
- **Frontend:** HTML, CSS, JavaScript (or React if applicable)  
- **AI/NLP:** SpaCy, NLTK, Scikit-learn  
- **Database:** PostgreSQL / MySQL / SQLite  
- **File Handling:** PyPDF2, python-docx  

## **🔧 Installation & Setup**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/Resume_Ranking_AI_by_Django.git
cd Resume_Ranking_AI_by_Django
```
### **2️⃣ Create & Activate Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```
### **4️⃣ Run Database Migrations**  
```bash
python manage.py migrate
```
### **5️⃣ Start the Development Server**  
```bash
python manage.py runserver
```
Access the app at **http://127.0.0.1:8000/**  

## **📂 Project Structure**  
```
Resume_Ranking_AI/
│── Resume_Ranking_AI/      # Main Django app
│── templates/              # Frontend templates
│── static/                 # CSS, JS, images
│── models.py               # Database models
│── views.py                # Business logic
│── serializers.py          # API serializers
│── resume_checker/         # AI resume processing logic
│── requirements.txt        # Dependencies
│── manage.py               # Django entry point
```


## **📌 Future Enhancements**  
✅ AI-based **Resume Summarization**  
✅ **Job Matching Recommendations**  
✅ **Dashboard with Data Analytics**  

## **🤝 Contributing**  
Pull requests are welcome! Follow the standard **Git flow** and create a feature branch before submitting PRs.  

## **📜 License**  
This project is open-source under the **MIT License**.  

