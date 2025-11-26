import pygame as pg
import numpy as np

from object_3D import Object3D

class SoftwareRenderer():
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
    
    def draw(self):
        self.screen.fill(pg.Color('PeachPuff'))
        for face in self.obj.faces:
            points = [self.obj.project(self.obj.vertexes[i]) for i in face]
            pg.draw.polygon(self.screen, pg.Color('Brown'), points, 10)
        self.obj.rotate_y(np.radians(2))
        self.obj.rotate_x(np.radians(1.5))
        
    def run(self):
        while True:
            self.draw()
            [exit() for e in pg.event.get() if e.type == pg.QUIT]
            pg.display.set_caption(f"{self.clock.get_fps()} FPS")
            pg.display.flip()
            self.clock.tick(self.FPS)
            

if __name__ == '__main__':
    app = SoftwareRenderer()
    app.obj = Object3D(app)
    app.run()