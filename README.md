# Hello world hackathon

#### Setup Python virtual environment
```bash
$ virtualenv .venv
$ source .venv/bin/activate
```

#### Install fastmcp python package
```bash
$ pip install fastmcp
```

#### Configure Cline MCP Servers to call helloworld, please update the command path to the actual path of helloworld.sh
```json
{
  "mcpServers": {
    "hello-world": {
      "command": "/home/username/mcphelloworld/helloworld.sh",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

#### In Cline to test hello world please type in Cline
hello-world Hackathon
