# 🎓Placement Predictor

This project predicts whether a student will be placed or not based on academic performance( CGPA) and other feature( IQ Score) using **Logistic Regression**, a fundamental Machine Learning algorithm.

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)
![ML Model](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-yellowgreen)
![Deployed on Hugging Face](https://img.shields.io/badge/Deployed-HuggingFace-orange)

🔗 **Live Demo**: [Try the Model on Hugging Face](https://huggingface.co/spaces/Dhirajgupta440/Campus-Placement-Predictor)

---

## 📌 Features

- Predicts **placement status** (Placed/Not Placed) using input data.
- Built using the **Logistic Regression** algorithm.
- Trained on a real-world **placement dataset** (`placement.csv`).
- Easy-to-use interface deployed on **Hugging Face Spaces (Gradio)**.
- Preprocessing includes:
  - Removal of irrelevant columns like `serial number`.
  - Encoding categorical values.
  - Feature scaling for numerical values.

---
## 
Placement_Predictor/
├── placement.csv         # Dataset used for training
├── model.pkl             # Trained Logistic Regression model
├── app.py                # Gradio app script
├── train_model.py        # Model training script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
🧠 Model Details
Algorithm: Logistic Regression

Target Variable: status (Placed / Not Placed)

Features Used:


CGPA
IQ Score



##📊 Dataset Overview
Source: placement.csv

##Preprocessing:

Dropped unnecessary column: serial number

Handled missing values

Encoded categorical features using LabelEncoder


##🧑‍💻 Author
Dhiraj Kumar

LinkedIn

GitHub

##💡 Future Improvements
Add more features Age

Gender

Secondary and Higher Secondary percentages

Degree percentage

Work experience

Employability test score, etc.
Add more algorithms (e.g., SVM, Random Forest) for comparison.

Improve UI with more visualizations.

Add resume-building suggestions based on prediction.

Explore deep learning models.

📄 License
This project is open source and available under the MIT License.
