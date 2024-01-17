const links = document.querySelectorAll('nav a');
links.forEach(link => {
  link.addEventListener('mouseenter', () => {
    link.style.color = 'red'; 
    link.style.textDecoration = 'none'; 
    link.style.setProperty('--underline-offset', '10px'); 
    link.style.setProperty('--overline-offset', '-10px'); 
  });

  link.addEventListener('mouseleave', () => {
    link.style.color = ''; 
    link.style.textDecoration = 'none'; 
    link.style.setProperty('--underline-offset', '0');
    link.style.setProperty('--overline-offset', '0');
  });
});