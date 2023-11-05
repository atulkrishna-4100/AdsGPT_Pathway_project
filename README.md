# AdsGPT: Getting quick insights into digital marketing ads

## About AdsGPT
AI app to find real-time that gives quick insights into latest changes in digital marketingss' ads who are spending a lot of money (and thus taking more data-led decisions) "
"It uses Pathway’s [LLM App features](https://github.com/pathwaycom/llm-app) to build real-time LLM(Large Language Model)-enabled data pipeline in Python and join data from multiple input sources.

## End User
The primary end users of AdsGPT are Digital Marketer, Marketing Leaders and Companies interested in gaining insights into the advertisements published by their competitors.

---

## Business Value
Maximizing Revenues

---

## Utilization of the LLM App
Ad copies have unstructured data / patterns, and advertisers need easy recommendations in natural language without a huge learning curve.

---

## Code sample
The code establishes a connection with the database and generates a JSONL file whenever there are updates in the database. The variable "last_known_row_count" monitors these updates to ensure real-time generation of the JSON file.

---

## How to run the project

Example only supports Unix-like systems (such as Linux, macOS, BSD). If you are a Windows user, we highly recommend leveraging Windows Subsystem for Linux (WSL) or Dockerize the app to run as a container.

---

### Prerequisites

1. Make sure that [Python](https://www.python.org/downloads/) 3.10 or above installed on your machine.
2. Download and Install [Pip](https://pip.pypa.io/en/stable/installation/) to manage project packages.
3. Create an [OpenAI](https://openai.com/) account and generate a new API Key: To access the OpenAI API, you will need to create an API Key. You can do this by logging into the [OpenAI website](https://openai.com/product) and navigating to the API Key management page.

Then, follow the easy steps to install and get started using the sample app.

---

### Step 1: Clone the repository

This is done with the `git clone` command followed by the URL of the repository:

```bash
git clone https://github.com/atulkrishna-4100/AdsGPT_Pathway_project.git
```

Next,  navigate to the project folder:

```bash
cd Ads_Pathway_project
```

### Step 2: Set environment variables

Create `.env` file in the root directory of the project, copy and paste the below config, and replace the `{OPENAI_API_KEY}` configuration value with your key. 

```bash
OPENAI_API_TOKEN={OPENAI_API_KEY}
HOST=0.0.0.0
PORT=8080
EMBEDDER_LOCATOR=text-embedding-ada-002
EMBEDDING_DIMENSION=1536
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=200
TEMPERATURE=0.0
```

### Step 3: Install the app dependencies

Install the required packages:

```bash
pip install --upgrade -r requirements.txt
```
### Step 4 (Optional): Create a new virtual environment

Create a new virtual environment in the same folder and activate that environment:

```bash
python -m venv pw-env && source pw-env/bin/activate
```

### Step 5: Run and start to use it

```bash
python main.py
```
### Step 6: Run Streamlit UI for file upload

You can run the UI separately by navigating to `cd advertisements/ui` and running Streamlit app
`streamlit run app.py` command. It connects to the Discounts backend API automatically and you will see the UI frontend is running http://localhost:8501/ on a browser:
