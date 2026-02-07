"""
System automation for KentAI - opening apps, managing workflows
"""
import subprocess
import platform
import os
import webbrowser
from typing import List, Optional
from pathlib import Path


class AutomationEngine:
    """Handles all system-level automation tasks"""
    
    def __init__(self):
        self.system = platform.system()
        self.app_paths = self._load_app_paths()
        
    def _load_app_paths(self) -> dict:
        """Load application paths from environment or use defaults"""
        from dotenv import load_dotenv
        load_dotenv()
        
        return {
            "vscode": os.getenv("VSCODE_PATH", "code"),
            "steam": os.getenv("STEAM_PATH", "steam"),
            "discord": os.getenv("DISCORD_PATH", "discord"),
        }
    
    def open_app(self, app_name: str) -> bool:
        """
        Open an application by name
        
        Args:
            app_name: Name of the app (e.g., "discord", "steam", "vscode")
            
        Returns:
            True if successful, False otherwise
        """
        try:
            app_name_lower = app_name.lower()
            
            # Special handling for common apps
            if "youtube" in app_name_lower or "yt" in app_name_lower:
                webbrowser.open("https://youtube.com")
                return True
            elif "gmail" in app_name_lower or "mail" in app_name_lower:
                webbrowser.open("https://mail.google.com")
                return True
            elif "notion" in app_name_lower:
                webbrowser.open("https://notion.so")
                return True
            
            # Try to launch from app_paths
            if app_name_lower in self.app_paths:
                cmd = self.app_paths[app_name_lower]
                return self._launch_command(cmd)
            
            # Try direct command
            return self._launch_command(app_name)
            
        except Exception as e:
            print(f"Failed to open {app_name}: {e}")
            return False
    
    def _launch_command(self, cmd: str) -> bool:
        """Launch a command based on the OS"""
        try:
            if self.system == "Windows":
                subprocess.Popen(cmd, shell=True)
            elif self.system == "Darwin":  # macOS
                subprocess.Popen(["open", "-a", cmd])
            else:  # Linux
                subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except Exception as e:
            print(f"Launch failed: {e}")
            return False
    
    def lazy_mode(self) -> dict:
        """
        Activate lazy day mode:
        - Open Steam
        - Open Discord
        - Open YouTube
        - Disable alarms (placeholder)
        
        Returns:
            Status dictionary
        """
        results = {
            "steam": self.open_app("steam"),
            "discord": self.open_app("discord"),
            "youtube": self.open_app("youtube"),
            "alarms_disabled": self.disable_alarms()
        }
        return results
    
    def work_mode(self) -> dict:
        """
        Activate work mode:
        - Open VS Code
        - Open Notion
        - Open Gmail
        
        Returns:
            Status dictionary
        """
        results = {
            "vscode": self.open_app("vscode"),
            "notion": self.open_app("notion"),
            "gmail": self.open_app("gmail")
        }
        return results
    
    def disable_alarms(self) -> bool:
        """
        Disable system alarms/notifications
        Note: This is a placeholder - actual implementation depends on OS
        """
        print("Alarms disabled (placeholder - would integrate with OS notification system)")
        return True
    
    def enable_alarms(self) -> bool:
        """
        Enable system alarms/notifications
        Note: This is a placeholder - actual implementation depends on OS
        """
        print("Alarms enabled (placeholder - would integrate with OS notification system)")
        return True
    
    def open_multiple_apps(self, app_list: List[str]) -> dict:
        """
        Open multiple applications
        
        Args:
            app_list: List of app names
            
        Returns:
            Dictionary with results for each app
        """
        results = {}
        for app in app_list:
            results[app] = self.open_app(app)
        return results
    
    def execute_action(self, action_data: dict) -> dict:
        """
        Execute an action based on parsed command
        
        Args:
            action_data: Dictionary with "action" and "value" keys
            
        Returns:
            Execution results
        """
        if not action_data:
            return {"status": "no_action"}
        
        action = action_data.get("action")
        value = action_data.get("value")
        
        if action == "lazy_mode" and value:
            return {"status": "success", "results": self.lazy_mode()}
        elif action == "work_mode" and value:
            return {"status": "success", "results": self.work_mode()}
        elif action == "open_apps" and isinstance(value, list):
            return {"status": "success", "results": self.open_multiple_apps(value)}
        elif action == "disable_alarms" and value:
            return {"status": "success", "results": {"alarms": self.disable_alarms()}}
        elif action == "enable_alarms" and value:
            return {"status": "success", "results": {"alarms": self.enable_alarms()}}
        else:
            return {"status": "unknown_action", "action": action}
