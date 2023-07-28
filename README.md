# ChatGPT Assistant.py (A ChatGPT assistant for Glyphs App)

This is a ChatGPT assistant for Glyphs App.
Basically, it writes Python code according to your prompt and runs it.

I highly recommend you to save your current Glyphs file before running it.
At this moment, if you ask a simple task to ChatGPT you would get the code in fifty percent.


#How to use

It requires running Flask server and then access to the server from Terminal with "curl" command.
ChatGPT Assistant.py use "subprocess" so that it is possible to send commands and get feedback from Terminal.

Install OpenAI library and Flask
```
pip install openai
pip install Flask
```

Edit flask_server.py and set your API key
```
openai.api_key = ""
```

Run Terminal and move to the folder in which your flask_server.py is located.
Run the Flask server.
```
python flask_server.py  
```

Place your ChatGPT Assistant.py in your script folder of Glyphs 3 App. 



## License

Copyright (c) 2023 Shotaro Nakano
Released under the MIT license
https://opensource.org/licenses/mit-license.php
