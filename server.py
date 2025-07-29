import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/zyla-labs-zyla-labs-default/api/concert-finder-api'

mcp = FastMCP('concert-finder-api')

@mcp.tool()
def concerts_by_location(country: Annotated[str, Field(description='')],
                         minDate: Annotated[str, Field(description='')]) -> dict: 
    '''To use this endpoint, you need to specify the name of a country in the required parameter. Additionally, there is an optional parameter where you can provide a date to filter concert information. Note: The specified date serves as the starting point for the search, returning details about concerts scheduled from that day onward.'''
    url = 'https://concert-finder-api.p.rapidapi.com/concerts%2Bby%2Bcountry'
    headers = {'x-rapidapi-host': 'concert-finder-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'minDate': minDate,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def find_concerts_by_artist(name: Annotated[str, Field(description='')]) -> dict: 
    '''Retrieve a list of upcoming events for any artist of your choice. Simply provide the artist's name and get detailed information about their scheduled performances.'''
    url = 'https://concert-finder-api.p.rapidapi.com/get%2Bconcerts%2Bby%2Bartist'
    headers = {'x-rapidapi-host': 'concert-finder-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
