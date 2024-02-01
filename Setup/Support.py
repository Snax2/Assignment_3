import pygame
import os
from os import walk

def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = os.path.join(path, image)

            # Skip non-image files
            if not image.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue
            try:
                image_surface = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surface)
            except pygame.error as e:
                print(f"Error loading image: {full_path}, {e}")

    return surface_list
