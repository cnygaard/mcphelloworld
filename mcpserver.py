from fastmcp import FastMCP

mcp = FastMCP("Hello World! 😊🚀")

@mcp.tool
def hello_hackathon(name: str) -> str:
    return(f"Hello World! 😊🚀 {name}")

if __name__ == "__main__":
    mcp.run()