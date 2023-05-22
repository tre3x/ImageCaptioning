from core import generate_caption
import gradio as gr
import os


def image_mod(image):
    captions = generate_caption().run(image)
    return captions


demo = gr.Interface(
    image_mod,
    inputs=gr.Image(type="pil"),
    outputs="text",
)

if __name__ == "__main__":
    demo.launch()
