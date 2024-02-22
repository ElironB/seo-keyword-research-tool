from fastapi import FastAPI, Query
from SeoKeywordResearch import SeoKeywordResearch



main  = FastAPI()

@main.get("/seo-keyword-research/")
async def seo_keyword_research(
  query: str = Query(...),serper_api_key: str = Query(...)
):
    keyword_research = SeoKeywordResearch(
        query=query,
        api_key=serper_api_key,
        lang='en',
        country='us',
        domain='google.com'
    )

    auto_complete_results = keyword_research.get_auto_complete()
    related_searches_results = keyword_research.get_related_searches()
    related_questions_results = keyword_research.get_related_questions()

    data = {
        'auto_complete': auto_complete_results,
        'related_searches': related_searches_results,
        'related_questions': related_questions_results
    }
    keyword_research.print_data(data)
    return data
