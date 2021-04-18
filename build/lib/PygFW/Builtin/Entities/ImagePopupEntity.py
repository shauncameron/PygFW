from PygFW.Entity import Entity
from PygFW.Event import Eventifies

class ImagePopupEntity(Entity):

    def __init__(self, scene, image, spawn, initial_opacity=255, fade_ferocity=2, justify_existence=True):


        Entity.__init__(self, scene, spawn=spawn)

        self.image = image
        self.justify_existence = justify_existence

        self.opacity = initial_opacity
        self.fade_ferocity=fade_ferocity

    def draw(self):

        self.opacity -= self.fade_ferocity
        self.image.fade(self.opacity)

        self.image.draw(self.scene.engine_surface.pygame_surface, self.relative_position)

        if self.justify_existence:

            if self.opacity <= 0:

                @Eventifies(scene=self.scene, listener=None)
                def remove_self(scene, event):
                    scene.entities.remove(scene.entities.get_tag(self), True)

                self.scene.engine_surface.single_events.add(remove_self)


