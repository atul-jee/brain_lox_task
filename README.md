# Codebasics Q&A 🌱

This repository contains a Flask application for a question-answering (QA) system based on a custom knowledge base. The knowledge base is created from documents loaded from a specified URL and is used to answer user queries.

## Features

- Load data from a specified URL and create a knowledge base.
- Use FAISS for vector-based retrieval of document embeddings.
- Utilize Google Palm as the language model for answering questions.
- Expose endpoints to create the knowledge base and ask questions via a Flask API.

## Requirements

- Python 3.10+
- [Google Palm API key](https://cloud.google.com/natural-language)
- Hugging Face `InstructorEmbeddings` model
- Flask
- FAISS
