
This comprehensive, step-by-step guide walks you through verifying your Azure subscription regional constraints, creating a resource group, deploying a **Microsoft Foundry** resource, and building/testing a custom autonomous AI Agent.

# Microsoft Foundry AI Agent Deployment Guide

🎬 **Quick Start**: For a complete visual walkthrough of the entire end-to-end setup process, please refer to the video: https://youtu.be/P9oPRnGcWGc

---

## Technical Overview
* **Platform:** Microsoft Azure & Microsoft Foundry
* **Deployment Region Constraints:** Dynamic (Subscription-dependent)
* **Default Model Utilized:** `gpt-4.1-mini`
* **Agent Core Capability:** Advanced Knowledge Retrieval & RAG (Retrieval-Augmented Generation)

---

## Phase 1: Verifying Your Allowed Subscription Regions
Because allowed deployment regions are not globally uniform and depend heavily on specific subscription parameters (such as academic or restricted tiers), you must verify your exact allowed locations first to prevent deployment blocks caused by absolute policy `Deny` rules.

1. **Access Subscriptions Portal**:
   * Navigate to the **Azure Portal Home**.
   * Under the *Azure services* grid or the *Navigate* section, click on **Subscriptions**.
  ![Uploading Screenshot 2026-05-31 152122.png…]()
<img width="1410" height="873" alt="Screenshot 2026-05-31 152110" src="https://github.com/user-attachments/assets/1c69922d-7c9b-4568-97c5-14c6ef1a1c27" />
## 

2. **Select Target Subscription**:
   * Review your active subscriptions table.
   * Click directly on your active management subscription link  `Azure for Students`).
<img width="1894" height="982" alt="Screenshot 2026-05-31 153924" src="https://github.com/user-attachments/assets/854e0034-a433-4401-8df9-527907103f70" />
## 
  
3. **Navigate to Compliance Policies**:
   * In the subscription's left-hand sidebar navigation menu, scroll down to the **Settings** sub-section.
   * Click on **Policies** to open the policy monitoring dashboard.
  <img width="1901" height="888" alt="Screenshot 2026-05-31 154023" src="https://github.com/user-attachments/assets/e4a7a484-156c-4c64-817c-6f9f1bf702fb" />
## 
     
4. **Locate Regional Restrictions**:
   * Under the *Policy | Compliance* view, review the list of assigned compliance rules at the bottom.
   * Click on the assignment link titled **Allowed resource deployment regions**.
<img width="1901" height="933" alt="Screenshot 2026-05-31 154053" src="https://github.com/user-attachments/assets/14b4429c-5315-4b05-9515-423719d193c6" />
## 
<img width="1911" height="909" alt="Screenshot 2026-05-31 154109" src="https://github.com/user-attachments/assets/ca6c89f7-f16e-4ff1-a2d2-827c7342bded" />
##      
5. **Inspect Parameter Values**:
   * Select the policy name to open its deep configuration properties.
   * Ensure you are viewing the **Parameters** tab.
   * Locate the **Parameter ID**: `listOfAllowedLocations` and look across to its **Parameter value** array.
   * *Example verified regions include:* `["southeastasia", "newzealandnorth", "indonesiacentral", "japaneast", "eastasia"]`.
   * **Crucial Rule:** Record these values. Any resource group or Foundry asset created in subsequent steps *must* be anchored inside one of these specific regional boundaries.
<img width="1906" height="824" alt="Screenshot 2026-05-31 154127" src="https://github.com/user-attachments/assets/f36f0ce6-79fd-439b-984d-c07ddc03e424" />

##
---

## Phase 2: Provisioning an Azure Resource Group
A Resource Group acts as a logical container hosting your cloud infrastructure dependencies.

1. **Open Resource Groups Workspace**:
   * Go back to the Azure home dashboard.
   * Click on **Resource groups**.
2. **Initiate Group Configuration**:
   * Click the **+ Create** button located on the top action bar.
3. **Configure Resource Metadata**:
   * **Subscription**: Ensure your verified subscription (e.g., `Azure for Students`) is selected.
   * **Resource group name**: Input a highly descriptive naming convention (e.g., `CSC300-bonus`).
   * **Region**: Select a region explicitly allowed by your policy verified in Phase 1 (e.g., `(Asia Pacific) Southeast Asia`).
4. **Validation and Lifecycle Creation**:
   * Click **Review + create** at the bottom of the interface.
   * Once the system greenlights the policy validation check, click **Create**.

---

## Phase 3: Deploying the Microsoft Foundry Infrastructure

1. **Launch Microsoft Foundry Console**:
   * Navigate to your organization's designated **Microsoft Foundry** cloud management console interface.
2. **Launch Setup Workflow**:
   * Find the *Create a Foundry Resource* card dashboard element.
   * Click on the **Create a resource** action button.
3. **Link Architecture Dependencies**:
   * **Resource group**: Select your freshly provisioned group from the dropdown menu (e.g., `CSC300-bonus`).
   * **Name**: Type a definitive, unique name identifier for your instance (e.g., `HE-Agent`).
   * **Region**: Mirror the region associated with your resource group context (e.g., `(Asia Pacific) Southeast Asia`).
4. **Execute Core Cloud Provisioning**:
   * Click **Review + create** to initialize the deployment validation step.
   * Once the template checking completes, click the **Create** button.
5. **Track Deployment Status**:
   * Wait on the loading screen as the foundational templates deploy.
   * When the notifications bar flashes **Your deployment is complete**, click the **Go to resource** button.

---

## Phase 4: Constructing Your Custom AI Agent

1. **Access Portal Workspace**:
   * Inside your deployed resource overview dashboard, locate the main service utility links.
   * Click on the **Go to Foundry portal** navigation button to pop open the dedicated agent studio.
2. **Instantiate a New Agent Node**:
   * From the welcoming canvas, locate the main control path and click **Create agents** or select **New Foundry**.
3. **Assign Identification**:
   * A configuration window titled **Create an agent** will appear on your screen.
   * **Agent name**: Input your specific naming convention (e.g., `HE-AI-Career-Agent`).
   * Click **Create** to launch the low-code development studio environment.
4. **Assign the Underlying LLM**:
   * Locate the **Model** option field block inside the playground setup menu.
   * Expand the dropdown list and select your computational engine requirement (e.g., `gpt-4.1-mini`).
5. **Define System Prompting & Behavioral Framework**:
   * Go to the **Instructions** workspace box.
   * Input your definitive system prompts, behavioral boundaries, response logic constraints, and domain orientation directives.
6. **Inject Specialized Knowledge Context (RAG)**:
   * Scroll down to the **Knowledge** management block asset element.
   * Click **Add** and choose **Upload files**.
   * Select your analytical file metadata context index from your local computer directory (e.g., markdown or data assets like `HE.md`).
   * Click **Attach** to begin vector indexing your uploaded reference context into the agent's memory bank.
7. **Commit Agent State**:
   * Verify all parameters align with your development goal.
   * Click the **Save** button in the upper-right corner to freeze versioning configurations.

---

## Phase 5: Executing Sandbox Testing Verification

1. **Enter Interactive Sandbox Mode**:
   * Click on the **Preview** button located next to your state saving controller on the top header tracking bar.
2. **Validate Contextual Alignment**:
   * Use the generated chatbot interface simulator pane to send complex queries matching the operational parameters defined in your system prompt instructions.
   * Verify that the engine correctly references your index data files (e.g., validating knowledge files, academic background contexts, or industry roles) to return exact, grounded answers without hallucinations.
