from core import generate_caption
import gradio as gr
import os


def image_mod(image, N):
  captions = generate_caption().run(image, N)
  captions = [caption.replace("\n", "") for caption in captions]
  captions = '\n'.join([f"- {caption}" for caption in captions])
  return captions


demo = gr.Interface(
    image_mod,
    inputs=[gr.Image(type="pil"), gr.Slider(1, 10, value=5, step = 1, label="Caption count", info="Choose between 1 and 10")],
    outputs="text",
)

if __name__ == "__main__":
    demo.launch()
