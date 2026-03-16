# 🤖 AgentForge

**AgentForge** is an intelligent multi-agent system that transforms product ideas into comprehensive technical documentation using AI-powered agents. Built with LangGraph and Google's Gemini AI, it orchestrates specialized agents that collaborate to generate complete product specifications, system architecture, backend design, and QA test plans.

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2.14-green.svg)](https://python.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2.16-orange.svg)](https://langchain-ai.github.io/langgraph/)
[![Gemini](https://img.shields.io/badge/Gemini-2.5--flash-blue.svg)](https://ai.google.dev/)

## 🌟 Features

- **Multi-Agent Architecture**: Leverages specialized AI agents working in sequence
- **Complete Documentation Suite**: Generates PRD, architecture docs, backend design, and test plans
- **LangGraph Orchestration**: Uses state-based workflow for agent coordination
- **Structured Output**: Validates all outputs using Pydantic schemas
- **Gemini Integration**: Powered by Google's Gemini 2.5 Flash model (you can also use the latest model)
- **Automated Project Generation**: Creates organized documentation folders automatically

## 🏗️ Architecture

AgentForge employs a sequential multi-agent workflow where each agent builds upon the previous agent's output:

```
Product Idea → Product Manager → Architect → Backend Engineer → QA Engineer → Documentation
```

### Agent Roles

1. **Product Manager Agent** 🎯
   - Analyzes product ideas
   - Generates Product Requirements Document (PRD)
   - Defines target users, core features, and success metrics

2. **Architect Agent** 🏛️
   - Designs system architecture
   - Defines microservices structure
   - Specifies database schema and tech stack

3. **Backend Engineer Agent** 💻
   - Creates detailed backend design
   - Defines API endpoints
   - Specifies database models and backend services

4. **QA Engineer Agent** 🧪
   - Generates comprehensive test plan
   - Defines test cases and edge cases
   - Creates API test specifications

## 🛠️ Tech Stack

- **Python 3.11+**: Core programming language
- **LangChain 0.2.14**: LLM application framework
- **LangGraph 0.2.16**: Agent workflow orchestration
- **Google Gemini**: Large Language Model
- **Pydantic 2.8.2**: Data validation and schema management
- **Python-dotenv**: Environment variable management

## 📋 Prerequisites

- Python 3.11 or higher
- Google AI API key (Gemini)
- Virtual environment (recommended)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd agentforge
```

### 2. Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_ai_api_key_here
GRPC_DNS_RESOLVER=native
```

**Note**: The `GRPC_DNS_RESOLVER=native` setting resolves DNS issues with gRPC on macOS.

## 💻 Usage

### Basic Usage

Run the main application with a default product idea:

```bash
python main.py
```

### Custom Product Idea

Modify the `main.py` file to specify your own product idea:

```python
state = {
    "idea": "Your custom product idea here",
    "product_spec": None,
    "architecture": None,
    "backend_design": None,
    "qa_plan": None
}
```

### Example Output

The system will generate a project folder in `generated_projects/` containing:

```
generated_projects/
└── your_product_name/
    ├── PRD.md                  # Product Requirements Document
    ├── architecture.md         # System Architecture
    ├── backend_design.md       # Backend Design Specification
    └── test_plan.md           # QA Test Plan
```

## 📁 Project Structure

```
agentforge/
├── agents/                     # AI Agent implementations
│   ├── product_manager.py     # Product Manager Agent
│   ├── architect.py           # System Architect Agent
│   ├── backend_engineer.py    # Backend Engineer Agent
│   ├── qa_engineer.py         # QA Engineer Agent
│   └── code_generator.py      # Code Generation Agent (future)
│
├── schemas/                    # Pydantic schemas for data validation
│   ├── agent_state.py         # Workflow state schema
│   ├── product_schema.py      # Product specification schema
│   ├── architecture_schema.py # Architecture schema
│   ├── backend_schema.py      # Backend design schema
│   └── qa_schema.py           # QA plan schema
│
├── workflows/                  # LangGraph workflow definitions
│   └── agent_graph.py         # Multi-agent workflow orchestration
│
├── services/                   # Service layer
│   └── llm_service.py         # LLM service wrapper
│
├── tools/                      # Utility tools
│   └── project_generator.py   # Documentation generator
│
├── config/                     # Configuration files
│   └── settings.py            # Application settings
│
├── generated_projects/         # Output directory for generated docs
│
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in git)
└── README.md                   # This file
```

## 🔄 How It Works

### 1. Initialization
```python
graph = build_agent_graph()  # Creates LangGraph workflow
```

### 2. State Management
AgentForge uses a typed state dictionary that flows through all agents:
- `idea`: Initial product concept
- `product_spec`: Product requirements
- `architecture`: System architecture
- `backend_design`: Backend specifications
- `qa_plan`: Test plan

### 3. Sequential Processing
Each agent processes the state and adds its output:

```python
Product Manager → Generates product_spec
       ↓
   Architect → Generates architecture (uses product_spec)
       ↓
Backend Engineer → Generates backend_design (uses architecture)
       ↓
  QA Engineer → Generates qa_plan (uses backend_design)
```

### 4. Documentation Generation
The `ProjectGenerator` tool creates formatted markdown documentation from all agent outputs.

## 📄 Generated Documentation

### Product Requirements Document (PRD.md)
- Product name and description
- Target user personas
- Core features list
- Success metrics and KPIs

### System Architecture (architecture.md)
- Microservices breakdown
- Database table specifications
- Technology stack recommendations

### Backend Design (backend_design.md)
- REST API endpoint definitions
- Database models and schemas
- Backend service specifications

### QA Test Plan (test_plan.md)
- Functional test cases
- Edge case scenarios
- API test specifications

## 🧪 Testing

Individual agents can be tested separately:

```bash
# Test Product Manager Agent
python test_product_manager_agent.py

# Test Product Schema validation
python test_product_schema.py

# Test LLM connectivity
python test_llm.py
```

## 🔧 Configuration

### LLM Settings

Modify `services/llm_service.py` to change model parameters:

```python
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",      # Model version
    temperature=0.2,                # Creativity (0.0-1.0)
    response_mime_type="application/json"  # Structured output
)
```

### Agent Prompts

Each agent's behavior can be customized by modifying the prompts in their respective files in `agents/`.

## 🐛 Troubleshooting

### DNS Resolution Errors
If you encounter gRPC DNS errors, ensure you have set:
```env
GRPC_DNS_RESOLVER=native
```

### Import Errors
Make sure your virtual environment is activated:
```bash
source venv/bin/activate
```

### API Key Issues
Verify your Gemini API key is correctly set in `.env`:
```bash
echo $GEMINI_API_KEY  # Should display your key
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions and classes
- Include type hints
- Write tests for new features
- Update README for significant changes

## 🗺️ Roadmap

- [ ] Add Code Generator Agent for automated code scaffolding
- [ ] Support for multiple LLM providers (OpenAI, Anthropic, etc.)
- [ ] Web UI for easier interaction
- [ ] Database integration for storing generated projects
- [ ] Version control for documentation iterations
- [ ] Export to different formats (PDF, DOCX)
- [ ] Integration with project management tools
- [ ] Custom agent creation framework

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [LangChain](https://python.langchain.com/) and [LangGraph](https://langchain-ai.github.io/langgraph/)
- Powered by [Google Gemini](https://ai.google.dev/)
- Inspired by the multi-agent system architecture pattern

## 📧 Contact

For questions, suggestions, or issues, please open an issue on GitHub.

---

**Made with ❤️ using AI and Python**
