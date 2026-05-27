// Back to top
const btn = document.getElementById('backToTop');
window.addEventListener('scroll', () => {
    btn?.classList.toggle('visible', window.scrollY > 300);
});
btn?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

// Cookie consent
window.addEventListener('DOMContentLoaded', () => {
    if (!localStorage.getItem('cookieConsent')) {
        setTimeout(() => {
            const banner = document.getElementById('cookieConsent');
            if (banner) banner.style.display = 'block';
        }, 1500);
    }
});
function acceptCookies() {
    localStorage.setItem('cookieConsent', 'accepted');
    document.getElementById('cookieConsent').style.display = 'none';
}
function declineCookies() {
    localStorage.setItem('cookieConsent', 'declined');
    document.getElementById('cookieConsent').style.display = 'none';
}

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const nav = document.getElementById('mainNav');
    if (nav) {
        if (window.scrollY > 50) {
            nav.style.padding = '8px 0';
            nav.style.boxShadow = '0 10px 15px -3px rgba(0, 0, 0, 0.1)';
        } else {
            nav.style.padding = '12px 0';
            nav.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.05)';
        }
    }
});

// Scroll-triggered animations
const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const el = entry.target;
            const anim = el.dataset.anim;
            if (anim) {
                el.classList.add(anim);
            }
            // Stop observing after animation applied
            scrollObserver.unobserve(el);
        }
    });
}, { threshold: 0.1 });

// Observe all elements with data-anim attribute
document.querySelectorAll('[data-anim]').forEach(el => {
    scrollObserver.observe(el);
});


// Reveal on scroll
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('.deal-card, .category-card, .store-card, .why-card, .reveal').forEach(el => {
    el.classList.add('reveal');
    revealObserver.observe(el);
});


// Auto-dismiss alerts
document.querySelectorAll('.custom-alert').forEach(alert => {
    setTimeout(() => {
        const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
        bsAlert.close();
    }, 5000);
});
