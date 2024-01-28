import cv2
import os
import glob

input_folder = 'raw'
output_folder = 'output'

extensions = ["*.jpeg", "*.jpg", "*.png","*.JPG","*.JPEG","*.PNG","*.webp"]

def convert_images_in_folder(input_base, output_base):
    processed_files = 0
    skipped_files = 0
    
    for extension in extensions:
        for img_file in glob.glob(os.path.join(input_base, '**', extension), recursive=True):
            img = cv2.imread(img_file)
            
            if img is None:
                print(f"Skipped file (image read failed): {img_file}")
                skipped_files += 1
                continue

            relative_path = os.path.relpath(img_file, input_base)
            webp_file_path = os.path.join(output_base, os.path.splitext(relative_path)[0] + '.webp')

            os.makedirs(os.path.dirname(webp_file_path), exist_ok=True)

            cv2.imwrite(webp_file_path, img, [int(cv2.IMWRITE_WEBP_QUALITY), 60])
            processed_files += 1

    print(f"Processed files: {processed_files}")
    print(f"Skipped files: {skipped_files}")

convert_images_in_folder(input_folder, output_folder)

print("Dönüşüm tamamlandı.")
