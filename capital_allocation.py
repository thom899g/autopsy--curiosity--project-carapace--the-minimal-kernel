"""
Project Carapace: The Minimal Kernel - Capital Allocation System
Fixed version with robust error handling and Firebase integration
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from decimal import Decimal
from typing import List, Optional, Dict, Any
from dataclasses import dataclass, field, asdict
import json
import logging
from logging.handlers import RotatingFileHandler

# Firebase imports with conditional handling
try:
    import firebase_admin