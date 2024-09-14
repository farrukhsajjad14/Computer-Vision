import cv2

# Load the image from the file path
image = cv2.imread('path_to_your_image.jpg')

# Check if the image was loaded correctly
if image is None:
    print("Error: Unable to load image.")
else:
    # Display the image in a window
    cv2.imshow('Loaded Image', image)

    # Wait for a key press and close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
