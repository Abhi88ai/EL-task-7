import os
from PIL import Image

# Folder paths
input_folder = "input_images"
output_folder = "output_images"

# Resize dimensions
new_width = 800
new_height = 600

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in input folder
for filename in os.listdir(input_folder):
    
    # Check image file extensions
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # Resize image
        resized_img = img.resize((new_width, new_height))
        
        # Convert to JPEG format
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path, "JPEG")
        
        print(f"Resized and saved: {filename}")

print("All images processed successfully!")