from agent import Agent, Performer

global agents
agents = []

def setup():
  size(600, 600)
  for i in range(10):
    agents.append(Agent(random(width), random(100, height)))
  #separationSlider = createSlider(0, 5, 1, 0.1)
  #separationSlider.position(2, height-20)
  #maxForceSlider = createSlider(0.01, 1, 0.01, 0.01)
  #maxForceSlider.position(135, height-20)
  #fovSlider = createSlider(16, 128, 32, 1)
  #fovSlider.position(268, height-20)
  global performer
  global performerTarg

  performer = Performer(width/2, 50)
  performerTarg = PVector(random(0, width), 50)
  

def draw():
  background(0)
  noStroke()
  fill(255)
  #text('Separation', separationSlider.position().x, separationSlider.position().y-10)
  #text('Max Force', maxForceSlider.position().x, maxForceSlider.position().y-10)
  #text('FOV', fovSlider.position().x, maxForceSlider.position().y-10)
  text('Click to add more agents',2, 12)
  
  for i in range(len(agents)):
    force = agents[i].seek(performer.pos)
    agents[i].applyForce(force)
    agents[i].flock(agents)
    agents[i].show()
    agents[i].update()

  performerForce = performer.seek(performerTarg)
  performer.applyForce(performerForce)
  performer.show()
  performer.update()
  push()
  translate(performerTarg.x, performerTarg.y)
  ellipse(0, 0, 4, 4)
  noStroke()
  fill(0, 255, 0, 150)
  textSize(8)
  text('Performer Target', -30, -10)
  pop()

  if performer.pos.dist(performerTarg) < 60:
    global performerTarg
    performerTarg = PVector(random(0, width), 50)


def mousePressed():
  agents.append(Agent(mouseX, mouseY))
