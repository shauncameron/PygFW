import pygame

def Screenshot(surface, image_path, position = (0, 0), size = (1960, 1080)):

    print(f'PygFW >> Attempting to save an image to path:\n    \'{image_path}\'')

    image = pygame.Surface(size)
    image.blit(surface, (0, 0), (position, size))
    pygame.image.save(surface, image_path)