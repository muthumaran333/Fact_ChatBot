# 🕵️‍♂️ FactChecker Bot  
> **Verify claims instantly** using AI, web search, and trusted sources — all from a simple Streamlit app.  

![FactChecker Banner](assets/banner.png)

---

## ✨ Features
✅ **AI-Powered Claim Verification** – Classifies claims as **True**, **False**, or **Uncertain**  
✅ **Evidence-Based Verdicts** – Explanations sourced from trusted references  
✅ **Preloaded Sample Claims** – Test the app quickly without typing  
✅ **Beautiful UI** – Sidebar suggestions, clean typography, and responsive layout  
✅ **Open-Source & Extensible** – Easy to add more verification sources and logic  

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/factchecker-bot.git
cd factchecker-bot
````

### 2️⃣ Install Dependencies

Make sure you have **Python 3.8+** installed, then run:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run streamlit_app1.py
```

📍 App will launch at: [http://localhost:8501](http://localhost:8501)

---

## 🖼 UI Overview

| Section          | Description                                               |
| ---------------- | --------------------------------------------------------- |
| **🧾 Header**    | Displays project title with custom colors                 |
| **📌 Sidebar**   | Quick sample claims to click and test instantly           |
| **🔍 Main Area** | Type a claim, verify it, and see verdict with explanation |

---

## 📂 Project Structure

```
factchecker-bot/
│
├── streamlit_app1.py        # Main Streamlit app
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
├── src/
│   ├── fact_check.py         # Core claim verification logic
│   ├── search_utils.py       # Web search helpers
│   └── ...
└── assets/                  # Images & static files
```

---

## 📜 Example Usage

**Claim:**

```
The moon is made of cheese.
```

**Verdict:** ❌ False
**Explanation:** Scientific evidence and NASA records confirm the moon is composed of rock and dust, not dairy products. 🧀🚫

---

## 🛠 Tech Stack

* 🐍 **Python 3.8+**
* 🎨 **Streamlit** – Interactive web app
* 🌐 **Requests / Search API** – Fetch evidence from the web
* 🔍 **BeautifulSoup** – Web scraping for additional verification

---

## 📄 License

📜 Licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 🙌 Acknowledgments

* [Streamlit](https://streamlit.io/) – UI framework
* [Wikipedia](https://wikipedia.org/) – Trusted reference source
* Public APIs & datasets for fact verification

---

> 💡 **Pro Tip:**
> Try claims like:
>
> * "Delhi is the capital of India." ✅
> * "Humans have walked on Mars." ❌
> * "Water boils at 100°C at sea level." ✅

---

![Footer Image](assets/footer.png)

```

