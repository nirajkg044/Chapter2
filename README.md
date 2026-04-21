# Chapter2 - Write Workflow Agents
This chapter guides you through writing a simple workflow agents. Workflow Agents are the "Project Managers" of your system which follows a deterministic script that you define

This `README.md` is designed to showcase your architectural mindset. It does explain how to write a LLM agent and run the code; it explains **why** you chose this multi-agent pattern and how the **Google ADK** handles state, reasoning, and tool-use.

---

# 🚗 Friend Trip Agent: root_agent assist a trip planner for friends

An agentic orchestration system built with the **Google Agent Development Kit (ADK)**. This project demonstrates a decoupled, multi-agent architecture designed to help friends to plan a vacation trip.

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/47ece08c-b4e8-420e-9ee8-bc997a25e9a1" />


## 🏗️ Architectural Overview

This project moves away from monolithic prompts by utilizing a **Modular Multi-Agent System**. By separating concerns between specialized agents, we improve reliability, reduce token overhead, and allow for deterministic guardrails.

### The ADK Pipeline
The system utilizes a `LLM-Based Agents` a standalone Intelligent Worker to accomplish a specific task

1.  **root_agent (SequentialAgent Agent):** Specialized in trip planner. It uses custom **Tools** to find friend availbility and frined budget for the trip.

---

## 🛠️ Technology Stack

* **Framework:** Google Agent Development Kit (ADK) v1.2+
* **Orchestration:** ADK `SequentialAgent` & `InMemoryRunner`
* **Models:** Gemini 2.5 Flash
* **Language:** Python 3.14+
* **Dev Tools:** ADK Web UI (for trace observability)

---

## 📂 Project Structure

```text
Chapter1/
├── agents/
│   ├── __init__.py     # LLM Agent with Search capabilities
│   ├── agent.py        # Logic for EV charging ROI
│   └── .env            # Python-based tools (PSE&G API, Lease Scraper)
├── .adk/               # google ADK tools package
│   
├── .venv/              # libraries and packages
│   
├── .vscode/
│   └── settings.json   # Python manager and package info
└── .env                # GOOGLE_API_KEY and other API keys
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have a Google AI Studio and python 
```bash
uv init
```

```bash
uv venv
```
```bash
.venv\Scripts\activate.bat	
```

```bash
uv add google-adk 
```

### 2. Running the Agent
You can interact with the concierge via the terminal:
```bash
python agent.py
```

### 3. Visual Debugging (The ADK UI)
To see the "Thought-Action-Observation" loop in real-time, launch the development dashboard:
```bash
adk web
```
*Navigate to `localhost:8080` to view the agentic trace, event logs, and tool execution status.*

---

## 💡 Key Agent Patterns Implemented

### **Tool Decoupling**
Instead of the LLM "hallucinating" trip budget, This tool returns field trip booking confirmation.

### **Stateful Sessions**
Using the `ADK Session` service, the agent remembers user constraints (e.g., "2 friends shows availablity") across multiple turns without needing to re-send the entire chat history in every prompt.

### **Workflow Agents**
1. `FriendLookupAgent` - This agent is responsible to pull list of freinds who are interested in the field trip
2. `DestinationLookupAgent` - Based out of total freinds count, suggest the places for the field trip
3. `ExpenseCalculatorAgent` - This agent calculate the total expenses required in the trip
4. `BookingAgent` - This agent will book the field trip location vanue and retrun booking number


---

## 🛤️ Roadmap
- [ ] **Cloud Deployment:** Migrate from `InMemoryRunner` to `CloudRunner` for deployment on **Vertex AI Agent Engine**.
- [ ] **Multi-Modal Support:** Use Gemini's vision capabilities to analyze places, wether, and other geolocations for vacation trip planner.


---
*Created by Niraj Gupta — Software Architect & AI Enthusiast.*

---

### Why this works for your GitHub:
* **Architectural Language:** Terms like "Decoupled," "Deterministic Guardrails," and "State Management" signal that you are a Software Architect, not just a casual coder.
* **Observability:** Mentioning the `ADK UI` shows you care about debugging and the lifecycle of an application.
* **Extensibility:** The roadmap shows you understand how to scale a local MVP into a production-grade cloud service.
