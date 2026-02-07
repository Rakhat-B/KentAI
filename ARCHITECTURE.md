# KentAI Architecture

This document explains how KentAI works under the hood.

## System Overview

```
┌─────────────┐
│    User     │
└──────┬──────┘
       │
       │ Natural language input
       ▼
┌─────────────────────────────────────────┐
│           KentAI Main Interface         │
│         (kentai/main.py)                │
│  - Colored terminal UI                  │
│  - Conversation management              │
│  - Command routing                      │
└──────┬──────────────────────┬───────────┘
       │                      │
       │                      │
       ▼                      ▼
┌──────────────┐      ┌──────────────────┐
│  KentAI Brain│      │ Automation Engine│
│(brain.py)    │      │ (automation.py)  │
│              │      │                  │
│- Local LLM   │      │- App launching   │
│- Personality │      │- Workflows       │
│- NLP parsing │◄─────┤- System control  │
└──────┬───────┘      └──────────────────┘
       │
       │ API calls
       ▼
┌──────────────┐
│    Ollama    │
│ (Local LLM)  │
└──────────────┘
```

## Component Details

### 1. Main Interface (`kentai/main.py`)

**Responsibilities:**
- User interaction via terminal
- Colorized output
- Session management
- Orchestration between brain and automation

**Key Features:**
- Interactive REPL loop
- Command history (via brain)
- Graceful error handling
- Pretty printing results

### 2. KentAI Brain (`kentai/brain.py`)

**Responsibilities:**
- Interface with Ollama LLM
- Maintain conversation context
- Parse natural language to actions
- Inject personality

**How it works:**
1. Receives user message
2. Sends to Ollama with system prompt (personality)
3. Parses response for JSON action blocks
4. Returns both conversational response and structured action

**Personality Injection:**
- System prompt defines "dude" character
- Examples of casual speech
- Instruction to include JSON actions
- Balance between friendly chat and functional commands

**Action Format:**
```json
{
  "action": "lazy_mode",
  "value": true
}
```

### 3. Automation Engine (`kentai/automation.py`)

**Responsibilities:**
- Execute system-level commands
- Launch applications
- Manage workflows
- Cross-platform compatibility

**Supported Actions:**
- `lazy_mode`: Gaming/relaxation setup
- `work_mode`: Productivity setup
- `open_apps`: Open specific applications
- `disable_alarms`/`enable_alarms`: System notifications

**Platform Handling:**
- **Linux**: Direct command execution via shell
- **macOS**: Uses `open -a` for app launching
- **Windows**: Shell commands with `.exe` support

### 4. Configuration (`.env`)

**Purpose:**
- Customize app paths per system
- Configure LLM model
- Set Ollama host

**Example:**
```bash
OLLAMA_MODEL=llama2
VSCODE_PATH=code
STEAM_PATH=/usr/games/steam
```

## Data Flow

### Typical Interaction:

1. **User Input:** "Hey KentAI, let's start a lazy day"

2. **Main Interface:** Routes to brain

3. **Brain Processing:**
   - Adds message to conversation history
   - Sends to Ollama with system prompt
   - Receives: "Yo dude, let's get gaming! 🎮 ```json{"action":"lazy_mode","value":true}```"
   - Extracts action: `{"action":"lazy_mode","value":true}`
   - Cleans response: "Yo dude, let's get gaming! 🎮"

4. **Action Execution:**
   - Main calls automation engine with action
   - Engine executes `lazy_mode()`
   - Opens Steam, Discord, YouTube
   - Disables alarms
   - Returns results

5. **User Feedback:**
   - Displays KentAI's response
   - Shows execution status
   - Ready for next command

## Extending KentAI

### Adding a New Mode

1. **Add automation method** (`automation.py`):
```python
def gaming_night_mode(self) -> dict:
    results = {
        "discord": self.open_app("discord"),
        "obs": self.open_app("obs"),
        "spotify": self.open_app("spotify")
    }
    return results
```

2. **Update system prompt** (`brain.py`):
```python
- gaming_night_mode: true - Sets up streaming (Discord, OBS, Spotify)
```

3. **Add execution handler** (`automation.py` in `execute_action`):
```python
elif action == "gaming_night_mode" and value:
    return {"status": "success", "results": self.gaming_night_mode()}
```

### Adding a New App

1. **Update `.env`:**
```bash
OBS_PATH=obs-studio
```

2. **Use in automation:**
```python
self.open_app("obs")
```

## Technical Design Decisions

### Why Local LLM (Ollama)?
- **Privacy:** No data leaves your machine
- **Cost:** No API fees
- **Speed:** Local inference
- **Control:** Choice of models

### Why JSON Actions?
- **Structured:** Easy to parse programmatically
- **Flexible:** Can add new action types
- **Clear:** Separates chat from commands
- **Reliable:** Less ambiguous than pure NLP

### Why Python?
- **Cross-platform:** Works on Linux, Mac, Windows
- **Rich ecosystem:** Easy access to system APIs
- **Readable:** Easy to customize
- **Rapid development:** Quick to extend

### Why Subprocess for Apps?
- **Universal:** Works across platforms
- **Simple:** Standard library
- **Non-blocking:** Apps run independently
- **Flexible:** Can launch anything

## Testing Strategy

### Unit Tests (`test_kentai.py`)
- **Automation Engine:** Action execution
- **Brain:** JSON parsing and response cleaning
- **Coverage:** Core functionality without external dependencies

### Demo Script (`demo.py`)
- Simulates automation without LLM
- Quick verification of system integration
- Shows expected output

### Manual Testing
- Requires Ollama running
- Tests full conversation flow
- Validates personality

## Performance Considerations

### LLM Response Time
- Depends on model size and hardware
- Typical: 1-5 seconds for response
- Can be improved with faster models (mistral)

### App Launch Time
- Depends on application
- Non-blocking (returns immediately)
- Apps start independently

### Memory Usage
- Minimal Python overhead (~50MB)
- Ollama depends on model (2GB+ for llama2)
- Each app runs separately

## Security Considerations

### No Credentials Storage
- No API keys required
- .env for local paths only
- No sensitive data in code

### Local Execution Only
- No external API calls (except Ollama)
- No data transmission
- Full user control

### Safe App Launching
- Uses standard subprocess
- No shell injection (when using list args)
- Platform-specific safety

## Future Enhancements

### Potential Features
- Voice input/output
- GUI interface
- More complex workflows
- Learning from user behavior
- Integration with system APIs (calendar, notifications)
- Plugin system
- Cloud sync for preferences (optional)

### Platform Improvements
- Better macOS notification control
- Windows notification integration
- Linux desktop environment detection
- Better error messages for missing apps
