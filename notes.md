Notes — Crypto Wallet Tracker

Overview

This is a lightweight Python project for checking Ethereum wallet balances using a public API.
The goal is to keep the structure simple but clean, with a layout that can be easily extended.

Current Structure

- "tracker.py" — main script (handles user input and API requests)
- "config.py" — configuration (API base URL, timeouts, debug mode)
- "utils.py" — helper functions (validation, formatting, conversions)
- "requirements.txt" — dependencies
- ".gitignore" — excludes unnecessary/local files

Features

- Validate Ethereum wallet address
- Fetch balance from BlockCypher API
- Convert Wei → ETH
- Format output for readability
- Basic error handling

Notes / Decisions

- Using public API for simplicity (no API key required)
- Config separated for scalability
- Utils extracted to avoid clutter in main logic
- Minimal dependencies (only "requests")

Possible Improvements

- Add support for multiple networks (BTC, BSC, etc.)
- Integrate Web3 (Infura / Alchemy)
- Add CLI arguments instead of input()
- Logging instead of print()
- Dockerize the project
- Build simple REST API on top

Dev Notes

- This repo is intentionally simple but structured
- Designed as a base for further crypto / Web3 tools
- Can be extended into automation or analytics service

Changelog

- Init project
- Added config system
- Added utils module
- Refactored project structure
