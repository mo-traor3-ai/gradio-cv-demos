from groundlight import Groundlight
from PIL.Image import Image
import gradio as gr


def detection_query(GROUNDLIGHT_TOKEN: str, det_name: str, pil_img: Image, det_query: str,
                    conf_threshold: float, wait_sec: float, patience_sec: float, human_review: str):
    
    # this variable is useful after setting a system environment variable for GROUNDLIGHT_PPE
    # GROUNDLIGHT_TOKEN is your Groundlight API key (accessible in "Api tokens")
    # GROUNDLIGHT_TOKEN = os.environ.get('GROUNDLIGHT_PPE')

    gl = Groundlight(api_token=GROUNDLIGHT_TOKEN)

    detector = gl.get_or_create_detector(
        name=det_name,#example: ppe
        query=det_query,
        confidence_threshold=conf_threshold#example: 0.7
        )

    image_query = gl.submit_image_query(
        detector=detector,
        image=pil_img,
        wait=wait_sec,#example: 10.0
        patience_time=patience_sec,#example: 10.0
        confidence_threshold=conf_threshold,#example: 0.7
        human_review=human_review#ALWAYS or NEVER
        )

    result_label = image_query.result.label
    result_confidence = f"{image_query.result.confidence:.2%}"
    print(f"\n** The answer is {result_label} | Query confidence = {result_confidence}")

    return result_label, result_confidence


interface = gr.Interface(
    fn=detection_query,
    inputs=[
        gr.Textbox(max_lines=1, label="Groundlight API Token", info="Create/access token: https://app.groundlight.ai/reef/my-account/api-tokens",
                   show_label=True, type="password"),
        gr.Textbox(max_lines=1, label="Detector Name", info="Example: ppe", show_label=True, type="text"),
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(value="Is the person in the image wearing both their hard hat and safety vest properly?",
                   info="What you'd like your model to answer", lines=2, max_lines=4, label="Detector Query", show_label=True),
        gr.Slider(minimum=0.10, maximum=0.99, value=0.70, step=0.01, label="Confidence Threshold",
                  info="Confidence threshold for ML detection results."),
        gr.Slider(minimum=1.0, maximum=60.0, value=10.0, step=1.0, label="Wait Time (seconds)",
                  info="How long to poll (in seconds) for a confident answer. This is a client-side timeout."),
        gr.Slider(minimum=1.0, maximum=60.0, value=10.0, step=1.0, label="Patience Time (seconds)",
                  info="How long to wait (in seconds) for a confident answer for this image query."),
        gr.Dropdown(choices=["ALWAYS", "NEVER"], value="ALWAYS", type="value", multiselect=False, label="Human Review for Query Results?",
                    info="Whether to send the image for human query (human-in-the-loop verification), regardless of ML result.")
    ],
    outputs=[gr.Textbox(max_lines=1, label="Query Result (Label)", info="The answer to your image query (for the submitted image).",
                        show_label=True, interactive=False, type="text", show_copy_button=True),
             gr.Textbox(max_lines=1, label="Query Result (Confidence)",  info="The confidence for your query result (for the submitted image).",
                        show_label=True, interactive=False, type="text", show_copy_button=True)
    ],
    title="Groundlight Python SDK: Single Image Detection Queries",
    description="Computer Vision powered by Natural Language. Groundlight makes it simple to build reliable visual applications."
)


if __name__ == "__main__":
    interface.launch()
