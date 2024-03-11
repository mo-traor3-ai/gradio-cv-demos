# gradio-cv-demos

Computer Vision model demos with Gradio interfaces.

The first example is a Gradio app for a Groundlight AI Detector.

## What is Groundlight?

Groundlight gives you the ability to answer questions about visual data (e.g images, or video feeds) using natural language queries. This allows you to create complex computer vision systems in just a few lines of Python code, the question that maps to your business value, and a stream of visual data.

### Example queries

1. *Use Case: Workplace Safety* - "Is the person in the image wearing both their hard hat and safety vest properly?"

2. *Use Case: Manufacturing Quality Assurance* - "Is there a warning label present on the product?"

3. *Use Case: Process Control & Safety* - "Is the machine control switch in the "Off" position?

4. *Use Case: Process Control* - "Are there two screws included in the packaging?

## Using the Groundlight Gradio Demo

1. Navigate to your chosen working directory.

2. Create and activate a virtual environment running a Python version between 3.8 and 3.12

Python 3.10 example (Linux):

```bash
python3.10 -m venv groundlight

source gradio/bin/activate
```

3. Install Gradio and Groundlight with PIP

```bash
pip install gradio
```

4. Run the App

```bash
python3 app.py
```

Click on the link that opens in your terminal, or copy and paste it in a browser window. The default link for the app is `http://127.0.0.1:7860` (running locally).

![Sample Terminal Output](/assets/terminal_output.png)

### Example Outputs

**Query: "Is the person in the image wearing both their hard hat and safety vest properly?"**

![Negative Example - Sample Query](/assets/app_example.png)

![Positive Example - Sample Query](/assets/app_example1.png)
