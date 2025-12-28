
// ================= CAMERA & CANVAS =================
const video = document.getElementById("video");
const overlay = document.getElementById("overlay");
const ctx = overlay.getContext("2d");

const faceStatus = document.getElementById("faceStatus");
const moveStatus = document.getElementById("moveStatus");
const warning = document.getElementById("warning");
const misCountEl = document.getElementById("misCount");
const phoneStatus = document.getElementById("phoneStatus");

// ================= CAMERA =================
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
    video.onloadedmetadata = () => {
      video.play();
      syncCanvas();
    };
  });

function syncCanvas() {
  overlay.width = video.clientWidth;
  overlay.height = video.clientHeight;
}
window.addEventListener("resize", syncCanvas);

// ================= FACE DETECTION =================
const faceDetection = new FaceDetection({
  locateFile: f => `https://cdn.jsdelivr.net/npm/@mediapipe/face_detection/${f}`
});

faceDetection.setOptions({
  model: "short",
  minDetectionConfidence: 0.6
});

// ================= STATE =================
let baseCenter = null;
let unstableFrames = 0;
const REQUIRED_UNSTABLE_FRAMES = 2;

let misbehaviorCount = 0;
let violationActive = false;

// ================= PHONE CACHE =================
let phoneDetected = false;
let phoneBox = null;

// ================= PHONE POLLING =================
async function pollPhoneDetection() {
  if (!video.videoWidth) return;

  const tempCanvas = document.createElement("canvas");
  tempCanvas.width = video.videoWidth;
  tempCanvas.height = video.videoHeight;

  const tctx = tempCanvas.getContext("2d");
  tctx.drawImage(video, 0, 0);

  const blob = await new Promise(r => tempCanvas.toBlob(r, "image/png"));

  const formData = new FormData();
  formData.append("frame", blob);

  try {
    const res = await fetch("/detect_phone", { method: "POST", body: formData });
    const data = await res.json();
    phoneDetected = data.phone;
    phoneBox = data.box;
  } catch {
    phoneDetected = false;
    phoneBox = null;
  }
}
setInterval(pollPhoneDetection, 700);

// ================= FACE DETECTION LOOP (STABLE) =================
setInterval(async () => {
  if (!video.videoWidth) return;
  await faceDetection.send({ image: video });
}, 120); // ~8 FPS (stable)

// ================= DRAW =================
faceDetection.onResults(results => {
  ctx.clearRect(0, 0, overlay.width, overlay.height);

  let currentlyUnstable = false;

  // ===== FACE STATUS =====
  if (results.detections.length === 0) {
    faceStatus.textContent = "Not Found";
    currentlyUnstable = true;
  } else if (results.detections.length > 1) {
    faceStatus.textContent = "Multiple Faces";
    currentlyUnstable = true;
  } else {
    faceStatus.textContent = "Detected";
  }

  // ===== FACE BOX =====
  if (results.detections.length === 1) {
    const box = results.detections[0].boundingBox;

    const cx = box.xCenter * overlay.width;
    const cy = box.yCenter * overlay.height;
    const w = box.width * overlay.width;
    const h = box.height * overlay.height;

    const x = cx - w / 2;
    const y = cy - h / 2;

    if (!baseCenter) baseCenter = { x: cx, y: cy };

    if (Math.abs(cx - baseCenter.x) > 14 || Math.abs(cy - baseCenter.y) > 14)
      currentlyUnstable = true;

    ctx.strokeStyle = currentlyUnstable ? "red" : "green";
    ctx.lineWidth = 4;
    ctx.strokeRect(x, y, w, h);

    if (!currentlyUnstable) {
      baseCenter.x = baseCenter.x * 0.9 + cx * 0.1;
      baseCenter.y = baseCenter.y * 0.9 + cy * 0.1;
    }
  }

  // ===== PHONE BOX =====
  if (phoneDetected && phoneBox) {
    phoneStatus.textContent = "Detected";
    phoneStatus.className = "danger";
    currentlyUnstable = true;

    const scaleX = overlay.width / video.videoWidth;
    const scaleY = overlay.height / video.videoHeight;
    const [x1, y1, x2, y2] = phoneBox;

    ctx.strokeStyle = "red";
    ctx.strokeRect(
      x1 * scaleX,
      y1 * scaleY,
      (x2 - x1) * scaleX,
      (y2 - y1) * scaleY
    );
  } else {
    phoneStatus.textContent = "None";
    phoneStatus.className = "ok";
  }

  // ===== VIOLATIONS =====
  if (currentlyUnstable) {
    unstableFrames++;
  } else {
    unstableFrames = 0;
    violationActive = false;
  }

  if (unstableFrames >= REQUIRED_UNSTABLE_FRAMES && !violationActive) {
    misbehaviorCount++;
    violationActive = true;
    misCountEl.textContent = misbehaviorCount;
  }

  moveStatus.textContent = currentlyUnstable ? "Suspicious" : "Stable";
  warning.style.display = currentlyUnstable ? "block" : "none";
});
// ================= EXAM TIMER =================
let examDuration = 30 * 60; // 30 minutes in seconds
const timerEl = document.getElementById("timer");

function startExamTimer() {
  setInterval(() => {
    if (examDuration <= 0) {
      alert("Time is up! Exam submitted automatically.");
      submitExam();
      return;
    }

    examDuration--;

    const minutes = Math.floor(examDuration / 60);
    const seconds = examDuration % 60;

    timerEl.textContent =
      `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
  }, 1000);
}

// START TIMER WHEN PAGE LOADS
startExamTimer();

function submitExam() {
  alert("Exam submitted successfully!");
  window.location.href = "/dashboard";
}
