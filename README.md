# 🕵️‍♂️ FactChecker Bot

> **Verify claims instantly** using AI, web search, and trusted sources — all from a simple Streamlit app.

---

## 🖼 Banner & UI Images

1. **Image 1:** 
   *Shows the app homepage with the project title, a clean header, and sidebar navigation for sample claims.*

   ![sample image](fact_checker_bot\image\image1.png)

2. **Image 2:** 
   *Demonstrates the sidebar with preloaded sample claims, allowing users to click and test instantly.*
    ![sample image](fact_checker_bot\image\image2.png)

3. **Image 3:** `fact_checker_bot\image\image3.png`
   *Displays a claim input field in the main area along with the verdict and explanation after verification.*
    ![sample image](fact_checker_bot\image\image3.png)

4. **Image 4:** `fact_checker_bot\image\image4.png`
   *Shows evidence and references fetched from trusted sources supporting the verdict (True/False/Uncertain).*

    ![sample image](fact_checker_bot\image\image4.png)

---

## ✨ Features (Detailed)

* ✅ **AI-Powered Claim Verification**
  The app uses AI models to classify claims as **True**, **False**, or **Uncertain**, leveraging both pre-trained models and contextual analysis.

* ✅ **Evidence-Based Verdicts**
  For every claim, the app provides an explanation with supporting evidence from credible online sources. This ensures the verdict is **transparent** and **verifiable**.

* ✅ **Preloaded Sample Claims**
  The sidebar contains ready-to-use sample claims to test the bot quickly without typing. Perfect for demonstrations or teaching.

* ✅ **Beautiful & Responsive UI**
  The app uses a modern, clean design with a responsive layout. Users can navigate easily between claim input, sample claims, and results.

* ✅ **Web Search Integration**
  Integrates with search engines and APIs to fetch current and reliable information for claim verification.

* ✅ **Open-Source & Extensible**
  The project is modular. Developers can extend verification logic, add more search sources, or enhance the UI with minimal effort.

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/muthumaran333/Fact_ChatBot
cd Fact_ChatBot/factchecker-bot
```

### 2️⃣ Install Dependencies

Make sure you have **Python 3.11+** installed:

 ### Create a Virtual Environment

It’s recommended to use a virtual environment to manage dependencies:

Windows:
```
python -m venv env
env\Scripts\activate
```



```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run streamlit_app.py
```

Access the app at: [http://localhost:8501](http://localhost:8501)

---

## 🖼 UI Overview (Detailed)

| Section          | Description                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------- |
| **🧾 Header**    | Project title with custom colors, providing a professional and attractive look.             |
| **📌 Sidebar**   | Sample claims for instant testing, category selection, and quick tips.                      |
| **🔍 Main Area** | Input field for new claims, real-time verification, verdict display, and explanation panel. |
| **📑 Evidence**  | Shows supporting sources, links, and references used by the bot to justify the verdict.     |


---

## 📂 Project Structure (Detailed)

```
factchecker-bot/
│
├── streamlit_app.py        # Main Streamlit app; entry point for users
├── requirements.txt         # Dependencies for Python environment
├── README.md                # Project documentation
├── src/
│   ├── fact_check.py        # Core logic for claim verification
│   ├── prompt_chain.py    # Web scraping & search helper functions
│   ├── search_tools.py        # AI model initialization and utilities
│   └── utils.py             # Utility functions (logging, formatting, etc.)
└── assets/
    ├── images/             # creenshots

```

---

## 📜 Example Usage (Detailed)

**Claim Input:**

```
The moon is made of cheese.
```

**Output:**

* **Verdict:** ❌ False
* **Explanation:**
  The moon consists of rock, dust, and minerals. NASA missions and geological studies confirm there is no dairy content.
* **Evidence Links:**

  * [NASA Moon Facts](https://solarsystem.nasa.gov/moons/earths-moon/overview/)
  * [Scientific American: Moon Composition](https://www.scientificamerican.com/article/fact-or-fiction-is-the-moon-made-of-cheese/)

**Claim Input (True Example):**

```
Water boils at 100°C at sea level.
```

* **Verdict:** ✅ True
* **Explanation:**
  At standard atmospheric pressure (1 atm), water boils at 100°C. This is a well-established physical fact.

---

## 🛠 Tech Stack (Detailed)

* **Python 3.11+** – Core programming language
* **Streamlit** – Interactive web interface for easy usage
* **OpenAI / AI Models / Gemini AI** – Natural Language Processing for claim classification
* **Requests / Search API** – Fetching real-time information online
* **BeautifulSoup** – Parsing HTML and extracting evidence from web pages
* **Pandas / JSON** – Optional for storing and managing claim histories or datasets

---

## 💡 Pro Tips

* Always verify **uncertain claims** manually if evidence is limited.
* Use short, clear sentences in claims for best AI accuracy.
* Try fun claims like:

  * "Delhi is the capital of India." ✅
  * "Humans have walked on Mars." ❌
  * "Bananas grow on trees." ❌ (Hint: They grow on plants, not trees!)

---