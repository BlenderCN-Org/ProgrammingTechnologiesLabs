from bge import logic
from math import sin, cos
from mathutils import Vector
 
gravity_factor = 10
 
def jupiter_controller():
    controller = logic.getCurrentController()
    jupiter = controller.owner
    jupiter_position = jupiter.worldPosition
    
    angle = 0.001
    x = jupiter_position.x
    y = jupiter_position.y
    jupiter_position.x = x * cos(angle) + y * sin(angle)
    jupiter_position.y = -x * sin(angle) + y * cos(angle)


def voyager_controller():
    voyager = logic.getCurrentController().owner
    voyager.applyForce([50, -35, 0])
     
def world_controller():
    scene = logic.getCurrentScene()
    owner = logic.getCurrentController().owner
    
    
    voyager = scene.objects['Voyager']
    
    distance = owner.worldPosition - voyager.worldPosition
    if distance.magnitude == 0:
        return
    gravity = gravity_factor * owner.mass * voyager.mass / distance.magnitude ** 2
    distance.normalize()
    voyager.applyForce(distance * gravity)
  

