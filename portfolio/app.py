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
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════
# NAVIGATION
# ═══════════════════════════════════════════════════════════
nav_cols = st.columns([1, 1, 1, 1, 1, 1, 1])
nav_items = [("🏠 Hero", "hero"), ("🤖 Demo Lab", "demo"), ("🚀 Projects", "projects"),
             ("📝 Blog", "blog"), ("📅 Research", "research"), ("📄 Publications", "pubs"), ("📬 Contact", "contact")]
for col, (label, anchor) in zip(nav_cols, nav_items):
    with col:
        st.markdown(f'<a href="#{anchor}" class="nav-link" style="text-align:center;display:block;">{label}</a>', unsafe_allow_html=True)
st.markdown('---')

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
with c1: st.metric("Projects", "6+")
with c2: st.metric("Publications", "2")
with c3: st.metric("Research Experience", "6 months")
with c4: st.metric("Accessibility Impact", "50+ users")

col1, col2, col3, col4 = st.columns(4)
with col1: st.markdown('📧 **Email:** akansha.sharma2k@gmail.com')
with col2: st.markdown('[🐙 GitHub](https://github.com/aka-sa)')
with col3: st.markdown('[💼 LinkedIn](https://linkedin.com/in/akansha-sharma)')
with col4: st.markdown('[🤗 Hugging Face](https://huggingface.co/aka-sa)')

st.markdown('---')

# ═══════════════════════════════════════════════════════════
# 2. LIVE AI DEMO LAB
# ═══════════════════════════════════════════════════════════
st.markdown('<div id="demo"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">🤖 Live AI Demo Lab</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#2D1B1B; font-size:1.1rem;">Interactive demos of my AI systems. Try them live!</p>', unsafe_allow_html=True)

demo_tab1, demo_tab2, demo_tab3 = st.tabs(["💬 AI Agent Chat", "🔍 RAG Query Demo", "🧠 Prompt Engineering Lab"])

with demo_tab1:
    st.markdown("### Autonomous AI Agent")
    user_q = st.text_input("Ask my AI agent anything:", placeholder="e.g., What is RAG?")
    if user_q:
        q_lower = user_q.lower()
        if "rag" in q_lower:
            resp = "RAG (Retrieval-Augmented Generation) combines retrieval systems with LLMs. I've built production RAG pipelines using FAISS, hybrid search, and chunking strategies — including the FormGen-AI document intelligence system achieving 95%+ extraction accuracy."
        elif "agent" in q_lower or "mcp" in q_lower:
            resp = "I build autonomous agents using LangGraph and CrewAI with tool use, reasoning loops, and safety validation. My Deterministic Hybrid Agent Architecture was published for state-aware prescription risk flagging."
        elif "skill" in q_lower or "tech" in q_lower:
            resp = "My core stack: Python, PyTorch, LangChain/LangGraph, FastAPI, Transformers, FAISS, Docker, AWS. I specialize in multimodal AI (Qwen2-VL, BLIP, Flamingo), RAG, fine-tuning (Unsloth/LoRA), and accessibility AI."
        elif "accessibility" in q_lower:
            resp = "I built STEM Helper — a Chrome extension using LangChain agents for blind learners, achieving 40% improvement in accessibility efficiency. Evaluated by 50+ visually impaired participants during my research internship at NIT Durgapur."
        else:
            resp = f"Great question about '{user_q}'! I work on AI agents, RAG systems, multimodal AI, and accessibility. Ask me about any of these topics!"
        st.markdown(f'<div class="card"><strong>🤖 AI Agent:</strong> {resp}</div>', unsafe_allow_html=True)

with demo_tab2:
    st.markdown("### RAG Pipeline Demo")
    rag_query = st.text_input("Query the knowledge base:", placeholder="e.g., How does chunking work?", key="rag")
    if rag_query:
        st.markdown("""
        <div class="card">
        <strong>📄 Retrieved Chunks:</strong><br>
        1. "Chunking strategies divide documents into semantic units..." (score: 0.94)<br>
        2. "Hybrid search combines dense + sparse retrieval..." (score: 0.87)<br>
        3. "FAISS enables fast similarity search at scale..." (score: 0.82)<br><br>
        <strong>🧠 Generated Answer:</strong> Based on retrieved context, chunking splits documents into semantic units for optimal retrieval. Hybrid search combines dense embeddings with sparse BM25 for best results. This mirrors the approach used in my FormGen-AI system (95%+ extraction accuracy).
        </div>
        """, unsafe_allow_html=True)

with demo_tab3:
    st.markdown("### Prompt Engineering Lab")
    prompt_style = st.selectbox("Select prompt style:", ["Chain-of-Thought", "Few-Shot", "System Prompt", "ReAct"])
    if st.button("Generate Example", type="primary"):
        examples = {
            "Chain-of-Thought": "Let me think step by step... First, I need to understand the prescription. Then, identify drug interactions using MediLens's knowledge graph...",
            "Few-Shot": "Example 1: Handwritten 'Amoxicillin 500mg' → Parsed: Amoxicillin 500mg (Confidence: 0.96). Example 2: 'Metformin 850mg' → Parsed: Metformin 850mg (Confidence: 0.94). Now parse: [input]",
            "System Prompt": "You are MediLens, a healthcare AI assistant specializing in prescription analysis. Always validate drug interactions and flag contraindications. Cite medical sources.",
            "ReAct": "Thought: I need to identify the medication in this prescription. Action: ocr_scan(prescription_image). Observation: Found 'Lisinopril 10mg'. Thought: Now check for interactions. Action: check_interactions('Lisinopril', patient_meds). Observation: Warning — interaction with Potassium supplements."
        }
        st.code(examples[prompt_style], language="text")

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
    '<li>Published accessibility models and datasets on <a href="https://huggingface.co/aka-sa">Hugging Face</a></li>'
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
    {"title": "A Deterministic Hybrid Agent Architecture for State-Aware Prescription Risk Flagging", "venue": "NCCCI 2.0 / Zenodo (Open Access)", "year": "2025–2026", "link": "https://zenodo.org"},
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
    <p><a href="https://linkedin.com/in/akansha-sharma">Connect</a></p>
    </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown("""
    <div class="card" style="text-align:center;">
    <h4>🤗 Hugging Face</h4>
    <p><a href="https://huggingface.co/aka-sa">@aka-sa</a></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('---')
st.markdown('<p style="text-align:center; color:#888; font-size:0.9rem;">Built with ❤️ using Streamlit | Warm Sunset Theme | © 2026 Akansha Sharma</p>', unsafe_allow_html=True)
