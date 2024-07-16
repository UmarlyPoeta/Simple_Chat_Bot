import json
from difflib import get_close_matches
from voice_recognition import SpeechRecognizer
import pyttsx3

EXIT_VALUES = ("quit", "cancel", "exit")


def load_knowledge_base(filepath: str) -> dict:
    with open(filepath, "r") as file:
        data = json.load(file)
    return data


def save_knowledge_base(filepath: str, data: dict):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None


def main():
    knowledge_base = load_knowledge_base("knowledge_base.json")
    speech_recognizer = SpeechRecognizer()
    voice = pyttsx3.init()
    
    while True:
        try:
            voice.say("Ask your question")
            voice.runAndWait()
            response = speech_recognizer.recognize_speech()
            user_input = response.get("transcription")
            if not user_input:
                raise ValueError("No transcription found")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")
            continue
        
        if user_input.lower() in EXIT_VALUES:
            break
        
        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            if answer:
                voice.say(answer)
                voice.runAndWait()
            else:
                voice.say("I don't know the answer to that question.")
                voice.runAndWait()
        else:
            voice.say("I don't know the answer. Can you tell me what I should say in response?")
            voice.runAndWait()
            try:
                new_answer_response = speech_recognizer.recognize_speech()
            except:
                continue
            new_answer = new_answer_response.get("transcription") if new_answer_response else None

            if new_answer:
                voice.say(f"Is this your answer: {new_answer}?")
                voice.runAndWait()
                yes_or_no_response = speech_recognizer.recognize_speech()
                yes_or_no = yes_or_no_response.get("transcription").lower() if yes_or_no_response else None

                if yes_or_no == "yes":
                    knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                    save_knowledge_base("knowledge_base.json", knowledge_base)
                    voice.say("Thank you! I learned a new response.")
                    voice.runAndWait()
                else:
                    voice.say("Okay, I'll try better next time.")
                    voice.runAndWait()
            else:
                voice.say("I didn't catch that. Could you repeat it?")
                voice.runAndWait()

if __name__ == "__main__":
    main()
