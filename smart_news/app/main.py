import json
from config.settings import NEWS_API_KEY, GOOGLE_API_KEY
from app.news_loader import NewsLoader
from app.ai_enhancer import enhance_article

def main():
    """Main function to run the news enhancement pipeline."""
    
    # 1. Load news articles
    print("Loading news articles...")
    loader = NewsLoader(api_key=NEWS_API_KEY, query="world news")
    documents = loader.load()
    print(f"Loaded {len(documents)} articles.")

    enhanced_articles = []
    for doc in documents:
        print(f"Enhancing article: {doc.metadata['title']}")
        article_content = doc.page_content
        
        if article_content and article_content != 'ONLY AVAILABLE IN PAID PLANS':
            # 2. Enhance the article
            try:
                enhancement = enhance_article(article_content, GOOGLE_API_KEY)
                
                # 3. Combine original data with enhancement
                enhanced_article = {
                    "original_article": doc.metadata,
                    "ai_enhancement": enhancement
                }
                enhanced_articles.append(enhanced_article)
                print("Enhancement successful.")
            except Exception as e:
                print(f"Could not enhance article: {e}")
        else:
            print("Skipping article with no content.")

    # 4. Save the results to a JSON file
    if enhanced_articles:
        with open("enhanced_news.json", "w", encoding="utf-8") as f:
            json.dump(enhanced_articles, f, indent=4, ensure_ascii=False)
        print(f"Successfully saved {len(enhanced_articles)} enhanced articles to enhanced_news.json")
    else:
        print("No articles were enhanced.")

if __name__ == "__main__":
    main()
