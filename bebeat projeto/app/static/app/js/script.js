document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.favorite-button').forEach((button) => {
    button.addEventListener('click', () => {
      const isFavorite = button.textContent.trim() === '♥';
      button.textContent = isFavorite ? '♡' : '♥';
      button.setAttribute('aria-pressed', String(!isFavorite));
    });
  });
});
