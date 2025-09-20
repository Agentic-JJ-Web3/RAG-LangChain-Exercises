# Smart News AI Enhancer

This project is the result of Exercise 1 from the LangChain 3-Hour Exercise Guide. It is a Python application that fetches news articles from the NewsData.io API, enhances them with AI-generated insights using the Google Gemini API, and saves the results.

## Technologies Used

*   **Python:** The core programming language.
*   **LangChain:** The framework used to build the application, including the custom document loader and the AI enhancement chain.
*   **Google Gemini:** The Large Language Model (LLM) used for AI-powered text analysis.
*   **NewsData.io API:** The source for fetching news articles.
*   **Virtual Environment (`venv`):** To manage project dependencies in an isolated environment.
*   **Jupyter Notebooks:** For interactive testing and development.

## How to Test the Program

1.  **Clone the repository and navigate to the `smart_news` directory.**

2.  **Create and activate a Python virtual environment:**
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file** in the root of the `smart_news` directory and add your API keys:
    ```
    NEWS_API_KEY="your_newsdata_io_api_key"
    GOOGLE_API_KEY="your_google_api_key"
    ```

5.  **Run the main application:**
    ```bash
    python -m app.main
    ```

    This will execute the pipeline. Since the live news API often restricts content, the program currently uses a mock article. It will generate an `enhanced_news.json` file in the project's root directory.

6.  **(Optional) Explore the notebooks:** You can explore the Jupyter notebooks in the `notebooks/` directory to see the step-by-step testing process.
