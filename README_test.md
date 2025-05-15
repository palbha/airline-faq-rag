# Airline FAQ RAG Project


Welcome to the **Airline FAQ RAG Project**! This repository houses an innovative pet project exploring the creation of airline-related FAQ data using an AI agent and building a Retrieval-Augmented Generation (RAG) application to provide accurate and context-aware responses. Whether you're an AI enthusiast, a developer, or someone curious about natural language processing (NLP) and information retrieval, this project offers insights into data generation, embedding strategies, and RAG system optimization.

## 🎯 Project Overview

This project has two primary components:

1. **FAQ Data Generation Agent**: An AI-driven agent that generates high-quality, airline-related FAQ data based on predefined topics, exploring the impact of prompt engineering on output quality.
2. **RAG Application**: A Retrieval-Augmented Generation system that leverages the generated FAQ data to answer queries, with experiments on different chunking strategies to optimize retrieval performance.

The goal is to build a foundation for an end-to-end conversational AI agent for airline customer support, starting with a robust RAG system.

## 🚀 Features

- **Dynamic FAQ Generation**: Automatically creates comprehensive airline FAQs covering topics like booking, baggage, cancellations, and in-flight services.
- **RAG Implementation**: Combines retrieval and generation to provide accurate, context-aware answers to user queries.
- **Chunking Experiments**: Evaluates multiple chunking strategies (e.g., full FAQ file vs. question-answer pair chunking) to optimize embedding and retrieval performance.
- **Prompt Engineering Insights**: Explores how different prompts affect the quality and relevance of generated FAQ data.
- **Scalable Design**: Lays the groundwork for extending the system into a fully autonomous airline support agent.

## 📂 Repository Structure

- `data_generation/`: Scripts for generating airline FAQ data using an AI agent.
- `rag_application/`: Implementation of the RAG system, including embedding creation and retrieval logic.
- `data/`: Sample FAQ datasets and embeddings.
- `experiments/`: Notebooks and scripts comparing chunking strategies and their performance.
- `docs/`: Additional documentation and analysis of findings.

## 🛠️ Getting Started

### Prerequisites
- Python 3.8+
- Libraries: `transformers`, `faiss`, `numpy`, `pandas`, `langchain` (or your preferred RAG framework)
- Optional: GPU for faster embedding generation

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/airline-faq-rag.git
   cd airline-faq-rag
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate FAQ data:
   ```bash
   python data_generation/generate_faq.py --topics "booking,baggage,cancellations"
   ```
4. Run the RAG application:
   ```bash
   python rag_application/run_rag.py
   ```

## 💡 Key Components

### 1. FAQ Data Generation
The FAQ generation agent creates airline-related question-answer pairs based on user-specified topics (e.g., booking, baggage, cancellations). Key features:
- **Prompt Engineering**: Experimented with various prompts to control tone, detail, and accuracy. For example:
  - Prompt 1: "Generate 10 FAQs about airline baggage policies in a formal tone."
  - Prompt 2: "Create concise FAQs for airline cancellations with customer-friendly language."
- **Learnings**:
  - Specific prompts with clear instructions (e.g., "include examples") yield more relevant and detailed FAQs.
  - Iterative prompt refinement improves output consistency and reduces hallucination.
  - Adding context (e.g., airline-specific policies) enhances realism but requires careful prompt design to avoid bias.

### 2. RAG Application
The RAG system retrieves relevant FAQ answers for user queries using embeddings and generates responses. Key experiments:
- **Embedding Strategies**:
  - **Full FAQ File Embedding**: Treated the entire FAQ dataset as a single document, creating one embedding per file.
  - **Question-Answer Pair Chunking**: Split FAQs into individual question-answer pairs, creating embeddings for each pair.
  - **Custom Chunking**: Grouped related FAQs (e.g., all baggage-related questions) into chunks to balance context and granularity.
- **Performance Evaluation**:
  - **Full FAQ Embedding**: Fast but less precise, as it struggles with fine-grained retrieval for specific questions.
  - **Question-Answer Pair Chunking**: Best performance for precise queries (e.g., "What is the baggage allowance?"), with higher relevance scores in retrieval.
  - **Custom Chunking**: Improved context for complex queries but increased retrieval latency.
- **Findings**: Question-answer pair chunking outperformed other methods in precision and recall, making it the preferred approach for this use case.

## 🔍 Key Learnings
- **Prompt Sensitivity**: Small changes in prompt wording significantly affect FAQ quality. For example, specifying "customer-friendly" vs. "formal" tones altered the output's readability and tone.
- **Chunking Matters**: Fine-grained chunking (question-answer pairs) improves retrieval accuracy but requires careful indexing to manage scale.
- **Embedding Trade-offs**: Dense embeddings (e.g., using BERT-based models) offer better semantic understanding but are computationally expensive compared to sparse methods.
- **Scalability Challenges**: Large FAQ datasets require efficient indexing (e.g., FAISS) to maintain low-latency retrieval.

## 🚀 Next Steps
To evolve this project into an end-to-end airline support agent:
1. **Context-Aware Generation**: Integrate user context (e.g., booking details) into the RAG pipeline for personalized responses.
2. **Multi-Turn Conversations**: Enhance the agent to handle follow-up questions and maintain conversation history.
3. **Real-Time Data Integration**: Incorporate live airline data (e.g., flight status APIs) to provide dynamic answers.
4. **Model Fine-Tuning**: Fine-tune the language model on airline-specific data to improve response accuracy and domain knowledge.
5. **Evaluation Metrics**: Implement automated evaluation (e.g., BLEU, ROUGE, or human-in-the-loop feedback) to quantify response quality.
6. **Deployment**: Package the RAG system as a web or mobile app for real-world testing.


## 📜 License
This project is licensed under the MIT License. See `LICENSE` for details.

## 📬 Contact
For questions or feedback, reach out via GitHub Issues or email at [palbhanazwale@gmail.com].

---

✈️ *Let's build the future of airline customer support together!*
