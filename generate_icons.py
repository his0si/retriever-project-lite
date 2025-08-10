from PIL import Image
import os

source_image_path = r"D:\_Code\retriever-project\frontend\public\images\logo.png"
icons_dir = r"D:\_Code\retriever-project\frontend\public\icons"

os.makedirs(icons_dir, exist_ok=True)

sizes = [72, 96, 128, 144, 152, 192, 384, 512]

try:
    img = Image.open(source_image_path)
    
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    for size in sizes:
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        output_path = os.path.join(icons_dir, f'icon-{size}x{size}.png')
        resized_img.save(output_path, 'PNG')
        print(f'Created: icon-{size}x{size}.png')
    
    chat_icon = img.resize((96, 96), Image.Resampling.LANCZOS)
    chat_icon.save(os.path.join(icons_dir, 'chat-icon.png'), 'PNG')
    print('Created: chat-icon.png')
    
    crawl_icon = img.resize((96, 96), Image.Resampling.LANCZOS)
    crawl_icon.save(os.path.join(icons_dir, 'crawl-icon.png'), 'PNG')
    print('Created: crawl-icon.png')
    
    print('모든 아이콘 생성 완료!')
    
except Exception as e:
    print(f'에러 발생: {e}')
    print('기본 아이콘으로 복사합니다...')
    import shutil
    for size in sizes:
        shutil.copy(source_image_path, os.path.join(icons_dir, f'icon-{size}x{size}.png'))
        print(f'Copied: icon-{size}x{size}.png')
    shutil.copy(source_image_path, os.path.join(icons_dir, 'chat-icon.png'))
    shutil.copy(source_image_path, os.path.join(icons_dir, 'crawl-icon.png'))