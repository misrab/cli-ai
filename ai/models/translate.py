from transformers import pipeline
from transformers.utils import logging

import warnings

# model_name = "google/t5-base"
model_name = "google-t5/t5-small"

# Suppress FutureWarning messages from the transformers library
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers")

# disable logging, doens't work but keeping it in case
logging.set_verbosity_error()

translator = pipeline("translation_en_to_fr", model=model_name, device=0)


def translate(text: str) -> str:
    result = translator(text)
    # print(result)
    return translator(text)[0]['translation_text']