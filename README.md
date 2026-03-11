# 📊 Sales Insight Automator

AI-powered **Sales Analytics Dashboard** that analyzes CSV sales data and generates business insights using **FastAPI, Docker, and Gemini LLM**.

---

## 🚀 Features

✨ Upload a CSV file with sales data
📈 Automatic revenue & unit calculations
🤖 AI-generated business insights using Gemini LLM
🐳 Fully containerized with Docker
⚡ Fast API built with FastAPI
💻 Simple frontend dashboard

---

## 🏗️ Tech Stack

* ⚡ **FastAPI** – Backend API
* 🐳 **Docker & Docker Compose** – DevOps containerization
* 🧠 **Google Gemini LLM** – AI insight generation
* 📊 **Pandas** – Data processing
* 🌐 **HTML + JavaScript** – Frontend dashboard

---

## 📂 Project Structure

```
sales-insight-automator
│
├── backend
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend
│   └── index.html
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## 🐳 Run the Project with Docker

Clone the repository:

```
git clone https://github.com/ShambhaviSood/sales-insight-automator.git
cd sales-insight-automator
```

Start the application:

```
docker compose up --build
```

---

## 🌐 API Documentation

After starting the server, open:

```
http://localhost:8000/docs
```

FastAPI automatically provides an interactive Swagger UI.

---

## 📊 Example CSV Format

```
Date,Product,Units_Sold,Revenue
2026-01-05,Electronics,100,15000
2026-01-12,Home Appliances,45,4500
2026-02-10,Electronics,80,12000
2026-02-20,Furniture,20,6000
```

---

## 🧠 AI Insights

The system sends the dataset to **Gemini LLM** which generates a short executive summary of the sales performance.

Example:

* 📈 Electronics category dominates revenue
* 📦 High unit sales indicate strong demand
* 🪑 Furniture shows lower sales volume
* 💰 Overall revenue trend is stable

---

## ⚙️ Environment Setup

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## 👩‍💻 Author

**Shambhavi Sood**

---

## ⭐ Future Improvements

* 📊 Data visualization charts
* 📧 Email automated reports
* ☁️ Cloud deployment (AWS / GCP)
* 📉 Advanced analytics with ML

---

## 📌 DevOps Focus

This project demonstrates:

* Docker containerization
* FastAPI microservice architecture
* Environment variable management
* AI integration with APIs

---

⭐ If you like this project, feel free to star the repository!
