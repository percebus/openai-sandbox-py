// Alias for Matter.js
const Engine = Matter.Engine,
  Render = Matter.Render,
  World = Matter.World,
  Bodies = Matter.Bodies,
  Constraint = Matter.Constraint,
  Mouse = Matter.Mouse,
  MouseConstraint = Matter.MouseConstraint;

let engine;
let world;
let boot1, boot2;
let constraint;
let ground;
let electricCable;

function setup() {
  createCanvas(windowWidth, windowHeight);

  // Create an engine
  engine = Engine.create();
  world = engine.world;

  // Create two boots connected by a constraint
  let bootSize = 40;
  boot1 = Bodies.rectangle(300, 200, bootSize, bootSize);
  boot2 = Bodies.rectangle(350, 200, bootSize, bootSize);
  constraint = Constraint.create({
    bodyA: boot1,
    bodyB: boot2,
    length: 60,
    stiffness: 0.5,
  });
  World.add(world, [boot1, boot2, constraint]);

  // Create ground
  ground = Bodies.rectangle(width / 2, height, width, 10, { isStatic: true });
  World.add(world, ground);

  // Create an electric cable
  electricCable = Bodies.rectangle(width / 2, height / 3, width, 10, {
    isStatic: true,
  });
  World.add(world, electricCable);

  // Add mouse control
  let canvasMouse = Mouse.create(canvas.elt);
  let options = { mouse: canvasMouse };
  let mConstraint = MouseConstraint.create(engine, options);
  World.add(world, mConstraint);
}

function draw() {
  background(51);
  Engine.update(engine);

  // Draw the boots
  drawBoot(boot1);
  drawBoot(boot2);

  // Draw the constraint (laces)
  stroke(255);
  line(boot1.position.x, boot1.position.y, boot2.position.x, boot2.position.y);

  // Draw the ground
  noStroke();
  fill(128);
  rectMode(CENTER);
  rect(ground.position.x, ground.position.y, width, 10);

  // Draw the electric cable
  fill(255, 0, 0);
  rect(electricCable.position.x, electricCable.position.y, width, 10);
}

function drawBoot(boot) {
  push();
  translate(boot.position.x, boot.position.y);
  rotate(boot.angle);
  fill(200);
  rectMode(CENTER);
  rect(0, 0, 40, 40);
  pop();
}
