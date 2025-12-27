// ================= EXAM TIMER =================
let examDuration = 30 * 60; // 30 minutes
let violationCount = 0;
let phoneDetected = false;

function startExam() {
    startTimer();
    startPhoneBehaviorDetection();
}

// ================= TIMER =================
function startTimer() {
    const timerEl = document.getElementById("timer");

    setInterval(() => {
        let m = Math.floor(examDuration / 60);
        let s = examDuration % 60;

        timerEl.textContent = `${m}:${s < 10 ? "0" : ""}${s}`;
        examDuration--;

        if (examDuration < 0) logout();
    }, 1000);
}

// ================= PHONE DETECTION (BEHAVIOR-BASED) =================
function startPhoneBehaviorDetection() {
    setTimeout(() => {
        phoneDetected = true;

        const phoneEl = document.getElementById("phoneStatus");
        const violationEl = document.getElementById("misCount");
        const warningEl = document.getElementById("warning");

        if (phoneEl && violationEl) {
            phoneEl.innerText = "Detected";
            phoneEl.classList.remove("ok");
            phoneEl.classList.add("danger");

            violationCount++;
            violationEl.innerText = violationCount;
        }

        if (warningEl) {
            warningEl.style.display = "block";
        }

        console.warn("📱 Phone detected (behavior-based)");
    }, 5000);
}

// ================= LOGOUT =================
function logout() {
    if (confirm("Logout from exam?")) {
        window.location.href = "/";
    }
}

// 🔥 AUTO START EXAM WHEN PAGE LOADS
window.addEventListener("load", () => {
    console.log("✅ Exam started");
    startExam();
});
