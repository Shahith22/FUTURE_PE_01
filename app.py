import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="PromptCraft Studio", layout="wide")

# ---------------- SIMPLE CLEAN STYLE ----------------
st.markdown("""
<style>
.output {
    padding: 20px;
    border-radius: 10px;
    background-color: #e3f2fd;
    color: black;
    font-size: 16px;
    white-space: pre-wrap;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🚀 PromptCraft Studio")

# ---------------- INPUT ----------------
business_name = st.text_input("Business Name", "PromptCraft Studio")
business_type = st.text_input("Business Type", "Freelancing Agency")
location = st.text_input("Location", "Coimbatore")

generate = st.button("Generate Copy")

# ---------------- DEFAULT CONTENT ----------------
homepage_content = """Headline:
Grow Your Business with High-Converting Website Copy

Sub-headline:
We help you attract more customers.

Intro:
We create content that builds trust and increases conversions.

CTA:
Book your free consultation today.
"""

services_content = """1. Website Copywriting
High-converting website content.

2. Content Optimization
Improve your existing content.

3. AI Content Solutions
Generate content faster.

Why Choose Us:
Affordable, Fast, Results-driven.
"""

cta_content = """Booking CTA:
Start today.

Urgency CTA:
Limited slots available.

Trust CTA:
Trusted by businesses.
"""

# ---------------- GENERATE NEW CONTENT ----------------
if generate:
    homepage_content = f"""Headline:
Grow your {business_type} in {location}

Sub-headline:
{business_name} helps you attract more customers.

Intro:
We build strong website content that converts visitors into clients.

CTA:
Contact us today.
"""

    services_content = f"""1. Website Copywriting
Custom content for {business_type}.

2. Content Optimization
Improve clarity and engagement.

3. AI Content Systems
Generate faster content.

Why Choose {business_name}:
Fast, Affordable, Result-focused.
"""

    cta_content = f"""Booking CTA:
Start with {business_name} today.

Urgency CTA:
Limited slots in {location}.

Trust CTA:
Trusted for real results.
"""

# ---------------- ALWAYS SHOW OUTPUT ----------------
tab1, tab2, tab3 = st.tabs(["🏠 Homepage", "🛠 Services", "🔥 CTA"])

with tab1:
    st.markdown(f"<div class='output'>{homepage_content}</div>", unsafe_allow_html=True)

with tab2:
    st.markdown(f"<div class='output'>{services_content}</div>", unsafe_allow_html=True)

with tab3:
    st.markdown(f"<div class='output'>{cta_content}</div>", unsafe_allow_html=True)

# ---------------- DOWNLOAD ----------------
full_text = f"""
HOMEPAGE:
{homepage_content}

SERVICES:
{services_content}

CTA:
{cta_content}
"""

st.download_button("📥 Download Copy", full_text, "website_copy.txt")

# ---------------- FOOTER ----------------
st.markdown("---")
st.write("Built for Freelance Copywriting Service")