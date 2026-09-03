/**
 * Notifications Engine: Polling unread alerts and playing local audio chimes.
 */

class NotificationManager {
  constructor() {
    this.unreadBadge = document.getElementById('notification-unread-badge');
    this.dropdownList = document.getElementById('notification-dropdown-items');
    this.pollIntervalMs = 30000; // 30 seconds
    this.lastCount = 0;

    if (this.unreadBadge) {
      this.init();
    }
  }

  init() {
    // Initial fetch
    this.fetchStatus();
    // Schedule periodic polling
    setInterval(() => this.fetchStatus(), this.pollIntervalMs);
  }

  async fetchStatus() {
    try {
      const response = await fetch('/notifications/api/unread-count/', {
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
      });
      if (!response.ok) return;

      const data = await response.json();
      this.updateUI(data.unread_count, data.items);
    } catch (e) {
      // Local network or offline fallback
    }
  }

  updateUI(count, items) {
    if (this.unreadBadge) {
      if (count > 0) {
        this.unreadBadge.textContent = count > 99 ? '99+' : count;
        this.unreadBadge.style.display = 'block';

        // Play chime if new notifications appeared
        if (count > this.lastCount && this.lastCount > 0) {
          this.playAlertChime();
        }
      } else {
        this.unreadBadge.style.display = 'none';
      }
    }
    this.lastCount = count;

    if (this.dropdownList && items && items.length > 0) {
      this.dropdownList.innerHTML = items.map(item => `
        <a href="/notifications/${item.id}/read/" class="notification-item unread">
          <div class="notification-item-title">${this.escapeHtml(item.title)}</div>
          <div class="notification-item-time">${item.created_at}</div>
        </a>
      `).join('');
    } else if (this.dropdownList && count === 0) {
      this.dropdownList.innerHTML = `
        <div style="padding: 1.5rem; text-align: center; color: var(--text-muted); font-size: 0.85rem;">
          No unread notifications
        </div>
      `;
    }
  }

  playAlertChime() {
    try {
      const ctx = new (window.AudioContext || window.webkitAudioContext)();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(587.33, ctx.currentTime); // D5
      osc.frequency.setValueAtTime(880, ctx.currentTime + 0.1); // A5

      gain.gain.setValueAtTime(0.2, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.35);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start();
      osc.stop(ctx.currentTime + 0.35);
    } catch (e) {
      // AudioContext blocked or unsupported
    }
  }

  escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.notificationManager = new NotificationManager();
});
