from setuptools import setup

setup(name = "package_speech_recognizer",
version="0.1",
description="In this package you can find the easiest way to create a speech recogniser including background recognizing solution",
author="Ankit Biswas",
packages=['package_speech_recognizer'],
install_requires=['SpeechRecognition', 'gTTS', 'pyttsx3'],
)
