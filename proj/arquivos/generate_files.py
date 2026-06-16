import os

files_to_create = {
    "poema.txt": (
        "Batatinha quando nasce\n"
        "Espalha rama pelo chão\n"
        "Menininha quando dorme\n"
        "Põe a mão no coração.\n"
    ),
    "documento_contagem.txt": (
        "Linha 1: Introdução ao processamento de arquivos.\n"
        "Linha 2: Usando blocos try-except para proteção.\n"
        "Linha 3: Gerenciadores de contexto com a instrução with.\n"
        "Linha 4: Fim do arquivo de testes.\n"
    ),
    "sistema.log": (
        "INFO: Conexão estabelecida com o servidor principal.\n"
        "DEBUG: Carregando módulos de segurança.\n"
        "ERROR: Falha no banco de dados ao tentar salvar registro.\n"
        "INFO: Tentativa de reconexão automática executada.\n"
        "ERROR: Tempo limite de requisição excedido (Timeout).\n"
        "DEBUG: Limpando buffers temporários.\n"
    ),
    "valores.txt": (
        "12.5\n"
        "45.0\n"
        "7.2\n"
        "100.8\n"
        "23.1\n"
    ),
    "notas.txt": (
        "Ana,8.5,9.0\n"
        "Bruno,7.0,6.5\n"
        "Carlos,5.5,8.0\n"
        "Daniela,10.0,9.5\n"
    ),
    "documento.txt": (
        "A programação estruturada é essencial para o aprendizado.\n"
        "Python facilita muito a automação de scripts.\n"
        "Trabalhar com arquivos exige atenção com caminhos de diretório.\n"
        "A automação poupa tempo e reduz erros humanos cotidianos.\n"
    ),
    "dados_sujos.txt": (
        "Registro 1: Ativo\n"
        "\n"
        "Registro 2: Inativo\n"
        "   \n"
        "Registro 3: Pendente\n"
        "\n"
        "Registro 4: Concluído\n"
    ),
    "dados_originais.csv": (
        "id;nome;cargo\n"
        "1;Alice;Engenheira de Dados\n"
        "2;Bob;Cientista de Dados\n"
        "3;Charlie;Analista de Sistemas\n"
    ),
    "planta_casa.txt": (
        "===============\n"
        "= S           =\n"
        "=       T     =\n"
        "=             =\n"
        "=    C        =\n"
        "===============\n"
    ),
    "coordenadas_planta.csv": (
        "Tipo,Linha,Coluna\n"
        "Parede,0,0\n"
        "Parede,0,1\n"
        "Parede,0,2\n"
        "Mesa,3,4\n"
        "Mesa,3,5\n"
        "Parede,9,9\n"
    ),
    "planta_vazada.txt": (
        "===============\n"
        "=             =\n"
        "=             =\n"
        "              =\n"
        "=             =\n"
        "===============\n"
    )
}

os.makedirs('proj/arquivos/exercicios/arquivos/')
for filename, content in files_to_create.items():
    with open('proj/arquivos/exercicios/arquivos/' + filename, "w", encoding="utf-8") as f:
        f.write(content)


print("Files generated succesfully!. Check exericios/arquivos/ in the current directory.")
