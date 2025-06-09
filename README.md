# CSV Data Analyzer

**An AI-powered Streamlit application for analyzing CSV data using LangChain agents and GROQ's LLaMA-3 model.**

---
## Project Deployed on Render: [https://your-csv-analyzer-app.onrender.com](https://csv-data-analysis-il2k.onrender.com/)

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Folder Structure](#folder-structure)  
- [How It Works](#how-it-works)  
- [Author](#author)

---

## Project Overview

This project is an intelligent data analysis tool that allows users to:

- Upload CSV files for instant analysis
- Get AI-powered insights through natural language queries
- Visualize data with interactive charts
- Leverage GROQ's high-performance LLaMA-3 model for accurate responses

Key components:
- **CSV Processing**: Clean loading and preview of uploaded data
- **Natural Language Interface**: Ask questions in plain English
- **Data Visualization**: Automatic chart generation for numeric columns
- **Custom UI**: Professionally styled Streamlit interface

---

## Features

- **CSV Upload & Preview**: Quickly view uploaded data structure
- **Interactive Visualizations**:
  - Bar charts
  - Line charts
  - Area charts
- **AI-Powered Analysis**:
  - Natural language query processing
  - Intelligent response generation
- **User-Friendly Interface**:
  - Clean, modern design
  - Responsive layout
  - Custom CSS styling
- **Multi-Column Analysis**: Select specific columns for visualization

---

## Tech Stack

- **Python 3.10+**
- [Streamlit](https://streamlit.io/) - Web application framework
- [LangChain](https://langchain.com/) - LLM integration framework
- [GROQ LLaMA-3](https://groq.com/) - High-performance LLM API
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [Python-dotenv](https://pypi.org/project/python-dotenv/) - Environment management

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/thelakshyadubey/csv_data_analysis.git
cd csv_data_analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

## Usage
1. Run the application:
```bash
streamlit run app.py
```

2. In the browser:
- Upload a CSV file
- View data preview
- Select columns for visualization
- Ask questions about your data
- View generated visualizations and responses

## Folder Structure
```text
csv-data-analyzer/
├── app.py                # Main application file
├── llm_utils.py          # LLM integration utilities
├── css_utils.py          # CSS injection utilities
├── style.css             # Custom styles
├── assets/
│   └── background.png    # Background image
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```
## How It Works
**1. Data Upload:**
- User uploads a CSV file
- System loads data into Pandas DataFrame
- Displays preview of the data

**2. Visualization:**
- Automatically detects numeric columns
- Provides multiple chart types
- Allows column selection

**3. Natural Language Processing:**
- User enters question in text area
- LangChain agent processes query using LLaMA-3
- Returns human-readable response

## Author
Lakshya Dubey

## Preview
![image](https://github.com/user-attachments/assets/fa90b7aa-0b45-4e0f-94ac-fd88b92dd97e)
![image](https://github.com/user-attachments/assets/3776224b-9f91-4cd3-9308-c486f5e101d7)
![image](https://github.com/user-attachments/assets/a9b4791e-dfe8-4761-931f-cdf43ddc2176)
