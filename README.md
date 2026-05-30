# 🤖 AI Career Agent (AI-900 Project Showcase)

Welcome to the **AI Career Agent** template repository! This project is a hands-on implementation designed for students and developers to move beyond theory and build a live, industry-grade portfolio piece. 

This framework leverages **Microsoft Foundry (2026 Standards)**, **Retrieval-Augmented Generation (RAG)**, and **Streamlit** to create an interactive, autonomous chat assistant grounded entirely in your professional CV.

🚀 **Live Demo Reference:** [Check out my live profile agent here!](https://hanem-ai-agent.streamlit.app/))

---

## 🛠 Features
- **Semantic Data Grounding:** Uses your CV as a knowledge base to prevent AI hallucinations.
- **2026 Framework Alignment:** Built using the native **Microsoft Foundry** ecosystem and OpenAI deployment infrastructure.
- **Secure Secret Management:** Fully integrates with Streamlit's encrypted `secrets.toml` architecture to keep cloud keys hidden.
- **Frictionless UI:** Streamlit interface crafted for recruiters to seamlessly navigate your technical achievements.

---

## 🎁 Quickstart Guide for Students (Fork & Deploy)

Follow these exact steps to launch your own personalized Career Agent for free using your **Azure for Students** credits.

### Step 1: Fork and Star this Repository
1. Click the **⭐ Star** button in the top-right corner of this page to save it.
2. Click the **Fork** button to generate an identical copy of this project directly inside your own GitHub profile.
3. Clone your forked repository to your local computer:
   ```shell
   git clone [https://github.com/YOUR-USERNAME/ai-career-agent.git](https://github.com/YOUR-USERNAME/ai-career-agent.git)
   cd ai-career-agent
   '''
   
### Step 2: Upload Your Agent-Ready CV
1. Navigate to the `data/` directory (or the root directory) in your forked repository.
2. Replace the placeholder curriculum vitae file with your own details. 
3. Ensure you follow the modular semantic headers (`## Technical Skills`, `## Key AI Projects`) so the retrieval engine parses your context perfectly.

### Step 3: Harvest Your Microsoft Foundry Credentials
1. Log into **Microsoft Foundry** ([ai.azure.com](https://ai.azure.com)) using your university credentials.
2. Navigate to your deployed project endpoint (e.g., `gpt-4o-mini`).
3. Copy your specific connection keys:
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_KEY`
   - `AZURE_OPENAI_MODEL_DEPLOYMENT_NAME`

### Step 4: Configure Local Environment Variables (For Local Testing)
To test the app locally before publishing, create a file named .env in the root folder of your project to store your secrets securely:
    ```shell
   AZURE_OPENAI_API_KEY=your_api_key_here
   AZURE_OPENAI_ENDPOINT=[https://your-endpoint.openai.azure.com/](https://your-endpoint.openai.azure.com/)
   AZURE_OPENAI_DEPLOYMENT=your_model_name_here
   '''
⚠️ Important Security Rule: Never commit your .env file to GitHub. It is included in the .gitignore by default to protect your student credit balance.


### Step 5: Install Dependencies & Run Locally
Make sure you have Python installed (>=3.9 recommended), then run:
   '''shell
   pip install -r requirements.txt
   streamlit run app.py
   '''
Open your web browser and navigate to: 👉 http://localhost:8501 to test it!

### Step 6: Deploy Instantly to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io) and log in using your GitHub account.
2. Click **New app**, then select your forked repository: `[Your-Username]/ai-career-agent`.
3. Set your main file path to `app.py`.
4. **⚠️ CRITICAL (Security Step):** Before hitting deploy, click **Advanced Settings** and inject your Azure credentials securely into the Secrets panel:
   ```toml
   AZURE_OPENAI_ENDPOINT = "[https://your-resource-name.openai.azure.com/](https://your-resource-name.openai.azure.com/)"
   AZURE_OPENAI_KEY = "your-40-character-secret-key"
   AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "your-model-deployment-name"
   '''
5. Click Deploy! Your application will be live globally in under two minutes.

   
## How to Customize Your AI Agent
### 🎯 1. Modify the AI Behavior (Prompt)
Find where the system prompt is defined (e.g., in app.py or agent.py).

'''Python
SYSTEM_PROMPT = "You are a helpful AI career advisor."
''' 

✨ Try changing it to match your target path, such as:

- Cybersecurity mentor

- Data science coach

- Software engineering career guide

### 🎯 2. Personalize for Your Career
Update the agent to focus on your specific degree path, target career goals, and technology stack interests.

## 🛑 Cloud Housekeeping: Resource Cleanup
To ensure your Azure for Students credits don't run out silently, get into the habit of cleaning up your resources when you finish testing:

1. Head back to the Azure Portal.

2. Open the Resource Group container you created for this lab.

3. Click Delete resource group, type the group name to verify, and confirm.

