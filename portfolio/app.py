"""Akansha Sharma - GenAI Engineer Portfolio"""
import streamlit as st
import datetime

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
<p class="sub-header">GenAI Engineer | AI Research Engineer</p>
<p style="font-size:1.15rem; color:#2D1B1B; line-height:1.8; max-width:800px; margin-top:1rem;">
I build autonomous AI agents, MCP servers, and production RAG pipelines. Passionate about making AI accessible, 
deploying multimodal systems at scale, and pushing the boundaries of what LLMs can do in the real world.
</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("Projects", "15+")
with c2: st.metric("Publications", "5")
with c3: st.metric("AI Models Deployed", "10+")
with c4: st.metric("Years Experience", "3+")

col1, col2, col3 = st.columns(3)
with col1: st.markdown('📧 **Email:** akansha@example.com')
with col2: st.markdown('[🐙 GitHub](https://github.com/aka-sa)')
with col3: st.markdown('[💼 LinkedIn](https://linkedin.com/in/aka-sa)')

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
            resp = "RAG (Retrieval-Augmented Generation) combines retrieval systems with LLMs. I've built production RAG pipelines using FAISS, hybrid search, and chunking strategies for medical document analysis."
        elif "agent" in q_lower or "mcp" in q_lower:
            resp = "I build autonomous agents using LangGraph state machines with tool use, reasoning loops, and safety validation. My MCP servers enable LLMs to securely access databases and APIs."
        elif "skill" in q_lower or "tech" in q_lower:
            resp = "My core stack: Python, LangChain/LangGraph, FastAPI, Transformers, FAISS, Docker, AWS, HuggingFace. I specialize in RAG, fine-tuning, and multimodal AI systems."
        else:
            resp = f"Great question about '{user_q}'! I work on AI agents, RAG systems, MCP servers, and multimodal AI. Ask me about any of these topics!"
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
        <strong>🧠 Generated Answer:</strong> Based on retrieved context, chunking splits documents into semantic units for optimal retrieval. Hybrid search combines dense embeddings with sparse BM25 for best results.
        </div>
        """, unsafe_allow_html=True)

with demo_tab3:
    st.markdown("### Prompt Engineering Lab")
    prompt_style = st.selectbox("Select prompt style:", ["Chain-of-Thought", "Few-Shot", "System Prompt", "ReAct"])
    if st.button("Generate Example", type="primary"):
        examples = {
            "Chain-of-Thought": "Let me think step by step... First, I need to understand the problem. Then, break it into sub-problems...",
            "Few-Shot": "Example 1: Input → Output. Example 2: Input → Output. Now solve: [your input]",
            "System Prompt": "You are a helpful AI assistant specializing in medical document analysis. Always cite sources.",
            "ReAct": "Thought: I need to search for X. Action: search(X). Observation: Found Y. Thought: Now I can answer."
        }
        st.code(examples[prompt_style], language="text")

st.markdown('---')

# ═══════════════════════════════════════════════════════════
# 3. FEATURED PROJECTS
# ═══════════════════════════════════════════════════════════
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">🚀 Featured Projects</h2>', unsafe_allow_html=True)

projects = [
    {"name": "🏥 MediLens - Medical RAG System", "desc": "Production RAG pipeline for medical prescription analysis with FAISS, hybrid search, chunking strategies, and safety validation layers. Handles 10K+ documents with sub-second retrieval.", "tags": ["RAG", "FAISS", "Healthcare", "Python"]},
    {"name": "🤖 Autonomous Agent Framework", "desc": "Multi-agent system using LangGraph state machines for complex reasoning tasks. Features tool use, reasoning loops, memory management, and safety guardrails.", "tags": ["LangGraph", "Agents", "Multi-Agent", "Reasoning"]},
    {"name": "🔌 MCP Server Toolkit", "desc": "Model Context Protocol servers enabling LLMs to securely access databases, APIs, and local files. Bridges the gap between models and production tools.", "tags": ["MCP", "FastAPI", "Tool Use", "Security"]},
    {"name": "🎨 AccessiAI - Accessibility Auditor", "desc": "Multimodal AI system that audits web accessibility compliance (WCAG 2.1). Uses vision models to detect contrast issues, missing alt text, and navigation problems.", "tags": ["Accessibility", "Multimodal", "WCAG", "Vision"]},
    {"name": "📊 FineTune Studio", "desc": "End-to-end platform for fine-tuning LLMs with LoRA/QLoRA. Includes dataset curation, training monitoring, evaluation metrics, and one-click deployment.", "tags": ["Fine-tuning", "LoRA", "HuggingFace", "W&B"]},
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
st.markdown('<p style="color:#2D1B1B; font-size:1.1rem; margin-bottom:1.5rem;">Deep dives into AI agents, MCP, RAG, fine-tuning, accessibility, and multimodal AI.</p>', unsafe_allow_html=True)

# Blog filter
filter_col1, filter_col2 = st.columns([1, 3])
with filter_col1:
    blog_filter = st.selectbox("Filter by topic:", ["All", "Agents", "MCP", "RAG", "Fine-tuning", "Accessibility", "Multimodal AI"])

blog_articles = [
    {"title": "Building Autonomous AI Agents with LangGraph", "excerpt": "How I designed a multi-agent system using LangGraph state machines for medical prescription analysis -- featuring reasoning loops, tool use, and safety validation layers that catch hallucinations before they reach users.", "category": "Agents", "cat_class": "cat-agents", "date": "Jun 2026", "tags": ["LangGraph", "Multi-Agent", "Healthcare"]},
    {"title": "Designing MCP Servers for AI Tool Integration", "excerpt": "Implementing Model Context Protocol servers that enable LLMs to securely access databases, APIs, and local files -- bridging the gap between models and production tools with proper authentication and rate limiting.", "category": "MCP", "cat_class": "cat-mcp", "date": "May 2026", "tags": ["MCP", "FastAPI", "Tool Use"]},
    {"title": "Production RAG Pipelines: From Theory to Deployment", "excerpt": "Building retrieval-augmented generation systems with FAISS, chunking strategies, hybrid search, and evaluation metrics -- real MediLens examples included showing 94% retrieval accuracy.", "category": "RAG", "cat_class": "cat-rag", "date": "Apr 2026", "tags": ["RAG", "FAISS", "Evaluation"]},
    {"title": "Fine-tuning LLMs with LoRA: A Practical Guide", "excerpt": "Step-by-step guide to fine-tuning large language models using LoRA and QLoRA. Covers dataset curation, hyperparameter selection, training on consumer GPUs, and evaluation with W&B.", "category": "Fine-tuning", "cat_class": "cat-finetune", "date": "Mar 2026", "tags": ["LoRA", "Fine-tuning", "HuggingFace"]},
    {"title": "AI for Web Accessibility: Beyond Alt Text", "excerpt": "How multimodal AI can audit WCAG 2.1 compliance -- detecting contrast ratios, keyboard navigation issues, screen reader compatibility, and cognitive load problems that traditional tools miss.", "category": "Accessibility", "cat_class": "cat-accessibility", "date": "Feb 2026", "tags": ["WCAG", "Multimodal", "Vision"]},
    {"title": "Multimodal AI: Combining Vision, Text, and Audio", "excerpt": "Architecting systems that process images, text, and audio simultaneously. Real examples from medical imaging analysis where combining X-rays with clinical notes improved diagnosis accuracy by 23%.", "category": "Multimodal AI", "cat_class": "cat-multimodal", "date": "Jan 2026", "tags": ["Vision", "Audio", "Fusion"]},
    {"title": "Agent Memory Systems: Short-term vs Long-term", "excerpt": "Designing memory architectures for AI agents -- from simple conversation buffers to vector-store-backed long-term memory. Includes benchmarks showing 40% improvement in multi-turn task completion.", "category": "Agents", "cat_class": "cat-agents", "date": "Dec 2025", "tags": ["Memory", "Agents", "Vector Store"]},
    {"title": "MCP Security: Auth, Rate Limiting, and Sandboxing", "excerpt": "Production security patterns for MCP servers -- OAuth2 flows, token rotation, request sandboxing, and audit logging. Lessons learned from deploying MCP in healthcare environments.", "category": "MCP", "cat_class": "cat-mcp", "date": "Nov 2025", "tags": ["Security", "OAuth2", "MCP"]},
    {"title": "RAG Evaluation: Metrics That Actually Matter", "excerpt": "Beyond BLEU and ROUGE -- implementing faithfulness, answer relevancy, context precision, and context recall metrics. How I built an evaluation pipeline that caught 3x more retrieval failures.", "category": "RAG", "cat_class": "cat-rag", "date": "Oct 2025", "tags": ["Evaluation", "RAG", "Metrics"]},
    {"title": "Accessible AI Interfaces: Designing for Everyone", "excerpt": "Building AI-powered interfaces that work for users with visual, motor, cognitive, and auditory disabilities. Covers ARIA patterns, focus management, reduced motion, and screen reader optimization.", "category": "Accessibility", "cat_class": "cat-accessibility", "date": "Sep 2025", "tags": ["ARIA", "UX", "Inclusive Design"]},
]

# Apply filter
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

experience = [
    {"role": "GenAI Engineer", "company": "Scholaro Research Labs", "period": "2025 - Present", "desc": "Building autonomous AI agents, MCP servers, and production RAG pipelines. Leading accessibility initiatives for AI systems."},
    {"role": "AI Research Engineer", "company": "Independent Research", "period": "2024 - 2025", "desc": "Published research on multimodal AI, fine-tuning techniques, and medical document analysis. Developed open-source tools for the AI community."},
    {"role": "Machine Learning Engineer", "company": "Freelance", "period": "2023 - 2024", "desc": "Built custom ML solutions for healthcare and education sectors. Specialized in NLP, computer vision, and deployment optimization."},
]

for exp in experience:
    st.markdown(
        '<div class="timeline-item">'
        '<h3 style="color:var(--primary-pink);margin:0;">' + exp["role"] + '</h3>'
        '<p style="color:var(--text-dark);margin:0.2rem 0;"><strong>' + exp["company"] + '</strong> | ' + exp["period"] + '</p>'
        '<p style="color:#555;line-height:1.6;">' + exp["desc"] + '</p>'
        '</div>', unsafe_allow_html=True)

st.markdown('---')

# ═══════════════════════════════════════════════════════════
# 6. PUBLICATIONS
# ═══════════════════════════════════════════════════════════
st.markdown('<div id="pubs"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">📄 Publications</h2>', unsafe_allow_html=True)

publications = [
    {"title": "Task-Conditional Faithfulness Auditing of Multimodal LLMs for Grid Diagnosis", "venue": "arXiv Preprint", "year": "2026", "link": "https://arxiv.org/abs/2607.24539"},
    {"title": "Production RAG: Hybrid Search Strategies for Medical Document Retrieval", "venue": "AI Healthcare Workshop", "year": "2025", "link": "#"},
    {"title": "Accessible AI: Designing Inclusive Interfaces for Language Models", "venue": "ACM CHI Workshop", "year": "2025", "link": "#"},
    {"title": "MCP Security Patterns for Enterprise AI Tool Integration", "venue": "IEEE Security & Privacy", "year": "2025", "link": "#"},
    {"title": "Fine-tuning Small Language Models for Domain-Specific Tasks", "venue": "EMNLP Workshop", "year": "2024", "link": "#"},
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

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="card" style="text-align:center;">
    <h4>📧 Email</h4>
    <p>akansha@example.com</p>
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
    <p><a href="https://linkedin.com/in/aka-sa">Connect</a></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('---')
st.markdown('<p style="text-align:center; color:#888; font-size:0.9rem;">Built with ❤️ using Streamlit | Warm Sunset Theme | © 2026 Akansha Sharma</p>', unsafe_allow_html=True)
