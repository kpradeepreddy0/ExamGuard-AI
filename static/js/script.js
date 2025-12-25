const video = document.getElementById("video");
const overlay = document.getElementById("overlay");
const ctx = overlay.getContext("2d");

const faceStatus = document.getElementById("faceStatus");
const moveStatus = document.getElementById("moveStatus");
const warning = document.getElementById("warning");
const misCountEl = document.getElementById("misCount");
const phoneStatus = document.getElementById("phoneStatus");

// Camera
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
    video.play();
  });

// Face Detection
const faceDetection = new FaceDetection({
  locateFile: f => `https://cdn.jsdelivr.net/npm/@mediapipe/face_detection/${f}`
});

faceDetection.setOptions({
  model: "short",
  minDetectionConfidence: 0.6
});

// ================= STATE =================
let baseCenter = null;
let detecting = false;
let unstableFrames = 0;
const REQUIRED_UNSTABLE_FRAMES = 2;

let misbehaviorCount = 0;
let violationActive = false;

// Phone cache
let phoneDetected = false;
let phoneBox = null;

// ================= PHONE POLLING =================
async function pollPhoneDetection() {
  if (!video.videoWidth) return;

  const canvas = document.createElement("canvas");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  const cctx = canvas.getContext("2d");
  cctx.drawImage(video, 0, 0);

  const blob = await new Promise(resolve =>
    canvas.toBlob(resolve, "image/png") // 🔴 IMPORTANT
  );

  const formData = new FormData();
  formData.append("frame", blob);

  try {
    const res = await fetch("/detect_phone", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    phoneDetected = data.phone;
    phoneBox = data.box;
  } catch {
    phoneDetected = false;
    phoneBox = null;
  }
}

// Poll every 700ms
setInterval(pollPhoneDetection, 700);

// ================= FACE LOOP =================
async function detectFrame() {
  if (video.videoWidth && !detecting) {
    detecting = true;
    await faceDetection.send({ image: video });
    detecting = false;
  }
  requestAnimationFrame(detectFrame);
}
requestAnimationFrame(detectFrame);

// ================= DRAW =================
faceDetection.onResults(results => {

  const rect = video.getBoundingClientRect();
  const scaleX = rect.width / video.videoWidth;
  const scaleY = rect.height / video.videoHeight;

  overlay.width = rect.width;
  overlay.height = rect.height;
  ctx.clearRect(0, 0, overlay.width, overlay.height);

  let currentlyUnstable = false;

  // PHONE BOX
  if (phoneDetected && phoneBox) {
    phoneStatus.textContent = "Detected";
    phoneStatus.className = "danger";
    currentlyUnstable = true;

    const [x1, y1, x2, y2] = phoneBox;

    ctx.strokeStyle = "red";
    ctx.lineWidth = 4;
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

  // FACE STATUS
  if (results.detections.length === 0) {
    faceStatus.textContent = "Not Found";
    currentlyUnstable = true;
  } else if (results.detections.length > 1) {
    faceStatus.textContent = "Multiple Faces";
    currentlyUnstable = true;
  } else {
    faceStatus.textContent = "Detected";
  }

  // FACE BOX
  if (results.detections.length === 1) {
    const face = results.detections[0];
    const box = face.boundingBox;

    const rawX = box.xCenter * video.videoWidth;
    const rawY = box.yCenter * video.videoHeight;

    const x = rawX * scaleX;
    const y = rawY * scaleY;
    const w = box.width * video.videoWidth * scaleX;
    const h = box.height * video.videoHeight * scaleY;

    if (!baseCenter) baseCenter = { x: rawX, y: rawY };

    const dx = Math.abs(rawX - baseCenter.x);
    const dy = Math.abs(rawY - baseCenter.y);

    if (dx > 14 || dy > 14) currentlyUnstable = true;

    ctx.strokeStyle = currentlyUnstable ? "red" : "green";
    ctx.lineWidth = 4;
    ctx.strokeRect(x - w / 2, y - h / 2, w, h);

    if (!currentlyUnstable) {
      baseCenter.x = baseCenter.x * 0.9 + rawX * 0.1;
      baseCenter.y = baseCenter.y * 0.9 + rawY * 0.1;
    }
  }

  // VIOLATIONS
  if (currentlyUnstable) {
    unstableFrames++;
  } else {
    unstableFrames = 0;
    violationActive = false;
  }

  const isSuspicious = unstableFrames >= REQUIRED_UNSTABLE_FRAMES;

  if (isSuspicious && !violationActive) {
    misbehaviorCount++;
    violationActive = true;
    misCountEl.textContent = misbehaviorCount;
  }

  moveStatus.textContent = isSuspicious ? "Suspicious" : "Stable";
  warning.style.display = isSuspicious ? "block" : "none";
});
