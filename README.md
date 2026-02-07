# KentAI 😎

**Your chill AI assistant bro** - A local desktop AI assistant with a funny, slightly sarcastic "dude" personality. He talks casually, can swear naturally, and feels like a smart friend who automates your computer tasks.

## 🎯 Features

- **100% Local & Private**: Runs entirely on your machine using Ollama - no API costs, no data sent to the cloud
- **Chill Personality**: KentAI talks like your smart friend, casually and with natural humor
- **Natural Language Commands**: Just tell KentAI what you want in plain English
- **Smart Automation**: Trigger complex workflows with simple requests
- **Extensible**: Easy to add new commands and automation scenarios

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama** (for local LLM):
   ```bash
   # Visit https://ollama.ai and install for your OS
   # Then pull a model:
   ollama pull llama2
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure (optional)**:
   ```bash
   cp .env.example .env
   # Edit .env to customize app paths for your system
   ```

### Running KentAI

```bash
# Start Ollama (in a separate terminal)
ollama serve

# Run KentAI
python kent.py
```

## 💬 Example Commands

KentAI understands natural language! Try these:

- **Lazy Day Mode**: "Hey KentAI, let's start a lazy day"
  - Opens Steam, Discord, YouTube
  - Disables alarms
  
- **Work Mode**: "Let's work on my project"
  - Opens VS Code, Notion, Gmail
  
- **Custom Commands**: "Open Discord and Steam"
  - Opens specific apps you mention

- **Just Chat**: "What's up dude?"
  - KentAI will chat with you in his chill style

## 🏗️ Project Structure

```
KentAI/
├── kentai/
│   ├── __init__.py
│   ├── brain.py         # LLM integration with personality
│   ├── automation.py    # System automation engine
│   └── main.py          # Main application interface
├── kent.py              # Launcher script
├── requirements.txt     # Python dependencies
├── .env.example         # Configuration template
└── README.md
```

## 🛠️ How It Works

1. **You speak**: Natural language input to KentAI
2. **LLM processes**: Local Ollama LLM understands your intent with KentAI's personality
3. **Action extraction**: System parses commands from the LLM response
4. **Automation**: Python automation engine executes system-level tasks
5. **Feedback**: KentAI responds in his chill, conversational style

## 🎨 Customization

### Adding Custom Automation Scenarios

Edit `kentai/automation.py` to add your own modes:

```python
def my_custom_mode(self) -> dict:
    """Your custom workflow"""
    results = {
        "app1": self.open_app("app1"),
        "app2": self.open_app("app2"),
    }
    return results
```

### Configuring App Paths

Edit `.env` to set paths for your specific system:

```bash
VSCODE_PATH=code
STEAM_PATH=steam
DISCORD_PATH=discord
# Add your own app paths
```

### Changing the LLM Model

In `.env`:
```bash
OLLAMA_MODEL=llama2  # or mistral, codellama, etc.
```

## 🤝 Contributing

Want to make KentAI even more awesome? Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [Ollama](https://ollama.ai) for local LLM inference
- Inspired by the need for a truly private, local AI assistant that doesn't feel corporate

## ⚠️ Troubleshooting

**"Can't connect to Ollama"**
- Make sure Ollama is installed and running: `ollama serve`
- Check that you've pulled a model: `ollama pull llama2`

**Apps not opening**
- Edit `.env` to set correct paths for your system
- On Linux, ensure apps are in your PATH or provide full paths

**KentAI seems confused**
- Try resetting the conversation: type `reset` or `clear`
- Make sure you're using a capable model (llama2 or better)

---

Made with 💙 by developers who believe AI assistants should be chill bros, not corporate robots.
