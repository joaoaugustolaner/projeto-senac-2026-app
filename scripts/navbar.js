document.addEventListener('DOMContentLoaded', function(){
    
    const token = localStorage.getItem('authToken');
    
    
    const links = document.querySelectorAll('.link-do-cabecalho');

    links.forEach(link => {
        
        if (link.getAttribute('href') === './auth.html') {
            
            
            if (token) {
                link.setAttribute('href', './form.html');
                link.setAttribute('text', 'Fofoca?!')
            }
        }
    })
})
