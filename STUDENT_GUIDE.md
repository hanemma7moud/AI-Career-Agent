
# 🚀 AI Career Agent — Student Guide

Welcome! In this lab, you will build and customize your own **AI Career Agent** using **Azure OpenAI + Streamlit**.

By the end of this guide, you will:
✅ Run the AI agent locally  
✅ Connect it to your own Azure account  
✅ Customize it for your career interests  
✅ Publish your own version  

---


## 📌 Overview
This project is a customizable AI assistant that helps with:
* **Career advice:** Automated guidance tailored to industry trends.
* **Resume feedback:** Evaluation based on targeted keyword match criteria.
* **Skill development:** Step-by-step custom training roadmaps.
* **Job preparation:** Mock interview question generation.

You will fork this template project and turn it into your own personalized portfolio piece.

---

## 🟢 Step 1: Fork and Clone the Template Repository

1. Navigate to the base template repository: 👉 [hanemma7moud/ai-career-agent](https://github.com/hanemma7moud/ai-career-agent)
2. Click the **⭐ Star** button in the upper-right corner to save it to your favorites.
3. Click the **Fork** button to generate an identical copy of this project under your own GitHub account profile.
4. Open your local terminal or command prompt and run these commands to pull the project onto your machine:

```shell
git clone [https://github.com/YOUR-USERNAME/ai-career-agent.git](https://github.com/YOUR-USERNAME/ai-career-agent.git)
cd ai-career-agent
```
## 🟢 Step 2: Provision Your Azure OpenAI Infrastructure
We will use your Azure for Students subscription credits ($100 active balance) to power the backend engine.

### 1. Create an Azure OpenAI Resource Instance
Log into your cloud portal: 👉 portal.azure.com

1- In the top search bar, look for Azure OpenAI and click Create.

2- Select or create a unified Resource Group (e.g., portfolio-ai-resources).

3- Select your closest geographical region, name your instance, and choose the Pricing Tier: S0. Click Review + Create.

### 2. Deploy Your Model
1- Once deployment completes, click Go to resource.

2- Launch the Azure AI Studio / Microsoft Foundry Portal.

3- Navigate to the Deployments tab under the management sidebar.

4- Click Create new deployment and provision either:

    - gpt-4o (Excellent for complex reasoning)
    - gpt-4o-mini (Extremely fast and highly conservative with your student credits)

### 🔑 Copy Your Access Keys
Keep these three strings copied safely in a temporary notepad file. You will need them to connect your Streamlit frontend to your cloud backend:

- API Key: Found under the Keys and Endpoint tab in your Azure resource.

- Endpoint URL: (Format: https://your-resource-name.openai.azure.com/)

- Deployment Name: The exact deployment identifier string you chose inside the studio portal.

## 🟢 Step 3: Configure Your Local Environment Variables
To protect your student credit balance from being scraped and exploited, never hardcode your API keys into your scripts. We manage these safely using environment variables.

In the root directory of your project folder, create a new file named exactly .env.

Open the file in your code editor and paste your credentials like this:

Code snippet
AZURE_OPENAI_API_KEY=your_40_character_secret_key_here
AZURE_OPENAI_ENDPOINT=[https://your-unique-endpoint.openai.azure.com/](https://your-unique-endpoint.openai.azure.com/)
AZURE_OPENAI_DEPLOYMENT=your_model_deployment_name_here
⚠️ Security Check: Your .env file is automatically ignored by git via the .gitignore file. Never push this file to your public GitHub profile.

## 🟢 Step 4: Install System Dependencies
Make sure you have a current version of Python installed (>= 3.9 is standard). Install the required application libraries using your terminal:

''' Shell
pip install -r requirements.txt
🟢 Step 5: Run the Application Locally
Launch your local Streamlit development server:
'''
''' Shell
streamlit run app.py
Your system will start a local node and open a browser window automatically at: 👉 http://localhost:8501
'''
🎉 Success! You should now see the base user interface of your interactive AI Career Agent running live on your machine.

## 🟢 Step 6: Customize Your Agent Persona 🚀
Now it's time to make this agent uniquely yours by changing its behavioral logic and data focus.

### 🎯 1. Modify the System Prompt
Locate the script file managing backend prompt payloads (typically found inside app.py or an isolated agent.py file).

Look for this baseline string:
''' shell
Python
SYSTEM_PROMPT = "You are a helpful AI career advisor."
'''
✨ Re-engineer this string to create a specialized industry mentor:

- **Data Science Profile**: "You are an expert Data Science Coach. Guide the user through my portfolio highlights, my experience with feature engineering, and my knowledge of Python data structures."

- **Cybersecurity Profile**: "You are an offensive security career mentor. Guide recruiters through my technical certifications, my lab strategies, and my blueprint for handling network vulnerabilities."

### 🎯 2. Personalize the Knowledge Base (RAG)
- Open the data assets directory inside the project folder.

- Replace the placeholder resume/CV data with your own professional history.

- **RAG Optimization Tip**: Use clean markdown headers (## Technical Skills, ## Key Projects) so the AI retrieval engine can find facts quickly when a recruiter asks a question.

### 🎯 3. Add Custom Code Features (Optional Challenges)
**Temperature Sliders** : Add a sidebar slider component to let users manipulate model properties dynamically (0.0 for highly factual technical answers, 1.0 for creative brainstorming).

**Interview Mode Toggle** : Build a checkbox that toggles the agent into a "Mock Interview" mode where it quizzes the user based on your target industry roles.

## 🟢 Step 7: Push Your Changes to GitHub
Once you are happy with your custom prompt logic and updates, commit your files and sync them back to your GitHub fork:

'''Shell
git add .
git commit -m "feat: personalized agent prompt persona and custom data assets"
git push origin main
'''
## 🟢 Step 8: Deploy Live to the Web!
✅ Streamlit Community Cloud (Recommended & Free)
Go to share.streamlit.io and log in using your active GitHub account.

Click New app, and select your forked repository: [YOUR-GITHUB-USERNAME]/ai-career-agent.

Set the target execution file path to app.py.

🔒 Critical Security Step: Before clicking deploy, click on Advanced Settings. Copy and paste your private environment variables directly into the secure secrets framework:

'''Shell
Ini, TOML
AZURE_OPENAI_API_KEY = "your_40_character_secret_key"
AZURE_OPENAI_ENDPOINT = "[https://your-resource-name.openai.azure.com/](https://your-resource-name.openai.azure.com/)"
AZURE_OPENAI_DEPLOYMENT = "your_model_deployment_name"
Click **Deploy**! Your app will build and go live on a public URL in less than two minutes.
'''

## 🟢 Step 9: Cloud Clean-Up (Protect Your Credits)
To ensure your **Azure for Students** credits don't run out silently over the break, get into the habit of cleaning up your resources when you finish testing.

1- Head back to the Azure Portal.

2- Open the **Resource Group** container you created for this lab.

3- Click **Delete resource group**, type the group name to verify your choice, and confirm the deletion.

4- Why this works: This completely stops all underlying cloud meters, preserving your remaining credits for your next big personal build!

💡 Creative Portfolio Ideas
You can pivot this codebase template into several different high-value tools:

- **🎓 Academic Guide Agent**: Built around specific course modules and study guides.

- 💼 **Job Application Matcher**: A tool that evaluates how well an uploaded job description matches your skill blocks.

- 🧠 **Technical Interview Coach**: Prone to testing edge cases in programming, architecture, or machine learning algorithms.

## 🧑‍🏫 Need a Hand?
If you hit a roadblock during your deployment:

Double-check that your secret keys match perfectly between your Azure portal and your Streamlit advanced configurations.

Reach out via our Canvas open discussion threads!

🚀 **Final Goal**: By completing this optional bonus project, you move beyond basic textbook theory and walk away with a real-world, cloud-connected Generative AI application to show future employers. Have fun building!
"""
