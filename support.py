import pygame
from os import walk

def import_folder(path):
    surface_list = []

    for information in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
        print(information)

    return surface_list