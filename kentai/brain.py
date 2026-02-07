"""
LLM integration for KentAI using local Ollama
"""
import json
import requests
from typing import Dict, Any, Optional


class KentAIBrain:
    """Local LLM interface with KentAI's dude personality"""
    
    SYSTEM_PROMPT = """You are KentAI, a chill, funny, slightly sarcastic AI assistant with a "dude" personality.
You talk casually like a smart friend. You can swear naturally when it feels right.
You help with computer automation tasks - opening apps, managing workflows, etc.

When a user asks you to do something, respond in a conversational way AND include a JSON action block.

Available commands:
- open_apps: ["app1", "app2"] - Opens applications
- lazy_mode: true - Activates lazy day mode (Steam, Discord, YouTube, disable alarms)
- work_mode: true - Activates work mode (VS Code, Notion, Gmail)
- disable_alarms: true - Disables system alarms
- enable_alarms: true - Enables system alarms

Example response:
"Yo dude, let's get that lazy day started! 🎮"
```json
{"action": "lazy_mode", "value": true}
```

Always be chill, supportive, and a bit sarcastic. Keep it real."""

    def __init__(self, model: str = "llama2", host: str = "http://localhost:11434"):
        self.model = model
        self.host = host
        self.conversation_history = []
        
    def chat(self, user_message: str) -> Dict[str, Any]:
        """
        Send a message to KentAI and get a response with possible actions
        
        Returns:
            {
                "response": "KentAI's text response",
                "action": {"action": "command", "value": ...} or None
            }
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Prepare the prompt
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            *self.conversation_history
        ]
        
        try:
            # Call Ollama API
            response = requests.post(
                f"{self.host}/api/chat",
                json={
                    "model": self.model,
                    "messages": messages,
                    "stream": False
                },
                timeout=60
            )
            response.raise_for_status()
            
            result = response.json()
            assistant_message = result.get("message", {}).get("content", "")
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # Parse action if present
            action = self._extract_action(assistant_message)
            
            # Clean response (remove JSON block)
            clean_response = self._clean_response(assistant_message)
            
            return {
                "response": clean_response,
                "action": action
            }
            
        except requests.exceptions.ConnectionError:
            return {
                "response": "Yo dude, I can't reach Ollama. Make sure it's running with 'ollama serve'!",
                "action": None
            }
        except Exception as e:
            return {
                "response": f"Damn, something went wrong: {str(e)}",
                "action": None
            }
    
    def _extract_action(self, message: str) -> Optional[Dict[str, Any]]:
        """Extract JSON action from message"""
        try:
            # Look for JSON code block
            if "```json" in message:
                start = message.find("```json") + 7
                end = message.find("```", start)
                json_str = message[start:end].strip()
                return json.loads(json_str)
            elif "```" in message:
                start = message.find("```") + 3
                end = message.find("```", start)
                json_str = message[start:end].strip()
                try:
                    return json.loads(json_str)
                except json.JSONDecodeError:
                    pass
        except (json.JSONDecodeError, ValueError, IndexError):
            pass
        return None
    
    def _clean_response(self, message: str) -> str:
        """Remove JSON blocks from response"""
        if "```" in message:
            parts = message.split("```")
            # Take only non-code parts
            return parts[0].strip()
        return message.strip()
    
    def reset_conversation(self):
        """Clear conversation history"""
        self.conversation_history = []
