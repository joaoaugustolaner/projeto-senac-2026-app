document.addEventListener('DOMContentLoaded', () => {
    const authForm = document.getElementById('auth');

    authForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        
        const email = document.getElementById('email').value;
        const password = document.getElementById('senha').value;

        const clicked = event.submitter.id;

        let url = 'http://localhost:8000/auth'; 
        let mensagemErroPadrao = 'Credenciais inválidas';
        let headers = {'Accept': 'application/json'}
        let request_body;

        if (clicked === 'create_acc') {
            url = 'http://localhost:8000/users'; 
            mensagemErroPadrao = 'Erro ao criar conta. Verifique os dados.';
            headers['Content-Type'] = 'application/json'
            request_body = JSON.stringify({email: email, password: password})
        } else {
            const params = new URLSearchParams();
            params.append('username', email);    
            params.append('password', password); 
            request_body = params

            console.log(request_body)
        }

        // Executa a requisição dinamicamente
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: headers,
                body: request_body
            });

            if (!response.ok) {
                throw new Error(mensagemErroPadrao);
            }

            const data = await response.json();
            
            // Armazena o token (comum tanto para login quanto para auto-login após cadastro)
            if (data.access_token) {
                localStorage.setItem('authToken', data.access_token);
            }
            
            // Redireciona o usuário
            window.location.href = './index.html';

        } catch (error) {
            console.log(error)
        }
    });
});

// async function handleLogin(email, senha) {
//     try {
//         const response = await fetch('http://localhost:8000/auth', {
//             method: 'POST',
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify({ email: email, senha: senha })
//         });

//         if (!response.ok) {
//             throw new Error('Credenciais inválidas');
//         }

//         const data = await response.json();
//         localStorage.setItem('authToken', data.access_token);
        

//         window.location.href = 'form.html';

//     } catch (error) {
//         document.getElementById('error-message').textContent = error.message;
//     }
// }