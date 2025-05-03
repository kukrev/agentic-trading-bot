from langchain.tools import tool
from langchain_text_splitters import RecursiveCharacterTextSplitter
from lancedb.rerankers import LinearCombinationReranker
from langchain_community.vectorstores import LanceDB
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.polygon.financials import PolygonFinancials
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools.bing_search import BingSearchResults 
from data_models.models import RagToolSchema

@tool(args_schema=RagToolSchema)
def retriever_tool(question):
    """this is retriever tool"""
    return ""
@tool
def tavily_tool(question:str):
    """this is a tavily tool"""
    return TavilySearchResults(
        question,
        max_results=5,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True
        )
@tool
def create_polygon_tool():
    """this is polygon tool"""
    return PolygonFinancials(api_wrapper=PolygonAPIWrapper())
@tool
def create_bing_tool():
    """this is a bing tool"""
    return BingSearchResults()

def get_all_tools(question):
    return [
        retriever_tool(question),
        tavily_tool,
        create_polygon_tool,
        create_bing_tool
 ]
    
if __name__=='__main__':
    print(get_all_tools("myquestion"))