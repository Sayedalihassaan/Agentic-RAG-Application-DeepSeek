# 🚀 Quick Start Guide

This guide will help you get the Agentic RAG System up and running in just a few minutes.

## Prerequisites

- Python 3.8 or higher installed
- Three API keys (see below)

## Step 1: Get Your API Keys

### 1. Tavily API Key (Web Search)
1. Go to [https://tavily.com/](https://tavily.com/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Copy your API key

### 2. OpenRouter API Key (DeepSeek R1)
1. Go to [https://openrouter.ai/](https://openrouter.ai/)
2. Sign up for an account
3. Go to Keys section
4. Create a new key and copy it

### 3. Groq API Key (Embeddings)
1. Go to [https://console.groq.com/](https://console.groq.com/)
2. Sign up for a free account
3. Navigate to API Keys
4. Create and copy your key

## Step 2: Install the Application

```bash
# Clone the repository
git clone https://github.com/yourusername/Agentic-RAG-Application-DeepSeek.git
cd Agentic-RAG-Application-DeepSeek

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 3: Configure API Keys

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys
# On Windows:
notepad .env
# On macOS/Linux:
nano .env
```

Your `.env` file should look like:
```
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxxx
OPEN_ROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxx
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxx
```

## Step 4: Prepare Your Data

```bash
# Create data directory
mkdir data

# Add your PDF files to the data directory
# The example uses attention_is_all_you_need.pdf
```

## Step 5: Run the Application

### Option A: Streamlit Web Interface (Recommended)

```bash
streamlit run streamlit_app.py
```

Then open your browser to `http://localhost:8501`

### Option B: Command Line

```bash
python app.py
```

## Step 6: Use the System

### In the Streamlit Interface:

1. **Configure PDF Path**: In the sidebar, verify or change the PDF document path
2. **Initialize System**: Click the "🚀 Initialize System" button
3. **Wait**: The system will initialize (may take 30-60 seconds)
4. **Ask Questions**: Type your question and click "🔍 Ask"

### Example Questions:

**About the PDF document:**
- "What is the Transformer architecture?"
- "Explain the attention mechanism"
- "What are the main contributions of this paper?"

**Real-time information:**
- "What's the weather in New York?"
- "Latest news about AI?"
- "Current stock price of Tesla?"

## Troubleshooting

### Common Issues:

1. **"Module not found" errors**
   ```bash
   pip install -r requirements.txt --upgrade
   ```

2. **API Key errors**
   - Verify all three API keys are in `.env`
   - Ensure no extra spaces or quotes
   - Check that keys are valid

3. **PDF not found**
   - Verify the file exists in the `data/` directory
   - Check the path in the Streamlit sidebar
   - Ensure correct file name

4. **Slow initialization**
   - First run downloads models (normal)
   - Subsequent runs should be faster
   - Large PDFs take longer to process

## Performance Tips

1. **First Query**: May take 15-30 seconds (model loading)
2. **Subsequent Queries**: Usually 5-10 seconds
3. **Large PDFs**: Consider splitting into smaller documents
4. **Rate Limits**: Free API tiers have limits; upgrade if needed

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore the code in `agents.py`, `tasks.py`, and `tools.py`
- Customize the system for your specific use case
- Try different PDF documents

## Getting Help

- Check the [README.md](README.md) for detailed documentation
- Review code comments in the source files
- Open an issue on GitHub for bugs or questions

## Success!

You should now have a fully functional Agentic RAG system! 🎉

Try asking it questions and explore its capabilities!