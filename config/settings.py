"""
RedCell Configuration Settings
DO NOT commit real API keys to public repositories
"""

# =========================
# Grok (xAI) API Settings
# =========================

GROK_API_KEY = "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"

# Recommended model (can change later)
GROK_MODEL = "grok-2"

# Grok Chat Completion API endpoint
GROK_API_URL = "https://api.x.ai/v1/chat/completions"


# =========================
# RedCell General Settings
# =========================

# Enable or disable AI explanations
ENABLE_GROK = True

# Safety mode (blocks exploit actions later)
SAFE_MODE = True

# Application name
APP_NAME = "RedCell"

# Version
VERSION = "0.1.0"
