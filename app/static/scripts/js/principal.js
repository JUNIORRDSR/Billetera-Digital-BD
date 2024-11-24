document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.overlay');
    const closeSidebar = document.querySelector('.close-sidebar');
    const mainContent = document.querySelector('.main-content');

    // Abrir sidebar
    menuToggle.addEventListener('click', function() {
        sidebar.classList.add('active');
        overlay.classList.add('active');
        mainContent.classList.add('sidebar-active');
    });

    // Cerrar sidebar
    function closeSidebarFunction() {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
        mainContent.classList.remove('sidebar-active');
    }

    closeSidebar.addEventListener('click', closeSidebarFunction);
    overlay.addEventListener('click', closeSidebarFunction);
});

