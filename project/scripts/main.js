const burger = document.getElementById('burger-menu');
const nav = document.getElementById('nav-menu');
const overlay = document.getElementById('menu-overlay');

// Toggle menu function
function toggleMenu() {
  burger.classList.toggle('active');
  nav.classList.toggle('active');
  overlay.classList.toggle('active');
  
  // Prevent body scrolling when menu is open
  document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
}

// Close menu function
function closeMenu() {
  burger.classList.remove('active');
  nav.classList.remove('active');
  overlay.classList.remove('active');
  document.body.style.overflow = '';
}

// Burger click handler
burger.addEventListener('click', toggleMenu);

// Overlay click to close
overlay.addEventListener('click', closeMenu);

// Close menu when clicking on nav links
document.querySelectorAll('.nav-menu a').forEach(link => {
  link.addEventListener('click', closeMenu);
});

// Close menu on Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && nav.classList.contains('active')) {
    closeMenu();
  }
});

// Close menu when window is resized past mobile breakpoint
window.addEventListener('resize', () => {
  if (window.innerWidth > 768 && nav.classList.contains('active')) {
    closeMenu();
  }
});