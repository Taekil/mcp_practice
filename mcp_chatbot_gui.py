# MCP Chatbot GUI (Streamlit)
# Client Side

import streamlit as st
import json
import requests

# Load registry of tools
with open("mcp_registry.json") as f:
    registry = json.load(f)

def call_tool(tool_name, inputs):
    tool = next((t for t in registry if t["name"] == tool_name), None)
    if not tool:
        return {"error": f"Tool '{tool_name}' not found."}

    url = tool["server"] + tool["route"]
    try:
        response = requests.get(url, params=inputs)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

st.set_page_config(page_title="MCP Chatbot", page_icon="🤖")
st.title("🤖 MCP Chatbot GUI")

# Simulate basic chatbot logic (manual intent mapping for now)
user_input = st.text_input("Ask something:")

if user_input:
    if "weather" in user_input.lower():
        st.write("Detected intent: `get_weather`")
        city = st.text_input("Which city?", value="Seattle")
        if st.button("Submit"):
            result = call_tool("get_weather", {"city": city})
            st.write("**Result:**")
            st.json(result)
    else:
        st.write("Sorry, I don't understand yet. Try asking about the weather.")
