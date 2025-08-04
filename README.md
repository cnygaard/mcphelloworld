# Hello world hackathon

# Setup Python virtual environment
virtualenv .venv
source .venv/bin/activate

# Install fastmcp python package
pip install fastmcp

# Configure Clint MCP Servers to call helloworld, please update the command path to the actual path of 
# helloworld.sh
{
  "mcpServers": {
    "hello-world": {
      "command": "/home/username/mcphelloworld/helloworld.sh",
      "disabled": false,
      "autoApprove": []
    }
  }
}

# In Cline to test hello world please type
hello-world Hackathon
