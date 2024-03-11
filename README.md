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

## Launching the Groundlight Gradio Demo

1. Navigate to your chosen working directory.

2. Create and activate a virtual environment running a Python version between 3.8 and 3.12

Python 3.10 example (Linux):

```bash
python3.10 -m venv groundlight

source groundlight/bin/activate
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

### How to Use the Interface

1. Enter your `Groundlight API Token` ([Create your Groundlight Account](https://app.groundlight.ai) --> [Navigate to API Tokens](https://app.groundlight.ai/reef/my-account/api-tokens) under your username --> Paste your API token in the Gradio app)
2. Enter Image & Text-Based Inputs
    * **`Detector Name`**: Create a name for your detector. Example: `ppe`
    * **`Upload Image`:** Click on 'Upload Image' to choose an image file to submit to your Groundlight detector.
    * **`Detector Query`** Type in your detector query (e.g the question that maps to your business value).
3. **Adjust Parameters:**
    * **`Wait Time`:** Slider to set how long to poll your detector (in seconds) for a confident answer. This is a client-side timeout.
    * **`Patience Time`:** Slider to set how long to wait (in seconds) for a confident answer for this image query..
    * **`Confidence Threshold`:** Slider to set the minimum confidence threshold for ML detection results.
    * **`Human Review`:** Dropdown menu to select whether to send the image for human query (human-in-the-loop verification), regardless of ML result.
4. **View Results:** Your detector will output the query result (e.g "YES", "NO") and the query confidence (%) for the submitted image.

![Sample Terminal Output](/assets/terminal_output.png)

* Sample terminal output when running the app

#### Example Usage

*Detector Query: "Is the person in the image wearing both their hard hat and safety vest properly?"*

![Negative Example - Sample Query](/assets/app_example.png)

![Positive Example - Sample Query](/assets/app_example1.png)
