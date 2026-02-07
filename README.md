# 📊 YouTube Sentiment Analyzer

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![ML](https://img.shields.io/badge/ML-Transformers-orange.svg)

> **YouTube Sentiment Analyzer** is a command-line tool powered by neural networks that lets you instantly assess audience sentiment for any video. No more reading thousands of comments manually!

---

## ✨ Key Features

* **🚀 Fast data collection**: Integration with the official *YouTube Data API v3*.
* **🧠 Neural Network Analysis**: Using the multilingual `xlm-roberta-base-sentiment` model from Hugging Face.
* **💻 Professional CLI**: Convenient control via command line arguments.
* **🌈 Colored Reports**: Clearly visualize results directly in the terminal.

---

## 🛠 Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3.10+** | Primary Development Language |
| **Transformers** | Running a neural network for NLP analysis |
| **PyTorch** | Backend for running the ML model |
| **Google API Client** | Interacting with the YouTube Data API |
| **Colorama** | Styling console output |

---

## 🚀 Quick Start

### 1. Preparing the Environment
Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/your-profile/youtube-sentiment-analyzer.git
cd youtube-sentiment-analyzer
```

### 2. Installing Dependencies
It is recommended to use a virtual environment:
```bash
pip install -r requirements.txt
```

### 3. Setting Up the API Key
1. Get your key in the [Google Cloud Console](https://console.cloud.google.com/).
2. Open `youtube_fetcher.py` and replace `YOUR_API_KEY` with your actual key.

---

## 📖 Usage

The program is controlled via command-line arguments. Use the `--video` flag to specify the ID (the characters after `v=` in the video link).

| Flag | Description | Default |
| :--- | :--- | :--- |
| `--video` | **(Required)** YouTube video ID | - |
| `--limit` | Maximum number of comments | 100 |

### Example commands:

**Standard analysis of 100 comments:**
```bash
python main.py --video dQw4w9WgXcQ
```

**Analysis with a limit (e.g., 50):**
```bash
python main.py --video dQw4w9WgXcQ --limit 50
```

---