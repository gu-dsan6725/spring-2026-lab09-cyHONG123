1. In original code, the user_id, agent_id, and run_id should be diverse info for each memory stored for comprehensive search for LLM agent. Unfortunately, seems MEM0 update the extraction api, making such divese metadata not working. agent_id should be name for llm model to search for cross conversation memory, and run_id should be a in-conversation search factor used by ai. Yet both are not functioning for inserting or searching at all. The only filter factor seems works is user_id, which record agent user name info.

2. There are several categories of data be stored, including technology, professional details and personal details. The data stored is reasonable since the question is about personal info, profession and data science knowledge.

3. In this test, agent use insert tool in almost every question asked. But in other test experience, there is less insert happened. The probability of agent using tool is highly depend on system prompt since i try several other prompt. And the agent can basiclly answer all question without reading the memory at least in this test.

4. Only turn one. It use the tool and code print out that use.

5. The agent.py is build base on anthropic provided model and mem0 framework. The framework allow tool call generaetion and apply tool call on local by using mem0 api to extract or insert info. The mem0 also contain a temporary memory structure which allow model to recall previous conversation without calling tool. Making ONE session agent memory possible.