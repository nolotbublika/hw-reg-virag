import re


def extract_image_links(html_text):
    metka = re.compile(r'<img src=[\'"](https?://[^\'"]+)')
    image_links = metka.findall(html_text)
    return image_links


sample_html = ("<img src='https://example.com/image1.jpg'> <img "
               "src='http://example.com/image2.png'> <img "
               "src='https://example.com/image3.gif'>")

image_links = extract_image_links(sample_html)
if image_links:
    for image_links in image_links:
        print(image_links)
else:
    print("Нет ссылок с картинками в HTML тексте.")
