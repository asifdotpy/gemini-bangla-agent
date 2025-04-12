# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines the root agent for the child conversation application."""

from google.adk.agents import Agent
from dotenv import load_dotenv
import os

# Assuming prompt.py is in the same directory or accessible via Python path
# If it's in the same directory, use: from .prompt import CHILD_CONVERSATION_PROMPT
# If it's in a parent directory or elsewhere, adjust the import accordingly.
# For this example, let's assume it's in the same directory:
from .prompt import CHILD_CONVERSATION_PROMPT

# Load environment variables from .env file
load_dotenv()

# It might be better to rename 'search_assistant' to something more descriptive
# like 'child_chat_assistant', but keeping it as requested for now.
root_agent = Agent(
    name="child_conversation_agent", # Renamed for clarity
    model=os.getenv("SELECTED_GEMINI_MODEL"),
    instruction=CHILD_CONVERSATION_PROMPT, # Use the imported prompt variable
    description="An AI assistant designed to converse playfully with young Bengali-speaking children.", # Updated description
)

# You might add other agents or tools here if needed later.
