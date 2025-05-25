# Simple Question and Answer App

A lightweight web application that allows users to ask questions and receive answers in real time.

## Features

- Submit questions and get instant answers
- Clean and intuitive user interface
- Responsive design for desktop and mobile

### Running the App

```bash
streamlit run main.py
```

The app will be available at `http://localhost:8501`.


### Command to run it as a docker container

```bash
docker run -d --name simple_qa_bot -e GROQ_API_KEY=GROQ_API_KEY -p 8001:8501 gopinath1723/conversational_bot:v1
```