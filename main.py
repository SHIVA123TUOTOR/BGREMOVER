import requests

API_KEY = "FRZPYZmMn895ZCh5GoctrSqK"
input_image_path = "input.jpg"
output_image_path = "output.png"

with open(input_image_path, "rb") as image_file:
    response = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": image_file},
        data={"size": "auto"},
        headers={"X-Api-Key": API_KEY}
    )

if response.status_code == 200:
    with open(output_image_path, "wb") as out:
        out.write(response.content)
    print("? Background removed!")
else:
    print("? Error:", response.text)
