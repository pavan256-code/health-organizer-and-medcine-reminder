/**
 * Local Data Visualization Engine: SVG & Canvas charting utilities.
 * Completely offline with zero external JS dependencies.
 */

class HealthCharts {
  /**
   * Renders a responsive line trend chart onto an HTML5 canvas.
   * @param {string} canvasId 
   * @param {Array<string>} labels 
   * @param {Array<number>} values 
   * @param {Object} options 
   */
  static renderLineChart(canvasId, labels, values, options = {}) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.parentElement.clientWidth || 400;
    const height = canvas.height = options.height || 220;

    ctx.clearRect(0, 0, width, height);

    if (!values || values.length === 0) {
      ctx.fillStyle = '#94a3b8';
      ctx.font = '14px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('No data available', width / 2, height / 2);
      return;
    }

    const padding = { top: 25, right: 25, bottom: 35, left: 45 };
    const chartW = width - padding.left - padding.right;
    const chartH = height - padding.top - padding.bottom;

    const minVal = options.min !== undefined ? options.min : Math.min(...values) * 0.9;
    const maxVal = options.max !== undefined ? options.max : Math.max(...values) * 1.1;
    const range = (maxVal - minVal) || 1;

    // Grid lines & Y-axis labels
    ctx.strokeStyle = '#e2e8f0';
    ctx.lineWidth = 1;
    ctx.fillStyle = '#64748b';
    ctx.font = '11px sans-serif';
    ctx.textAlign = 'right';

    const ySteps = 4;
    for (let i = 0; i <= ySteps; i++) {
      const yVal = minVal + (range * (i / ySteps));
      const yPos = padding.top + chartH - (chartH * (i / ySteps));
      ctx.beginPath();
      ctx.moveTo(padding.left, yPos);
      ctx.lineTo(width - padding.right, yPos);
      ctx.stroke();
      ctx.fillText(Math.round(yVal), padding.left - 8, yPos + 4);
    }

    // Points calculation
    const points = values.map((val, idx) => {
      const x = padding.left + (chartW * (idx / Math.max(values.length - 1, 1)));
      const y = padding.top + chartH - ((val - minVal) / range * chartH);
      return { x, y, val };
    });

    // Gradient fill under line
    const gradient = ctx.createLinearGradient(0, padding.top, 0, height - padding.bottom);
    gradient.addColorStop(0, options.fillColor || 'rgba(2, 132, 199, 0.25)');
    gradient.addColorStop(1, 'rgba(2, 132, 199, 0.0)');

    ctx.beginPath();
    ctx.moveTo(points[0].x, height - padding.bottom);
    points.forEach(pt => ctx.lineTo(pt.x, pt.y));
    ctx.lineTo(points[points.length - 1].x, height - padding.bottom);
    ctx.closePath();
    ctx.fillStyle = gradient;
    ctx.fill();

    // Line stroke
    ctx.beginPath();
    ctx.moveTo(points[0].x, points[0].y);
    points.forEach(pt => ctx.lineTo(pt.x, pt.y));
    ctx.strokeStyle = options.lineColor || '#0284c7';
    ctx.lineWidth = 3;
    ctx.stroke();

    // Data points & X labels
    ctx.textAlign = 'center';
    ctx.fillStyle = '#64748b';
    points.forEach((pt, idx) => {
      // Circle dot
      ctx.beginPath();
      ctx.arc(pt.x, pt.y, 4, 0, Math.PI * 2);
      ctx.fillStyle = '#ffffff';
      ctx.fill();
      ctx.strokeStyle = options.lineColor || '#0284c7';
      ctx.lineWidth = 2;
      ctx.stroke();

      // X Label
      if (labels && labels[idx]) {
        ctx.fillStyle = '#64748b';
        ctx.fillText(labels[idx], pt.x, height - 10);
      }
    });
  }

  /**
   * Renders a bar chart onto an HTML5 canvas.
   */
  static renderBarChart(canvasId, labels, values, options = {}) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.parentElement.clientWidth || 400;
    const height = canvas.height = options.height || 220;

    ctx.clearRect(0, 0, width, height);
    if (!values || values.length === 0) return;

    const padding = { top: 20, right: 20, bottom: 35, left: 40 };
    const chartW = width - padding.left - padding.right;
    const chartH = height - padding.top - padding.bottom;

    const maxVal = Math.max(...values, 1) * 1.15;
    const barWidth = Math.min((chartW / values.length) * 0.6, 40);
    const spacing = chartW / values.length;

    values.forEach((val, idx) => {
      const barH = (val / maxVal) * chartH;
      const x = padding.left + (spacing * idx) + (spacing - barWidth) / 2;
      const y = padding.top + chartH - barH;

      ctx.fillStyle = options.barColor || '#0d9488';
      ctx.beginPath();
      ctx.roundRect ? ctx.roundRect(x, y, barWidth, barH, [4, 4, 0, 0]) : ctx.rect(x, y, barWidth, barH);
      ctx.fill();

      // Value label on top
      ctx.fillStyle = '#0f172a';
      ctx.font = '11px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(val, x + barWidth / 2, y - 5);

      // Category label below
      if (labels && labels[idx]) {
        ctx.fillStyle = '#64748b';
        ctx.fillText(labels[idx], x + barWidth / 2, height - 10);
      }
    });
  }
}

window.HealthCharts = HealthCharts;
