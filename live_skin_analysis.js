/* =========================
   DOM References
========================= */

const statusText = document.getElementById("poseStatus");
const captureBtn = document.getElementById("captureBtn");
const analyzeBtn = document.getElementById("analyzeBtn");
const img = document.getElementById("cameraFeed");
const canvas = document.getElementById("captureCanvas");
const previewImage = document.getElementById("previewImage");
const resultBox = document.getElementById("resultBox");
const radarCanvas = document.getElementById("radarChart");

let stableFrames = 0;
let poseReady = false;
let capturedBlob = null;
let radarChart = null;

/* =========================
   Pose Monitoring
========================= */

setInterval(() => {
  fetch("/face-shape-result")
    .then(res => res.json())
    .then(data => {
      if (!data || data.status === "processing") {
        stableFrames = 0;
        statusText.innerText = "Detecting face…";
        captureBtn.style.display = "none";
        return;
      }

      if (data.faceWidth && data.faceHeight && data.confidence >= 95) {
        stableFrames++;
      } else {
        stableFrames = 0;
      }

      if (stableFrames > 6) {
        poseReady = true;
        statusText.innerText = "Perfect pose detected";
        captureBtn.style.display = "inline-block";
      } else {
        poseReady = false;
        statusText.innerText = "Hold still…";
        captureBtn.style.display = "none";
      }
    })
    .catch(() => {
      statusText.innerText = "Camera sync lost";
    });
}, 500);

/* =========================
   Capture Only
========================= */

captureBtn.addEventListener("click", () => {
  if (!poseReady) return;

  canvas.width = img.naturalWidth;
  canvas.height = img.naturalHeight;

  const ctx = canvas.getContext("2d");
  ctx.drawImage(img, 0, 0);

  canvas.toBlob(blob => {
    capturedBlob = blob;

    // Preview image
    previewImage.src = URL.createObjectURL(blob);
    previewImage.style.display = "block";

    analyzeBtn.disabled = false;
    resultBox.textContent = "Ready to analyze ✔";

  }, "image/jpeg", 0.95);
});

/* =========================
   Result Formatter
========================= */

function formatResult(metrics) {
  let output = "";

  for (const key in metrics) {
    const value = metrics[key];
    if (Array.isArray(value)) {
      const label = key.replaceAll("_", " ").toUpperCase();
      const score = Number(value[1]).toFixed(1);
      output += `<div><strong>${label}</strong> : ${value[0]} (${score})</div>`;
    }
  }

  return output || "No metrics detected";
}

/* =========================
   Radar Chart Renderer
========================= */

function renderRadarChart(metrics) {

  const labels = [];
  const values = [];

  for (const key in metrics) {
    const value = metrics[key];
    if (Array.isArray(value)) {
      labels.push(key.replaceAll("_", " "));
      values.push(Number(value[1]));
    }
  }

  // Destroy previous chart if exists
  if (radarChart) {
    radarChart.destroy();
  }

  radarChart = new Chart(radarCanvas, {
    type: "radar",
    data: {
      labels: labels,
      datasets: [{
        label: "Skin Score",
        data: values,
        fill: true,
        backgroundColor: "rgba(0, 84, 255, 0.2)",
        borderColor: "#0054ff",
        pointBackgroundColor: "#0054ff",
        pointBorderColor: "#fff",
        pointHoverRadius: 5
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          suggestedMin: 0,
          suggestedMax: 100,
          ticks: {
            stepSize: 20
          }
        }
      },
      plugins: {
        legend: {
          display: false
        }
      }
    }
  });
}

/* =========================
   Analyze Captured Image
========================= */

analyzeBtn.addEventListener("click", async () => {
  if (!capturedBlob) {
    alert("Please capture image first");
    return;
  }

  analyzeBtn.disabled = true;
  resultBox.innerHTML = "Analyzing...";

  const formData = new FormData();
  formData.append("image", capturedBlob, "live.jpg");

  try {
    const res = await fetch("/analyze-skin", {
      method: "POST",
      body: formData
    });

    const data = await res.json();

    if (!res.ok || !data.skinMetrics) {
      resultBox.innerHTML = "❌ Analysis failed";
      analyzeBtn.disabled = false;
      return;
    }

    // Render text result
    resultBox.innerHTML = formatResult(data.skinMetrics);

    // ✅ Render spider graph
    renderRadarChart(data.skinMetrics);

  } catch (err) {
    resultBox.innerHTML = "⚠️ Client error: " + err.message;
  }

  analyzeBtn.disabled = false;
});
