// Alias for Matter.js
const Engine = Matter.Engine,
  Render = Matter.Render,
  World = Matter.World,
  Bodies = Matter.Bodies,
  Constraint = Matter.Constraint,
  Events = Matter.Events,
  Mouse = Matter.Mouse,
  MouseConstraint = Matter.MouseConstraint;

let engine;
let world;
let boot1, boot2;
let constraint;
let ground;
let electricCable;
let boot1Passed = false;
let boot2Passed = false;

function setup() {
  createCanvas(windowWidth, windowHeight);

  // Create an engine
  engine = Engine.create();
  world = engine.world;

  // Create two boots connected by a constraint
  let bootSize = 40;
  boot1 = Bodies.rectangle(300, 200, bootSize, bootSize, {
    density: 0.001,
    friction: 0.9,
    collisionFilter: { category: 0x0001 },
  });
  boot2 = Bodies.rectangle(350, 200, bootSize, bootSize, {
    density: 0.001,
    friction: 0.9,
    collisionFilter: { category: 0x0001 },
  });
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

  // Create an electric cable with a width of 300 pixels
  electricCable = Bodies.rectangle(width / 2, height / 3, 300, 10, {
    isStatic: true,
    collisionFilter: { category: 0x0002 },
  });
  World.add(world, electricCable);

  // Add mouse control
  let canvasMouse = Mouse.create(canvas.elt);
  let options = { mouse: canvasMouse };
  let mConstraint = MouseConstraint.create(engine, options);
  World.add(world, mConstraint);

  // Add collision event listener
  Events.on(engine, "collisionStart", handleCollision);
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
  rect(electricCable.position.x, electricCable.position.y, 300, 10);
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

function handleCollision(event) {
  let pairs = event.pairs;

  for (let i = 0; i < pairs.length; i++) {
    let pair = pairs[i];

    if (
      (pair.bodyA === boot1 || pair.bodyA === boot2) &&
      pair.bodyB === electricCable
    ) {
      let boot =
        pair.bodyA === boot1 || pair.bodyA === boot2 ? pair.bodyA : pair.bodyB;
      let otherBoot = boot === boot1 ? boot2 : boot1;
      let bootPassed = boot === boot1 ? boot1Passed : boot2Passed;

      // Check if the boot is falling down and has already passed through the cable once
      if (boot.velocity.y > 0 && bootPassed) {
        // Check if the boot is moving slowly enough to be considered "stuck"
        if (Matter.Vector.magnitude(boot.velocity) < 1) {
          // Adjust the boot's position to make it "stick" to the cable
          Matter.Body.setPosition(boot, {
            x: boot.position.x,
            y: electricCable.position.y - 20, // Adjust the offset as needed
          });

          // Set the boot's velocity to zero
          Matter.Body.setVelocity(boot, { x: 0, y: 0 });

          // Set the boot's angular velocity to zero
          Matter.Body.setAngularVelocity(boot, 0);

          // Make the boot static so it doesn't fall off
          Matter.Body.setStatic(boot, true);

          // Allow only one boot to be stuck at a time
          break;
        }
      }

      // Mark the boot as having passed through the cable when moving upwards
      if (boot.velocity.y < 0) {
        if (boot === boot1) {
          boot1Passed = true;
        } else {
          boot2Passed = true;
        }
      }

      // Reset the flag for the other boot if it is still moving upwards
      if (otherBoot.velocity.y < 0) {
        if (otherBoot === boot1) {
          boot1Passed = false;
        } else {
          boot2Passed = false;
        }
      }
    }
  }
}
