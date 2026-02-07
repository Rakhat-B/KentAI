#!/usr/bin/env python3
"""
Demo script for KentAI - Shows the automation capabilities without requiring Ollama
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from kentai.automation import AutomationEngine
from colorama import Fore, Style, init

init(autoreset=True)

def demo():
    print(f"{Fore.CYAN}{'='*60}")
    print(f"  KentAI Demo - Automation Showcase 🤖")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    engine = AutomationEngine()
    
    # Demo 1: Lazy Mode
    print(f"{Fore.YELLOW}Demo 1: Lazy Day Mode{Style.RESET_ALL}")
    print(f"  Simulating: 'Hey KentAI, let's start a lazy day'\n")
    result = engine.execute_action({'action': 'lazy_mode', 'value': True})
    print(f"{Fore.GREEN}  ✓ Lazy mode activated!{Style.RESET_ALL}")
    print(f"  Results: {result}\n")
    
    # Demo 2: Work Mode
    print(f"{Fore.YELLOW}Demo 2: Work Mode{Style.RESET_ALL}")
    print(f"  Simulating: 'Let's work on my project'\n")
    result = engine.execute_action({'action': 'work_mode', 'value': True})
    print(f"{Fore.GREEN}  ✓ Work mode activated!{Style.RESET_ALL}")
    print(f"  Results: {result}\n")
    
    # Demo 3: Custom Apps
    print(f"{Fore.YELLOW}Demo 3: Open Custom Apps{Style.RESET_ALL}")
    print(f"  Simulating: 'Open YouTube and Gmail'\n")
    result = engine.execute_action({'action': 'open_apps', 'value': ['youtube', 'gmail']})
    print(f"{Fore.GREEN}  ✓ Apps opened!{Style.RESET_ALL}")
    print(f"  Results: {result}\n")
    
    print(f"{Fore.CYAN}{'='*60}")
    print(f"  Demo Complete! 🎉")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    print(f"To use KentAI with full AI capabilities:")
    print(f"  1. Install Ollama: https://ollama.ai")
    print(f"  2. Run: ollama serve")
    print(f"  3. Pull a model: ollama pull llama2")
    print(f"  4. Run: python kent.py")

if __name__ == "__main__":
    demo()
