# FUTURE_PE_01 – AI Website Copy Generator

## 📌 Task Overview

This project is part of the **Prompt Engineering Internship (Track Code: PE)**.

The objective is to design a structured prompt system that generates high-quality, conversion-focused website copy for local businesses.

---

## 🏢 Business Chosen

**PromptCraft Studio** – Freelancing Agency
Location: Coimbatore

---

## 🎯 Features

* Generates **Homepage Copy**
* Creates **Services Page Content**
* Produces **Call-To-Action (CTA) Sections**
* Clean **SaaS-style UI using Streamlit**
* Download generated content as `.txt`
* Structured prompt system (modular prompts)

---

## 🧠 Prompt Engineering Approach

This project uses a **modular prompt system**, dividing tasks into separate prompts:

### 📁 Prompts

* `homepage_prompt.txt` → Generates homepage content
* `services_prompt.txt` → Generates services content
* `cta_prompt.txt` → Generates CTA sections

Each prompt is designed to:

* Be reusable
* Produce business-specific output
* Maintain clarity and conversion focus

---

## 📄 Output

* `freelancing_agency_copy.txt` → Final generated website copy including:

  * Homepage
  * Services
  * CTA sections

---

## ⚙️ Tech Stack

* Python
* Streamlit

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 💼 Real-World Use Case

This tool can be used by freelancers and agencies to:

* Generate website content for local businesses
* Improve clarity and conversion rates
* Offer AI-powered copywriting services
* Reduce dependency on expensive copywriters

---

## 📂 Project Structure

```
FUTURE_PE_01
│
├── app.py
├── README.md
├── requirements.txt
│
├── prompts/
│   ├── homepage_prompt.txt
│   ├── services_prompt.txt
│   └── cta_prompt.txt
│
├── outputs/
│   └── freelancing_agency_copy.txt
```

---

## 🔗 Live Demo

(Add your deployed Streamlit link here)

---

## 👤 Author

Syed Mohammed Shahith S
- Ready for real-world use
