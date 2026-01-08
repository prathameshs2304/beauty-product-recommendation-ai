/* ===============================
   Global App Script (Safe Version)
=============================== */

document.addEventListener("DOMContentLoaded", () => {

  /* ================= LOGIN FORM ================= */

  const loginForm = document.getElementById("loginForm");
  const usernameInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");

  if (loginForm && usernameInput && passwordInput) {

    loginForm.addEventListener("submit", (event) => {
      event.preventDefault();

      const username = usernameInput.value.trim();
      const password = passwordInput.value.trim();

      console.log("Username:", username);
      console.log("Password:", password);

      if (!username || !password) {
        alert("Please enter both username and password.");
        return;
      }

      // ✅ Simulated authentication (replace later with real auth)
      window.location.href = "feature_selection.html";
    });

  }


  /* ================= SIGNUP / LOGIN TOGGLE ================= */

  const showSignupBtn = document.getElementById("showSignup");
  const showLoginBtn = document.getElementById("showLogin");
  const loginContainer = document.querySelector(".form-container");
  const signupContainer = document.getElementById("signupContainer");

  if (showSignupBtn && showLoginBtn && loginContainer && signupContainer) {

    showSignupBtn.addEventListener("click", (e) => {
      e.preventDefault();
      loginContainer.style.display = "none";
      signupContainer.style.display = "block";
    });

    showLoginBtn.addEventListener("click", (e) => {
      e.preventDefault();
      signupContainer.style.display = "none";
      loginContainer.style.display = "block";
    });

  }


  /* ================= SKIN IMAGE UPLOAD UX ================= */
  /* Safe: Runs only if elements exist on page */

  const imageInput = document.getElementById("imageInput");
  const uploadBtn  = document.getElementById("uploadBtn");
  const preview    = document.getElementById("preview");

  if (imageInput && uploadBtn && preview) {

    imageInput.addEventListener("change", () => {
      const file = imageInput.files[0];
      if (!file) return;

      // ✅ Preview image
      preview.src = URL.createObjectURL(file);
      preview.style.display = "block";

      // ✅ Visual feedback for user
      uploadBtn.innerText = "Image Selected ✅";
      uploadBtn.style.opacity = "0.9";

      console.log("📷 Image selected:", file.name);
    });

  }


  /* ================= SAFETY LOG ================= */

  console.log("✅ Global script loaded safely");

});
