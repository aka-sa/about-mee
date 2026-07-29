"""Akansha Sharma - GenAI Engineer Portfolio (Minimal Version)"""
import streamlit as st

st.set_page_config(
    page_title="Akansha Sharma | GenAI Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with warm sunset palette
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
.stApp { background-color: var(--bg-cream); }
.main-header {
    font-size: 3rem;
    color: var(--primary-pink);
    font-weight: 700;
    margin-bottom: 1rem;
}
.section-title {
    font-size: 2rem;
    color: var(--text-dark);
    border-bottom: 3px solid var(--accent-coral);
    padding-bottom: 0.5rem;
    margin-top: 2rem;
    margin-bottom: 1.5rem;
}
.card {
    background: var(--card-warm);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
}
.skill-tag {
    background: var(--bg-peach);
    color: var(--text-dark);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    display: inline-block;
    margin: 0.25rem;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<h1 class="main-header">👋 Hi, I\'m Akansha Sharma</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.3rem; color: var(--text-dark);"><strong>GenAI Engineer | AI Research Engineer</strong></p>', unsafe_allow_html=True)
st.markdown('''
<p style="font-size: 1.1rem; color: var(--text-dark); line-height: 1.8;">
I build autonomous AI agents, MCP servers, and production RAG pipelines.
Passionate about making AI accessible and deploying multimodal systems at scale.
</p>
''', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('[📧 Email](mailto:akansha@example.com)')
with col2:
    st.markdown('[💼 LinkedIn](https://linkedin.com/in/aka-sa)')
with col3:
    st.markdown('[🐙 GitHub](https://github.com/aka-sa)')

st.markdown('---')

# Featured Projects
st.markdown('<h2 class="section-title">🚀 Featured Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "name": "MediLens - Medical RAG System",
        "desc": "Production RAG pipeline for medical prescription analysis with safety validation layers.",
        "tags": ["RAG", "Healthcare", "FAISS"],
    },
    {
        "name": "Autonomous Agent Framework",
        "desc": "Multi-agent system using LangGraph state machines for complex reasoning tasks.",
        "tags": ["LangGraph", "Agents", "Reasoning"],
    },
    {
        "name": "MCP Server Toolkit",
        "desc": "Model Context Protocol servers enabling LLMs to access databases and APIs securely.",
        "tags": ["MCP", "FastAPI", "Tool Use"],
    }
]

for proj in projects:
    tags_html = " ".join('<span class="skill-tag">' + tag + '</span>' for tag in proj["tags"])
    st.markdown(
        '<div class="card">'
        '<h3 style="color: var(--primary-pink); margin-top: 0;">' + proj["name"] + '</h3>'
        '<p style="color: var(--text-dark);">' + proj["desc"] + '</p>'
        '<p>' + tags_html + '</p>'
        '</div>',
        unsafe_allow_html=True
    )

st.markdown('---')

# Technical Skills
st.markdown('<h2 class="section-title">🛠️ Technical Skills</h2>', unsafe_allow_html=True)

skills = {
    "Languages": ["Python", "JavaScript", "SQL", "TypeScript"],
    "Frameworks": ["LangChain", "LangGraph", "FastAPI", "Streamlit", "React"],
    "ML/AI": ["Transformers", "Llama.cpp", "RAG", "Fine-tuning", "Prompt Engineering"],
    "Tools": ["Git", "Docker", "AWS", "HuggingFace", "Weights & Biases"]
}

for category, items in skills.items():
    items_html = " ".join('<span class="skill-tag">' + item + '</span>' for item in items)
    st.markdown('<strong>' + category + ':</strong> ' + items_html, unsafe_allow_html=True)

st.markdown('---')

# Contact
st.markdown('<h2 class="section-title">📬 Get In Touch</h2>', unsafe_allow_html=True)
st.markdown('''
<div class="card">
<p style="color: var(--text-dark); font-size: 1.1rem;">
Interested in collaborating on AI projects or discussing research? Feel free to reach out!
</p>
<p>
<strong>Email:</strong> akansha@example.com<br>
<strong>GitHub:</strong> <a href="https://github.com/aka-sa">@aka-sa</a><br>
<strong>Location:</strong> Remote / Open to opportunities
</p>
</div>
''', unsafe_allow_html=True)

st.markdown('---')
st.caption('Built with ❤️ using Streamlit | Warm Sunset Theme')
