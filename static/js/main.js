/**
 * Main application JavaScript: Theme switching, responsive sidebar,
 * modal dialogs, dropdowns, keyboard shortcuts, and active family switcher.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Theme Management
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  let storedTheme = localStorage.getItem('med_theme');
  if (!storedTheme || storedTheme === 'dark') {
    storedTheme = 'light';
    localStorage.setItem('med_theme', 'light');
  }
  document.documentElement.setAttribute('data-theme', storedTheme);

  const sunSvg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>';
  const moonSvg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';

  function updateThemeButton(theme) {
    if (themeToggleBtn) {
      themeToggleBtn.innerHTML = theme === 'dark' ? sunSvg : moonSvg;
      themeToggleBtn.setAttribute('title', theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode');
    }
  }

  updateThemeButton(storedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const nextTheme = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', nextTheme);
      localStorage.setItem('med_theme', nextTheme);
      updateThemeButton(nextTheme);
    });
  }

  // Sidebar Toggle for Mobile Viewport
  const sidebarToggleBtn = document.getElementById('sidebar-toggle-btn');
  const appSidebar = document.getElementById('app-sidebar');
  const sidebarBackdrop = document.getElementById('sidebar-backdrop');

  if (sidebarToggleBtn && appSidebar) {
    sidebarToggleBtn.addEventListener('click', () => {
      appSidebar.classList.toggle('open');
      if (sidebarBackdrop) {
        sidebarBackdrop.classList.toggle('show');
      }
    });
  }

  if (sidebarBackdrop) {
    sidebarBackdrop.addEventListener('click', () => {
      if (appSidebar) appSidebar.classList.remove('open');
      sidebarBackdrop.classList.remove('show');
    });
  }

  // Dropdown Toggles (Notification bell & User menu)
  setupDropdown('notification-bell-btn', 'notification-dropdown');
  setupDropdown('user-menu-btn', 'user-menu-dropdown');

  function setupDropdown(buttonId, dropdownId) {
    const btn = document.getElementById(buttonId);
    const dropdown = document.getElementById(dropdownId);

    if (btn && dropdown) {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        // Close other open dropdowns
        document.querySelectorAll('.dropdown-menu-active').forEach(d => {
          if (d !== dropdown) d.classList.remove('show', 'dropdown-menu-active');
        });
        dropdown.classList.toggle('show');
        dropdown.classList.toggle('dropdown-menu-active');
      });
    }
  }

  // Close dropdowns on outside click
  document.addEventListener('click', () => {
    document.querySelectorAll('.dropdown-menu-active').forEach(d => {
      d.classList.remove('show', 'dropdown-menu-active');
    });
  });

  // Global Search Input with Ctrl+K shortcut
  const searchInput = document.getElementById('global-search-input');
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (searchInput) {
        searchInput.focus();
        searchInput.select();
      }
    }
  });

  // Quick Table / Card Filter on Global Search input
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      // Filter any data table rows or dose items on current page
      const rows = document.querySelectorAll('.table tbody tr, .dose-item');
      rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(q) ? '' : 'none';
      });
    });
  }

  // Alert Dismissal & Auto-Fade
  document.querySelectorAll('.alert').forEach(alert => {
    const closeBtn = alert.querySelector('.alert-close');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        alert.style.opacity = '0';
        alert.style.transform = 'translateY(-6px)';
        setTimeout(() => alert.remove(), 250);
      });
    }

    // Auto dismiss non-error alerts after 6 seconds
    if (!alert.classList.contains('alert-danger')) {
      setTimeout(() => {
        if (document.body.contains(alert)) {
          alert.style.transition = 'opacity 300ms ease, transform 300ms ease';
          alert.style.opacity = '0';
          alert.style.transform = 'translateY(-6px)';
          setTimeout(() => alert.remove(), 300);
        }
      }, 6000);
    }
  });

  // Modal Dialog Handlers
  window.openModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.style.display = 'flex';
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeModal = function(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.style.display = 'none';
      document.body.style.overflow = '';
    }
  };

  // Close modals on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-overlay').forEach(modal => {
        if (modal.style.display === 'flex') {
          modal.style.display = 'none';
          document.body.style.overflow = '';
        }
      });
    }
  });

  // Active Family Switcher Form Auto-Submit
  const patientSelect = document.getElementById('header-patient-select');
  if (patientSelect) {
    patientSelect.addEventListener('change', () => {
      const memberId = patientSelect.value;
      const form = document.getElementById('header-patient-form');
      if (form && memberId) {
        form.action = `/family/switch/${memberId}/`;
        form.submit();
      }
    });
  }
});
