

## **Step 1: Project Setup**

**Goal:** Prepare the environment and folder structure.

1. Run your CMD commands to create the folders and files (the script you shared).
2. Create a **virtual environment**:

```cmd
python -m venv venv
venv\Scripts\activate    :: Windows
source venv/bin/activate :: Linux/Mac
```

3. Install essential packages using `requirements.txt` (we’ll create it next).
4. Create `.env` from `.env.example` and add API keys for OpenAI, DuckDuckGo, NewsAPI, etc.

---

## **Step 2: Configuration**

**Goal:** Centralize all configurable parameters.

1. `config/settings.py` → store API keys, model parameters, search settings.
2. `config/prompts.yaml` → define prompt templates and few-shot examples.

> This allows all other modules to read from a single source.

---

## **Step 3: Core Fact-Checking Logic**

**Goal:** Build the main engine that coordinates all operations.

1. Implement `src/fact_checker.py`:

   * Accept claims
   * Generate initial response using LLM
   * Extract assumptions
   * Gather evidence
   * Synthesize final answer

> This module will call the prompt chains and search tools.

---

## **Step 4: Prompt Chaining**

**Goal:** Implement structured reasoning using LangChain.

1. Create `src/prompt_chains.py`
2. Define the chain:

   * Initial Response → Assumption Extraction → Verification → Evidence Synthesis → Final Answer
3. Load prompts from `config/prompts.yaml`.

---

## **Step 5: Evidence Retrieval / Web Search**

**Goal:** Connect to the web to validate assumptions.

1. Implement `src/search_tools.py`
2. Integrate DuckDuckGo, NewsAPI, or SerpAPI
3. Handle rate-limiting and errors gracefully
4. Return top evidence snippets or URLs

---

## **Step 6: Utilities**

**Goal:** Support all modules with helpers.

1. Implement `src/utils.py`

   * Logging
   * Text cleaning
   * Caching repeated queries
   * Formatting outputs

---

## **Step 7: User Interfaces**

**Goal:** Allow users to interact with your bot.

1. Start with **CLI** (`src/ui/cli.py`) → simplest to test
2. Then build **Streamlit** (`src/ui/streamlit_app.py`) → web interface with chat history
3. Optional: **Gradio** (`src/ui/gradio_app.py`) → quick demo interface

---

## **Step 8: Testing**

**Goal:** Ensure reliability of core features.

1. `tests/test_fact_checker.py` → test fact-checking pipeline
2. `tests/test_search_tools.py` → test web search results
3. Use `pytest` or `unittest`

---

## **Step 9: Examples & Demo**

**Goal:** Provide sample queries and notebooks for demonstration.

1. `examples/example_queries.txt` → short claims for testing
2. `examples/demo_notebook.ipynb` → show how to use the bot interactively

---

## **Step 10: Database / Knowledge Storage (Optional)**

**Goal:** Cache results or support vector search.

1. `data/knowledge_base.db` → previous claims & evidence
2. `data/embeddings/` → store vector embeddings for semantic search

---

### **✅ Recommended Development Flow**

1. **Setup project structure & virtual environment**
2. **Add configuration files & API keys**
3. **Implement core logic (`fact_checker.py`)**
4. **Implement prompt chains (`prompt_chains.py`)**
5. **Integrate web search (`search_tools.py`)**
6. **Add utility functions (`utils.py`)**
7. **Build CLI interface for initial testing**
8. **Add Streamlit / Gradio interface**
9. **Write unit tests & run examples**
10. **Optional: database caching & embeddings**

---

If you want, I can **start giving the code for Step 1–3 first**, i.e., the **core fact-checking skeleton + prompt chaining + web search integration**, so you can run a minimal working bot immediately.

Do you want me to do that next?
