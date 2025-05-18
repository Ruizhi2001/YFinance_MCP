from smolagents import ToolCallingAgent, ToolCollection, LiteLLMModel

from mcp import StdioServerParameters

model = LiteLLMModel(model_id = "ollama_chat/qwen3:1.7b", num_ctx=8192)

server_params = StdioServerParameters(
    command = 'uv',
    args=['run', 'server.py'],
    env = None,
)

with ToolCollection.from_mcp(server_params, trust_remote_code=True) as tool_collection:
    # Define the tools to be used by the agent
    agent = ToolCallingAgent(tools=[*tool_collection.tools], model=model)
    agent.run("What was EBITDA for IBM?")
