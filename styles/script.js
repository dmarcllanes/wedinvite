// Service Worker Registration
if ("serviceWorker" in navigator) {
  navigator.serviceWorker
    .register(
      "data:application/javascript," +
        encodeURIComponent(`
        const CACHE_NAME = 'wedding-invite-v2';
        const urlsToCache = ['/', '/styles/style.css', '/styles/script.js'];
        self.addEventListener('install', (event) => {
            event.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(urlsToCache).catch(()=>Promise.resolve())));
            self.skipWaiting();
        });
        self.addEventListener('activate', (event) => {
            event.waitUntil(caches.keys().then((cacheNames) => Promise.all(cacheNames.map((cacheName) => {
                if (cacheName !== CACHE_NAME) return caches.delete(cacheName);
            }))));
            self.clients.claim();
        });
        self.addEventListener('fetch', (event) => {
            event.respondWith(caches.match(event.request).then((response) => {
                return response || fetch(event.request).then((response) => {
                    if (event.request.method === 'GET') {
                        const cache = caches.open(CACHE_NAME);
                        cache.then((c) => c.put(event.request, response.clone()));
                    }
                    return response;
                }).catch(() => caches.match('/'));
            }));
        });
    `),
    )
    .catch((err) => console.log("SW registration failed:", err));
}

// Install PWA Banner
let deferredPrompt;
window.addEventListener("beforeinstallprompt", (e) => {
  e.preventDefault();
  deferredPrompt = e;
  const installBanner = document.getElementById("install-banner");
  if (installBanner) {
    installBanner.style.display = "block";
    document.getElementById("install-btn").addEventListener("click", () => {
      deferredPrompt.prompt();
      deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === "accepted") console.log("PWA installed");
        deferredPrompt = null;
        installBanner.style.display = "none";
      });
    });
    document
      .getElementById("close-install-btn")
      .addEventListener("click", () => {
        installBanner.style.display = "none";
      });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  // 1. Music Modal
  const musicModal = document.getElementById("musicModal1");
  const btnYes = document.getElementById("modalYes");
  const btnNo = document.getElementById("modalNo");
  const audio = document.getElementById("audioPlayer");
  const playPauseBtn = document.getElementById("playPauseBtn");

  setTimeout(() => {
    if (musicModal) musicModal.classList.add("show");
  }, 500);

  if (btnYes) {
    btnYes.addEventListener("click", () => {
      musicModal.classList.remove("show");
      setTimeout(() => (musicModal.style.display = "none"), 300);
      audio.play().catch((e) => console.log("Audio autoplay blocked"));
    });
  }

  if (btnNo) {
    btnNo.addEventListener("click", () => {
      musicModal.classList.remove("show");
      setTimeout(() => (musicModal.style.display = "none"), 300);
    });
  }

  if (playPauseBtn) {
    playPauseBtn.addEventListener("click", () => {
      if (audio.paused) {
        audio.play();
      } else {
        audio.pause();
      }
    });
  }

  // 2. Envelope Animation
  const envelope = document.querySelector(".envelope");
  const envelopeWrapper = document.querySelector(".envelope-wrapper");

  if (envelope) {
    envelope.addEventListener("click", () => {
      envelope.classList.add("open");
      setTimeout(() => {
        envelopeWrapper.classList.add("hidden");
        document.body.style.overflowY = "visible";
      }, 3000);
    });
  }

  // 3. Scroll Reveal via IntersectionObserver
  const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.15,
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        observer.unobserve(entry.target); // Optional: animate only once
      }
    });
  }, observerOptions);

  const revealElements = document.querySelectorAll(".hidden-element");
  revealElements.forEach((el) => observer.observe(el));

  // 4. Countdown (Target: June 15, 2026 16:00:00)
  const targetDate = new Date("Jun 15, 2026 16:00:00").getTime();

  const timerInterval = setInterval(() => {
    const now = new Date().getTime();
    const distance = targetDate - now;

    if (distance < 0) {
      clearInterval(timerInterval);
      document.getElementById("days").innerText = "00";
      document.getElementById("hours").innerText = "00";
      document.getElementById("minutes").innerText = "00";
      document.getElementById("seconds").innerText = "00";
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor(
      (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60),
    );
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("days").innerText = days < 10 ? "0" + days : days;
    document.getElementById("hours").innerText =
      hours < 10 ? "0" + hours : hours;
    document.getElementById("minutes").innerText =
      minutes < 10 ? "0" + minutes : minutes;
    document.getElementById("seconds").innerText =
      seconds < 10 ? "0" + seconds : seconds;
  }, 1000);

  // 5. RSVP form submission
  const rsvpForm = document.getElementById("rsvp-form");
  if (rsvpForm) {
    rsvpForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const btn = rsvpForm.querySelector('button[type="submit"]');
      const origText = btn.innerText;
      btn.innerText = "SENDING...";
      btn.disabled = true;

      setTimeout(() => {
        btn.innerText = origText;
        btn.disabled = false;
        closeAttendanceModal();
        alert(
          "Thank you for your RSVP! We look forward to celebrating with you.",
        );
        rsvpForm.reset();
      }, 1000);
    });
  }

  // 6. Navbar Scroll Effect
  const header = document.querySelector(".header");
  if (header) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 50) {
        header.classList.add("scrolled");
      } else {
        header.classList.remove("scrolled");
      }
    });
  }

  // 7. Navbar Active Link Highlighting (ScrollSpy)
  const sections = document.querySelectorAll("section[id], div[id='pinicial']");
  const navLinks = document.querySelectorAll(".nav-links a");

  const highlightNavOpt = {
    threshold: 0.3, // Trigger when 30% of the section is visible
  };

  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        let currentId = entry.target.getAttribute("id");

        // Map section IDs to nav link hrefs
        navLinks.forEach((link) => {
          link.classList.remove("active");
          if (link.getAttribute("href") === `#${currentId}`) {
            link.classList.add("active");
          }
        });
      }
    });
  }, highlightNavOpt);

  sections.forEach((section) => {
    navObserver.observe(section);
  });
});

window.toggleMenu = function () {
  const navMenu = document.getElementById("nav-menu");
  const overlay = document.querySelector(".overlay");
  navMenu.classList.toggle("open");
  overlay.classList.toggle("open");
};

window.closeAttendanceModal = function () {
  document.getElementById("attendanceModal").classList.remove("show");
};

// 6. Particles JS Initialize
if (typeof particlesJS !== "undefined") {
  particlesJS("particles-js", {
    particles: {
      number: { value: 80, density: { enable: true, value_area: 800 } },
      color: { value: "#ffffff" },
      shape: {
        type: "circle",
        stroke: { width: 0, color: "#000000" },
        polygon: { nb_sides: 5 },
        image: { src: "img/github.svg", width: 100, height: 100 },
      },
      opacity: {
        value: 0.5,
        random: true,
        anim: { enable: true, speed: 1, opacity_min: 0.1, sync: false },
      },
      size: {
        value: 3,
        random: true,
        anim: { enable: true, speed: 2, size_min: 0.1, sync: false },
      },
      line_linked: { enable: false },
      move: {
        enable: true,
        speed: 1,
        direction: "top",
        random: true,
        straight: false,
        out_mode: "out",
        bounce: false,
        attract: { enable: false, rotateX: 600, rotateY: 1200 },
      },
    },
    interactivity: {
      detect_on: "canvas",
      events: {
        onhover: { enable: true, mode: "bubble" },
        onclick: { enable: false },
        resize: true,
      },
      modes: {
        bubble: { distance: 250, size: 0, duration: 2, opacity: 0, speed: 3 },
      },
    },
    retina_detect: true,
  });
}
