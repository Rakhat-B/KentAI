#!/bin/bash
# Setup script for KentAI

echo "🤖 Setting up KentAI..."
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version || { echo "Error: Python 3 is required"; exit 1; }

# Install dependencies
echo ""
echo "Installing Python dependencies..."
pip install -r requirements.txt || { echo "Error: Failed to install dependencies"; exit 1; }

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "Creating .env file..."
    cp .env.example .env
    echo "✓ Created .env - customize it for your system"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Install Ollama: https://ollama.ai"
echo "2. Run: ollama serve"
echo "3. Pull a model: ollama pull llama2"
echo "4. (Optional) Edit .env to customize app paths"
echo "5. Run KentAI: python kent.py"
echo ""
echo "Or try the demo without Ollama:"
echo "  python demo.py"
