
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
> ### 💳 Important Note on Azure Credit Consumption
> **This system uses a Serverless Consumption Model.** Streamlit Cloud hosting is completely free, and the Azure backend only consumes your student credits **when the agent is actively being used to process a chat query.** > If no one is actively interacting with your live app, it consumes **zero tokens** and costs **$0.00** to stay online. You do *not* need to worry about hourly background idling costs!

### Step 1: Fork and Star this Repository
1. Click the **⭐ Star** button in the top-right corner of this page to save it.
2. Click the **Fork** button to generate an identical copy of this project directly inside your own GitHub profile.

   
### Step 2: Set Up Your Agent & Harvest Microsoft Foundry Credentials

Now, configure your cloud brain. You will build the agent inside your portal and collect the keys needed to power your frontend app.

> 📖 **Detailed Walkthrough Available:** For an exact, step-by-step breakdown of this entire phase—including policy checks, resource provisioning, and file indexing—please refer to our dedicated [AI-Agent-deployment-guide.md](./AI-Agent-deployment-guide.md) reference file.

1. Log into **Microsoft Foundry** ([ai.azure.com](https://ai.azure.com)) using your university credentials.
2. **Create your AI-Career-Agent:** Use the skills you mastered during our CSC300 learning journey to configure your assistant workspace.
*(🎥 Click here to watch my [Step-by-Step Video Guide](https://youtu.be/P9oPRnGcWGc) if you need a quick portal walkthrough!)*
3. **Upload Your Knowledge Base**: Inside the Agent Builder pane, toggle the **File Search / Knowledge** utility and upload your personal resume file so the engine can ground its responses. 
   *(💡 **Pro-Tip**: For the absolute best grounding and retrieval results, adapt your details using our structured [cv.md](./CV.md) template!)*. 
4. **Harvest Connection Keys**: Navigate to your deployed project hub and securely copy these four specific connection keys into your environment setup:
   - 'AZURE_ENDPOINT'
   - 'AZURE_API_KEY'
   - 'AZURE_AGENT_NAME'
   - 'AZURE_AGENT_VERSION'


### Step 6: Deploy Instantly to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io) and log in using your GitHub account.
2. Click **New app**, then select your forked repository: `[Your-Username]/ai-career-agent`.
3. Set your main file path to `app.py`.
4. **⚠️ CRITICAL (Security Step):** Before hitting deploy, click **Advanced Settings** and inject your Azure credentials securely into the Secrets panel:
5. 
   ```toml
   AZURE_ENDPOINT = "[https://your-resource-name.azure.com/](https://your-resource-name.azure.com/)"
   AZURE_API_KEY = "your 40 character secret key"
   AZURE_AGENT_NAME = "your agent deployment name"
   AZURE_AGENT_VERSION="your agent version numbe, e.g 5"
   
   
6. Click Deploy! Your application will be live globally in under two minutes.
 
---
   
### Congratulations your agent is life now and you can use it in your github profile like mine :)

<img width="652" height="148" alt="Screenshot 2026-05-31 140758" src="https://github.com/user-attachments/assets/994a52f8-a925-4e56-9b21-485e0e37fabe" />


---
## 📄 License
Distributed under the MIT License. See [LICENSE](https://github.com/hanemma7moud/AI-Career-Agent/blob/main/LICENSE) for more information.
