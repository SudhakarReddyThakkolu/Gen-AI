from mcp.server.fastmcp import FastMCP
from tools.add_note import add_notes
from tools.search_notes import search_notes

mcp = FastMCP("notes-server")

@mcp.tool()
def add_note_tool(text:str):
    """ Add notes"""
    return add_notes(text)

@mcp.tool()
def search_notes_tool(query:str):
    """Search notes"""
    return search_notes(query)

if __name__=="__main__":
    mcp.run()