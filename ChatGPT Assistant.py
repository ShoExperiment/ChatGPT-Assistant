#MenuTitle: ChatGPT Assistant
# -*- coding: utf-8 -*-
__doc__="""
ChatGPT will assist you.
"""

import vanilla
import subprocess
import json

class ChatGPTInterface:

    def __init__(self):
        self.w = vanilla.FloatingWindow((400, 300), "ChatGPT Assistant")  # Adjusted window size

        self.w.promptLabel = vanilla.TextBox((10, 10, -10, 20), "Enter your prompt:")
        self.w.promptInput = vanilla.EditText((10, 30, -10, 20))
        self.w.runButton = vanilla.Button((10, 60, -10, 20), "Run", callback=self.runCallback)
        self.w.resultLabel = vanilla.TextBox((10, 90, -10, 60), "Response will appear here.")
        
        # Additional Retry button, initially hidden
        self.w.retryButton = vanilla.Button((10, 160, -10, 20), "Retry Code?", callback=self.retryCallback)
        self.w.retryButton.show(False)
        
        self.received_code = ""  # Placeholder to store received code

        self.w.open()

    def get_code_from_chatgpt(self, prompt):
        cmd = [
            'curl', '-X', 'POST', 'http://localhost:5000/chatgpt', 
            '-H', 'Content-Type: application/json', 
            '-d', json.dumps({"prompt": prompt})
        ]

        result = subprocess.check_output(cmd).decode('utf-8')
        response = json.loads(result)

        return response.get("response", "No response received.")
    
    def runCallback(self, sender):
        # Hide retry button initially
        self.w.retryButton.show(False)
        
        try:
            iterations = 3
            error_msg = None
            
            self.original_prompt = f"You are a great font engineer. Give me a simple and short Python3 script for Glyphs3 App. {self.w.promptInput.get()}"
            prompt = self.original_prompt

            while iterations > 0:
                full_response = self.get_code_from_chatgpt(prompt)
                self.original_response = full_response  # Store the original response

                # Extract the Python code from the response
                code_start = full_response.find("```python")
                code_end = full_response.find("```", code_start + 9)  # 9 is the length of "```python"
                if code_start != -1 and code_end != -1:
                    self.received_code = full_response[code_start + 9:code_end].strip()
                else:
                    self.received_code = ""

                # Check if code was received
                if not self.received_code:
                    self.w.resultLabel.set("No code received from ChatGPT.")
                    return

                # Execute the received code
                try:
                    exec(self.received_code)
                    self.w.resultLabel.set("Code executed successfully.")
                    return
                except Exception as e:
                    error_msg = f"Error executing code: {str(e)}"
                    self.w.resultLabel.set(error_msg)
                
                    # Show the retry button to the user
                    self.w.retryButton.show(True)
                    return

            # If we reach here, it means there was an error after 3 attempts or the user chose not to continue
            self.w.resultLabel.set(error_msg)
        except Exception as e:
            self.w.resultLabel.set(f"An error occurred: {str(e)}")

    def retryCallback(self, sender):
        # Logic for retrying the code generation
        self.w.retryButton.show(False)  # Hide the retry button after clicked
        prompt = f"The original prompt was: {self.original_prompt}\nThe response I got was: {self.original_response}\nBut the code you gave me did not work. please update the code for me. I just need the updated code and no explanation is needed."
        
        self.runCallback(None)  # Call the runCallback again

ChatGPTInterface()
