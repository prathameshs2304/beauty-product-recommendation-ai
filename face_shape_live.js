function setText(id, value) {
  const el = document.getElementById(id);
  if (!el) return;
  el.innerText = value ?? "—";
}

setInterval(() => {
  fetch("/face-shape-result")
    .then(res => res.json())
    .then(data => {
      if (!data || data.status === "processing") {
        document.getElementById("status").innerText = "Analyzing…";
        return;
      }

      // Base metrics
      setText("faceShape", data.faceShape);
      setText("faceWidth", data.faceWidth ? `${data.faceWidth} px` : "—");
      setText("faceHeight", data.faceHeight ? `${data.faceHeight} px` : "—");

      // Derived
      if (data.faceWidth && data.faceHeight) {
        const ratio = (data.faceWidth / data.faceHeight).toFixed(2);
        setText("faceRatio", ratio);
        setText("facialBalance", ratio > 0.85 ? "Balanced" : "Elongated");
      }

    

      // Confidence
      setText("shapeConfidence", data.confidence ? `${data.confidence}%` : "—");
      setText("confidence", data.confidence ? `${data.confidence}%` : "—");

      setText(
        "explanation",
        data.explanation || "Based on stable facial landmark geometry"
      );

      document.getElementById("status").innerText = "Analysis complete";
    })
    .catch(err => {
      console.error("Face shape fetch error:", err);
    });
}, 600);
