// === Config ===
const DISTANCE_BETWEEN_STEPS = 50;      // px
const TIME_BEFORE_REMOVE_STEP = 700;    // ms
const MIN_TIME_BETWEEN_STEPS = 30;      // ms

// Flask static URLs (absolute paths)
const LEFT_SRC = "./static/assets/footsteps-left.png";
const RIGHT_SRC = "./static/assets/footsteps-right.png";

let lastX;
let lastY;
let stepSide = "left";
let wait = false;

window.addEventListener("mousemove", (event) => {
  if (wait) return;

  // Use clientX/Y (consistent across browsers)
  const x = event.clientX;
  const y = event.clientY;

  if (lastX === undefined && lastY === undefined) {
    lastX = x;
    lastY = y;
    return;
  }

  const distance = calculateDistance(lastX, lastY, x, y);
  if (distance < DISTANCE_BETWEEN_STEPS) return;

  putStep(lastX, lastY, x, y);

  lastX = x;
  lastY = y;

  waitBetweenSteps();
});

function calculateDistance(xA, yA, xB, yB) {
  return Math.hypot(xB - xA, yB - yA);
}

function putStep(xA, yA, xB, yB) {
  const angle = calculateAngle(xA, yA, xB, yB);
  const step = createStepOnDOM();

  // Position
  step.style.left = `${xA}px`;
  step.style.top = `${yA}px`;
  step.style.transform = `translate(-50%, -50%) rotate(${angle}deg)`;

  // Fade in
  requestAnimationFrame(() => {
    step.classList.add("present");
  });

  removeStepAfterTimer(step);
}

function calculateAngle(xA, yA, xB, yB) {
  return (Math.atan2(yB - yA, xB - xA) * 180) / Math.PI + 90;
}

function createStepOnDOM() {
  const step = document.createElement("img");
  step.classList.add("step");

  step.src = stepSide === "left" ? LEFT_SRC : RIGHT_SRC;
  stepSide = stepSide === "left" ? "right" : "left";

  document.body.appendChild(step);
  return step;
}

function removeStepAfterTimer(step) {
  setTimeout(() => {
    step.classList.remove("present");
    step.addEventListener("transitionend", () => step.remove(), { once: true });
  }, TIME_BEFORE_REMOVE_STEP);
}

function waitBetweenSteps() {
  wait = true;
  setTimeout(() => {
    wait = false;
  }, MIN_TIME_BETWEEN_STEPS);
}
