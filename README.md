🎓 Placement Predictor
A machine learning project that predicts whether a student is likely to be placed or not based on academic and profile attributes, using Logistic Regression.


🔗 Live Demo (Hugging Face)
📌 Overview
This project uses a supervised machine learning model to predict campus placement outcomes. Based on a dataset of student academic records and other attributes, it helps to assess the likelihood of a student getting placed.

The Linear Regression model has been trained to output a binary classification—placed or not placed—by rounding the regression output.

📁 Dataset Description
File Used: placement.csv

Modification: The serial number column was removed as it had no predictive value.

Target Variable: status (Placed / Not Placed)

🔑 Features Used:

cgpa (1 to 10)

iq level (1 to 150)

🧠 Model Details
Algorithm Used: Logistic Regression

Preprocessing Steps:

Categorical encoding for features like cgpa , iq leveletc.

Dropped non-contributing column: serial number

Feature scaling applied where needed


🖥️ Run Locally
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Dhirajgupta440/Placement_Predictor.git
cd Placement_Predictor
Install the requirements:

bash
Copy
Edit
pip install -r requirements.txt
Open the notebook or run the script:

placement_analysis.ipynb for full model training

Prediction.ipynb for testing on custom input

🧪 Sample Usage
python
Copy
Edit
import pickle
import numpy as np

# Load model
model = pickle.load(open('models/model.pkl', 'rb'))

# Example encoded input (already preprocessed)
sample_input = np.array([[0, 85, 90, 82, 1, 45, 0, 88.5, 1]])
prediction = model.predict(sample_input)
final_result = round(prediction[0])
print("Placed" if final_result == 1 else "Not Placed")
🚀 Deployed Application
Try the model interactively using the UI hosted on Hugging Face:

🔗 Campus Placement Predictor – Deployed

Built using Gradio

Inputs: Gender, Education scores, Experience, Specialisation, etc.

Output: Placement prediction in real-time

📊 Project Structure
Copy
Edit
Placement_Predictor/
├── placement.csv
├── placement_analysis.ipynb
├── Prediction.ipynb
├── model.pkl
├── app.py (if applicable)
├── requirements.txt
└── README.md
✅ Future Work
Improve prediction accuracy with classification models (e.g., Logistic Regression, Random Forest)

Add more student attributes (e.g., certifications, projects)

Deploy using Streamlit/FastAPI for enhanced interface

🙋‍♂️ Author
Dhiraj Kumar

GitHub: @Dhirajgupta440

Deployed App: Hugging Face Space

📄 License
This project is open-source and available under the MIT License.
