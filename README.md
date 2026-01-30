# 🤖 Agentic RAG Application with DeepSeek

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CrewAI](https://img.shields.io/badge/CrewAI-Powered-orange.svg)](https://www.crewai.com/)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-R1-green.svg)](https://www.deepseek.com/)

An intelligent **Agentic Retrieval-Augmented Generation (RAG)** system that combines the power of multi-agent AI, vector search, and web search to provide accurate and context-aware answers to user queries. This system intelligently routes queries between local document knowledge bases and real-time web information.

![Agentic RAG Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-brightgreen)

## ✨ Features

- **🧠 Multi-Agent Architecture**: Utilizes 5 specialized AI agents working together
- **🔍 Intelligent Routing**: Automatically determines whether to use vector search or web search
- **📚 PDF Knowledge Base**: Processes and indexes PDF documents for semantic search
- **🌐 Real-time Web Search**: Integrates Tavily search for current information
- **✅ Quality Assurance**: Multi-stage validation including relevance grading and hallucination detection
- **🎨 Beautiful UI**: Professional Streamlit interface for easy interaction
- **⚡ High Performance**: Powered by DeepSeek R1 model via OpenRouter

## 🏗️ Architecture

The system employs a sophisticated multi-agent workflow:

```
User Query
    ↓
[Router Agent] → Determines search strategy
    ↓
[Retriever Agent] → Fetches information (PDF/Web)
    ↓
[Grader Agent] → Validates relevance
    ↓
[Hallucination Grader] → Checks factual accuracy
    ↓
[Answer Grader] → Final quality check
    ↓
Final Answer
```

### Agent Roles

1. **Router Agent**: Analyzes queries and routes to appropriate data source
2. **Retriever Agent**: Retrieves information from vector database or web
3. **Grader Agent**: Filters irrelevant retrievals
4. **Hallucination Grader**: Ensures answers are grounded in facts
5. **Answer Grader**: Final validation and web fallback if needed

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- API Keys:
  - OpenRouter API key (for DeepSeek R1)
  - Tavily API key (for web search)
  - Groq API key (for embeddings)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Agentic-RAG-Application-DeepSeek.git
   cd Agentic-RAG-Application-DeepSeek
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Copy the example environment file and add your API keys:
   ```bash
   cp _env_example .env
   ```
   
   Edit `.env` and add your API keys:
   ```env
   TAVILY_API_KEY=your_tavily_api_key_here
   OPEN_ROUTER_API_KEY=your_openrouter_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Prepare your data**
   
   Create a `data` directory and add your PDF documents:
   ```bash
   mkdir data
   # Copy your PDF files to the data directory
   ```

## 💻 Usage

### Running the Streamlit Application (Recommended)

Launch the interactive web interface:

```bash
streamlit run streamlit_app.py
```

Then:
1. Open your browser to `http://localhost:8501`
2. Configure the PDF path in the sidebar
3. Click "Initialize System"
4. Start asking questions!

### Running the Command-Line Version

For programmatic use:

```bash
python app.py
```

Edit the `user_question` variable in `app.py` to change the query.

## 📖 Example Queries

### Document-based Questions
```
- "What is the Transformer architecture?"
- "Explain the attention mechanism in detail"
- "What are the key components of the encoder?"
- "How does multi-head attention work?"
```

### Real-time Questions
```
- "What is the weather in New York?"
- "Latest developments in AI research"
- "Current stock price of Tesla"
- "Recent news about climate change"
```

## 🔧 Configuration

### Customizing the LLM

Edit `agents.py` to change the model:

```python
llm = LLM(
    model="deepseek/deepseek-r1-0528:free",  # Change model here
    temperature=0,
    api_key=OPEN_ROUTER_API_KEY
)
```

### Adjusting PDF Processing

Modify `tools.py` to configure embeddings and search:

```python
def create_pdf_tool(pdf_path):
    return PDFSearchTool(
        pdf=pdf_path,
        config=dict(
            llm=dict(
                provider="groq",
                config=dict(
                    model="deepseek-r1-distill-qwen-32b",
                    api_key=GROQ_API_KEY,
                ),
            ),
            embedder=dict(
                provider="huggingface",
                config=dict(
                    model="BAAI/bge-small-en-v1.5",
                ),
            ),
        ),
    )
```

## 📁 Project Structure

```
Agentic-RAG-Application-DeepSeek/
│
├── streamlit_app.py          # Streamlit web interface
├── app.py                     # Command-line interface
├── agents.py                  # Agent definitions
├── tasks.py                   # Task definitions
├── tools.py                   # RAG and web search tools
├── config.py                  # Configuration and API keys
├── utils.py                   # Utility functions
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (create from _env_example)
├── _env_example               # Example environment file
├── _gitignore                 # Git ignore file
├── LICENSE                    # MIT License
├── README.md                  # This file
│
└── data/                      # Directory for PDF documents
    └── attention_is_all_you_need.pdf
```

## 🛠️ Tech Stack

- **AI Framework**: [CrewAI](https://www.crewai.com/) - Multi-agent orchestration
- **LLM**: [DeepSeek R1](https://www.deepseek.com/) via OpenRouter
- **Embeddings**: [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) via HuggingFace
- **Web Search**: [Tavily API](https://tavily.com/)
- **UI Framework**: [Streamlit](https://streamlit.io/)
- **Vector DB**: ChromaDB (via CrewAI tools)
- **PDF Processing**: PDFMiner, PDFPlumber

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **DeepSeek** for their powerful R1 reasoning model
- **CrewAI** for the excellent multi-agent framework
- **Vaswani et al.** for the "Attention Is All You Need" paper (used as example document)
- **Tavily** for web search capabilities
- **Streamlit** for making beautiful UIs easy

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

## 🔮 Future Enhancements

- [ ] Support for multiple PDF documents
- [ ] Conversation memory and context management
- [ ] Export conversation history
- [ ] Advanced analytics and metrics
- [ ] Custom model fine-tuning
- [ ] API endpoint for external integrations
- [ ] Support for additional file formats (DOCX, TXT, etc.)
- [ ] Voice input/output capabilities

## ⚠️ Known Limitations

- PDF processing can be slow for very large documents
- Web search requires active internet connection
- API rate limits apply based on your subscription tier
- First query may take longer due to model initialization

## 📊 Performance Metrics

Typical performance on standard queries:
- **PDF-based queries**: 5-10 seconds
- **Web-based queries**: 3-8 seconds
- **Hybrid queries**: 8-15 seconds

*Performance may vary based on document size, query complexity, and API response times.*

---

**Built with ❤️ using AI**

If you find this project helpful, please consider giving it a ⭐!