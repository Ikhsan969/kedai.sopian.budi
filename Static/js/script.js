document.querySelector('.search-bar input').addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    const items = document.querySelectorAll('.menu-item');

    items.forEach(item => {
        const title = item.querySelector('h3').textContent.toLowerCase();
        item.style.display = title.includes(searchTerm) ? '' : 'none';
    });
});
