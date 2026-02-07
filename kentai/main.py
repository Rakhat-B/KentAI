#!/usr/bin/env python3
"""
KentAI - Your chill AI assistant bro
Main entry point for the application
"""
import os
import sys
from pathlib import Path

# Add the parent directory to path so we can import kentai
sys.path.insert(0, str(Path(__file__).parent.parent))

from kentai.brain import KentAIBrain
from kentai.automation import AutomationEngine
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)


class KentAI:
    """Main KentAI application"""
    
    def __init__(self):
        print(f"{Fore.CYAN}Initializing KentAI...{Style.RESET_ALL}")
        try:
            self.brain = KentAIBrain()
            self.automation = AutomationEngine()
            print(f"{Fore.GREEN}✓ KentAI is ready!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error initializing KentAI: {e}{Style.RESET_ALL}")
            sys.exit(1)
    
    def process_command(self, user_input: str):
        """Process a user command through KentAI"""
        print(f"\n{Fore.YELLOW}You: {Style.RESET_ALL}{user_input}")
        
        # Get response from the brain
        result = self.brain.chat(user_input)
        
        # Display KentAI's response
        print(f"{Fore.CYAN}KentAI: {Style.RESET_ALL}{result['response']}")
        
        # Execute any actions
        if result['action']:
            print(f"{Fore.MAGENTA}[Executing automation...]{Style.RESET_ALL}")
            execution_result = self.automation.execute_action(result['action'])
            
            if execution_result['status'] == 'success':
                print(f"{Fore.GREEN}✓ Done!{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}Action status: {execution_result}{Style.RESET_ALL}")
    
    def run_interactive(self):
        """Run KentAI in interactive mode"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"  Welcome to KentAI - Your Chill AI Assistant Bro 😎")
        print(f"{'='*60}{Style.RESET_ALL}\n")
        print("Try commands like:")
        print('  - "Hey KentAI, let\'s start a lazy day"')
        print('  - "Let\'s work on my project"')
        print('  - "Open Discord and Steam"')
        print(f"\nType 'quit' or 'exit' to leave\n")
        
        while True:
            try:
                user_input = input(f"{Fore.GREEN}> {Style.RESET_ALL}").strip()
                
                if not user_input:
                    continue
                    
                if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                    print(f"{Fore.CYAN}KentAI: Later dude! 👋{Style.RESET_ALL}")
                    break
                
                if user_input.lower() in ['clear', 'reset']:
                    self.brain.reset_conversation()
                    print(f"{Fore.YELLOW}[Conversation reset]{Style.RESET_ALL}")
                    continue
                
                self.process_command(user_input)
                
            except KeyboardInterrupt:
                print(f"\n{Fore.CYAN}KentAI: Catch you later! 👋{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")


def main():
    """Main entry point"""
    # Check if Ollama is likely running
    import requests
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code != 200:
            print(f"{Fore.YELLOW}Warning: Ollama might not be running properly{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}⚠ Warning: Can't connect to Ollama!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Make sure Ollama is installed and running:{Style.RESET_ALL}")
        print("  1. Install: https://ollama.ai")
        print("  2. Run: ollama serve")
        print("  3. Pull a model: ollama pull llama2")
        print()
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return
    
    # Create and run KentAI
    kent = KentAI()
    kent.run_interactive()


if __name__ == "__main__":
    main()
