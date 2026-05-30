# TechFlow Solutions - Sistema de Gerenciamento Ágil

## Objetivo do Projeto
Sistema de gerenciamento de tarefas desenvolvido para uma startup de logística fictícia (TechFlow Solutions). [cite_start]O objetivo é permitir que a equipe acompanhe o fluxo de trabalho em tempo real, priorize entregas críticas e faça o controle de qualidade[cite: 6, 7].

## Metodologia Adotada
O projeto foi gerenciado utilizando a metodologia **Kanban** através do GitHub Projects, organizando as tarefas nas colunas "A Fazer", "Em Progresso" e "Concluído" para garantir fluxo contínuo e visibilidade do progresso.

## Como Executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute o arquivo principal: `python app.py`
3. Acesse no navegador: `http://127.0.0.1:5000`

## Gestão de Mudanças (Alteração de Escopo)
Durante o desenvolvimento, identificou-se a necessidade de uma mudança de escopo: a inclusão de um campo de **"Data de Previsão de Entrega"**. 
* **Justificativa:** No setor de logística, monitorar o status e a prioridade não é suficiente sem o controle de prazos. A adição desse campo permite à equipe visualizar as entregas de forma temporal, mitigando atrasos.
* **Ação:** O esquema do banco de dados (SQLite) foi atualizado, a interface foi adaptada para receber inputs de data e um novo card foi processado no Kanban para documentar a mudança.