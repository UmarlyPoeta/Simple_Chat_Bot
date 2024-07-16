import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self) -> None:
        # Create recognizer and mic instances
        self.recognizer = sr.Recognizer()
        try:
            self.microphone = sr.Microphone(device_index=1)
        except IOError:
            raise IOError("No available microphones")
        self.microphones_list = sr.Microphone.list_microphone_names()

    def set_audio(self, user_choice_microphone: str) -> str:
        """
        Reinitialize the Microphone instance with the user-chosen microphone.

        Args:
            user_choice_microphone (str): Name of the microphone chosen by the user.

        Returns:
            str: Confirmation message on successful microphone change.
        """
        try:
            microphone_index = self.microphones_list.index(user_choice_microphone)
        except ValueError:
            raise ValueError("Microphone name not in the available audio list")

        try:
            self.microphone = sr.Microphone(device_index=microphone_index)
        except IOError:
            raise IOError("Failed to initialize the microphone with the given index")

        return "Microphone change succeeded"

    def list_audios(self) -> list:
        """
        Provides all available microphones to the user as a list.

        Returns:
            list: List of available microphone names.
        """
        return self.microphones_list

    def recognize_speech(self) -> dict:
        """
        Transcribe speech recorded from the microphone.

        Returns:
            dict: A dictionary with keys:
                "success" (bool): Whether the API request was successful.
                "error" (str or None): Error message if an error occurred, otherwise None.
                "transcription" (str or None): Transcribed text if speech was recognized, otherwise None.
        """
        if not isinstance(self.recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be an instance of `Recognizer`")
        if not isinstance(self.microphone, sr.Microphone):
            raise TypeError("`microphone` must be an instance of `Microphone`")

        # Adjust the recognizer sensitivity to ambient noise and record audio from the microphone
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        # Set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # Try recognizing the speech in the recording
        try:
            response["transcription"] = self.recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # Speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response

