let examDuration = 30 * 60;

function startExam() {
    startTimer();
}

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

function toggleFullScreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        document.exitFullscreen();
    }
}

function logout() {
    if (confirm("Logout from exam?")) {
        window.location.href = "/";
    }
}
