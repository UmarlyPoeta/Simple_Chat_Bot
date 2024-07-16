## Chat Bot and Voice Recognition

This project combines a chat bot with voice recognition capabilities to create an interactive Q&A system. The chat bot can recognize speech input, find the best match for a given question from a knowledge base, and provide an appropriate response. Additionally, it can learn new responses from the user.

### Features

- **Speech Recognition:** Uses the `speech_recognition` library to convert spoken words into text.
- **Text-to-Speech:** Uses the `pyttsx3` library to convert text responses back into speech.
- **Knowledge Base:** Stores questions and answers in a JSON file.
- **Learning Capability:** Can learn new responses from the user and update the knowledge base.

### Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/YourUsername/chat_bot_voice_recognition.git
   cd chat_bot_voice_recognition
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

### Dependencies

- `speech_recognition`
- `pyttsx3`
- `json`
- `difflib`

You can install these dependencies using the following command:

```sh
pip install speechrecognition pyttsx3
```

### File Structure

```sh
chat_bot_voice_recognition/
│
├── voice_recognition.py   # Speech recognition module
├── chat_bot.py            # Main chat bot script
├── knowledge_base.json    # JSON file containing Q&A
└── README.md              # This README file
```

### Usage

1. **Setup the Knowledge Base:**

   Make sure `knowledge_base.json` is present in the root directory with the following structure:

   ```json
   {
       "questions": [
           {
               "question": "What is Python?",
               "answer": "Python is a high-level, interpreted programming language known for its readability and versatility."
           },
           {
               "question": "Who developed Python?",
               "answer": "Python was developed by Guido van Rossum and was first released in 1991."
           }
           // Add more questions and answers here
       ]
   }
   ```

2. **Run the Chat Bot:**

   ```sh
   python chat_bot.py
   ```

3. **Interact with the Chat Bot:**

   - Speak into your microphone when prompted.
   - The chat bot will recognize your speech, find the best match for your question in the knowledge base, and respond.
   - If the bot doesn't know the answer, it will ask you for the correct response and learn it.

### Code Explanation

#### voice_recognition.py

This module handles all speech recognition tasks. It initializes the recognizer and microphone, provides methods to list available microphones, set a specific microphone, and recognize speech.

#### chat_bot.py

This script loads the knowledge base, initializes the speech recognizer and text-to-speech engine, and contains the main loop for interacting with the user. It processes the user's speech input, finds the best match for their question, and responds appropriately. If the bot doesn't know the answer, it asks the user to provide it and updates the knowledge base accordingly.

### Example Knowledge Base

Here is an expanded example of `knowledge_base.json`:

```json
{
    "questions": [
        {
            "question": "What is Python?",
            "answer": "Python is a high-level, interpreted programming language known for its readability and versatility."
        },
        {
            "question": "Who developed Python?",
            "answer": "Python was developed by Guido van Rossum and was first released in 1991."
        },
        {
            "question": "What is a function in Python?",
            "answer": "A function in Python is a block of reusable code that performs a specific task."
        },
        {
            "question": "How do you define a function in Python?",
            "answer": "You define a function in Python using the 'def' keyword followed by the function name and parentheses."
        },
        {
            "question": "What is a list in Python?",
            "answer": "A list in Python is a collection of items that are ordered and changeable."
        },
        {
            "question": "How do you create a list in Python?",
            "answer": "You create a list in Python by placing comma-separated values inside square brackets, like this: my_list = [1, 2, 3, 4]."
        }
        // Add more questions and answers here
    ]
}
```

### Contributions

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License.

---

Feel free to customize and expand this README to better suit your project's needs.
