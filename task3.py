import pyautogui
import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(image):
    # Apply dot product with the given weights for each channel
    gray_image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])
    return gray_image

def plot_image_with_grid(image):
    fig, ax = plt.subplots()
    ax.imshow(image)
    
    # Enable grid
    ax.grid(True)
    plt.show()

def crop_image(image, x_start, x_end, y_start, y_end):
    # Crop the image using numpy slicing
    return image[y_start:y_end, x_start:x_end]

def screenshot_and_process(x_start, x_end, y_start, y_end):
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    
    # Crop the image to the region of interest
    cropped_image = crop_image(screenshot_np, x_start, x_end, y_start, y_end)
    
    # Convert to greyscale
    gray_image = rgb2gray(cropped_image)
    
    return gray_image

x_start, x_end, y_start, y_end = 0, 400, 100, 600  # Example coordinates
gray_roi = screenshot_and_process(x_start, x_end, y_start, y_end)

# Display the greyscale region
plt.imshow(gray_roi, cmap='gray')
plt.show()
