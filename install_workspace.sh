#!/bin/bash

# Genealogical DNA Analysis Workspace Installation Script
# Created: January 10, 2026

set -e  # Exit on error

echo "🧬 Setting up Genealogical DNA Analysis Workspace..."

# Create virtual environment
echo "1. Creating virtual environment..."
python3 -m venv genealogy_env
source genealogy_env/bin/activate

# Install Python dependencies
echo "2. Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Download reference data
echo "3. Downloading reference data..."
mkdir -p data/reference
cd data/reference

# Download ISOGG Y-DNA tree
echo "   Downloading ISOGG Y-DNA tree..."
if command -v wget &> /dev/null; then
    wget -q https://raw.githubusercontent.com/isogg/isogg.github.io/master/tree/Y_Tree_list.csv || echo "   Warning: Could not download ISOGG tree. Download manually from https://isogg.org/tree/"
else
    echo "   Warning: wget not found. Please download ISOGG tree manually from https://isogg.org/tree/"
fi

cd ../..

# Create database
echo "4. Creating database..."
python src/database/migrations.py || echo "   Warning: Database creation failed. Check dependencies."

# Run tests (if any exist)
echo "5. Running tests..."
if [ -f "tests/__init__.py" ]; then
    pytest tests/ || echo "   Warning: Some tests failed."
else
    echo "   No tests found. Skipping."
fi

echo ""
echo "✅ Workspace setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate virtual environment: source genealogy_env/bin/activate"
echo "2. Add your DNA data to data/raw/"
echo "3. Run the analysis pipeline: python pipeline.py"
echo "4. Start with notebooks: jupyter notebook notebooks/"
