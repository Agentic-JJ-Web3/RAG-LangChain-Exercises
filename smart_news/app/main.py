import json
from config.settings import GOOGLE_API_KEY
from app.ai_enhancer import enhance_article

def main():
    """Main function to run the news enhancement pipeline with a mock article."""
    
    mock_article_content = (
        "After years of development, the new Artemis rocket is set to launch next month, "
        "marking a new era in lunar exploration. The mission's primary goal is to establish a sustainable "
        "presence on the Moon, which will serve as a stepping stone for future missions to Mars. "
        "Scientists are hopeful that the data collected will unlock new insights into the formation of our solar system."
    )
    mock_article_metadata = {
        "title": "Artemis Rocket Set for Historic Lunar Launch",
        "link": "https://example.com/artemis-launch",
        "source": "space-news-inc",
        "publish_date": "2025-09-20",
    }

    print("Enhancing mock article...")
    try:
        enhancement = enhance_article(mock_article_content, GOOGLE_API_KEY)
        
        enhanced_article = {
            "original_article": mock_article_metadata,
            "ai_enhancement": enhancement
        }
        
        with open("enhanced_news.json", "w", encoding="utf-8") as f:
            json.dump([enhanced_article], f, indent=4, ensure_ascii=False)
            
        print("Successfully saved enhanced mock article to enhanced_news.json")

    except Exception as e:
        print(f"Could not enhance article: {e}")

if __name__ == "__main__":
    main()