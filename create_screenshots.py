from PIL import Image, ImageDraw, ImageFont
import os

screenshots_dir = r"D:\_Code\retriever-project\frontend\public\screenshots"
os.makedirs(screenshots_dir, exist_ok=True)

def create_screenshot(title, filename, bg_color=(255, 255, 255)):
    img = Image.new('RGB', (1280, 720), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 48)
        small_font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    text_color = (0, 0, 0) if bg_color == (255, 255, 255) else (255, 255, 255)
    
    draw.text((640, 300), title, font=font, anchor="mm", fill=text_color)
    draw.text((640, 400), "Retriever Project", font=small_font, anchor="mm", fill=text_color)
    
    img.save(os.path.join(screenshots_dir, filename))
    print(f"Created: {filename}")

create_screenshot("홈 화면", "screenshot1.png")
create_screenshot("채팅 화면", "screenshot2.png", bg_color=(240, 240, 240))

print("스크린샷 생성 완료!")