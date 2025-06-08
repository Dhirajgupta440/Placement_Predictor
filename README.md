# 🎓 Placement Predictor

This project predicts whether a student will be **placed** or **not placed** based on academic performance (**CGPA**) and other features (**IQ Score**) using **Logistic Regression**, a foundational algorithm in Machine Learning.

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)
![ML Model](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-yellowgreen)
![Deployed on Hugging Face](https://img.shields.io/badge/Deployed-HuggingFace-orange)

🔗 **Live Demo**: [Try the Model on Hugging Face](https://huggingface.co/spaces/Dhirajgupta440/Campus-Placement-Predictor)

---

## 📌 Features

- Predicts **placement status**: Placed ✅ or Not Placed ❌
- Uses the **Logistic Regression** ML algorithm.
- Trained on a real-world dataset: `placement.csv`
- Hosted using **Gradio** on **Hugging Face Spaces**
- Data preprocessing includes:
  - Removal of irrelevant columns (e.g., `serial number`)
  - Encoding of categorical variables
  - Feature scaling for better performance

---

## 📁 Project Structure

Placement_Predictor/
├── placement.csv # Dataset used for training
├── model.pkl # Trained Logistic Regression model
├── app.py # Gradio interface script
├── train_model.py # Model training script
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## 🧠 Model Details

- **Algorithm:** Logistic Regression
- **Target Variable:** `status` (Placed / Not Placed)
- **Features Used:**
  - CGPA
  - IQ Score

---

## 📊 Dataset Overview

- **Source:** `placement.csv`
- **Preprocessing Steps:**
  - Removed the `serial number` column
  - Handled missing values
  - Encoded categorical variables using `LabelEncoder`
  - Scaled numerical features for better model performance

---

## 🧑‍💻 Author

**Dhiraj Kumar**

- [LinkedIn](https://www.linkedin.com/in/dhiraj-kumar-93a17a308)
- [GitHub](https://github.com/Dhirajgupta440)

---

## 💡 Future Improvements

- Add more input features:
  - Age
  - Gender
  - Secondary and Higher Secondary percentages
  - Degree percentage
  - Work experience
  - Employability test score
- Implement multiple ML algorithms (e.g., SVM, Random Forest)
- Add data visualizations and graphs to the UI
- Suggest resume improvements based on model prediction
- Explore deep learning-based predictors

---

## 📄 License

This project is open source and available under the **MIT License**.
