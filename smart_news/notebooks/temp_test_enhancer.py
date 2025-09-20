import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import GOOGLE_API_KEY
from app.ai_enhancer import enhance_article

# A mock news article for testing
mock_article = (
    "After years of development, the new Artemis rocket is set to launch next month, "
    "marking a new era in lunar exploration. The mission's primary goal is to establish a sustainable "
    "presence on the Moon, which will serve as a stepping stone for future missions to Mars. "
    "Scientists are hopeful that the data collected will unlock new insights into the formation of our solar system."
)

enhancement = enhance_article(mock_article, GOOGLE_API_KEY)
print(enhancement)