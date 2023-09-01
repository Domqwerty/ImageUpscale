import argparse
from PIL import Image
import os

def upscale_image(input_path, output_path, scale_factor):
    # Open the input image
    input_image = Image.open(input_path)
    
    # Calculate new dimensions after upscale
    new_width = int(input_image.width * scale_factor)
    new_height = int(input_image.height * scale_factor)
    
    # Perform image upscale using the Lanczos algorithm
    upscaled_image = input_image.resize((new_width, new_height), Image.LANCZOS)
    
    # Save the upscaled image
    upscaled_image.save(output_path)

def upscale_images_in_folder(input_folder, output_folder, scale_factor):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            upscale_image(input_path, output_path, scale_factor)

# If the script is being run as the command line
if __name__ == "__main__":

    # Create a command-line argument parser with a description.
    parser = argparse.ArgumentParser(description="Image Upscaler")
    parser.add_argument("--input_folder", required=True, help="Input folder path")
    parser.add_argument("--output_folder", required=True, help="Output folder path")
    parser.add_argument("--scale_factor", type=int, required=True, help="Scale factor")
    
    # Parse the command-line arguments and store them in the 'args' variable.
    args = parser.parse_args()
    
    # Pass the values of the command-line arguments to the upscale_images_in_folder() function.
    upscale_images_in_folder(args.input_folder, args.output_folder, args.scale_factor)
