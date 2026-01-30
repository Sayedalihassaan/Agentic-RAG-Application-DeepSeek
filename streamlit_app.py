import streamlit as st
import time
import os
from datetime import datetime

try:
    from crewai import Crew
except ImportError:
    st.error("CrewAI is not installed. Please run: pip install crewai")
    st.stop()

from tools import create_pdf_tool, web_search_tool
from agents import (
    create_router_agent,
    create_retriever_agent,
    create_grader_agent,
    create_hallucination_grader,
    create_answer_grader,
)
from tasks import (
    create_router_task,
    create_retriever_task,
    create_grader_task,
    create_hallucination_task,
    create_answer_task,
)

# Page configuration
st.set_page_config(
    page_title="Agentic RAG System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .query-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .result-box {
        background-color: #e8f4f8;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
    }
    .metrics-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    h1 {
        color: #1f77b4;
    }
    h2 {
        color: #2c3e50;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1557a0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "rag_crew" not in st.session_state:
    st.session_state.rag_crew = None
if "crew_initialized" not in st.session_state:
    st.session_state.crew_initialized = False


def initialize_crew(pdf_path):
    """Initialize the RAG crew with all agents and tasks."""
    try:
        with st.spinner("Initializing RAG system... This may take a moment."):
            # Create tools
            rag_tool = create_pdf_tool(pdf_path)

            # Create agents
            router_agent = create_router_agent()
            retriever_agent = create_retriever_agent()
            grader_agent = create_grader_agent()
            hallucination_grader = create_hallucination_grader()
            answer_grader = create_answer_grader()

            # Create tasks
            router_task = create_router_task(router_agent)
            retriever_task = create_retriever_task(
                retriever_agent, router_task, rag_tool, web_search_tool
            )
            grader_task = create_grader_task(grader_agent, retriever_task)
            hallucination_task = create_hallucination_task(
                hallucination_grader, grader_task
            )
            answer_task = create_answer_task(
                answer_grader, hallucination_task, web_search_tool
            )

            # Create crew
            rag_crew = Crew(
                agents=[
                    router_agent,
                    retriever_agent,
                    grader_agent,
                    hallucination_grader,
                    answer_grader,
                ],
                tasks=[
                    router_task,
                    retriever_task,
                    grader_task,
                    hallucination_task,
                    answer_task,
                ],
                verbose=False,
            )

            return rag_crew
    except Exception as e:
        st.error(f"Error initializing crew: {str(e)}")
        return None


def process_query(crew, query):
    """Process a user query through the RAG system."""
    start_time = time.time()

    try:
        result = crew.kickoff(inputs={"question": query})
        end_time = time.time()
        processing_time = end_time - start_time

        return {
            "answer": str(result),
            "processing_time": processing_time,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    except Exception as e:
        return {
            "answer": f"Error processing query: {str(e)}",
            "processing_time": 0,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "error": True,
        }


# Sidebar
with st.sidebar:
    st.image(
        "https://img.icons8.com/color/96/000000/artificial-intelligence.png",
        width=100,
    )
    st.title("🤖 Agentic RAG System")
    st.markdown("---")

    st.header("📚 Configuration")

    # PDF file path input
    pdf_path = st.text_input(
        "PDF Document Path",
        value="data/attention_is_all_you_need.pdf",
        help="Enter the path to your PDF document",
    )

    # Initialize button
    if st.button("🚀 Initialize System", type="primary"):
        if os.path.exists(pdf_path):
            st.session_state.rag_crew = initialize_crew(pdf_path)
            if st.session_state.rag_crew:
                st.session_state.crew_initialized = True
                st.success("✅ System initialized successfully!")
        else:
            st.error("❌ PDF file not found. Please check the path.")

    st.markdown("---")

    # System status
    st.header("📊 System Status")
    if st.session_state.crew_initialized:
        st.success("🟢 System Ready")
    else:
        st.warning("🟡 System Not Initialized")

    st.metric("Queries Processed", len(st.session_state.chat_history))

    st.markdown("---")

    # Information section
    st.header("ℹ️ About")
    st.markdown(
        """
    This is an **Agentic RAG System** that combines:
    
    - 🔍 **Vector Search** for document retrieval
    - 🌐 **Web Search** for real-time information
    - 🤖 **Multi-Agent System** for intelligent routing
    - ✅ **Quality Grading** for accurate responses
    
    **Powered by:**
    - CrewAI
    - DeepSeek R1
    - LangChain
    - Tavily Search
    """
    )

    st.markdown("---")

    # Clear history button
    if st.button("🗑️ Clear History"):
        st.session_state.chat_history = []
        st.rerun()


# Main content
st.title("🤖 Agentic RAG Question Answering System")
st.markdown(
    """
Welcome to the **Agentic RAG System**! This intelligent system uses multiple AI agents to answer your questions 
by combining document search and web search capabilities.
"""
)

# Check if system is initialized
if not st.session_state.crew_initialized:
    st.warning(
        "⚠️ Please initialize the system using the sidebar configuration before asking questions."
    )
    st.info(
        """
    **How to get started:**
    1. Verify the PDF document path in the sidebar
    2. Click the '🚀 Initialize System' button
    3. Wait for the system to initialize
    4. Start asking questions!
    """
    )
else:
    # Query input section
    st.markdown("### 💬 Ask Your Question")

    col1, col2 = st.columns([4, 1])

    with col1:
        user_query = st.text_input(
            "Enter your question:",
            placeholder="e.g., What is the Transformer architecture? or What is the weather in New York?",
            label_visibility="collapsed",
        )

    with col2:
        ask_button = st.button("🔍 Ask", type="primary", use_container_width=True)

    # Example questions
    with st.expander("📝 Example Questions"):
        st.markdown(
            """
        **Document-related questions:**
        - What is the Transformer architecture?
        - Explain the attention mechanism
        - What are the key components of the encoder?
        
        **Real-time questions:**
        - What is the weather in New York?
        - Latest news about AI?
        - Current stock price of Tesla?
        """
        )

    # Process query
    if ask_button and user_query:
        with st.spinner("🔄 Processing your query... This may take a moment."):
            result = process_query(st.session_state.rag_crew, user_query)

            # Add to chat history
            st.session_state.chat_history.append(
                {"query": user_query, "result": result}
            )

    # Display results
    if st.session_state.chat_history:
        st.markdown("---")
        st.markdown("### 📜 Conversation History")

        # Display chat history in reverse order (newest first)
        for idx, chat in enumerate(reversed(st.session_state.chat_history)):
            with st.container():
                st.markdown(f"**Question {len(st.session_state.chat_history) - idx}:**")
                st.markdown(
                    f'<div class="query-box">❓ {chat["query"]}</div>',
                    unsafe_allow_html=True,
                )

                if chat["result"].get("error"):
                    st.error(f"❌ {chat['result']['answer']}")
                else:
                    st.markdown(
                        f'<div class="result-box">💡 {chat["result"]["answer"]}</div>',
                        unsafe_allow_html=True,
                    )

                # Display metrics
                col1, col2 = st.columns(2)
                with col1:
                    st.caption(f"⏱️ Processing time: {chat['result']['processing_time']:.2f}s")
                with col2:
                    st.caption(f"🕐 Timestamp: {chat['result']['timestamp']}")

                st.markdown("---")

# Footer
st.markdown("---")
st.markdown(
    """
<div style='text-align: center; color: #7f8c8d;'>
    <p>Built with ❤️ using CrewAI, DeepSeek R1, and Streamlit</p>
    <p>© 2025 Agentic RAG System | <a href='https://github.com' target='_blank'>GitHub</a></p>
</div>
""",
    unsafe_allow_html=True,
)