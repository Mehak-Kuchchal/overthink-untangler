# Overthink Untangler

A small Python app that helps overthinkers calm down. You type the thought
that keeps looping, and an open-source AI model replies with:
1. Feeling: a kind sentence
2. What is in my control
3. What is not in my control
4. One small step for the next 10 minutes
5. A short breathing exercise

## How to run
1. Create an API key at ollama.com
2. Save it: setx OLLAMA_API_KEY "your_key"
3. pip install ollama
4. python untangler.py

## Important
This is a relaxation helper, not therapy or medical advice.
Messages are sent to Ollama's cloud, so do not type private information.
