from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class ArticleEnhancement(BaseModel):
    summary: str = Field(description="A concise summary of the article in no more than 2 sentences.")
    sentiment: str = Field(description="The sentiment of the article (positive, negative, or neutral).")
    topics: List[str] = Field(description="A list of 3-5 key topics discussed in the article.")
    credibility: str = Field(description="A brief assessment of the article's credibility.")

def enhance_article(article_content: str, api_key: str) -> dict:
    """Enhances a news article with AI-generated insights."""
    
    # Set up a parser + inject instructions into the prompt template.
    parser = JsonOutputParser(pydantic_object=ArticleEnhancement)

    prompt = PromptTemplate(
        template="Analyze the following news article and provide the requested information.\n{format_instructions}\nArticle:\n{article}\n",
        input_variables=["article"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    # Initialize the Gemini model
    model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key, temperature=0)

    # Create the chain
    chain = prompt | model | parser

    # Invoke the chain with the article content
    return chain.invoke({"article": article_content})
