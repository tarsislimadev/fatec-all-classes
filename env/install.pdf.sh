#!/bin/bash

# Script to install tools for converting Markdown to PDF on Ubuntu/Debian
# This script installs Pandoc and a minimal LaTeX distribution.

echo "Updating package lists..."
sudo apt-get update

echo "Installing Pandoc and LaTeX dependencies..."
sudo apt-get install -y \
    pandoc \
    texlive-latex-base \
    texlive-fonts-recommended \
    dvipng \
    cm-super

echo "Installation complete. You can now convert .md files to .pdf using:"
echo "pandoc input.md -o output.pdf"
