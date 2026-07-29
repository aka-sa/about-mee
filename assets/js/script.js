/**
 * Scholaro Research Labs — Main JavaScript
 * Vanilla JS — no dependencies
 */

(function () {
  'use strict';

  /* --- Theme (Dark Mode) --- */
  const THEME_KEY = 'scholaro-theme';

  function getPreferredTheme() {
    const stored = localStorage.getItem(THEME_KEY);
    if (stored) return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(THEME_KEY, theme);
    const toggle = document.querySelector('.theme-toggle');
    if (toggle) {
      toggle.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
    }
  }

  setTheme(getPreferredTheme());

  document.querySelectorAll('.theme-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const current = document.documentElement.getAttribute('data-theme');
      setTheme(current === 'dark' ? 'light' : 'dark');
    });
  });

  /* --- Sticky Header --- */
  const header = document.querySelector('.header');
  if (header) {
    let lastScroll = 0;
    window.addEventListener('scroll', function () {
      const scrollY = window.scrollY;
      header.classList.toggle('header--scrolled', scrollY > 20);
      lastScroll = scrollY;
    }, { passive: true });
  }

  /* --- Mobile Navigation --- */
  const menuToggle = document.querySelector('.menu-toggle');
  const mobileNav = document.querySelector('.mobile-nav');

  if (menuToggle && mobileNav) {
    function closeMobileNav() {
      menuToggle.setAttribute('aria-expanded', 'false');
      mobileNav.classList.remove('mobile-nav--open');
      mobileNav.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    function openMobileNav() {
      menuToggle.setAttribute('aria-expanded', 'true');
      mobileNav.classList.add('mobile-nav--open');
      mobileNav.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }

    menuToggle.addEventListener('click', function () {
      const isOpen = menuToggle.getAttribute('aria-expanded') === 'true';
      isOpen ? closeMobileNav() : openMobileNav();
    });

    mobileNav.addEventListener('click', function (e) {
      if (e.target === mobileNav) closeMobileNav();
    });

    mobileNav.querySelectorAll('.mobile-nav__link').forEach(function (link) {
      link.addEventListener('click', closeMobileNav);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMobileNav();
    });
  }

  /* --- Active Nav Link --- */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__link, .mobile-nav__link').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('nav__link--active');
      link.setAttribute('aria-current', 'page');
    }
  });

  /* --- Animated Counters --- */
  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-count'), 10);
    const suffix = el.getAttribute('data-suffix') || '';
    const prefix = el.getAttribute('data-prefix') || '';
    const duration = 2000;
    const start = performance.now();

    function update(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const value = Math.floor(eased * target);
      el.textContent = prefix + value.toLocaleString() + suffix;
      if (progress < 1) requestAnimationFrame(update);
    }

    requestAnimationFrame(update);
  }

  const counterObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting && !entry.target.dataset.counted) {
        entry.target.dataset.counted = 'true';
        animateCounter(entry.target);
      }
    });
  }, { threshold: 0.3 });

  document.querySelectorAll('[data-count]').forEach(function (el) {
    counterObserver.observe(el);
  });

  /* --- Scroll Reveal --- */
  const revealObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal--visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(function (el) {
    revealObserver.observe(el);
  });

  /* --- Back to Top --- */
  const backToTop = document.querySelector('.back-to-top');
  if (backToTop) {
    window.addEventListener('scroll', function () {
      backToTop.classList.toggle('back-to-top--visible', window.scrollY > 500);
    }, { passive: true });

    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* --- Publications Filter, Search & Sort --- */
  const pubList = document.querySelector('.pub-list');
  if (pubList) {
    const searchInput = document.getElementById('pub-search');
    const filterSelect = document.getElementById('pub-filter');
    const sortSelect = document.getElementById('pub-sort');
    const pubCount = document.getElementById('pub-count');
    const items = Array.from(pubList.querySelectorAll('.pub-item'));

    function getVisibleItems() {
      const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
      const filter = filterSelect ? filterSelect.value : 'all';

      return items.filter(function (item) {
        const type = item.getAttribute('data-type');
        const text = item.textContent.toLowerCase();
        const matchesSearch = !query || text.includes(query);
        const matchesFilter = filter === 'all' || type === filter;
        return matchesSearch && matchesFilter;
      });
    }

    function renderPublications() {
      const sort = sortSelect ? sortSelect.value : 'newest';
      const visible = getVisibleItems();

      visible.sort(function (a, b) {
        const yearA = parseInt(a.getAttribute('data-year'), 10);
        const yearB = parseInt(b.getAttribute('data-year'), 10);
        const titleA = a.getAttribute('data-title').toLowerCase();
        const titleB = b.getAttribute('data-title').toLowerCase();

        if (sort === 'oldest') return yearA - yearB;
        if (sort === 'title') return titleA.localeCompare(titleB);
        return yearB - yearA;
      });

      items.forEach(function (item) { item.hidden = true; });
      visible.forEach(function (item) {
        item.hidden = false;
        pubList.appendChild(item);
      });

      if (pubCount) {
        pubCount.textContent = 'Showing ' + visible.length + ' of ' + items.length + ' publications';
      }
    }

    if (searchInput) searchInput.addEventListener('input', renderPublications);
    if (filterSelect) filterSelect.addEventListener('change', renderPublications);
    if (sortSelect) sortSelect.addEventListener('change', renderPublications);
    renderPublications();
  }

  /* --- Lab Section Navigation --- */
  const labNavLinks = document.querySelectorAll('.lab-nav__link');
  const labSections = document.querySelectorAll('.lab-section');

  if (labNavLinks.length && labSections.length) {
    const labObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          labNavLinks.forEach(function (link) {
            link.classList.toggle('lab-nav__link--active', link.getAttribute('href') === '#' + id);
          });
        }
      });
    }, { rootMargin: '-40% 0px -50% 0px' });

    labSections.forEach(function (section) {
      labObserver.observe(section);
    });
  }

  /* --- Form Handling --- */
  document.querySelectorAll('form[data-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const btn = form.querySelector('[type="submit"]');
      const originalText = btn.textContent;
      btn.textContent = 'Submitted ✓';
      btn.disabled = true;
      btn.style.opacity = '0.7';
      setTimeout(function () {
        btn.textContent = originalText;
        btn.disabled = false;
        btn.style.opacity = '';
        form.reset();
      }, 3000);
    });
  });

  /* --- Lazy Loading Images --- */
  if ('loading' in HTMLImageElement.prototype) {
    document.querySelectorAll('img[loading="lazy"]').forEach(function (img) {
      if (img.dataset.src) {
        img.src = img.dataset.src;
      }
    });
  } else {
    const lazyObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          const img = entry.target;
          if (img.dataset.src) img.src = img.dataset.src;
          lazyObserver.unobserve(img);
        }
      });
    });

    document.querySelectorAll('img[data-src]').forEach(function (img) {
      lazyObserver.observe(img);
    });
  }

  /* --- Smooth scroll for anchor links --- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();
