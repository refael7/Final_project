import speech_recognition as sr
import logging


class OcrEngine:
    def __init__(self,logger:logging.Logger):
        self.logger=logger
    def  extract_text(self,image_path):
        try:
            r = sr.Recognizer()
            with sr.AudioFile(image_path) as source:
                text = r.record(source)
            return text

        except Exception as e:
            self.logger.error(f"audio failed for {image_path}: {e}")
            raise

