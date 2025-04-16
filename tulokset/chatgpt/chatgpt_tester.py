

from openai import OpenAI

client = OpenAI(api_key = OPENAI_API_KEY)

prompt_txt = "Describe this image"
img_Url = "https://github.com/kaski2/AIkandikuvat/blob/main/kuvatEnglanti/E_IMG6PEOPLE.jpg?raw=true"
img_Name = "IMG6PEOPLE"

response = client.responses.create(
    model = "gpt-4o",
    input = [{
        "role": "user",
        "content": [
            {"type": "input_text", "text": prompt_txt},
            {
                "type": "input_image",
                "image_url": img_Url,
            },
        ],
    }],
)

print(response.output_text)

print(img_Name)
print("prompt:" + prompt_txt)
