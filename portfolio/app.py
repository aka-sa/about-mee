"""
Akansha Sharma — Professional GenAI Engineer Portfolio
Production-Ready Generative AI Systems | Multimodal AI | LLMs | RAG | Accessibility
"""
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ═══════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════
st.set_page_config(
    page_title="Akansha Sharma | GenAI Engineer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════
if "theme" not in st.session_state:
    st.session_state.theme = "dark"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ═══════════════════════════════════════
# PROFESSIONAL CSS (Slate/Indigo Theme)
# ═══════════════════════════════════════
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Fira+Code:wght@400;500;600&display=swap');

        :root {
            --bg-primary: #FFF7CD;
            --bg-secondary: #FDC3A1;
            --bg-card: #FFFBF0;
            --bg-card-hover: #FFF5E6;
            --accent-primary: #F57799;
            --accent-secondary: #FB9B8F;
            --accent-success: #10B981;
            --accent-warning: #F59E0B;
            --text-primary: #2D1B1B;
            --text-secondary: #4A2C2C;
            --text-muted: #6B4A4A;
            --border: #FB9B8F;
            --gradient-hero: linear-gradient(135deg, #FFF7CD 0%, #FDC3A1 50%, #FB9B8F 100%);
            --gradient-card: linear-gradient(180deg, rgba(251, 155, 143, 0.08) 0%, transparent 100%);
        }

        * { font-family: 'Inter', sans-serif !important; box-sizing: border-box; }
        code { font-family: 'Fira Code', monospace !important; }

        // Hide Streamlit chrome — handled above
        // Added: subtle shadow to metric cards
        .metric-card {
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        }
        .metric-card:hover {
            box-shadow: 0 8px 24px rgba(245, 119, 153, 0.15);
        }
        /* Hide Streamlit chrome */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        .stDeployButton { visibility: hidden; }
        header { visibility: hidden; }
        .block-container { max-width: 1280px !important; padding-top: 2rem !important; }
        .st-emotion-cache-18ni7ak { display: none; }
        .st-emotion-cache-u4bgbl { display: none; }
        /* Make input fields clean white */
        input, textarea {
            background: var(--bg-card) !important;
            border: 1px solid var(--border) !important;
            color: var(--text-primary) !important;
            border-radius: 8px !important;
        }
        /* Label color */
        label, .st-emotion-cache-162p3mx {
            color: var(--text-muted) !important;
        }
        /* Select / button overrides */
        button[kind="primary"] {
            background: var(--gradient-hero) !important;
            border: none !important;
        }
        
        /* ── Accessibility Features ── */
        /* Focus indicators for keyboard navigation */
        *:focus-visible {
            outline: 3px solid var(--accent-primary) !important;
            outline-offset: 2px !important;
        }
        /* Skip to main content link */
        .skip-link {
            position: absolute;
            top: -40px;
            left: 0;
            background: var(--accent-primary);
            color: white;
            padding: 8px 16px;
            text-decoration: none;
            border-radius: 0 0 8px 0;
            z-index: 10000;
            transition: top 0.2s;
        }
        .skip-link:focus {
            top: 0;
        }
        /* High contrast mode support */
        @media (prefers-contrast: high) {
            :root {
                --text-primary: #000000;
                --text-secondary: #1a1a1a;
                --border: #000000;
            }
        }
        /* Reduced motion support */
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }
        /* Screen reader only text */
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }

        /* ── Sticky Navigation ── */
        .nav-bar {
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(255, 247, 205, 0.95);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
            padding: 0.8rem 0;
            margin: -2rem -2rem 2rem -2rem;
        }
        .nav-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 2rem;
        }
        .nav-logo {
            font-size: 1.3rem;
            font-weight: 800;
            background: var(--gradient-hero);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .nav-links {
            display: flex;
            gap: 1.5rem;
            align-items: center;
        }
        .nav-link {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            transition: color 0.2s;
        }
        .nav-link:hover { color: var(--accent-primary); }
        .nav-btn {
            background: var(--accent-primary);
            color: white;
            padding: 0.5rem 1.2rem;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
        }
        .nav-btn:hover {
            background: var(--accent-secondary);
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(245, 119, 153, 0.3);
            color: white;
        }

        /* ── Hero Section ── */
        .hero {
            background: linear-gradient(180deg, rgba(245, 119, 153, 0.08) 0%, transparent 100%);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 3rem 2.5rem;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }
        .hero::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(251, 155, 143, 0.15) 0%, transparent 70%);
            animation: pulse 8s ease-in-out infinite;
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); opacity: 0.3; }
            50% { transform: scale(1.1); opacity: 0.5; }
        }
        .hero-title {
            font-size: 3rem;
            font-weight: 900;
            color: var(--text-primary);
            line-height: 1.2;
            margin-bottom: 0.5rem;
        }
        .hero-subtitle {
            font-size: 1.4rem;
            color: var(--accent-primary);
            font-weight: 600;
            margin-bottom: 1rem;
        }
        .hero-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }
        .hero-tag {
            background: rgba(245, 119, 153, 0.1);
            color: var(--accent-primary);
            padding: 0.3rem 0.8rem;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 500;
            border: 1px solid rgba(245, 119, 153, 0.2);
        }
        .hero-cta {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.5rem;
            border-radius: 10px;
            font-size: 0.9rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
        }
        .btn-primary {
            background: var(--gradient-hero);
            color: white;
            border: none;
        }
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(245, 119, 153, 0.4);
            color: white;
        }
        .btn-secondary {
            background: transparent;
            color: var(--text-primary);
            border: 1px solid var(--border);
        }
        .btn-secondary:hover {
            background: var(--bg-card-hover);
            border-color: var(--accent-primary);
            color: var(--text-primary);
        }

        /* ── Terminal Animation ── */
        .terminal {
            background: #111827;
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.5rem;
            font-family: 'Fira Code', monospace;
            font-size: 0.85rem;
            margin-bottom: 2rem;
            overflow-x: auto;
        }
        .terminal-line {
            color: var(--text-secondary);
            margin-bottom: 0.3rem;
        }
        .terminal-cmd { color: var(--accent-success); }
        .terminal-ok { color: var(--accent-success); }
        .terminal-pending { color: var(--accent-warning); }
        .cursor {
            display: inline-block;
            width: 8px;
            height: 16px;
            background: var(--accent-primary);
            animation: blink 1s step-end infinite;
            vertical-align: middle;
        }
        @keyframes blink { 50% { opacity: 0; } }

        /* ── Section Headers ── */
        .section-header {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin: 2.5rem 0 1.5rem 0;
            padding-bottom: 0.8rem;
            border-bottom: 1px solid var(--border);
        }
        .section-icon { font-size: 1.8rem; }
        .section-title {
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--text-primary);
        }

        /* ── Cards ── */
        .card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.5rem;
            transition: all 0.3s;
        }
        .card:hover {
            background: var(--bg-card-hover);
            border-color: rgba(245, 119, 153, 0.3);
            transform: translateY(-2px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }

        /* ── Metrics Grid ── */
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            margin: 1.5rem 0;
        }
        .metric-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
            transition: all 0.3s;
        }
        .metric-card:hover {
            border-color: var(--accent-primary);
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(245, 119, 153, 0.2);
        }
        .metric-value {
            font-size: 2rem;
            font-weight: 800;
            background: var(--gradient-hero);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .metric-label {
            color: var(--text-muted);
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 0.3rem;
        }

        /* ── Model Stack Bars ── */
        .model-stack {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.5rem;
        }
        .model-item {
            margin-bottom: 0.8rem;
        }
        .model-name {
            display: flex;
            justify-content: space-between;
            color: var(--text-secondary);
            font-size: 0.85rem;
            font-weight: 500;
            margin-bottom: 0.3rem;
        }
        .model-bar-bg {
            background: rgba(148, 163, 184, 0.1);
            border-radius: 4px;
            height: 8px;
            overflow: hidden;
        }
        .model-bar-fill {
            height: 100%;
            background: var(--gradient-hero);
            border-radius: 4px;
            transition: width 1s ease-out;
        }

        /* ── Project Cards ── */
        .project-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.5rem;
            height: 100%;
            transition: all 0.3s;
            display: flex;
            flex-direction: column;
        }
        .project-card:hover {
            border-color: var(--accent-primary);
            transform: translateY(-4px);
            box-shadow: 0 12px 40px rgba(245, 119, 153, 0.15);
        }
        .project-icon {
            font-size: 2rem;
            margin-bottom: 0.8rem;
        }
        .project-title {
            color: var(--text-primary);
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }
        .project-desc {
            color: var(--text-secondary);
            font-size: 0.9rem;
            line-height: 1.6;
            margin-bottom: 0.8rem;
            flex-grow: 1;
        }
        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-bottom: 1rem;
        }
        .tech-badge {
            background: rgba(245, 119, 153, 0.1);
            color: var(--accent-primary);
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 600;
        }
        .project-links {
            display: flex;
            gap: 0.5rem;
        }
        .project-link {
            flex: 1;
            text-align: center;
            padding: 0.5rem;
            background: rgba(148, 163, 184, 0.1);
            border-radius: 8px;
            color: var(--text-secondary);
            font-size: 0.8rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
        }
        .project-link:hover {
            background: var(--accent-primary);
            color: white;
        }

        /* ── Architecture Diagram ── */
        .arch-diagram {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 0 1px 4px rgba(0,0,0,0.04);
        }
        .arch-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 0.5rem;
        }
        .arch-node {
            background: rgba(251, 155, 143, 0.06);
            border: 1px solid rgba(251, 155, 143, 0.25);
            border-radius: 8px;
            padding: 0.6rem 1rem;
            color: var(--accent-primary);
            font-size: 0.85rem;
            font-weight: 600;
            min-width: 100px;
            text-align: center;
        }
        .arch-arrow {
            color: var(--text-muted);
            font-size: 1.2rem;
        }

        /* ── Chat Interface ── */
        .chat-container {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 1px 4px rgba(0,0,0,0.06);
        }
        .chat-message {
            margin-bottom: 1rem;
            padding: 0.8rem 1rem;
            border-radius: 12px;
            max-width: 80%;
        }
        .chat-user {
            background: rgba(251, 155, 143, 0.1);
            margin-left: auto;
            border: 1px solid rgba(251, 155, 143, 0.15);
        }
        .chat-bot {
            background: var(--bg-secondary);
            border: 1px solid var(--border);
        }
        .chat-label {
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.3rem;
        }
        .chat-user .chat-label { color: var(--accent-primary); }
        .chat-bot .chat-label { color: var(--accent-success); }
        .chat-text { color: var(--text-secondary); font-size: 0.9rem; line-height: 1.5; }

        /* ── Timeline ── */
        .timeline {
            position: relative;
            padding-left: 2rem;
        }
        .timeline::before {
            content: '';
            position: absolute;
            left: 6px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: var(--border);
        }
        .timeline-item {
            position: relative;
            margin-bottom: 1.5rem;
            padding-left: 1.5rem;
        }
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -1.8rem;
            top: 6px;
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background: var(--accent-primary);
            border: 3px solid var(--bg-primary);
        }
        .timeline-year {
            color: var(--accent-primary);
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }
        .timeline-title {
            color: var(--text-primary);
            font-size: 1rem;
            font-weight: 700;
        }
        .timeline-org {
            color: var(--text-secondary);
            font-size: 0.9rem;
        }


        /* ── Blog Cards ── */
        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        .blog-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 1.5rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .blog-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 40px rgba(245, 119, 153, 0.15);
        }
        .blog-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.8rem;
        }
        .blog-category {
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
        }
        .cat-agents { background: rgba(245,119,153,0.15); color: #F57799; }
        .cat-mcp { background: rgba(251,155,143,0.15); color: #FB9B8F; }
        .cat-rag { background: rgba(253,195,161,0.3); color: #c47a40; }
        .cat-finetune { background: rgba(245,119,153,0.12); color: #d4507a; }
        .cat-accessibility { background: rgba(255,247,205,0.5); color: #a08000; }
        .cat-multimodal { background: rgba(251,155,143,0.2); color: #d46a50; }
        .blog-date {
            font-size: 0.75rem;
            color: var(--text-secondary);
        }
        .blog-title {
            color: var(--text-primary);
            font-size: 1rem;
            font-weight: 700;
            margin-bottom: 0.6rem;
            line-height: 1.3;
        }
        .blog-excerpt {
            color: var(--text-secondary);
            font-size: 0.85rem;
            line-height: 1.5;
            margin-bottom: 0.8rem;
        }
        .blog-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-bottom: 0.8rem;
        }
        .blog-tag {
            font-size: 0.7rem;
            background: var(--bg-secondary);
            color: var(--text-secondary);
            padding: 0.15rem 0.5rem;
            border-radius: 4px;
        }
        .blog-read-more {
            color: var(--accent-primary);
            font-size: 0.85rem;
            font-weight: 600;
            text-decoration: none;
        }
        .blog-read-more:hover {
            text-decoration: underline;
        }

        /* ── Tech Radar ── */
        .radar-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 0.8rem;
        }
        .radar-item {
            background: rgba(251, 155, 143, 0.05);
            border: 1px solid rgba(251, 155, 143, 0.12);
            border-radius: 10px;
            padding: 0.8rem;
            text-align: center;
            transition: all 0.2s;
        }
        .radar-item:hover {
            background: rgba(251, 155, 143, 0.1);
            border-color: var(--accent-primary);
            transform: scale(1.05);
        }
        .radar-check { color: var(--accent-success); margin-right: 0.3rem; }
        .radar-text { color: var(--text-secondary); font-size: 0.85rem; font-weight: 500; }

        /* ── Blog Section ── */
        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 1.5rem;
            margin: 1rem 0;
        }
        .blog-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 1.5rem;
            transition: all 0.3s;
            height: 100%;
            display: flex;
            flex-direction: column;
        }
        .blog-card:hover {
            border-color: var(--accent-primary);
            transform: translateY(-4px);
            box-shadow: 0 12px 40px rgba(245, 119, 153, 0.15);
        }
        .blog-card-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.8rem;
        }
        .blog-category {
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
        }
        .cat-agents { background: rgba(245, 119, 153, 0.15); color: #F57799; }
        .cat-mcp { background: rgba(253, 195, 161, 0.3); color: #D97A3E; }
        .cat-rag { background: rgba(251, 155, 143, 0.15); color: #FB9B8F; }
        .cat-finetune { background: rgba(255, 247, 205, 0.6); color: #8B6914; }
        .cat-accessibility { background: rgba(16, 185, 129, 0.12); color: #059669; }
        .cat-multimodal { background: rgba(245, 119, 153, 0.12); color: #DB5584; }
        .blog-date {
            color: var(--text-muted);
            font-size: 0.75rem;
        }
        .blog-title {
            color: var(--text-primary);
            font-size: 1.05rem;
            font-weight: 700;
            line-height: 1.35;
            margin-bottom: 0.6rem;
        }
        .blog-excerpt {
            color: var(--text-secondary);
            font-size: 0.85rem;
            line-height: 1.6;
            flex-grow: 1;
            margin-bottom: 1rem;
        }
        .blog-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.3rem;
        }
        .blog-tag {
            font-size: 0.7rem;
            padding: 0.15rem 0.5rem;
            border-radius: 4px;
            background: rgba(251, 155, 143, 0.08);
            color: var(--text-muted);
            font-weight: 500;
        }
        .blog-read-more {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            color: var(--accent-primary);
            font-size: 0.8rem;
            font-weight: 600;
            text-decoration: none;
            margin-top: 1rem;
            transition: all 0.2s;
        }
        .blog-read-more:hover {
            gap: 0.5rem;
            color: var(--accent-secondary);
        }

        /* ── Live Demo Lab ── */
        .demo-lab {
            background: linear-gradient(135deg, rgba(245, 119, 153, 0.08) 0%, rgba(253, 195, 161, 0.08) 100%);
            border: 2px solid var(--accent-primary);
            border-radius: 20px;
            padding: 2.5rem;
            margin: 2rem 0;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .demo-lab::before {
            content: '⭐';
            position: absolute;
            top: 12px;
            right: 16px;
            font-size: 1.2rem;
        }
        .demo-lab-title {
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--text-primary);
            margin-bottom: 0.5rem;
        }
        .demo-lab-desc {
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin-bottom: 1.5rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        .demo-tabs {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }
        .demo-tab {
            padding: 0.5rem 1.2rem;
            border-radius: 10px;
            font-size: 0.85rem;
            font-weight: 600;
            border: 1px solid var(--border);
            background: var(--bg-card);
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.2s;
        }
        .demo-tab:hover, .demo-tab.active {
            background: var(--accent-primary);
            color: white;
            border-color: var(--accent-primary);
        }
        .demo-output {
            background: #111827;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: left;
            font-family: 'Fira Code', monospace;
            font-size: 0.85rem;
            min-height: 180px;
        }
        .demo-code-line { color: #9CA3AF; margin-bottom: 0.2rem; }
        .demo-code-keyword { color: #C084FC; }
        .demo-code-string { color: #34D399; }
        .demo-code-comment { color: #6B7280; font-style: italic; }
        .demo-code-func { color: #60A5FA; }

        /* ── Footer ── */
        .footer {
            text-align: center;
            color: var(--text-muted);
            font-size: 0.85rem;
            padding: 2rem 0;
            border-top: 1px solid var(--border);
            margin-top: 3rem;
            background: var(--bg-secondary);
            border-radius: 16px 16px 0 0;
            margin-left: -2rem;
            margin-right: -2rem;
        }
        .footer-tech {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
            margin-top: 0.5rem;
        }
        .footer-tech span {
            background: var(--bg-card);
            border: 1px solid var(--border);
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            font-size: 0.75rem;
            color: var(--text-muted);
        }

        /* Responsive */
        @media (max-width: 768px) {
            .nav-links { display: none; }
            .hero-title { font-size: 2rem; }
            .metrics-grid { grid-template-columns: repeat(2, 1fr); }
            .hero-cta { flex-direction: column; }
            .btn { width: 100%; justify-content: center; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# NAVIGATION BAR
# ═══════════════════════════════════════
st.markdown(
    """
    <div class="nav-bar">
        <div class="nav-content">
            <div class="nav-logo">🧠 Akansha Sharma</div>
            <div class="nav-links">
                <a href="#hero" class="nav-link">Hero</a>
                <a href="#demo-lab" class="nav-link">Demo Lab</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#blog" class="nav-link">Blog</a>
                <a href="#research" class="nav-link">Research</a>
                <a href="#publications" class="nav-link">Publications</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>
            <a href="https://github.com/aka-sa" target="_blank" class="nav-btn">⚡ GitHub</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# HERO SECTION
# ═══════════════════════════════════════
st.markdown(
    """
    <div class="hero" id="hero">
        <div class="hero-title">Building Production-Ready<br>Generative AI Systems</div>
        <div class="hero-subtitle">GenAI Engineer | LLM Specialist | Research Engineer</div>
        <div class="hero-tags">
            <span class="hero-tag">Multimodal AI</span>
            <span class="hero-tag">LLMs</span>
            <span class="hero-tag">AI Agents</span>
            <span class="hero-tag">RAG</span>
            <span class="hero-tag">Vision-Language</span>
            <span class="hero-tag">Accessibility</span>
        </div>
        <p style="color:var(--text-secondary); line-height:1.7; max-width:650px; margin-bottom:1.5rem;">
            I specialize in building end-to-end AI systems that bridge research and production.
            From fine-tuning vision-language models to deploying scalable RAG pipelines and
            accessibility tools — I turn complex AI concepts into real-world solutions.
        </p>
        <div class="hero-cta">
            <a href="#projects" class="btn btn-primary">🚀 View Projects</a>
            <a href="mailto:akansha.sharma2k@gmail.com" class="btn btn-secondary">📧 Contact Me</a>
            <a href="https://linkedin.com/in/aka-sa" target="_blank" class="btn btn-secondary">💼 LinkedIn</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# TERMINAL ANIMATION
# ═══════════════════════════════════════
st.markdown(
    """
    <div class="terminal">
        <div class="terminal-line"><span class="terminal-cmd">$ python launch.py</span></div>
        <div class="terminal-line"><span class="terminal-ok">✓</span> Loading Qwen2-VL...</div>
        <div class="terminal-line"><span class="terminal-ok">✓</span> Initializing LangChain agents...</div>
        <div class="terminal-line"><span class="terminal-ok">✓</span> Starting FastAPI server...</div>
        <div class="terminal-line"><span class="terminal-ok">✓</span> Connecting Pinecone vector DB...</div>
        <div class="terminal-line"><span class="terminal-ok">✓</span> Loading OCR pipeline...</div>
        <div class="terminal-line"><span class="terminal-ok">✓</span> Agent ready.</div>
        <div class="terminal-line"><span class="cursor"></span></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# METRICS
# ═══════════════════════════════════════
st.markdown(
    """
    <div class="metrics-grid">
        <div class="metric-card">
            <div class="metric-value">4+</div>
            <div class="metric-label">Projects Built</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">2</div>
            <div class="metric-label">Publications</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">6mo</div>
            <div class="metric-label">Research Experience</div>
        </div>
        <div class="metric-card">
            <div class="metric-value">15+</div>
            <div class="metric-label">Technologies</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# MODEL STACK
# ═══════════════════════════════════════
st.markdown('<div class="section-header"><span class="section-icon">🤖</span><span class="section-title">Model Expertise</span></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="model-stack">
        <div class="model-item">
            <div class="model-name"><span>Qwen2-VL / Qwen-VL</span><span>Expert</span></div>
            <div class="model-bar-bg"><div class="model-bar-fill" style="width:95%"></div></div>
        </div>
        <div class="model-item">
            <div class="model-name"><span>Llama 3 / Llama 2</span><span>Advanced</span></div>
            <div class="model-bar-bg"><div class="model-bar-fill" style="width:80%"></div></div>
        </div>
        <div class="model-item">
            <div class="model-name"><span>Gemma / Phi</span><span>Proficient</span></div>
            <div class="model-bar-bg"><div class="model-bar-fill" style="width:70%"></div></div>
        </div>
        <div class="model-item">
            <div class="model-name"><span>Mistral / Mixtral</span><span>Proficient</span></div>
            <div class="model-bar-bg"><div class="model-bar-fill" style="width:65%"></div></div>
        </div>
        <div class="model-item">
            <div class="model-name"><span>PaddleOCR</span><span>Expert</span></div>
            <div class="model-bar-bg"><div class="model-bar-fill" style="width:90%"></div></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# LIVE AI DEMO LAB
# ═══════════════════════════════════════
demo_tabs_content = {
    "OCR Pipeline": [
        '<span class="demo-code-comment"># Upload document image → OCR extraction</span>',
        '<span class="demo-code-keyword">import</span> paddleocr',
        '',
        '<span class="demo-code-keyword">from</span> paddleocr <span class="demo-code-keyword">import</span> PaddleOCR',
        'ocr = PaddleOCR(use_angle_cls=<span class="demo-code-string">True</span>, lang=<span class="demo-code-string">en</span>)',
        '',
        '<span class="demo-code-comment"># Process image through OCR engine</span>',
        '<span class="demo-code-keyword">def</span> <span class="demo-code-func">extract_text</span>(image_path):',
        '    result = ocr.ocr(image_path)',
        '    text_blocks = []',
        '<span class="demo-code-keyword">for</span> line <span class="demo-code-keyword">in</span> result[<span class="demo-code-string">0</span>]:',
        '    text_blocks.append({',
        '        <span class="demo-code-string">"text"</span>: line[<span class="demo-code-string">1</span>][<span class="demo-code-string">0</span>],',
        '        <span class="demo-code-string">"confidence"</span>: <span class="demo-code-func">round</span>(line[<span class="demo-code-string">1</span>][<span class="demo-code-string">1</span>], <span class="demo-code-string">4</span>),',
        '        <span class="demo-code-string">"bbox"</span>: line[<span class="demo-code-string">0</span>]',
        '    })',
        '    <span class="demo-code-keyword">return</span> pd.DataFrame(text_blocks)',
        '',
        '<span class="demo-code-func">df</span> = extract_text(<span class="demo-code-string">"prescription.png"</span>)',
        '<span class="demo-code-func">print</span>(f<span class="demo-code-string">"Extracted {len(df)} text blocks"</span>)',
    ],
    "RAG Pipeline": [
        '<span class="demo-code-comment"># Retrieve augmented context for LLM responses</span>',
        '<span class="demo-code-keyword">from</span> langchain.chains <span class="demo-code-keyword">import</span> RetrievalQA',
        '<span class="demo-code-keyword">from</span> langchain.text_splitter <span class="demo-code-keyword">import</span> RecursiveCharacterTextSplitter',
        '',
        '<span class="demo-code-comment"># Load and chunk knowledge base</span>',
        'loader = DocumentLoader(<span class="demo-code-string">"medical_docs/"</span>)',
        'documents = loader.load()',
        'splitter = RecursiveCharacterTextSplitter(',
        '    chunk_size=<span class="demo-code-string">500</span>, chunk_overlap=<span class="demo-code-string">50</span>',
        ')',
        'chunks = splitter.split_documents(documents)',
        '',
        '<span class="demo-code-comment"># Embed & store in vector database</span>',
        'vectorstore = FAISS.from_documents(chunks, embeddings)',
        'retriever = vectorstore.as_retriever(',
        '    search_type=<span class="demo-code-string">"similarity"</span>, k=<span class="demo-code-string">3</span>',
        ')',
        '',
        '<span class="demo-code-comment"># Query with augmented context</span>',
        'qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)',
        'response = qa_chain.run(<span class="demo-code-string">"Drug interactions for Metformin?"</span>)',
    ],
    "AI Agents": [
        '<span class="demo-code-comment"># Autonomous reasoning agent with tools</span>',
        '<span class="demo-code-keyword">from</span> langgraph <span class="demo-code-keyword">import</span> StateGraph',
        '<span class="demo-code-keyword">from</span> langchain_core.tools <span class="demo-code-keyword">import</span> tool',
        '',
        '<span class="demo-code-comment"># Define agent tools</span>',
        '@tool',
        '<span class="demo-code-keyword">def</span> <span class="demo-code-func">search_medical_db</span>(query: str) -> str:',
        '    <span class="demo-code-string">"""Search medical knowledge graph for drug data."""</span>',
        '    return knowledge_graph.query(query)',
        '',
        '@tool',
        '<span class="demo-code-keyword">def</span> <span class="demo-code-func">validate_prescription</span>(rx_data: dict) -> bool:',
        '    <span class="demo-code-string">"""Validate prescription safety rules."""</span>',
        '    <span class="demo-code-keyword">return</span> safety_engine.check(rx_data)',
        '',
        '<span class="demo-code-comment"># Build agentic workflow</span>',
        'workflow = StateGraph(AgentState)',
        'workflow.add_node(<span class="demo-code-string">"reason"</span>, reason_step)',
        'workflow.add_node(<span class="demo-code-string">"act"</span>, tool_execution)',
        'workflow.add_conditional_edges(<span class="demo-code-string">"reason"</span>, should_act)',
        'workflow.set_entry_point(<span class="demo-code-string">"reason"</span>)',
        'agent = workflow.compile()',
    ],
    "Fine-Tuning": [
        '<span class="demo-code-comment"># Efficient fine-tuning with Unsloth + LoRA</span>',
        '<span class="demo-code-keyword">from</span> unsloth <span class="demo-code-keyword">import</span> FastLanguageModel',
        '<span class="demo-code-keyword">from</span> trl <span class="demo-code-keyword">import</span> SFTTrainer',
        '',
        '<span class="demo-code-comment"># Load base model for fine-tuning</span>',
        'model, tokenizer = FastLanguageModel.from_pretrained(',
        '    model_name=<span class="demo-code-string">"unsloth/Qwen2.5-7B-Instruct"</span>,',
        '    max_seq_length=<span class="demo-code-string">2048</span>,',
        '    load_in_4bit=<span class="demo-code-string">True</span>',
        ')',
        '',
        '<span class="demo-code-comment"># Apply LoRA adapters</span>',
        'model = get_peft_model(model, PeftConfig(',
        '    r=<span class="demo-code-string">16</span>, lora_alpha=<span class="demo-code-string">32</span>,',
        '    target_modules=[<span class="demo-code-string">"q_proj"</span>, <span class="demo-code-string">"v_proj"</span>],',
        '    lora_dropout=<span class="demo-code-string">0.05</span>',
        '))',
        '',
        '<span class="demo-code-comment"># Train on custom dataset</span>',
        'trainer = SFTTrainer(',
        '    model=model, tokenizer=tokenizer,',
        '    train_dataset=finetune_ds,',
        '    args=SFTConfig(per_device_train_batch_size=<span class="demo-code-string">2</span>),',
        ')',
        'trainer.train()',
    ],
}

st.markdown(
    """
    <div class="demo-lab" id="demo-lab">
        <div class="demo-lab-title">Live AI Demo Lab</div>
        <p class="demo-lab-desc">
            Explore the core systems I've built. Select a pipeline below to see the architecture in action.
        </p>
        <div class="demo-tabs">
            <button class="demo-tab active" onclick="this.parentElement.querySelectorAll('.demo-tab').forEach(t=>t.classList.remove('active'));this.classList.add('active');document.getElementById('code-panel').innerHTML=demoData['OCR Pipeline'];">OCR Pipeline</button>
            <button class="demo-tab" onclick="this.parentElement.querySelectorAll('.demo-tab').forEach(t=>t.classList.remove('active'));this.classList.add('active');document.getElementById('code-panel').innerHTML=demoData['RAG Pipeline'];">RAG Pipeline</button>
            <button class="demo-tab" onclick="this.parentElement.querySelectorAll('.demo-tab').forEach(t=>t.classList.remove('active'));this.classList.add('active');document.getElementById('code-panel').innerHTML=demoData['AI Agents'];">AI Agents</button>
            <button class="demo-tab" onclick="this.parentElement.querySelectorAll('.demo-tab').forEach(t=>t.classList.remove('active'));this.classList.add('active');document.getElementById('code-panel').innerHTML=demoData['Fine-Tuning'];">Fine-Tuning</button>
        </div>
        <div class="demo-output" id="code-panel"></div>
    </div>
    <script>
        const demoData = {
            "OCR Pipeline": `&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Upload document image → OCR extraction&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;import&lt;/span&gt; paddleocr&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;from&lt;/span&gt; paddleocr &lt;span class="demo-code-keyword"&gt;import&lt;/span&gt; PaddleOCR&lt;/span&gt;
&lt;span class="demo-code-line"&gt;ocr = PaddleOCR(use_angle_cls=&lt;span class="demo-code-string"&gt;True&lt;/span&gt;, lang=&lt;span class="demo-code-string"&gt;"en"&lt;/span&gt;)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Process image through OCR engine&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;def&lt;/span&gt; &lt;span class="demo-code-func"&gt;extract_text&lt;/span&gt;(image_path):&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    result = ocr.ocr(image_path)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    text_blocks = []&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;for&lt;/span&gt; line &lt;span class="demo-code-keyword"&gt;in&lt;/span&gt; result[&lt;span class="demo-code-string"&gt;0&lt;/span&gt;]:&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    text_blocks.append({&lt;/span&gt;
&lt;span class="demo-code-line"&gt;        &lt;span class="demo-code-string"&gt;"text"&lt;/span&gt;: line[&lt;span class="demo-code-string"&gt;1&lt;/span&gt;][&lt;span class="demo-code-string"&gt;0&lt;/span&gt;],&lt;/span&gt;
&lt;span class="demo-code-line"&gt;        &lt;span class="demo-code-string"&gt;"confidence"&lt;/span&gt;: &lt;span class="demo-code-func"&gt;round&lt;/span&gt;(line[&lt;span class="demo-code-string"&gt;1&lt;/span&gt;][&lt;span class="demo-code-string"&gt;1&lt;/span&gt;], &lt;span class="demo-code-string"&gt;4&lt;/span&gt;),&lt;/span&gt;
&lt;span class="demo-code-line"&gt;        &lt;span class="demo-code-string"&gt;"bbox"&lt;/span&gt;: line[&lt;span class="demo-code-string"&gt;0&lt;/span&gt;]&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    })&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    &lt;span class="demo-code-keyword"&gt;return&lt;/span&gt; pd.DataFrame(text_blocks)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-func"&gt;df&lt;/span&gt; = extract_text(&lt;span class="demo-code-string"&gt;"prescription.png"&lt;/span&gt;)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-func"&gt;print&lt;/span&gt;(f&lt;span class="demo-code-string"&gt;"Extracted {len(df)} text blocks"&lt;/span&gt;)&lt;/span&gt;`,
            "RAG Pipeline": `&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Retrieve augmented context for LLM responses&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;from&lt;/span&gt; langchain.chains &lt;span class="demo-code-keyword"&gt;import&lt;/span&gt; RetrievalQA&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;from&lt;/span&gt; langchain.text_splitter &lt;span class="demo-code-keyword"&gt;import&lt;/span&gt; RecursiveCharacterTextSplitter&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Load and chunk knowledge base&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;loader = DocumentLoader(&lt;span class="demo-code-string"&gt;"medical_docs/"&lt;/span&gt;)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;documents = loader.load()&lt;/span&gt;
&lt;span class="demo-code-line"&gt;splitter = RecursiveCharacterTextSplitter(&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    chunk_size=&lt;span class="demo-code-string"&gt;500&lt;/span&gt;, chunk_overlap=&lt;span class="demo-code-string"&gt;50&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;chunks = splitter.split_documents(documents)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Embed &amp;amp; store in vector database&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;vectorstore = FAISS.from_documents(chunks, embeddings)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;retriever = vectorstore.as_retriever(&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    search_type=&lt;span class="demo-code-string"&gt;"similarity"&lt;/span&gt;, k=&lt;span class="demo-code-string"&gt;3&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Query with augmented context&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;response = qa_chain.run(&lt;span class="demo-code-string"&gt;"Drug interactions for Metformin?"&lt;/span&gt;)&lt;/span&gt;`,
            "AI Agents": `&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Autonomous reasoning agent with tools&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;from&lt;/span&gt; langgraph &lt;span class="demo-code-keyword"&gt;import&lt;/span&gt; StateGraph&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;from&lt;/span&gt; langchain_core.tools &lt;span class="demo-code-keyword"&gt;import&lt;/span&gt; tool&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Define agent tools&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;@tool&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;def&lt;/span&gt; &lt;span class="demo-code-func"&gt;search_medical_db&lt;/span&gt;(query: str) -&amp;gt; str:&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    &lt;span class="demo-code-string"&gt;&amp;quot;&amp;quot;&amp;quot;Search medical knowledge graph for drug data.&amp;quot;&amp;quot;&amp;quot;&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    &lt;span class="demo-code-keyword"&gt;return&lt;/span&gt; knowledge_graph.query(query)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;@tool&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;def&lt;/span&gt; &lt;span class="demo-code-func"&gt;validate_prescription&lt;/span&gt;(rx_data: dict) -&amp;gt; bool:&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    &lt;span class="demo-code-string"&gt;&amp;quot;&amp;quot;&amp;quot;Validate prescription safety rules.&amp;quot;&amp;quot;&amp;quot;&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    &lt;span class="demo-code-keyword"&gt;return&lt;/span&gt; safety_engine.check(rx_data)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Build agentic workflow&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;workflow = StateGraph(AgentState)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;workflow.add_node(&lt;span class="demo-code-string"&gt;"reason"&lt;/span&gt;, reason_step)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;workflow.add_node(&lt;span class="demo-code-string"&gt;"act"&lt;/span&gt;, tool_execution)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;workflow.add_conditional_edges(&lt;span class="demo-code-string"&gt;"reason"&lt;/span&gt;, should_act)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;workflow.set_entry_point(&lt;span class="demo-code-string"&gt;"reason"&lt;/span&gt;)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;agent = workflow.compile()&lt;/span&gt;`,
            "Fine-Tuning": `&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Efficient fine-tuning with Unsloth + LoRA&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;from&lt;/span&gt; unsloth &lt;span class="demo-code-keyword"&gt;import&lt;/span&gt; FastLanguageModel&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-keyword"&gt;from&lt;/span&gt; trl &lt;span class="demo-code-keyword"&gt;import&lt;/span&gt; SFTTrainer&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Load base model for fine-tuning&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;model, tokenizer = FastLanguageModel.from_pretrained(&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    model_name=&lt;span class="demo-code-string"&gt;"unsloth/Qwen2.5-7B-Instruct"&lt;/span&gt;,&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    max_seq_length=&lt;span class="demo-code-string"&gt;2048&lt;/span&gt;,&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    load_in_4bit=&lt;span class="demo-code-string"&gt;True&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Apply LoRA adapters&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;model = get_peft_model(model, PeftConfig(&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    r=&lt;span class="demo-code-string"&gt;16&lt;/span&gt;, lora_alpha=&lt;span class="demo-code-string"&gt;32&lt;/span&gt;,&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    target_modules=[&lt;span class="demo-code-string"&gt;"q_proj"&lt;/span&gt;, &lt;span class="demo-code-string"&gt;"v_proj"&lt;/span&gt;],&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    lora_dropout=&lt;span class="demo-code-string"&gt;0.05&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;))&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;&lt;span class="demo-code-comment"&gt;# Train on custom dataset&lt;/span&gt;&lt;/span&gt;
&lt;span class="demo-code-line"&gt;trainer = SFTTrainer(&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    model=model, tokenizer=tokenizer,&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    train_dataset=finetune_ds,&lt;/span&gt;
&lt;span class="demo-code-line"&gt;    args=SFTConfig(per_device_train_batch_size=&lt;span class="demo-code-string"&gt;2&lt;/span&gt;),&lt;/span&gt;
&lt;span class="demo-code-line"&gt;)&lt;/span&gt;
&lt;span class="demo-code-line"&gt;trainer.train()&lt;/span&gt;`
        };
        // Initialize with OCR Pipeline
        document.getElementById('code-panel').innerHTML = demoData["OCR Pipeline"];
    </script>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# PROJECTS
# ═══════════════════════════════════════
st.markdown('<div class="section-header" id="projects"><span class="section-icon">🚀</span><span class="section-title">Featured Projects</span></div>', unsafe_allow_html=True)

projects = [
    {
        "icon": "🏥",
        "title": "MediLens",
        "desc": "Multimodal healthcare reasoning system for handwritten prescription understanding and drug interaction analysis using Qwen2-VL.",
        "tech": ["Computer Vision", "Qwen2-VL", "NLP", "Healthcare AI"],
        "github": "https://github.com/aka-sa",
        "demo": "#",
    },
    {
        "icon": "📄",
        "title": "FormGen-AI",
        "desc": "Document intelligence system with multimodal RAG for structured information extraction from PDFs and images.",
        "tech": ["FastAPI", "Qwen-VL", "OCR", "RAG"],
        "github": "https://github.com/aka-sa",
        "demo": "#",
    },
    {
        "icon": "🎙️",
        "title": "Meeting Analyzer",
        "desc": "Real-time audio intelligence with speaker diarization, topic segmentation, and structured summarization.",
        "tech": ["Speech-to-Text", "NLP", "Diarization"],
        "github": "https://github.com/aka-sa",
        "demo": "#",
    },
    {
        "icon": "📐",
        "title": "LaTeX Reasoning Engine",
        "desc": "Fine-tuned transformer models for symbolic mathematical reasoning across 200+ constructs using Unsloth.",
        "tech": ["Transformers", "Unsloth", "LaTeX", "Reasoning"],
        "github": "https://github.com/aka-sa",
        "demo": "#",
    },
]

cols = st.columns(2)
for i, p in enumerate(projects):
    with cols[i % 2]:
        tech_html = "".join(f'<span class="tech-badge">{t}</span>' for t in p["tech"])
        st.markdown(
            f"""
            <div class="project-card">
                <div class="project-icon">{p['icon']}</div>
                <div class="project-title">{p['title']}</div>
                <div class="project-desc">{p['desc']}</div>
                <div class="project-tech">{tech_html}</div>
                <div class="project-links">
                    <a href="{p['github']}" target="_blank" class="project-link">GitHub</a>
                    <a href="{p['demo']}" class="project-link">Demo</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ═══════════════════════════════════════
# ARCHITECTURE DIAGRAM
# ═══════════════════════════════════════
st.markdown('<div class="section-header"><span class="section-icon">🏗️</span><span class="section-title">System Architecture</span></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="arch-diagram">
        <div style="text-align:center; color:var(--text-muted); font-size:0.85rem; margin-bottom:1rem;">
            Multimodal AI Pipeline for Document Intelligence
        </div>
        <div class="arch-row">
            <div class="arch-node">Input Image/PDF</div>
        </div>
        <div class="arch-row">
            <div class="arch-arrow">↓</div>
        </div>
        <div class="arch-row">
            <div class="arch-node">PaddleOCR</div>
            <div class="arch-node">Layout Detection</div>
        </div>
        <div class="arch-row">
            <div class="arch-arrow">↓</div>
        </div>
        <div class="arch-row">
            <div class="arch-node">Qwen-VL</div>
            <div class="arch-node">Vision Encoder</div>
        </div>
        <div class="arch-row">
            <div class="arch-arrow">↓</div>
        </div>
        <div class="arch-row">
            <div class="arch-node">LLM Reasoning</div>
        </div>
        <div class="arch-row">
            <div class="arch-arrow">↓</div>
        </div>
        <div class="arch-row">
            <div class="arch-node">RAG Retrieval</div>
            <div class="arch-node">Context Augmentation</div>
        </div>
        <div class="arch-row">
            <div class="arch-arrow">↓</div>
        </div>
        <div class="arch-row">
            <div class="arch-node">Structured Output</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# TECH RADAR
# ═══════════════════════════════════════
st.markdown('<div class="section-header"><span class="section-icon">📡</span><span class="section-title">Current Focus</span></div>', unsafe_allow_html=True)

radar_items = [
    "AI Agents", "MCP", "RAG", "Multimodal AI",
    "OCR", "Accessibility", "RLHF", "Evaluation",
    "Fine-tuning", "Vector DBs", "Edge Deployment", "Safety"
]

st.markdown(
    f"""
    <div class="radar-grid">
        {"".join(f'<div class="radar-item"><span class="radar-check">✓</span><span class="radar-text">{item}</span></div>' for item in radar_items)}
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# ===================================================
# RESEARCH BLOG
# ===================================================
st.markdown(
    '<div class="section-header" id="blog">'
    '<span class="section-icon">&#x1f4dd;</span>'
    '<span class="section-title">Research Blog</span>'
    '</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="color:var(--text-secondary);margin-bottom:1.5rem;">'
    'Deep dives into AI agents, MCP, RAG, fine-tuning, accessibility, and multimodal AI.</p>',
    unsafe_allow_html=True,
)

blog_articles = [
    {
        "title": "Building Autonomous AI Agents with LangGraph",
        "excerpt": "How I designed a multi-agent system using LangGraph state machines for medical prescription analysis -- reasoning loops, tool use, and safety validation layers.",
        "category": "Agents",
        "cat_class": "cat-agents",
        "date": "Jun 2026",
        "tags": ["LangGraph", "Multi-Agent", "Healthcare"],
    },
    {
        "title": "Designing MCP Servers for AI Tool Integration",
        "excerpt": "Implementing Model Context Protocol servers that enable LLMs to securely access databases, APIs, and local files -- bridging the gap between models and production tools.",
        "category": "MCP",
        "cat_class": "cat-mcp",
        "date": "May 2026",
        "tags": ["MCP", "FastAPI", "Tool Use"],
    },
    {
        "title": "Production RAG Pipelines: From Theory to Deployment",
        "excerpt": "Building retrieval-augmented generation systems with FAISS, chunking strategies, hybrid search, and evaluation metrics -- real MediLens examples included.",
        "category": "RAG",
        "cat_class": "cat-rag",
        "date": "Apr 2026",
        "tags": ["RAG", "FAISS", "Evaluation"],
    },
    {
        "title": "Efficient Fine-Tuning with Unsloth + LoRA",
        "excerpt": "Cut fine-tuning costs by 90% while maintaining model quality. 4-bit quantization, FlashAttention-2, and custom LoRA configs for domain-specific adaptation.",
        "category": "Fine-Tuning",
        "cat_class": "cat-finetune",
        "date": "Mar 2026",
        "tags": ["Unsloth", "LoRA", "4-bit"],
    },
    {
        "title": "AI Accessibility: Building Tools for Visually Impaired Users",
        "excerpt": "NIT Durgapur research on multimodal OCR pipelines, screen reader integration, and Chrome extensions that transformed document accessibility.",
        "category": "Accessibility",
        "cat_class": "cat-accessibility",
        "date": "Feb 2026",
        "tags": ["A11y", "OCR", "Chrome Extension"],
    },
    {
        "title": "Multimodal AI: Bridging Vision and Language Models",
        "excerpt": "Exploring vision-language architectures (Qwen2-VL, LLaVA, CLIP) for medical image understanding, scene description, and diagram parsing.",
        "category": "Multimodal",
        "cat_class": "cat-multimodal",
        "date": "Jan 2026",
        "tags": ["Vision-Language", "Qwen2-VL", "CLIP"],
    },
    {
        "title": "Document Intelligence at Scale with FormGen-AI",
        "excerpt": "Production-grade document extraction pipeline combining PaddleOCR layout detection, Qwen-VL reasoning, and intelligent validation rules.",
        "category": "Engineering",
        "cat_class": "cat-rag",
        "date": "Dec 2025",
        "tags": ["FastAPI", "Docker", "CI/CD"],
    },
    {
        "title": "Evaluating LLM Reasoning: Metrics That Actually Matter",
        "excerpt": "Beyond accuracy -- measuring factual consistency, hallucination rates, and reasoning traces. A rigorous evaluation framework across 5 benchmark tasks.",
        "category": "Research",
        "cat_class": "cat-finetune",
        "date": "Nov 2025",
        "tags": ["Evaluation", "Benchmarking", "Prompt Eng."],
    },
    {
        "title": "Speech-to-Text Pipeline for Meeting Analytics",
        "excerpt": "Real-time audio intelligence with speaker diarization, topic segmentation, and structured summarization for multi-speaker conversations.",
        "category": "Engineering",
        "cat_class": "cat-agents",
        "date": "Oct 2025",
        "tags": ["Speech AI", "NLP", "Audio Processing"],
    },
    {
        "title": "Hybrid Agent Architecture for Healthcare Risk Detection",
        "excerpt": "Published in NCCCI 2.0: An agent-based framework combining rule-based safety checks with LLM reasoning for prescription risk flagging.",
        "category": "Research",
        "cat_class": "cat-accessibility",
        "date": "Sep 2025",
        "tags": ["Agents", "Healthcare", "Safety"],
    },
]

# Build blog cards HTML
blog_cards_parts = []
for a in blog_articles:
    tags_html = "".join(
        "<span class='blog-tag'>" + t + "</span>" for t in a["tags"]
    )
    card = (
        "<div class='blog-card' role='article' aria-label='" + a["title"] + "'>"
        "<div class='blog-card-header'>"
        "<span class='blog-category " + a["cat_class"] + "'>" + a["category"] + "</span>"
        "<span class='blog-date'>" + a["date"] + "</span>"
        "</div>"
        "<h3 class='blog-title'>" + a["title"] + "</h3>"
        "<p class='blog-excerpt'>" + a["excerpt"] + "</p>"
        "<div class='blog-tags'>" + tags_html + "</div>"
        "<a href='#' class='blog-read-more' role='link' "
        "aria-label='Read more about " + a["title"] + "'>"
        "Read More &#8594;</a>"
        "</div>"
    )
    blog_cards_parts.append(card)

st.markdown(
    "<div class='blog-grid'>" + "".join(blog_cards_parts) + "</div>",
    unsafe_allow_html=True,
)

# ===================================================
# RESEARCH TIMELINE
# ===================================================
# ═══════════════════════════════════════
st.markdown('<div class="section-header" id="research"><span class="section-icon">📅</span><span class="section-title">Research Journey</span></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="timeline">
        <div class="timeline-item">
            <div class="timeline-year">Feb 2024 – Jul 2024</div>
            <div class="timeline-title">AI & STEM Accessibility Research Intern</div>
            <div class="timeline-org">National Institute of Technology, Durgapur</div>
            <p style="color:var(--text-secondary); font-size:0.9rem; margin-top:0.5rem;">
                Built multimodal AI pipeline for visually impaired users using LangChain, Hugging Face, and PaddleOCR.
                Developed Flask-based Chrome extension improving accessibility efficiency by 40%.
            </p>
        </div>
        <div class="timeline-item">
            <div class="timeline-year">2024</div>
            <div class="timeline-title">Publication: PLMSAWK</div>
            <div class="timeline-org">Research Paper on Knowledge-Augmented LLMs</div>
            <p style="color:var(--text-secondary); font-size:0.9rem; margin-top:0.5rem;">
                Published methods to improve factual reasoning and knowledge integration in Large Language Models.
            </p>
        </div>
        <div class="timeline-item">
            <div class="timeline-year">2026</div>
            <div class="timeline-title">Publication: Hybrid Agent Architecture</div>
            <div class="timeline-org">NCCCI 2.0 Conference</div>
            <p style="color:var(--text-secondary); font-size:0.9rem; margin-top:0.5rem;">
                Proposed agent-based framework for intelligent prescription analysis and healthcare risk detection.
            </p>
        </div>
        <div class="timeline-item">
            <div class="timeline-year">Present</div>
            <div class="timeline-title">Independent Research & Development</div>
            <div class="timeline-org">Building MediLens, FormGen-AI, Meeting Analyzer</div>
            <p style="color:var(--text-secondary); font-size:0.9rem; margin-top:0.5rem;">
                Continuing work on multimodal AI systems, fine-tuning, and production deployment.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# SKILLS
# ═══════════════════════════════════════
st.markdown('<div class="section-header" id="skills"><span class="section-icon">🛠️</span><span class="section-title">Technical Skills</span></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <div style="color:var(--accent-primary); font-size:0.8rem; font-weight:700; text-transform:uppercase; margin-bottom:0.8rem;">AI / ML</div>
            <div style="display:flex; flex-wrap:wrap; gap:0.4rem;">
                <span class="tech-badge">Python</span>
                <span class="tech-badge">PyTorch</span>
                <span class="tech-badge">TensorFlow</span>
                <span class="tech-badge">Hugging Face</span>
                <span class="tech-badge">Transformers</span>
                <span class="tech-badge">LangChain</span>
                <span class="tech-badge">Unsloth</span>
                <span class="tech-badge">RAG</span>
                <span class="tech-badge">FAISS</span>
                <span class="tech-badge">Pinecone</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <div style="color:var(--accent-primary); font-size:0.8rem; font-weight:700; text-transform:uppercase; margin-bottom:0.8rem;">Development</div>
            <div style="display:flex; flex-wrap:wrap; gap:0.4rem;">
                <span class="tech-badge">FastAPI</span>
                <span class="tech-badge">Flask</span>
                <span class="tech-badge">Streamlit</span>
                <span class="tech-badge">Docker</span>
                <span class="tech-badge">Git</span>
                <span class="tech-badge">Linux</span>
                <span class="tech-badge">AWS</span>
                <span class="tech-badge">Nginx</span>
                <span class="tech-badge">CI/CD</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <div style="color:var(--accent-primary); font-size:0.8rem; font-weight:700; text-transform:uppercase; margin-bottom:0.8rem;">Research</div>
            <div style="display:flex; flex-wrap:wrap; gap:0.4rem;">
                <span class="tech-badge">AI Accessibility</span>
                <span class="tech-badge">Model Evaluation</span>
                <span class="tech-badge">Dataset Curation</span>
                <span class="tech-badge">Experimental Design</span>
                <span class="tech-badge">Prompt Engineering</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ===================================================
# PUBLICATIONS
# ===================================================
st.markdown(
    '<div class="section-header" id="publications">'
    '<span class="section-icon">&#x1f4c4;</span>'
    '<span class="section-title">Publications</span>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="card" style="margin-bottom:1rem;">
        <div style="display:flex;justify-content:space-between;align-items:start;gap:1rem;flex-wrap:wrap;">
            <div style="flex:1;min-width:200px;">
                <div style="color:var(--accent-primary);font-size:0.75rem;font-weight:700;margin-bottom:0.4rem;">
                    NCCCI 2.0 | 2026
                </div>
                <div style="color:var(--text-primary);font-weight:700;font-size:1rem;margin-bottom:0.4rem;">
                    Hybrid Agent Architecture for Intelligent Prescription Analysis and Drug Interaction Risk Flagging
                </div>
                <div style="color:var(--text-secondary);font-size:0.85rem;line-height:1.6;">
                    Proposed a novel agent-based framework combining rule-based clinical knowledge graphs with Qwen2-VL
                    reasoning for automated drug interaction detection. Achieved high precision in identifying adverse interactions.
                </div>
            </div>
            <div style="display:flex;gap:0.4rem;flex-shrink:0;">
                <a href="#" class="project-link" style="width:auto;padding:0.4rem 0.8rem;">PDF</a>
                <a href="#" class="project-link" style="width:auto;padding:0.4rem 0.8rem;">Citation</a>
            </div>
        </div>
    </div>
    <div class="card">
        <div style="display:flex;justify-content:space-between;align-items:start;gap:1rem;flex-wrap:wrap;">
            <div style="flex:1;min-width:200px;">
                <div style="color:var(--accent-primary);font-size:0.75rem;font-weight:700;margin-bottom:0.4rem;">
                    Research Publication
                </div>
                <div style="color:var(--text-primary);font-weight:700;font-size:1rem;margin-bottom:0.4rem;">
                    PLMSAWK: Knowledge-Augmented Pre-Trained Language Models for Improved Factual Reasoning
                </div>
                <div style="color:var(--text-secondary);font-size:0.85rem;line-height:1.6;">
                    Introduced methods to enhance factual reasoning and knowledge integration in large language models
                    through external knowledge graph augmentation and retrieval mechanisms.
                </div>
            </div>
            <div style="display:flex;gap:0.4rem;flex-shrink:0;">
                <a href="#" class="project-link" style="width:auto;padding:0.4rem 0.8rem;">PDF</a>
                <a href="#" class="project-link" style="width:auto;padding:0.4rem 0.8rem;">DOI</a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# AI CHAT AGENT
# ═══════════════════════════════════════
st.markdown('<div class="section-header"><span class="section-icon">🤖</span><span class="section-title">Ask My AI Assistant</span></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="chat-container">
        <p style="color:var(--text-muted); font-size:0.85rem; margin-bottom:1rem;">
            Ask about my projects, skills, research, or experience. Try: "What is MediLens?" or "Tell me about your publications"
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

user_query = st.text_input("", placeholder="e.g., What projects have you built?", label_visibility="collapsed")

if user_query:
    query = user_query.lower()

    responses = {
        "skill": "**My core skills:** Generative AI, LLMs, multimodal systems (Qwen2-VL), RAG pipelines, OCR (PaddleOCR), and accessibility tools. I work with PyTorch, LangChain, FastAPI, and Docker for production deployment.",
        "project": "**My main projects:** MediLens (healthcare prescription AI), FormGen-AI (document intelligence), Meeting Analyzer (audio intelligence with diarization), and LaTeX Reasoning Engine (symbolic math reasoning).",
        "medi": "**MediLens** uses Qwen2-VL to understand handwritten medical prescriptions, extract dosage information, and flag potential drug interactions. Built with a multimodal reasoning pipeline and evaluated on 500+ real samples.",
        "formgen": "**FormGen-AI** extracts structured data from PDFs and images using RAG + OCR + Qwen-VL. Features an intelligent validation layer for field mapping and error correction. Reduced deployment time by 60% via CI/CD.",
        "meeting": "**Meeting Analyzer** processes multi-speaker audio in real-time with speaker diarization, topic segmentation, and structured summarization. Uses speech-to-text models and evaluation loops for consistency.",
        "latex": "**LaTeX Reasoning Engine** fine-tunes transformers on structured LaTeX datasets for symbolic mathematical reasoning. Supports 200+ mathematical constructs using Unsloth for efficient training.",
        "publication": "**Two publications:** (1) PLMSAWK — knowledge-augmented pre-trained language models for improved factual reasoning. (2) Hybrid Agent Architecture for prescription risk flagging at NCCCI 2.0 (2026).",
        "paper": "**Two publications:** (1) PLMSAWK — knowledge-augmented pre-trained language models. (2) Hybrid Agent Architecture for prescription risk flagging at NCCCI 2.0.",
        "education": "**B.Tech in Information Technology** at Asansol Engineering College (Expected May 2026). Previously Higher Secondary (Science) from Narayana Junior College.",
        "experience": "**AI & STEM Accessibility Research Intern** at NIT Durgapur (Feb–Jul 2024). Built multimodal AI for visually impaired users, developed a Flask Chrome extension (+40% efficiency), and mentored 3 junior members.",
        "intern": "Interned at **NIT Durgapur** building accessibility tools with LangChain, Hugging Face, and PaddleOCR. Created a Chrome extension that improved efficiency by 40%.",
        "contact": "**Email:** akansha.sharma2k@gmail.com | **LinkedIn:** linkedin.com/in/aka-sa | **GitHub:** github.com/aka-sa | **Hugging Face:** huggingface.co/aka-sa",
        "email": "akansha.sharma2k@gmail.com",
        "name": "I'm **Akansha Sharma**, a GenAI Engineer specializing in multimodal AI systems, LLMs, and accessibility tools. Currently pursuing B.Tech at Asansol Engineering College.",
        "hello": "Hi! 👋 I'm Akansha's portfolio assistant. Ask me about her **projects** (MediLens, FormGen-AI), **skills** (LLMs, RAG, OCR), **publications**, or **experience** at NIT Durgapur.",
        "hi": "Hi! 👋 I'm Akansha's portfolio assistant. Ask about **projects**, **skills**, **publications**, or **research**.",
    }

    answer = None
    for key in responses:
        if key in query:
            answer = responses[key]
            break

    if not answer:
        answer = "I can tell you about Akansha's **projects** (MediLens, FormGen-AI, Meeting Analyzer), **skills** (LLMs, RAG, OCR, multimodal AI), **publications**, **education**, or **research experience**. Try asking something specific!"

    st.markdown(
        f"""
        <div class="chat-container">
            <div class="chat-message chat-user">
                <div class="chat-label">You</div>
                <div class="chat-text">{user_query}</div>
            </div>
            <div class="chat-message chat-bot">
                <div class="chat-label">AI Assistant</div>
                <div class="chat-text">{answer}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ═══════════════════════════════════════
# CONTACT
# ═══════════════════════════════════════
st.markdown('<div class="section-header" id="contact"><span class="section-icon">📬</span><span class="section-title">Get In Touch</span></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="card" style="text-align:center; padding:2.5rem;">
        <div style="font-size:3rem; margin-bottom:1rem;">🤝</div>
        <div style="color:var(--text-primary); font-size:1.3rem; font-weight:700; margin-bottom:0.5rem;">Let's Build Something Amazing</div>
        <p style="color:var(--text-secondary); max-width:500px; margin:0 auto 1.5rem auto;">
            I'm always open to discussing new projects, research collaborations, or creative AI ideas.
        </p>
        <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap;">
            <a href="mailto:akansha.sharma2k@gmail.com" class="btn btn-primary">📧 Send Email</a>
            <a href="https://github.com/aka-sa" target="_blank" class="btn btn-secondary">⚡ GitHub</a>
            <a href="https://linkedin.com/in/aka-sa" target="_blank" class="btn btn-secondary">💼 LinkedIn</a>
            <a href="https://huggingface.co/aka-sa" target="_blank" class="btn btn-secondary">🤗 Hugging Face</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════
st.markdown(
    f"""
    <div class="footer">
        <div>Built by <strong style="color:var(--accent-primary)">Akansha Sharma</strong> · GenAI Engineer · {datetime.now().year}</div>
        <div class="footer-tech">
            <span>Python</span>
            <span>FastAPI</span>
            <span>Streamlit</span>
            <span>Qwen2-VL</span>
            <span>LangChain</span>
            <span>Docker</span>
            <span>AWS</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
