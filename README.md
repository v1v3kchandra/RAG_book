# RAG_book
Adding a PDF to persistent data and running PDF-specific queries on a Local LLM (open-source models).

## Installation

### 1. Clone the Repository

git clone https://github.com/v1v3kchandra/RAG_book.git
cd RAG_book

### 2. Create a Virtual Environment and Install Dependencies
python -m venv venv
source venv/bin/activate  

### 3. Install the Required Packages
pip install -r requirements.txt

## Usage

### 1. Prepare the dataset
Place your PDFs in the data/ directory. The script will automatically read and index them.

### 2. 2: Run the Main Script (llamaIndex.py)
python llamaIndex.py

### 3: Example Query and reponse will be from the data uploaded
response = query_engine.query("What is Italian seasoning?")

response will be based on the 

## Customization

### 1. Change the Embedding Model
Right now using the free embedding models from Hugging Face

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

### 2. Change the LLM
Modify this line 
llm = Ollama(model="llama3.2")

# ENJOY THE FREE LLM EXPERIENCE :)

