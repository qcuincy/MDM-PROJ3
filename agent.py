class Agent(object):
  def __init__(self, x, y):
    self.pos = PVector(x, y)
    self.vel = PVector.random2D()
    self.acc = PVector(0, 0)
    self.maxSpeed = 5
    self.maxForce = 0.1
    self.r = 4
    self.fov = 64
    self.sScale = 2

  
  def separation(self,agents):
    count = 0;
    avgPos = PVector()
    for i in range(len(agents)):
      d = self.pos.dist(agents[i].pos)
      if d <= self.fov and agents[i] != self:
        diff = PVector.sub(self.pos, agents[i].pos)
        if d != 0:
          diff.div(d)
        avgPos.add(diff)
        count+=1

    if count > 0:
      avgPos.div(count)
      avgPos.setMag(self.maxSpeed)
      avgPos.sub(self.vel)
      avgPos.limit(self.maxForce)

    return avgPos
  
  def applyForce(self,force):
    self.acc.add(force)
  
  def flock(self,agents):
    separation = self.separation(agents)
    separation.mult(self.sScale)
    self.acc.add(separation)
   
  def seek(self,targetPos):
    #v = PVector(targetPos)
    #print(v)
    d = targetPos.dist(self.pos)
    force = PVector.sub(targetPos, self.pos)
    force.setMag(self.maxSpeed)
    force.sub(self.vel)
    if d != 0:
      force.div(d)
    force.limit(self.maxForce)
    
    return force;
  
  
  def update(self):
    #self.maxForce = maxForceSlider.value()
    #self.fov = fovSlider.value()
    self.pos.add(self.vel)
    self.vel.add(self.acc)
    self.vel.limit(self.maxSpeed)
    self.acc.mult(0)
    self.pos.x = constrain(self.pos.x, 0, width)
    self.pos.y = constrain(self.pos.y, 100, height)
  
  def show(self):
    strokeWeight(2)
    stroke(255)
    push()
    translate(self.pos.x, self.pos.y)
    ellipse(0, 0, self.r, self.r)
    fill(255, 0, 0, 50)
    noStroke()
    ellipse(0, 0, self.fov, self.fov)
    rotate(self.vel.heading()-PI/4)
    stroke(255)
    line(0, 0, 10, 10)
    pop()
    
    
class Performer(Agent):
  def __init__(self, x, y):
    super(Performer,self).__init__(x, y)
    self.maxForce = 10
  
  def show(self):
    self.pos.x = constrain(self.pos.x, 0, width)
    self.pos.y = constrain(self.pos.y, 50, 50)
    strokeWeight(2)
    stroke(255)
    push()
    translate(self.pos.x, self.pos.y)
    ellipse(0, 0, self.r, self.r)
    textSize(8)
    fill(255, 0, 0)
    noStroke()
    text('Performer', -18, -10)
    pop()
