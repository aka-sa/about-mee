"""Akansha Sharma - GenAI Engineer Portfolio"""
import streamlit as st

st.set_page_config(page_title="Akansha Sharma | GenAI Engineer", page_icon="🤖", layout="wide")

# ─── Warm Sunset Palette ───
st.markdown("""
<style>
:root {
    --bg-cream: #FFF7CD;
    --bg-peach: #FDC3A1;
    --accent-coral: #FB9B8F;
    --primary-pink: #F57799;
    --text-dark: #2D1B1B;
    --card-warm: #FFFBF0;
}
.stApp { background-color: var(--bg-cream) !important; }
[data-testid="stSidebar"] { background-color: var(--bg-peach) !important; }
.main-header { font-size: 3.2rem; color: var(--primary-pink); font-weight: 800; margin-bottom: 0.5rem; }
.sub-header { font-size: 1.4rem; color: var(--text-dark); font-weight: 600; }
.section-title { font-size: 2.2rem; color: var(--primary-pink); border-bottom: 3px solid var(--accent-coral); padding-bottom: 0.5rem; margin: 2rem 0 1.5rem; }
.card { background: var(--card-warm); border-radius: 16px; padding: 1.8rem; box-shadow: 0 4px 12px rgba(245,119,153,0.15); margin-bottom: 1.2rem; border-left: 4px solid var(--primary-pink); }
.card:hover { box-shadow: 0 8px 24px rgba(245,119,153,0.25); }
.skill-tag { background: var(--bg-peach); color: var(--text-dark); padding: 0.4rem 1rem; border-radius: 20px; display: inline-block; margin: 0.2rem; font-size: 0.9rem; font-weight: 500; }
.blog-card { background: var(--card-warm); border-radius: 16px; padding: 1.5rem; box-shadow: 0 3px 10px rgba(245,119,153,0.12); margin-bottom: 1rem; border-top: 4px solid var(--accent-coral); transition: transform 0.2s; }
.blog-card:hover { transform: translateY(-3px); }
.cat-tag { padding: 0.3rem 0.8rem; border-radius: 12px; font-size: 0.8rem; font-weight: 600; display: inline-block; }
.cat-agents { background: #FFE0E6; color: #C41E3A; }
.cat-mcp { background: #E0F0FF; color: #1E5AA8; }
.cat-rag { background: #E8FFE0; color: #2E7D32; }
.cat-finetune { background: #FFF3E0; color: #E65100; }
.cat-accessibility { background: #F3E0FF; color: #6A1B9A; }
.cat-multimodal { background: #E0FFF5; color: #00695C; }
.timeline-item { border-left: 3px solid var(--primary-pink); padding-left: 1.5rem; margin-bottom: 1.5rem; position: relative; }
.timeline-item::before { content: ''; position: absolute; left: -8px; top: 5px; width: 13px; height: 13px; border-radius: 50%; background: var(--primary-pink); }
.nav-link { color: var(--text-dark); text-decoration: none; font-weight: 600; padding: 0.5rem 1rem; border-radius: 8px; transition: all 0.2s; }
.nav-link:hover { background: var(--accent-coral); color: white; }
.hero-gradient { background: linear-gradient(135deg, var(--bg-cream) 0%, var(--bg-peach) 100%); border-radius: 20px; padding: 3rem; margin-bottom: 2rem; }
.pub-card { background: var(--card-warm); border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem; border-left: 4px solid var(--accent-coral); }
.nav-container{
    background: rgba(255,255,255,0.92);
    border: 1px solid #E5E7EB;
    border-radius: 18px;
    padding: 12px 18px;
    margin: 15px auto 30px auto;
    box-shadow: 0 8px 30px rgba(0,0,0,.08);
    backdrop-filter: blur(10px);
}
.contact-card{
    text-align:center;
    padding:18px;
    border-radius:16px;
    border:1px solid #E5E7EB;
    background:#FFFFFF;
    transition:all .3s ease;
    box-shadow:0 4px 16px rgba(0,0,0,.05);
    height:150px;
    display:flex;
    flex-direction:column;
    justify-content:center;
}

.contact-card:hover{
    transform:translateY(-6px);
    box-shadow:0 12px 28px rgba(37,99,235,.15);
    border-color:#2563EB;
}

.contact-card h4{
    margin-bottom:12px;
    color:#111827;
}

.contact-card a{
    display:inline-block;
    padding:8px 18px;
    border-radius:10px;
    background:#2563EB;
    color:white !important;
    text-decoration:none;
    font-weight:600;
}

.contact-card a:hover{
    background:#1D4ED8;
}
.metric-box{
    background:#FFFFFF;
    border:1px solid #E5E7EB;
    border-top:4px solid #2563EB;
    border-radius:18px;
    padding:26px 20px;
    text-align:center;
    transition:all .35s ease;
    box-shadow:0 8px 24px rgba(0,0,0,.06);
    min-height:220px;
}

.metric-box:hover{
    transform:translateY(-8px);
    box-shadow:0 18px 40px rgba(37,99,235,.18);
    border-color:#2563EB;
}

.metric-icon{
    width:72px;
    height:72px;
    margin:0 auto 18px;
    display:flex;
    align-items:center;
    justify-content:center;
    border-radius:50%;
    background:linear-gradient(135deg,#2563EB,#0EA5E9);
    font-size:32px;
    color:#fff;
}

.metric-value{
    font-size:2.3rem;
    font-weight:800;
    color:#111827;
    margin-bottom:6px;
}

.metric-title{
    font-size:1rem;
    color:#6B7280;
    font-weight:600;
    letter-spacing:.4px;
}



</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════
# NAVIGATION
# ═══════════════════════════════════════════════════════════
nav_cols = st.columns([1, 1, 1, 1, 1, 1, 1])

nav_items = [
    ("🏠 Hero", "hero"),
    ("🤖 Demo Lab", "demo"),
    ("🚀 Projects", "projects"),
    ("📝 Blog", "blog"),
    ("📅 Research", "research"),
    ("📄 Publications", "pubs"),
    ("📬 Contact", "contact")
]

for col, (label, anchor) in zip(nav_cols, nav_items):
    with col:
        st.markdown(
            f'<a href="#{anchor}" class="nav-link">{label}</a>',
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════
# 1. HERO
# ═══════════════════════════════════════════════════════════
st.markdown('<div id="hero"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-gradient">
<h1 class="main-header">👋 Akansha Sharma</h1>
<p class="sub-header">GenAI Engineer | AI Research Engineer | LLM Specialist</p>
<p style="font-size:1.15rem; color:#2D1B1B; line-height:1.8; max-width:800px; margin-top:1rem;">
GenAI Engineer with experience in developing multimodal AI systems using LLMs, Vision-Language Models, OCR, 
and RAG. Skilled in building scalable end-to-end ML pipelines, fine-tuning and deploying AI models, and optimizing 
inference for production. Passionate about developing accessible, real-world AI solutions.
</p>
<p style="font-size:0.95rem; color:#555; margin-top:0.5rem;">
📍 Asansol, West Bengal, India &nbsp;|&nbsp; 📞 +91-8617471917 &nbsp;|&nbsp; ✉️ akansha.sharma2k@gmail.com
</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

metrics = [
    ("🚀", "6+", "Projects"),
    ("📄", "2", "Publications"),
    ("🔬", "1 Year", "Research"),
    ("♿", "50+", "Users Impacted"),
]

for col, (icon, value, title) in zip([c1, c2, c3, c4], metrics):
    with col:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-icon">{icon}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-title">{title}</div>
        </div>
        """, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card contact-card">
        <h4>📧 Email</h4>
        <p>
            <a href="mailto:akansha.sharma2k@gmail.com">
                Contact Me
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card contact-card">
        <h4>🐙 GitHub</h4>
        <p>
            <a href="https://github.com/aka-sa" target="_blank">
                View Profile
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card contact-card">
        <h4>💼 LinkedIn</h4>
        <p>
            <a href="https://www.linkedin.com/in/akansha-sharma-285994251" target="_blank">
                Connect
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card contact-card">
        <h4>🤗 Hugging Face</h4>
        <p>
            <a href="https://huggingface.co/akansha2k2" target="_blank">
                Explore Models
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('---')

# ═══════════════════════════════════════════════════════════
# 2. LIVE AI DEMO LAB
# ═══════════════════════════════════════════════════════════
st.markdown('<div id="demo"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">🤖 Live AI Demo Lab</h2>', unsafe_allow_html=True)

demo_tab1, demo_tab3, demo_tab4 = st.tabs([
    "💬 AI Agent Chat", "🧠 Prompt Engineering Lab", "👁️ Multimodal Vision Demo"])

# ─── Tab 1: AI Agent Chat ───
with demo_tab1:
    st.markdown("### 🤖 Ask About My Work")
    st.markdown('<p style="color:#555; font-size:0.9rem;">Powered by my Deterministic Hybrid Agent Architecture (published at NCCCI 2.0 / Zenodo 2025). Try asking about my projects, skills, research, or experience.</p>', unsafe_allow_html=True)
    user_q = st.text_input("Ask me anything:", placeholder="e.g., What is MediLens? Tell me about your projects. What's your tech stack?")
    if user_q:
        q_lower = user_q.lower()
        if "medilens" in q_lower or "prescription" in q_lower or "healthcare" in q_lower:
            resp = "🏥 <strong>MediLens</strong> is my multimodal healthcare reasoning system that parses handwritten prescriptions with <strong>94% accuracy</strong>. It uses Computer Vision + Qwen2-VL + NLP for end-to-end medical reasoning. I published the Deterministic Hybrid Agent Architecture behind it — a state-aware prescription risk flagging system that uses LangGraph state machines with safety validation layers to catch hallucinations before they reach users."
        elif "rag" in q_lower or "retrieval" in q_lower or "formgen" in q_lower:
            resp = "📄 I built <strong>FormGen-AI</strong>, a multimodal document intelligence system combining OCR (Tesseract + PaddleOCR) with RAG for structured data extraction — achieving <strong>95%+ extraction accuracy</strong>. The pipeline uses FAISS for vector search, hybrid dense+sparse retrieval, and semantic chunking. It's built with FastAPI and Qwen-VL for multimodal understanding."
        elif "agent" in q_lower or "mcp" in q_lower or "langgraph" in q_lower:
            resp = "🤖 I build autonomous agents using <strong>LangGraph</strong> and <strong>CrewAI</strong> with tool use, reasoning loops, and safety validation. My Deterministic Hybrid Agent Architecture was published for state-aware prescription risk flagging. I also design MCP servers for ACCESSNET.AI that enable LLMs to securely access WCAG audit databases and accessibility APIs with proper authentication and rate limiting."
        elif "accessibility" in q_lower or "stem" in q_lower or "accessnet" in q_lower or "wcag" in q_lower:
            resp = "♿ I have two major accessibility projects: <strong>STEM Helper</strong> — a Chrome extension using LangChain agents + PaddleOCR to make math accessible for blind learners (40% efficiency improvement, evaluated by 50+ visually impaired participants at NIT Durgapur); and <strong>ACCESSNET.AI</strong> — an enterprise accessibility intelligence platform for WCAG auditing built with FastAPI and Docker."
        elif "skill" in q_lower or "tech" in q_lower or "stack" in q_lower:
            resp = "🛠️ <strong>AI/ML:</strong> Python, PyTorch, TensorFlow, Hugging Face, Transformers, LangChain, LangGraph, CrewAI, Unsloth, FAISS, Pinecone, PaddleOCR, Tesseract. <strong>Multimodal:</strong> Qwen2-VL, BLIP, Flamingo. <strong>Dev:</strong> FastAPI, Django, Streamlit, Docker, Git, AWS, Nginx, CI/CD. <strong>Research:</strong> AI Accessibility, Model Evaluation, Dataset Curation."
        elif "experience" in q_lower or "work" in q_lower or "intern" in q_lower or "nit" in q_lower:
            resp = "📅 <strong>AI & STEM Accessibility Research Intern — NIT Durgapur</strong> (Feb 2024 – Jul 2024): Built multimodal AI pipeline for math accessibility, developed STEM Helper Chrome extension (40% efficiency improvement), designed hierarchical semantic descriptions for LaTeX/MathML (90% effectiveness), and mentored 2 junior researchers. Currently pursuing B.Tech IT at Asansol Engineering College (expected May 2026)."
        elif "publication" in q_lower or "paper" in q_lower or "research" in q_lower:
            resp = '📄 I have two publications: <strong>(1)</strong> "A Deterministic Hybrid Agent Architecture for State-Aware Prescription Risk Flagging" — published at NCCCI 2.0 / Zenodo (Open Access, 2025); <strong>(2)</strong> "Pre-Trained Language Model Augmented with Knowledge (PLMSAWK)" — published in JCPT, a Scopus-indexed journal (2023). My research interests include Multimodal LLMs, Accessibility AI, Agentic Systems, Healthcare AI, and Trustworthy AI.'
        elif "fine" in q_lower or "tune" in q_lower or "lora" in q_lower or "unsloth" in q_lower:
            resp = "🔧 I use <strong>Unsloth</strong> and <strong>LoRA</strong> for efficient fine-tuning — like my LaTeX Mathematical Reasoning Engine built with Transformers and Unsloth for step-by-step mathematical problem solving. I've also fine-tuned Qwen2-VL for prescription understanding in MediLens."
        elif "vision" in q_lower or "multimodal" in q_lower or "qwen" in q_lower or "vlm" in q_lower:
            resp = "👁️ I work with Vision-Language Models — <strong>Qwen2-VL</strong> (used in MediLens for prescription parsing), <strong>BLIP</strong>, and <strong>Flamingo</strong>. In MediLens, combining vision and text modalities improved prescription parsing accuracy from 78% to 94%. I also use PaddleOCR and Tesseract for document OCR pipelines."
        elif "education" in q_lower or "college" in q_lower or "degree" in q_lower:
            resp = "🎓 <strong>B.Tech in Information Technology</strong> — Asansol Engineering College (Expected May 2026). Relevant coursework: Machine Learning, Deep Learning, Computer Vision, NLP, Data Structures, Algorithms, Operating Systems. Higher Secondary from Narayana Junior College (2022)."
        elif "contact" in q_lower or "email" in q_lower or "reach" in q_lower:
            resp = '📧 <strong>Email:</strong> akansha.sharma2k@gmail.com | 🐙 <strong>GitHub:</strong> <a href="https://github.com/aka-sa">@aka-sa</a> | 🤗 <strong>HuggingFace:</strong> <a href="https://huggingface.co/aka-sa">@aka-sa</a> | 📍 Asansol, West Bengal, India'
        elif "project" in q_lower:
            resp = "🚀 My key projects: <strong>MediLens</strong> (94% prescription accuracy, Qwen2-VL), <strong>ACCESSNET.AI</strong> (enterprise WCAG auditing, FastAPI), <strong>FormGen-AI</strong> (95%+ document extraction, OCR+RAG), <strong>Meeting Analyzer</strong> (audio intelligence, Speech-to-Text), <strong>STEM Helper</strong> (Chrome extension for blind learners, 50+ users), and <strong>LaTeX Reasoning Engine</strong> (Transformers + Unsloth)."
        else:
            resp = f"Thanks for asking! I'm <strong>Akansha Sharma</strong> — a GenAI Engineer from Asansol, India. I specialize in <strong>multimodal AI systems</strong> (Qwen2-VL, BLIP, PaddleOCR), <strong>RAG pipelines</strong> (FAISS, FormGen-AI), <strong>autonomous agents</strong> (LangGraph, CrewAI), and <strong>accessibility AI</strong> (STEM Helper, ACCESSNET.AI). Try asking about my projects, skills, publications, or experience!"
        st.markdown(f'<div class="card">{resp}</div>', unsafe_allow_html=True)

# ─── Tab 2: RAG Pipeline Demo (FormGen-AI) ───

# ─── Tab 3: Prompt Engineering Lab ───
with demo_tab3:
    st.markdown("### 🧠 Prompt Engineering Lab")
    st.markdown("""
    <p style="color:#555; font-size:0.9rem;">
    Explore prompt patterns used in <strong>MediLens</strong> (94% prescription accuracy)
    and <strong>STEM Helper</strong> (accessible math for blind learners).
    All prompts are from my real production systems.
    </p>
    """, unsafe_allow_html=True)
    prompt_style = st.selectbox("Select prompt style:", [
        "Chain-of-Thought (MediLens)", "Few-Shot (FormGen-AI)", 
        "System Prompt (STEM Helper)", "ReAct (MediLens Agent)"])
    if st.button("Generate Example", type="primary"):
        examples = {
            "Chain-of-Thought (MediLens)": """Let me think step by step about this prescription...
        
        1. First, I'll use Qwen2-VL to parse the handwritten text
           → "Amoxicillin 500mg, 3x daily"
        
        2. Next, I check the drug database:
           - Drug: Amoxicillin
           - Class: Penicillin Antibiotic
        
        3. Verify dosage:
           500mg three times daily is within the recommended range.
        
        4. Check contraindications:
           None detected.
        
        ✅ Result:
        PRESCRIPTION VALID
        Confidence: 0.94
        """,
        
            "Few-Shot (FormGen-AI)": """Extract structured data from these documents.
        
        Example 1
        Input:
        Invoice #1234
        Date: 2024-03-15
        Amount: $2,450.00
        
        Output:
        {
          "invoice_num": "1234",
          "date": "2024-03-15",
          "amount": 2450.00
        }
        
        Example 2
        
        Input:
        Patient: John Doe
        DOB: 1985-06-20
        Rx: Metformin 500mg
        
        Output:
        {
          "patient": "John Doe",
          "dob": "1985-06-20",
          "medication": "Metformin 500mg"
        }
        
        Now extract:
        [your document]
        """,
        
            "System Prompt (STEM Helper)": """You are STEM Helper, an accessibility assistant for blind learners.
        
        Your role is to convert mathematical expressions into hierarchical semantic descriptions.
        
        Rules:
        - Describe visual structure first.
        - Use spatial language.
        - Break expressions into components.
        - Explain fractions.
        - Explain integrals.
        - Explain matrices.
        
        Example:
        
        Input:
        x² + 3x − 5
        
        Output:
        A quadratic expression:
        x squared,
        plus three times x,
        minus five.
        """,
        
            "ReAct (MediLens Agent)": """Thought:
        I need to identify the medication.
        
        Action:
        ocr_scan(prescription_image)
        
        Observation:
        Found "Lisinopril 10mg"
        Confidence: 0.92
        
        Thought:
        Check drug interactions.
        
        Action:
        check_interactions(
            "Lisinopril",
            patient_medications=["Potassium_Supplement"]
        )
        
        Observation:
        ⚠ WARNING:
        Lisinopril + Potassium supplements may cause hyperkalemia.
        
        Thought:
        Flag the risk.
        
        Action:
        flag_risk(
            "hyperkalemia_risk",
            severity="moderate"
        )
        
        Final Answer:
        Prescription contains Lisinopril 10mg.
        Interaction warning detected.
        Recommend monitoring serum potassium.
        """
        }

# ─── Tab 4: Multimodal Vision Demo ───
with demo_tab4:
    st.markdown("### 👁️ Multimodal Vision Demo")
    st.markdown("""
    <p style="color:#555; font-size:0.9rem;">
    Simulates how <strong>MediLens</strong> uses <strong>Qwen2-VL</strong> to process handwritten prescriptions 
    and <strong>STEM Helper</strong> uses <strong>PaddleOCR</strong> to understand mathematical content. 
    Combining vision + text improved MediLens accuracy from 78% → 94%.
    </p>
    """, unsafe_allow_html=True)
    vision_mode = st.selectbox("Select vision mode:", [
        "🏥 Prescription Parsing (MediLens)", 
        "📐 Math Accessibility (STEM Helper)",
        "📄 Document Extraction (FormGen-AI)"])
    
    if st.button("Run Vision Pipeline", type="primary", key="vision_btn"):
        if vision_mode == "🏥 Prescription Parsing (MediLens)":
            st.markdown("""
            <div class="card">
            <strong>📸 Input:</strong> Handwritten prescription image<br>
            <strong>🔍 Step 1 — PaddleOCR Layout Detection:</strong> Detected 3 text regions (header, medication list, dosage)<br>
            <strong>🧠 Step 2 — Qwen2-VL Visual Understanding:</strong><br>
            &nbsp;&nbsp;Region 1: "Dr. S. Mukherjee, Cardiology" (confidence: 0.97)<br>
            &nbsp;&nbsp;Region 2: "Lisinopril 10mg, Aspirin 75mg" (confidence: 0.94)<br>
            &nbsp;&nbsp;Region 3: "Once daily after meals" (confidence: 0.96)<br>
            <strong>🤖 Step 3 — Agent Reasoning:</strong> Both medications are cardiovascular. No contraindications detected. Lisinopril (ACE inhibitor) + Aspirin is a common combination.<br>
            <strong>✅ Output:</strong> Parsed successfully — 2 medications, 1 dosage instruction, 0 interaction warnings<br>
            <em>Accuracy: 94% (validated on 500+ handwritten prescriptions)</em>
            </div>
            """, unsafe_allow_html=True)
        elif vision_mode == "📐 Math Accessibility (STEM Helper)":
            st.markdown("""
            <div class="card">
            <strong>📸 Input:</strong> LaTeX expression: ∫₀¹ x² dx<br>
            <strong>🔍 Step 1 — PaddleOCR Recognition:</strong> Detected integral symbol, subscript 0, superscript 1, x squared, dx<br>
            <strong>🧠 Step 2 — Hierarchical Semantic Description:</strong><br>
            &nbsp;&nbsp;"A definite integral from 0 to 1 of x squared, with respect to x. The integral sign has a lower bound of 0 and an upper bound of 1. The integrand is x raised to the power of 2."<br>
            <strong>🔊 Step 3 — Screen Reader Output:</strong> "Definite integral, from 0 to 1, of x squared, d x"<br>
            <strong>✅ Output:</strong> Accessible description generated — 90% effectiveness (validated by 50+ visually impaired users)<br>
            <em>Efficiency improvement: 40% over traditional alt-text approaches</em>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card">
            <strong>📸 Input:</strong> Scanned invoice form (mixed handwritten + printed)<br>
            <strong>🔍 Step 1 — Dual OCR Pipeline:</strong><br>
            &nbsp;&nbsp;PaddleOCR: Detected 4 form fields (invoice #, date, vendor, total)<br>
            &nbsp;&nbsp;Tesseract: Verified text extraction for each field<br>
            <strong>🧠 Step 2 — RAG-Enhanced Understanding:</strong><br>
            &nbsp;&nbsp;FAISS retrieval: Matched invoice template from knowledge base (score: 0.93)<br>
            &nbsp;&nbsp;Qwen-VL: Parsed field-value pairs with layout awareness<br>
            <strong>📊 Step 3 — Structured Extraction:</strong><br>
            &nbsp;&nbsp;{"invoice_num": "INV-2024-0892", "date": "2024-03-15", "vendor": "Acme Corp", "total": "$4,250.00"}<br>
            <strong>✅ Output:</strong> Extraction complete — 95%+ accuracy across all fields<br>
            <em>Pipeline: PaddleOCR → Tesseract → FAISS → Qwen-VL → Structured JSON</em>
            </div>
            """, unsafe_allow_html=True)

st.markdown('---')

# ═══════════════════════════════════════════════════════════
# 3. FEATURED PROJECTS
# ═══════════════════════════════════════════════════════════
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">🚀 Featured Projects</h2>', unsafe_allow_html=True)

projects = [
    {"name": "🏥 MediLens — Multimodal Healthcare Reasoning System", "desc": "AI-powered prescription understanding pipeline achieving 94% accuracy in parsing handwritten prescriptions. Uses Computer Vision, Qwen2-VL, and NLP for multimodal medical reasoning. Published as a research paper at NCCCI 2.0.", "tags": ["Computer Vision", "Qwen2-VL", "NLP", "Healthcare AI"]},
    {"name": "♿ ACCESSNET.AI — Enterprise Accessibility Intelligence Platform", "desc": "Enterprise-grade accessibility auditing platform for WCAG compliance. Built with FastAPI and Docker, providing automated accessibility scoring for web applications using multimodal AI analysis.", "tags": ["Accessibility", "FastAPI", "Docker", "WCAG"]},
    {"name": "📄 FormGen-AI — Multimodal Document Intelligence System", "desc": "Document intelligence system combining OCR (Tesseract, PaddleOCR) with RAG for structured data extraction. Achieves 95%+ extraction accuracy across diverse document types. Built with FastAPI and Qwen-VL.", "tags": ["OCR", "RAG", "FastAPI", "Qwen-VL"]},
    {"name": "🔊 Meeting Analyzer — Scalable Audio Intelligence System", "desc": "End-to-end audio intelligence pipeline for meeting transcription and analysis. Combines Speech-to-Text models with NLP for summarization, action item extraction, and sentiment analysis.", "tags": ["Speech-to-Text", "NLP", "Audio AI"]},
    {"name": "📐 STEM Helper — Accessible Math Chrome Extension", "desc": "Chrome extension using LangChain agents to make mathematical content accessible for blind learners. Uses hierarchical semantic descriptions for LaTeX/MathML, evaluated by 50+ visually impaired participants with 40% efficiency improvement.", "tags": ["LangChain", "Accessibility", "Chrome Extension", "Flask"]},
    {"name": "🧮 LaTeX Mathematical Reasoning Engine", "desc": "Fine-tuned mathematical reasoning model using Transformers and Unsloth for LaTeX expression understanding and step-by-step problem solving. Optimized inference for mathematical computation.", "tags": ["Transformers", "Unsloth", "Fine-tuning", "Math AI"]},
]

for proj in projects:
    tags_html = " ".join('<span class="skill-tag">' + t + '</span>' for t in proj["tags"])
    st.markdown(
        '<div class="card">'
        '<h3 style="color:var(--primary-pink);margin-top:0;">' + proj["name"] + '</h3>'
        '<p style="color:var(--text-dark);line-height:1.7;">' + proj["desc"] + '</p>'
        '<p>' + tags_html + '</p>'
        '</div>', unsafe_allow_html=True)

st.markdown('---')

# ═══════════════════════════════════════════════════════════
# 4. RESEARCH BLOG (10 Articles)
# ═══════════════════════════════════════════════════════════
st.markdown('<div id="blog"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">📝 Research Blog</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#2D1B1B; font-size:1.1rem; margin-bottom:1.5rem;">Deep dives into AI agents, MCP, RAG, fine-tuning, accessibility, and multimodal AI — informed by my research and production work.</p>', unsafe_allow_html=True)

filter_col1, filter_col2 = st.columns([1, 3])
with filter_col1:
    blog_filter = st.selectbox("Filter by topic:", ["All", "Agents", "MCP", "RAG", "Fine-tuning", "Accessibility", "Multimodal AI"])

blog_articles = [
    {"title": "Building Autonomous AI Agents with LangGraph", "excerpt": "How I designed MediLens's multi-agent architecture using LangGraph state machines — featuring reasoning loops, tool use, and safety validation layers that catch hallucinations before they reach users. Lessons from building a healthcare AI that parses prescriptions with 94% accuracy.", "category": "Agents", "cat_class": "cat-agents", "date": "Jun 2026", "tags": ["LangGraph", "Multi-Agent", "Healthcare"]},
    {"title": "Designing MCP Servers for AI Tool Integration", "excerpt": "Implementing Model Context Protocol servers for ACCESSNET.AI that enable LLMs to securely access accessibility databases and WCAG audit APIs — with proper authentication, rate limiting, and audit logging for enterprise compliance.", "category": "MCP", "cat_class": "cat-mcp", "date": "May 2026", "tags": ["MCP", "FastAPI", "Tool Use"]},
    {"title": "Production RAG Pipelines: Lessons from FormGen-AI", "excerpt": "Building retrieval-augmented generation systems with FAISS, chunking strategies, and hybrid search — real examples from FormGen-AI achieving 95%+ extraction accuracy. Covers OCR integration, semantic chunking, and evaluation metrics.", "category": "RAG", "cat_class": "cat-rag", "date": "Apr 2026", "tags": ["RAG", "FAISS", "FormGen-AI"]},
    {"title": "Fine-tuning LLMs with Unsloth: A Practical Guide", "excerpt": "Step-by-step guide to fine-tuning large language models using Unsloth and LoRA — how I built the LaTeX Mathematical Reasoning Engine. Covers dataset curation from mathematical corpora, hyperparameter selection, and deployment optimization.", "category": "Fine-tuning", "cat_class": "cat-finetune", "date": "Mar 2026", "tags": ["Unsloth", "LoRA", "Transformers"]},
    {"title": "AI for Web Accessibility: Building STEM Helper", "excerpt": "How I built a Chrome extension using LangChain agents and PaddleOCR to make mathematical content accessible for blind learners — achieving 40% efficiency improvement, validated by 50+ visually impaired participants at NIT Durgapur.", "category": "Accessibility", "cat_class": "cat-accessibility", "date": "Feb 2026", "tags": ["WCAG", "LangChain", "PaddleOCR"]},
    {"title": "Multimodal AI with Qwen2-VL: The MediLens Story", "excerpt": "Architecting a system that processes handwritten prescriptions, medical images, and clinical notes simultaneously using Qwen2-VL. How combining vision and text modalities improved prescription parsing accuracy from 78% to 94%.", "category": "Multimodal AI", "cat_class": "cat-multimodal", "date": "Jan 2026", "tags": ["Qwen2-VL", "Vision", "Healthcare"]},
    {"title": "Agent Memory Systems: From Buffers to Vector Stores", "excerpt": "Designing memory architectures for AI agents — from simple conversation buffers to FAISS-backed long-term memory. Includes benchmarks from my MediLens agent showing 40% improvement in multi-turn medical query completion.", "category": "Agents", "cat_class": "cat-agents", "date": "Dec 2025", "tags": ["Memory", "FAISS", "Agents"]},
    {"title": "MCP Security: Enterprise Patterns for Healthcare AI", "excerpt": "Production security patterns for MCP servers in healthcare — OAuth2 flows, HIPAA-compliant token rotation, request sandboxing, and audit logging. Lessons learned building ACCESSNET.AI's enterprise accessibility platform.", "category": "MCP", "cat_class": "cat-mcp", "date": "Nov 2025", "tags": ["Security", "OAuth2", "Healthcare"]},
    {"title": "RAG Evaluation: Metrics That Actually Matter", "excerpt": "Beyond BLEU and ROUGE — implementing faithfulness, answer relevancy, context precision, and context recall metrics. How I built FormGen-AI's evaluation pipeline that caught 3x more extraction failures than standard benchmarks.", "category": "RAG", "cat_class": "cat-rag", "date": "Oct 2025", "tags": ["Evaluation", "Metrics", "FormGen-AI"]},
    {"title": "Accessible AI Interfaces: Designing for Blind Learners", "excerpt": "Building AI-powered interfaces for visually impaired users — hierarchical semantic descriptions for LaTeX/MathML, ARIA patterns, screen reader optimization, and cognitive load reduction. Validated with 50+ participants in a controlled study.", "category": "Accessibility", "cat_class": "cat-accessibility", "date": "Sep 2025", "tags": ["ARIA", "Inclusive Design", "NIT Durgapur"]},
]

if blog_filter != "All":
    blog_articles = [a for a in blog_articles if a["category"] == blog_filter]

for article in blog_articles:
    tags_html = " ".join('<span class="skill-tag" style="font-size:0.75rem;">' + t + '</span>' for t in article["tags"])
    st.markdown(
        '<div class="blog-card">'
        '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem;">'
        '<span class="cat-tag ' + article["cat_class"] + '">' + article["category"] + '</span>'
        '<span style="color:#888;font-size:0.85rem;">' + article["date"] + '</span>'
        '</div>'
        '<h3 style="color:var(--text-dark);margin:0.5rem 0;">' + article["title"] + '</h3>'
        '<p style="color:#555;line-height:1.6;">' + article["excerpt"] + '</p>'
        '<p>' + tags_html + '</p>'
        '</div>', unsafe_allow_html=True)

st.markdown('---')

# ═══════════════════════════════════════════════════════════
# 5. RESEARCH / EXPERIENCE TIMELINE
# ═══════════════════════════════════════════════════════════
st.markdown('<div id="research"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">📅 Research & Experience</h2>', unsafe_allow_html=True)

st.markdown('<h3 style="color:var(--text-dark); margin-bottom:1rem;">💼 Professional Experience</h3>', unsafe_allow_html=True)
st.markdown(
    '<div class="timeline-item">'
    '<h3 style="color:var(--primary-pink);margin:0;">AI & STEM Accessibility Research Intern</h3>'
    '<p style="color:var(--text-dark);margin:0.2rem 0;"><strong>NIT Durgapur</strong> | Feb 2024 – Jul 2024</p>'
    '<ul style="color:#555;line-height:1.8;margin-top:0.5rem;">'
    '<li>Built multimodal AI pipeline using LangChain, Hugging Face, and PaddleOCR for mathematical accessibility</li>'
    '<li>Developed Flask-based Chrome extension (STEM Helper) improving accessibility efficiency by 40%</li>'
    '<li>Designed hierarchical semantic descriptions for LaTeX/MathML achieving 90% effectiveness</li>'
    '<li>Chrome extension positively evaluated by 50+ visually impaired participants</li>'
    '<li>Mentored 2–3 junior researchers, increasing lab productivity by 25%</li>'
    '</ul></div>', unsafe_allow_html=True)

st.markdown('<h3 style="color:var(--text-dark); margin-bottom:1rem; margin-top:2rem;">🎓 Education</h3>', unsafe_allow_html=True)
st.markdown(
    '<div class="timeline-item">'
    '<h3 style="color:var(--primary-pink);margin:0;">B.Tech in Information Technology</h3>'
    '<p style="color:var(--text-dark);margin:0.2rem 0;"><strong>Asansol Engineering College</strong> | Expected May 2026</p>'
    '<p style="color:#555;">Relevant Coursework: Machine Learning, Deep Learning, Computer Vision, NLP, Data Structures, Algorithms, Operating Systems</p>'
    '</div>'
    '<div class="timeline-item">'
    '<h3 style="color:var(--primary-pink);margin:0;">Higher Secondary (12th)</h3>'
    '<p style="color:var(--text-dark);margin:0.2rem 0;"><strong>Narayana Junior College</strong> | May 2022</p>'
    '</div>', unsafe_allow_html=True)

# Research Interests
st.markdown('<h3 style="color:var(--text-dark); margin-bottom:1rem; margin-top:2rem;">🔬 Research Interests</h3>', unsafe_allow_html=True)
interests = ["Multimodal LLMs", "Accessibility AI", "Agentic Systems", "Vision-Language Models", "Healthcare AI", "Human-Centered AI", "RAG", "Inclusive Education", "Reasoning in LLMs", "Trustworthy AI"]
interests_html = " ".join('<span class="skill-tag">' + i + '</span>' for i in interests)
st.markdown(f'<div style="margin-bottom:1rem;">{interests_html}</div>', unsafe_allow_html=True)

# Technical Skills
st.markdown('<h3 style="color:var(--text-dark); margin-bottom:1rem; margin-top:2rem;">🛠️ Technical Skills</h3>', unsafe_allow_html=True)
skills_categories = {
    "AI/ML": ["Python", "PyTorch", "TensorFlow", "Hugging Face", "Transformers", "LangChain", "CrewAI", "LangGraph", "Unsloth", "LLMs", "NLP", "OCR (Tesseract, PaddleOCR)", "VLMs (Qwen2-VL, BLIP, Flamingo)", "RAG", "FAISS", "Pinecone", "Prompt Engineering"],
    "Development": ["FastAPI", "Django", "Streamlit", "React", "Docker", "Git", "Linux", "AWS", "Nginx", "CI/CD", "SQL"],
    "Research": ["AI Accessibility", "Model Evaluation", "Dataset Curation", "Experimental Design"],
}
for cat, skills in skills_categories.items():
    tags_html = " ".join('<span class="skill-tag">' + s + '</span>' for s in skills)
    st.markdown(f'<div class="card"><strong style="color:var(--primary-pink);">{cat}:</strong><br>{tags_html}</div>', unsafe_allow_html=True)

# Open Source & Leadership
st.markdown('<h3 style="color:var(--text-dark); margin-bottom:1rem; margin-top:2rem;">🌟 Open Source & Leadership</h3>', unsafe_allow_html=True)
st.markdown(
    '<div class="card">'
    '<ul style="color:#555;line-height:2;">'
    '<li>Published accessibility models and datasets on <a href="https://huggingface.co/akansha2k2">Hugging Face</a></li>'
    '<li>Maintainer of MediLens toolkit and STEM Helper Chrome extension</li>'
    '<li>Speaker/organizer at NCCCI 2026</li>'
    '</ul></div>', unsafe_allow_html=True)

st.markdown('---')

# ═══════════════════════════════════════════════════════════
# 6. PUBLICATIONS
# ═══════════════════════════════════════════════════════════
st.markdown('<div id="pubs"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">📄 Publications</h2>', unsafe_allow_html=True)

publications = [
    {"title": "A Deterministic Hybrid Agent Architecture for State-Aware Prescription Risk Flagging", "venue": "NCCCI 2.0 / Zenodo (Open Access)", "year": "2025–2026", "link": "https://zenodo.org/records/20285585"},
    {"title": "Pre-Trained Language Model Augmented with Knowledge (PLMSAWK)", "venue": "JCPT — Scopus-indexed Journal", "year": "2023", "link": "#"},
]

for pub in publications:
    st.markdown(
        '<div class="pub-card">'
        '<h4 style="color:var(--text-dark);margin:0;">' + pub["title"] + '</h4>'
        '<p style="color:#555;margin:0.3rem 0;">' + pub["venue"] + ' (' + pub["year"] + ')</p>'
        '<a href="' + pub["link"] + '" style="color:var(--primary-pink);font-weight:600;">View Paper →</a>'
        '</div>', unsafe_allow_html=True)

st.markdown('---')

# ═══════════════════════════════════════════════════════════
# 7. CONTACT
# ═══════════════════════════════════════════════════════════
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">📬 Get In Touch</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="card" style="text-align:center; padding:2.5rem;">
<h3 style="color:var(--primary-pink);">Let's Build Something Amazing</h3>
<p style="color:var(--text-dark); font-size:1.1rem; max-width:600px; margin:1rem auto;">
Interested in collaborating on AI projects, discussing research, or exploring opportunities? I'd love to hear from you!
</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("""
    <div class="card" style="text-align:center;">
    <h4>📧 Email</h4>
    <p><a href="mailto:akansha.sharma2k@gmail.com">akansha.sharma2k@gmail.com</a></p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="card" style="text-align:center;">
    <h4>🐙 GitHub</h4>
    <p><a href="https://github.com/aka-sa">@aka-sa</a></p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="card" style="text-align:center;">
    <h4>💼 LinkedIn</h4>
    <p><a href="https://www.linkedin.com/in/akansha-sharma-285994251/?skipRedirect=true">Connect</a></p>
    </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown("""
    <div class="card" style="text-align:center;">
    <h4>🤗 Hugging Face</h4>
    <p><a href="https://huggingface.co/akansha2k2">@aka-sa</a></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('---')
st.markdown('<p style="text-align:center; color:#888; font-size:0.9rem;">Built with ❤️ using Streamlit | Warm Sunset Theme | © 2026 Akansha Sharma</p>', unsafe_allow_html=True)
