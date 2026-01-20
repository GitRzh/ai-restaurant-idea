# :9 AI Restaurant Idea Generator

A modern web application that uses AI to generate creative restaurant names and menu items based on selected cuisines. Built with Streamlit and Google's Gemini AI.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![Google](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

---

## ▣ Project Overview

The AI Restaurant Idea Generator is an interactive web application that leverages Google's Gemini 2.5 Flash model to generate unique restaurant concepts instantly.

This project demonstrates:
- AI-powered creative content generation
- Sequential prompt chaining using LangChain
- Real-time web application development with Streamlit
- Integration with Google's Gemini API
- Modern Python development practices

Users select a cuisine type and receive a tailored restaurant name along with five signature menu items that perfectly complement the concept.

---

## ▣ Problem Statement

Generate creative and contextually relevant restaurant concepts that inspire entrepreneurs, food enthusiasts, and creative professionals in their culinary ventures.

### Output
- `Restaurant Name` → Unique, fancy name based on selected cuisine
- `Menu Items` → 5 signature dishes matching the restaurant theme

---

## ▣ Project Structure

```text
Restaurant-Generator/
│
├── app.py
│   # Streamlit web application and user interface
│
├── langchain_helper.py
│   # LangChain logic, AI model setup, and prompt chains
│
├── requirments.txt
│   # Project dependencies
│
├── .env
│   # Environment variables (API keys)
│
└── README.md
    # Project documentation
```

---

## ▣ Tech Stack

### Programming Language
- **Python 3.11**

### AI & LLM Framework
- **LangChain**
- **Google Gemini 2.5 Flash**

### Web Framework
- **Streamlit**

### Data Processing
- **python-dotenv**

### Development Tools
- **VS Code**
- **Conda**
- **Git & GitHub**

---

## ▣ Clone and Deploy the Project

### Step 1: Clone the Repository
```bash
git clone git@github.com:GitRzh/ai-restaurant-idea.git
cd ai-restaurant-idea
```

### Step 2: Create Virtual Enviroment
```bash
python3.11 -m venv venv
```
```bash
source venv/bin/activate        #linux/mac
```
```bash
venv\Scripts\activate           #windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirments.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### Step 5: Run the Application Locally
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

---

## ▣ How It Works

### Workflow
1. User selects a cuisine from the sidebar (Indian, Thai, Continental, English, Japanese)
2. First LangChain chain generates a fancy restaurant name based on the cuisine
3. Second LangChain chain creates 5 menu items tailored to the restaurant name
4. Results are displayed with formatted UI elements

### Technical Implementation
- **Prompt Templates**: Structured prompts ensure consistent AI responses
- **Chain Architecture**: Sequential chains pass restaurant name to menu generation
- **Output Parsing**: StrOutputParser extracts clean text from model responses
- **Temperature Setting**: 0.7 for balanced creativity and coherence
- **Error Handling**: Exception catching with user-friendly error messages

---

## ▣ Features

### Current Features
- Interactive sidebar cuisine selection
- AI-generated restaurant names
- 5 signature menu items per concept
- Clean, modern UI with Streamlit
- Loading animations during generation
- Error handling and user feedback

---

## ▣ Current Limitations

- Fixed cuisine options (only 5 available)
- Always generates exactly 5 menu items
- No customization of AI temperature or creativity
- Results are not saved between sessions
- Requires active internet connection
- Dependent on Google API availability
- No multi-language support
- Filename typo: `requirments.txt` instead of `requirements.txt`

---

## ▣ Future Improvements

Potential enhancements include:
- **Custom Cuisine Input**: Allow users to enter any cuisine type
- **Menu Size Control**: Adjustable number of menu items (3-10)
- **Export Functionality**: Download results as PDF, JSON, or CSV
- **History Feature**: Save and browse previous generations
- **Pricing Estimates**: AI-generated dish pricing suggestions
- **Detailed Descriptions**: Full restaurant concept with ambiance and target audience
- **Image Generation**: AI-generated dish images using DALL-E or similar
- **Dietary Filters**: Vegan, vegetarian, gluten-free, halal options
- **Multi-language Support**: Generate names in different languages
- **Advanced Customization**: Control creativity, formality, and style
- **Database Integration**: Store concepts for later retrieval
- **User Accounts**: Personal collections and favorites
- **Deployment**: Docker containerization and cloud hosting

---

## © Made by

**Raz**

Python Developer | AI & ML Enthusiast

---

## ✉ Acknowledgement

Thanks to Google for the Gemini API and the open-source community for LangChain and Streamlit.

---

## ✎ Note

This project is for educational and creative purposes. API costs may apply when using Google's Gemini model.
