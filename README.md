# Unclip

A straightforward, lightweight Python script that sits in the background and cleans up your clipboard. It intercepts URLs to strip aggressive tracking parameters (like `utm_*` and `fbclid`) and fixes messy multi-line spacing when copying text.

## Why it exists

We copy and paste links constantly. Most of those links come bloated with trackers that look messy when shared and compromise basic privacy. On top of that, copying text from PDFs or certain web layouts often introduces broken paragraphs and weird line breaks. 

Unclip runs a quiet loop in your environment. If it catches a link or text block that needs fixing, it cleans it instantly. You just paste clean data.

## Key Features

* **Zero-Effort Cleaning:** Monitors your clipboard dynamically. If you copy a messy text or link, it updates the clipboard contents in less than half a second.
* **Aggressive Parameter Stripping:** Automatically removes tracking junk including `utm_source`, `utm_medium`, `utm_campaign`, `fbclid`, `gclid`, and Spotify's tracking ID (`si`).
* **Format Fixing:** Cleans up weird multi-line spacing glitches while maintaining intentional paragraph breaks.
* **Zero Overhead:** No heavy GUI, no bloated frameworks—just raw Python and a single lightweight library.

## Tech Stack

* **Language:** Python 3.x
* **Libraries:** `pyperclip` (cross-platform clipboard management)
* **Standard Core Modules:** `urllib.parse` for strict, safe URL rebuilding.

## Quick Start

### Option A: Local Setup (Recommended)

1. Clone or download this repository.
2. Install the single required dependency:
   ```bash
   pip install -r requirements.txt
   1. Run the script:
       python main.py

### Option B: Cloud-Based Testing (GitHub Codespaces)

If you just want to see how the logic handles formatting strings before running it on your machine:

Click the green Code button on this repository.

Select the Codespaces tab and click Create codespace on main.

Once the environment loads, run pip install -r requirements.txt followed by python main.py inside the integrated terminal.

Note: Since cloud environments lack a native local desktop clipboard, it will simulate actions within the container interface.

## Project Structure
```bash
├── .github/
│   └── workflows/
│       └── ci.yml          # Basic syntax and quality checks
├── .gitignore              # Keeps your env files out of source control
├── README.md               # This documentation
├── main.py                 # Main application logic
└── requirements.txt        # Dependency manifest
```
## Roadmap
[ ] Add a native tray icon for quick toggling and background process control.

[ ] Implement a local config file to let users define custom string rules or custom parameter blacklists.

[ ] Bundle into a standalone executable (PyInstaller) for direct distribution.
