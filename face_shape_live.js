/* =========================
   DOM References
========================= */

const video = document.getElementById("video");
const canvas = document.getElementById("captureCanvas");
const statusText = document.getElementById("status");
const confidenceBar = document.getElementById("confidenceBar");

/* =========================
   Safe Text Setter
========================= */

function setText(id, value) {
  const el = document.getElementById(id);
  if (!el) return;
  el.innerText = value ?? "—";
}

/* =========================
   Start Camera
========================= */

async function startCamera() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode: "user" },
      audio: false
    });
    video.srcObject = stream;
    statusText.innerHTML = `<span class="status-dot"></span> Camera ready`;
  } catch (err) {
    alert("Camera permission denied or unavailable.");
    console.error("Camera error:", err);
    statusText.innerHTML = `<span class="status-dot"></span> Camera error`;
  }
}

startCamera();

/* =========================
   Send Frame to Backend
========================= */

async function sendFrame() {
  if (!video.videoWidth) return;

  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  const ctx = canvas.getContext("2d");
  ctx.drawImage(video, 0, 0);

  canvas.toBlob(async blob => {
    if (!blob) return;

    const formData = new FormData();
    formData.append("image", blob, "frame.jpg");

    try {
      const res = await fetch("/analyze-frame", {
        method: "POST",
        body: formData
      });

      const data = await res.json();

      if (!data || data.status === "processing") {
        statusText.innerHTML = `<span class="status-dot"></span> Analyzing…`;
        return;
      }

      /* =========================
         UI Updates
      ========================= */

      setText("faceShape", data.faceShape);
      setText("faceWidth", data.faceWidth ? `${data.faceWidth} px` : "—");
      setText("faceHeight", data.faceHeight ? `${data.faceHeight} px` : "—");

      if (data.faceWidth && data.faceHeight) {
        const ratio = (data.faceWidth / data.faceHeight).toFixed(2);
        setText("faceRatio", ratio);
        setText("facialBalance", ratio > 0.85 ? "Balanced" : "Elongated");
      }

      setText("confidence", data.confidence ? `${data.confidence}%` : "—");

      setText(
        "explanation",
        "Based on stable facial landmark geometry"
      );

      /* =========================
         Animate Confidence Bar
      ========================= */

      if (data.confidence && confidenceBar) {
        confidenceBar.style.width = `${data.confidence}%`;
      }

      statusText.innerHTML = `<span class="status-dot"></span> Analysis complete`;

    } catch (err) {
      console.error("Frame upload error:", err);
      statusText.innerHTML = `<span class="status-dot"></span> Connection error`;
    }
  }, "image/jpeg", 0.85);
}

/* =========================
   Loop Controller
========================= */

// ~3 FPS (stable + low bandwidth)
setInterval(sendFrame, 300);
