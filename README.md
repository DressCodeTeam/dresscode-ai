# dresscode-ai  

This API accepts an image URL and returns a description of the image using AI (mocked in this version).

---

## 🚀 Features

- ✅ FastAPI-based REST API
- ✅ Swagger/OpenAPI auto documentation
- ✅ Modular folder structure (routes, services, config)
- ✅ Uses image URLs directly (no local image processing)
- ✅ .env support for secure config
- ✅ Plug-and-play for real AI APIs (e.g., DeepAI, Hugging Face)

---

## 🗂️ Project Structure

```
image_description_api/
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── routes/ # API endpoints
│ │ └── image.py
│ ├── services/ # Business logic (e.g., call AI model)
│ │ └── image_analyzer.py
│ └── config.py # Loads environment variables
├── .env # Contains PORT and AI_API_KEY
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/image-description-api.git
cd image-description-api
```

### 2. Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create your .env file
```bash
PORT=8000
AI_API_KEY=your_ai_api_key_here
```

### 4. Run the API server
```bash
python3 app/main.py
```

---

## 📘 API Docs

Interactive API documentation is available by default:
- Swagger UI → http://localhost:8000/docs
