# Iris Flower Classifier - Machine Learning App

A complete, basic, end-to-end Machine Learning web application that predicts the species of an Iris flower using input features. This project integrates a trained ML model with a responsive Streamlit frontend and a FastAPI backend, deployed seamlessly with CI/CD using GitHub, Streamlit Cloud, and Render.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://iris-flower-classifier-suriyasuresh.streamlit.app/)

---

## 🧠 Project Overview

This application allows users to input the sepal and petal dimensions of an Iris flower and get an instant prediction of its species. The ML model is trained using the popular **Iris dataset** from scikit-learn and is served through a RESTful API built using **FastAPI**.

---

## ⚙️ Tech Stack

| Layer          | Technology     | Purpose                                       |
|----------------|----------------|-----------------------------------------------|
| Frontend       | Streamlit      | User interface for input and result display   |
| Backend        | FastAPI        | REST API to serve predictions                 |
| ML Model       | Scikit-learn   | Classification of Iris flower species         |
| Deployment     | Streamlit Cloud & Render | Frontend and API hosting          |
| Logging        | Python `logging` | Unified and structured logging system       |
| CI/CD          | GitHub         | Version control and continuous deployment     |

---

## 🧩 Project Architecture


User Input (Streamlit UI)
⬇
Frontend (Streamlit)  ➡️  FastAPI Backend ➡️ ML Model (Iris Classifier)
⬇                                        ⬆
Prediction Output                     Singleton Pattern (model/logger)


---

## 🧰 Features

- 🔢 Input: Sepal length, Sepal width, Petal length, Petal width
- 🌸 Output: Predicted Iris flower species (Setosa, Versicolor, Virginica)
- 🔗 Streamlit frontend with API calls to backend
- 🔁 Real-time inference using deployed FastAPI server
- 🔐 Efficient design using **Singleton Pattern** to avoid repeated loading of models and loggers
- 📦 Fully containerized and version-controlled via GitHub

---

## 💡 Design Patterns Used

### 🔁 Singleton Design Pattern

To ensure that the ML model and logger are instantiated only once across the application lifecycle, the **Singleton pattern** was used:

- **`singleton_model.py`**: Loads the model only once during the app lifecycle to save memory and improve performance.
- **`singleton_logger.py`**: Creates a single instance of a logger, ensuring all modules log to the same destination uniformly.

This ensures **thread safety**, **performance optimization**, and **clean architecture**.

---

## 📦 Folder Structure

iris-flower-classifier/
├── backend/
│   ├── main.py                  # FastAPI backend logic
│   ├── singleton\_model.py       # Singleton for model loading
│   └── singleton\_logger.py      # Singleton for logger
├── frontend/
│   └── app.py                   # Streamlit frontend
├── model/
│   └── iris\_model.pkl           # Trained scikit-learn model
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .gitignore


---

## 🚀 How to Run Locally

### 🔧 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/iris-flower-classifier.git
cd iris-flower-classifier
````

### ⚙️ Step 2: Create and Activate Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🚀 Step 4: Run Backend (FastAPI)

```bash
cd backend
uvicorn api.main:app --reload
```

### 💻 Step 5: Run Frontend (Streamlit)

```bash
cd ../frontend
streamlit run app.py
```

---

## 🌐 Deployment Details

* **Frontend**: Deployed via [Streamlit Cloud](https://streamlit.io/cloud) with GitHub integration
* **Backend**: Deployed using [Render](https://render.com) as a FastAPI web service
* **CI/CD**: Automatic deployment triggered on every GitHub push

---

## 📚 Learnings & Highlights

* Building REST APIs using FastAPI
* Using `requests` to connect Streamlit with backend
* Streamlining ML app structure for scalability
* Learning and applying the Singleton Design Pattern
* Deploying full-stack ML apps with GitHub-based CI/CD

---

## 🙌 Acknowledgements

* Scikit-learn for the Iris dataset
* Streamlit and FastAPI for their outstanding open-source tools
* Render and Streamlit Cloud for free deployment hosting

---

## 📫 Connect With Me

Let's connect and build more ML solutions together!

🔗 [LinkedIn](https://linkedin.com/in/suriya-s-653b48328/)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
