# KentAI Example Scenarios

This file contains example scenarios and commands you can use with KentAI.

## Predefined Modes

### 🎮 Lazy Day Mode
**Triggers:** "lazy day", "chill mode", "gaming time", "relax"

**Actions:**
- Opens Steam
- Opens Discord
- Opens YouTube
- Disables alarms/notifications

**Example commands:**
```
Hey KentAI, let's start a lazy day
Time to chill, open my gaming setup
I want to relax today
```

### 💼 Work Mode
**Triggers:** "work mode", "work on my project", "productive mode"

**Actions:**
- Opens VS Code
- Opens Notion
- Opens Gmail

**Example commands:**
```
Let's work on my project
Time to be productive
Set up my work environment
```

## Custom Commands

### Open Specific Apps
```
Open Discord and Steam
Launch YouTube and Spotify
Start VS Code
```

### Web-based Apps
```
Open Gmail
Show me YouTube
Open Notion
```

## Conversation Examples

### Casual Chat
```
You: What's up dude?
KentAI: Hey man! Just chillin', ready to help with whatever you need. Want me to fire up some apps or just here to chat?
```

### Getting Help
```
You: What can you do?
KentAI: Yo! I can help you open apps, set up your workspace, start gaming sessions - basically automate your computer stuff. Just tell me what you need in plain English!
```

### Custom Workflows
```
You: I need to start streaming
KentAI: [Would open OBS, Discord, Spotify, etc. - customize in automation.py]
```

## Creating Custom Scenarios

### Edit kentai/automation.py

Add your own methods:

```python
def streaming_mode(self) -> dict:
    """Set up streaming environment"""
    results = {
        "obs": self.open_app("obs"),
        "discord": self.open_app("discord"),
        "spotify": self.open_app("spotify"),
        "twitch": self.open_app("https://twitch.tv")
    }
    return results
```

### Update kentai/brain.py

Add to the SYSTEM_PROMPT:

```python
- streaming_mode: true - Activates streaming setup (OBS, Discord, Spotify, Twitch)
```

### Add to execution in kentai/automation.py

In the `execute_action` method:

```python
elif action == "streaming_mode" and value:
    return {"status": "success", "results": self.streaming_mode()}
```

## Tips for Best Results

1. **Be Natural**: KentAI understands casual language
2. **Be Specific**: Mention exact app names when needed
3. **Chain Commands**: "Open Discord and start my work mode"
4. **Reset if Confused**: Type `reset` to clear conversation history
5. **Customize**: Edit .env for your specific app paths

## Platform-Specific Notes

### Linux
- Apps must be in PATH or use full paths in .env
- Some apps may need specific launch commands

### macOS
- Uses `open -a` for app launching
- App names should match those in /Applications

### Windows
- Uses shell commands
- May need .exe extension for some apps
- Can use full paths in .env

## Advanced Usage

### Environment Variables (.env)
```bash
# Custom app paths
VSCODE_PATH=/usr/bin/code
STEAM_PATH=/usr/games/steam
DISCORD_PATH=/opt/discord/Discord

# LLM settings
OLLAMA_MODEL=mistral  # or llama2, codellama, etc.
OLLAMA_HOST=http://localhost:11434
```

### Different LLM Models
KentAI works with any Ollama model:
- `llama2` - Good balance (default)
- `mistral` - Fast and capable
- `llama3` - More advanced
- `codellama` - Better at code-related tasks

Change in .env:
```bash
OLLAMA_MODEL=mistral
```
