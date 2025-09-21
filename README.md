# Adversarial-Prompt-Stress-Testing-for-AI-Security

# Inspiration 
With AI copilots and assistants being widely adopted, we saw a major risk: adversarial prompts can 
trick models into revealing secrets or bypassing safeguards. We wanted a proactive way to test and 
strengthen AI security before deployment. 

# What It Does 
The system generates adversarial prompts using an LLM, runs them against a target AI model 
(cloud or local), captures the responses, and evaluates vulnerabilities. It helps identify weaknesses 
like prompt injection, data leakage, or unsafe outputs. 

# How We Built It 
• Used LangChain + ChatOpenAI wrapper to connect with the GenAI Lab API for generating 
adversarial prompts. 
• Created a vulnerable test AI model to simulate attacks. 
• Developed scripts to generate prompts, run tests, and save outputs. 
• Designed a workflow that evaluates model responses and reports findings.

<img width="1536" height="1024" alt="Image Sep 20, 2025, 07_16_27 PM" src="https://github.com/user-attachments/assets/7e73e264-5b38-4180-b7e8-15d819907106" />


# Challenges We Ran Into 
• Dealing with version mismatches in LangChain imports. 
• Converting LLM responses into consistent strings for saving. 
• Designing a vulnerable AI model that is simple but realistic enough for testing. 

# Accomplishments That We’re Proud Of 
• Built a working adversarial testing pipeline end-to-end. 
• Successfully generated and executed adversarial prompts. 
• Created a clear workflow diagram and hackathon submission framework. 

# What We Learned 
• Hands-on experience with LLM prompt injection attacks and mitigations. 
• How to integrate LangChain with custom AI endpoints. 
• The importance of version control and defensive coding when dealing with rapidly evolving 
AI frameworks. 

# The Future Is Bright
• Extend evaluation with automated scoring metrics (e.g., risk level, severity). 
• Integrate into CI/CD pipelines for AI model deployment. 
• Build a dashboard for real-time monitoring and security reporting. 

**Built With **
• LangChain 
• OpenAI / GenAI Lab API 
• Python 
• httpx 
• Custom test AI model
