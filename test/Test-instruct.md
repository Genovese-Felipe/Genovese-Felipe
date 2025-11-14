# Instruction for Advanced evaluation: Code Human Preference Eval

Passing qualifies you for higher-paying engineering work with Alignerr.

You will have a single attempt.

Difficulty: Advanced

## How You’re Assessed
Your reasoning matters. The quality of your prompts and the clarity of your rationale directly impact whether you pass. We’re evaluating not just the final code, but how you guide the LLM and justify each step.

## About This Evaluation
Define a well-scoped coding task for an LLM
Guide the LLM through at least 3 conversational turns
Ensure the final code is production-ready and merge-worthy

## Review the full instructions:

### Doc Instructions:
---

'''
# Code Eval Project Instructions

## Problem Introduction

Please read all of these instructions carefully:

This evaluation assesses your ability to play the role of a software engineer using an LLM to complete a coding task. You’re given the following codebase: AI ChatKit [https://github.com/pasonk/ai-chatkit].

You must construct 2-3 well-scoped coding tasks for an LLM to implement. Your job is to have 2-3 one-turn conversations with the LLM directing it to complete coding tasks to your satisfaction. 

AI usage to is permitted. But it can't be identifiable and the responses must be humam made likely as it if has beem made and written by you (the human attempting for the assessment).

### Time Limit: 
1 hour 30 minutes

### Turns: 2-3 unique turns 
[Each turn is independent of previous turn, and can be treated as a new conversation with the model.]

## Task Introduction
You may want to clone the repository locally first. You will be using the Labelbox AI platform to generate code. After the model finishes responding, rate its response along the axes you see. For each turn, you must write thorough justifications for your ratings that convey your expertise and instill confidence that your ratings are accurate. Aim for prompt diversity to showcase breadth of knowledge and skill.

### Useful Tips

 Keep the prompts relatively constrained so you are able to understand the generated code.

 Consider running the generated code.

There is no timer on reading instructions. Take your time clearly going through them.

Check provided screenshots below for how the platform looks.
Prompting Instructions

### Here are some example prompts that define well sized scopes

You will need to come up with your own original prompt. Make sure the scope is **well-sized**, solution correctness is **verifiable**, and the problem defined is **unambiguous**. Try to only define scope, and avoid prescribing implementation details.

#### Good Examples

**Refactor Prompt**: Implement a reusable RadioSelectorCard component to replace the existing multiple implementations present in the ecomm user journeys. They all deliver the same UI/UX experience, but for whatever reason were implemented over and over.

**Feature Prompt**: Implement a streaming SSE client that renders LLM responses token by token. Currently, users wait for the full response to complete before seeing it all at once.

#### Bad Examples

**Refactor Prompt**: refactor the logging and configuration system to make the output more human readable and pretty like a json file and show the code changes in files and example of the output **(too subjective)**

**Feature Prompt**: add a command line feature called letscheck that analyzes the current python project and reports potential issues with a very detailed , human readable format **(ambiguous)**

**Feature Prompt**: add a new tool called Smart-log-analyzer that scans all the logs, classifies them (info,warning,error,critical) and explain each issue clearly with cause and fix with best solution up to 2 solutions, and generate a professional json report with summaries and AI-based suggestions then merge it with the existing letscheck report into one final report file **(scope size is too large)**

## Evaluation Criteria

You will be evaluated on:
  - **The quality of your prompting**,
  - **Adherence to project instructions**, and 
  - **Ability to communicate** how you justify your ratings effectively in writing. You are **writing to convince and impress** upon a reviewer **real coding skill** and **investigative effort**.

We would like you to **provide clear reasoning justifying your ratings**. Please **write at length for your overall preference justification (5+ sentences)**. 
You may see the responses are not in an ideal format, or some tool calls are exposed in raw json. You may utilize other programmers and devs tools to understand them (not AI). 
Usually just using python's print works. Please do not consider or penalize these factors, and still attempt to rate the code changes.
Any usage of automous  and asynchronous AI to generate opinions will lead to disqualification of results. You can use Coding Copillots and AI assistants for all the steps needes, since you follow what they are doing and take your decisions to use what they have done to use as your answers.

## Screenshots of Platform 

The following screenshots transcripts are after you have successfully logged in and clicked 'View' on the Code Human Preference Evaluation project:


### Platform overview screenshot transcript:

'''
A imagem apresenta uma captura de tela de uma interface de usuário (dashboard) de uma plataforma de trabalho online, aparentemente voltada para a anotação ou avaliação de dados. A interface está em "modo escuro" (fundo preto/cinza escuro com texto branco e detalhes em azul).
Aqui está uma descrição detalhada de cada seção:
1. Cabeçalho (Topo):
 * Título do Projeto: No canto superior esquerdo, lê-se "Code Human Preference Eval - New" (Avaliação de Preferência Humana em Código - Novo).
 * Abas de Navegação: Logo abaixo do título, há abas para diferentes seções: Overview (Visão Geral - atualmente selecionada), Data Rows, Performance, Issues, Notifications e Settings.
 * Botão de Ação: No canto superior direito, há um botão azul escrito "Start" com uma seta para baixo.
2. Barra Lateral Esquerda:
 * Uma faixa vertical fina contendo ícones de navegação rápida: um cubo (ativo), um troféu, um sol (provavelmente para tema claro/escuro), um sino de notificações, um ponto de interrogação (ajuda) e uma letra "S" (perfil do usuário).
3. Área Central (Conteúdo Principal):
 * Banner de Status: Um retângulo azul com um ícone de informação "i" e o texto: "Production - This project is in Production stage. Label data with precision and speed." (Produção - Este projeto está na fase de Produção. Rotule os dados com precisão e velocidade).
 * Seção "Available work" (Trabalho disponível):
   * Uma tabela mostrando a tarefa disponível.
   * Task: Labeling (Rotulagem).
   * Available data rows: 505 (linhas de dados disponíveis).
   * Pay rate: 45 $/task (Taxa de pagamento: 45 dólares por tarefa).
   * Há um botão azul "Start" ao lado dessa linha.
 * Seção "My performance" (Meu desempenho):
   * Mostra métricas vazias no momento: Labels created (Rótulos criados), Total time (Tempo total), Labeling time (Tempo de rotulagem), Rework % (% de retrabalho), Approval % (% de aprovação).
   * No centro, a mensagem: "No performance data available" (Nenhum dado de desempenho disponível).
   * No rodapé desta seção, há um texto pequeno: "To view your exact earnings visit Alignerr. Detailed insights in the performance tab." (Isso identifica a plataforma provável como Alignerr).
4. Barra Lateral Direita:
 * Project info: Exibe novamente a taxa de pagamento (Pay rate) de "45 $/task".
 * Labeling instructions:
   * Um link para "Read labeling instructions" (Ler instruções de rotulagem).
   * Data da última atualização: "Last updated: 2025-10-07".
 * Discord:
   * Um botão azul "Access Discord channel" (Acessar canal do Discord).
   * Um botão secundário "Go to landing channel".
 * Issues:
   * Um link "View issues" (Ver problemas).
   * Texto indicando "No unread issues" (Nenhum problema não lido).

Resumo Geral:
A tela mostra um painel de visão geral para um usuário que tem tarefas de rotulagem de código pendentes (505 tarefas), com um pagamento alto por tarefa ($45), numa plataforma chamada Alignerr. O projeto está ativo e as instruções foram atualizadas recentemente (considerando a data na imagem como outubro de 2025).
'''

### Post Clicking Start and Reading Instruction (code repository):

'''
## Esta imagem mostra uma janela sobreposta (modal) de "Time tracking notice" (Aviso de rastreamento de tempo), que apareceu provavelmente após clicar em "Start" na tela anterior. O fundo mostra a interface de trabalho real, que parece ser a plataforma Labelbox.

### Aqui está a descrição detalhada:

#### 1. Janela Central (Modal de Aviso):
O objetivo principal desta janela é instruir o trabalhador sobre como o tempo e o pagamento são calculados.
 * Título: "Time tracking notice" com um ícone de cronômetro.
 * Instrução Principal: "For this project, we require both a Hubstaff timer and a Labelbox timer to be active." (Para este projeto, exigimos que tanto o temporizador do Hubstaff quanto o do Labelbox estejam ativos).

##### * Caixa 1 - Hubstaff timer:
   * Diz: "This is used to monitor your system-wide activity." (Isso é usado para monitorar a atividade de todo o seu sistema). Ou seja, é para garantir que você está trabalhando, mas não define o valor a receber.

##### * Caixa 2 - Labelbox timer:
   * Diz: "Your payment for this project will be based exclusively on the time reported by the Labelbox timer. Please keep the Labelbox tab open while you are working." (Seu pagamento será baseado exclusivamente no tempo reportado pelo Labelbox. Mantenha a aba aberta).
 * Aviso Importante (Em laranja):
   * "Important: Time reported by the Hubstaff timer will NOT be used for billing purposes. Always refer to the Labelbox timer for accurate time tracking." (O tempo do Hubstaff NÃO será usado para faturamento. Baseie-se sempre no cronômetro do Labelbox).

##### * Botão: Um botão azul escrito "Acknowledge" (Reconhecer/Entendi).

#### 2. Interface de Fundo (O Ambiente de Trabalho):

Embora escurecida, é possível ver a estrutura da tarefa de rotulagem:

##### * Canto Superior Esquerdo: 
Indica "Turn 1" (Turno 1), sugerindo que a tarefa envolve uma conversa ou interação em etapas.

##### * Prompt Instructions (Esquerda):

   * Há um texto instruindo a escrever um prompt para o modelo baseado em um repositório ("repo").
   * Pede para pensar em uma tarefa de engenharia bem definida ("Think of a well-scoped engineering task").
   * Há um campo de entrada: "Send a message".

##### * Labeling Instructions (Barra Lateral Direita):

   * Submission Rules: Regras de envio. Destaca-se a regra: "Do not hit 'Submit' until at least 3 turns are complete." (Não clique em enviar até que pelo menos 3 turnos/interações estejam completos).
   * Menciona que cada interação deve envolver revisão e ciclos de iteração.
   * Git Repo: Há um link azul indicando acesso a um repositório Git.
   * Nota: "One model can take upto 15 mins to output the generated code" (Um modelo pode levar até 15 minutos para gerar o código).

### Resumo para o Usuário:
A plataforma está alertando que você precisa rodar o software Hubstaff (para provar que está no computador) e manter a aba do Labelbox aberta (que é o que realmente vai contar as horas para o seu pagamento de $45/tarefa). A tarefa em si envolve interagir com uma IA para gerar código baseado em um repositório Git, exigindo no mínimo 3 trocas de mensagens (turnos) antes de enviar.
'''

### Prompting Page:

'''
## Esta imagem mostra a interface de trabalho ativa ("workspace") dentro da plataforma Labelbox, onde a tarefa descrita nas imagens anteriores deve ser executada.

### Aqui está a descrição detalhada dos elementos visíveis:

#### 1. Área Principal de Trabalho (Centro e Esquerda):
Esta é a área de interação onde o trabalho criativo acontece.
 * Turn 1 (Turno 1): Indica que esta é a primeira mensagem da conversa.
 * Caixa "Prompt instructions" (Instruções do Prompt):
   * O texto instrui especificamente: "Try writing a prompt for the model based on this repo: beeai-framework." (Tente escrever um prompt para o modelo baseado neste repositório: beeai-framework).
   * Detalha o escopo: "Think of a well-scoped engineering task (new feature, refactor, extension, or tests) that fits naturally within the project." (Pense em uma tarefa de engenharia bem escopada — novo recurso, refatoração, extensão ou testes — que se encaixe naturalmente no projeto).
 * Campo de Entrada:
   * Abaixo das instruções, há um campo de chat padrão com o texto "Send a message" (Enviar uma mensagem), um ícone de clipe de papel (anexo) e uma seta para enviar.

#### 2. Barra de Ferramentas Superior:
 * Esquerda: Ícones de ferramentas. O ícone de "Informação" (i) está azul e selecionado, o que provavelmente exibe os painéis de dados à direita. Ao lado, há ícones para comentários, links, instruções (livro) e atalhos.
 * Direita: Botões de navegação da tarefa.
   * O botão "SUBMIT" (Enviar) está cinza/desativado. Isso confirma a regra vista na imagem anterior de que você não pode enviar o trabalho no primeiro turno (são necessários pelo menos 3).
   * Botão "SKIP" (Pular) está disponível.

#### 3. Barra Lateral Direita (Painéis de Informação):
Esta área exibe os metadados técnicos da tarefa atual (asset).
 * Seção "Data" (Dados):
   * ID: Um código longo alfanumérico (cmg0gz53...).
   * Created: "26 days ago" (Criado há 26 dias).
   * Asset type: "Conversational Text" (Texto Conversacional).
 * Seção "Media attributes" (Atributos de Mídia):
   * Asset type: conversational.
   * File size: 143 B (Arquivo muito pequeno, pois é apenas texto inicial).
   * Draft: true (Indica que é um rascunho).
   * Mime type / Sub type: Formatos internos do Labelbox (application/vnd.labelbox...).
 * Seção "Attachments" (Anexos):
   * Contém um item listado como "Text url".
 * Seção "Metadata": Está recolhida.

### Resumo do Contexto para o Usuário:
Você está agora dentro da tarefa. O objetivo claro é iniciar uma conversa simulando uma tarefa de engenharia de software. Você deve atuar como o usuário solicitando algo ao modelo de IA. O tema obrigatório é o repositório "beeai-framework". Você precisará propor, por exemplo, criar uma nova feature ou um teste unitário para esse framework específico.

'''















# Instruction for Advanced evaluation: Code Human Preference Eval

Passing qualifies you for higher-paying engineering work with Alignerr.

You will have a single attempt.

Difficulty: Advanced

## How You’re Assessed
Your reasoning matters. The quality of your prompts and the clarity of your rationale directly impact whether you pass. We’re evaluating not just the final code, but how you guide the LLM and justify each step.

## About This Evaluation
Define a well-scoped coding task for an LLM
Guide the LLM through at least 3 conversational turns
Ensure the final code is production-ready and merge-worthy

## Review the full instructions:

### Doc Instructions:
---

'''
# Code Eval Project Instructions

## Problem Introduction

Please read all of these instructions carefully:

This evaluation assesses your ability to play the role of a software engineer using an LLM to complete a coding task. You’re given the following codebase: AI ChatKit [https://github.com/pasonk/ai-chatkit].

You must construct 2-3 well-scoped coding tasks for an LLM to implement. Your job is to have 2-3 one-turn conversations with the LLM directing it to complete coding tasks to your satisfaction. 

AI usage to is permitted. But it can't be identifiable and the responses must be humam made likely as it if has beem made and written by you (the human attempting for the assessment).

### Time Limit: 
1 hour 30 minutes

### Turns: 2-3 unique turns 
[Each turn is independent of previous turn, and can be treated as a new conversation with the model.]

## Task Introduction
You may want to clone the repository locally first. You will be using the Labelbox AI platform to generate code. After the model finishes responding, rate its response along the axes you see. For each turn, you must write thorough justifications for your ratings that convey your expertise and instill confidence that your ratings are accurate. Aim for prompt diversity to showcase breadth of knowledge and skill.

### Useful Tips

 Keep the prompts relatively constrained so you are able to understand the generated code.

 Consider running the generated code.

There is no timer on reading instructions. Take your time clearly going through them.

Check provided screenshots below for how the platform looks.
Prompting Instructions

### Here are some example prompts that define well sized scopes

You will need to come up with your own original prompt. Make sure the scope is **well-sized**, solution correctness is **verifiable**, and the problem defined is **unambiguous**. Try to only define scope, and avoid prescribing implementation details.

#### Good Examples

**Refactor Prompt**: Implement a reusable RadioSelectorCard component to replace the existing multiple implementations present in the ecomm user journeys. They all deliver the same UI/UX experience, but for whatever reason were implemented over and over.

**Feature Prompt**: Implement a streaming SSE client that renders LLM responses token by token. Currently, users wait for the full response to complete before seeing it all at once.

#### Bad Examples

**Refactor Prompt**: refactor the logging and configuration system to make the output more human readable and pretty like a json file and show the code changes in files and example of the output **(too subjective)**

**Feature Prompt**: add a command line feature called letscheck that analyzes the current python project and reports potential issues with a very detailed , human readable format **(ambiguous)**

**Feature Prompt**: add a new tool called Smart-log-analyzer that scans all the logs, classifies them (info,warning,error,critical) and explain each issue clearly with cause and fix with best solution up to 2 solutions, and generate a professional json report with summaries and AI-based suggestions then merge it with the existing letscheck report into one final report file **(scope size is too large)**

## Evaluation Criteria

You will be evaluated on:
  - **The quality of your prompting**,
  - **Adherence to project instructions**, and 
  - **Ability to communicate** how you justify your ratings effectively in writing. You are **writing to convince and impress** upon a reviewer **real coding skill** and **investigative effort**.

We would like you to **provide clear reasoning justifying your ratings**. Please **write at length for your overall preference justification (5+ sentences)**. 
You may see the responses are not in an ideal format, or some tool calls are exposed in raw json. You may utilize other programmers and devs tools to understand them (not AI). 
Usually just using python's print works. Please do not consider or penalize these factors, and still attempt to rate the code changes.
Any usage of automous  and asynchronous AI to generate opinions will lead to disqualification of results. You can use Coding Copillots and AI assistants for all the steps needes, since you follow what they are doing and take your decisions to use what they have done to use as your answers.

## Screenshots of Platform 

The following screenshots transcripts are after you have successfully logged in and clicked 'View' on the Code Human Preference Evaluation project:


### Platform overview screenshot transcript:

'''
A imagem apresenta uma captura de tela de uma interface de usuário (dashboard) de uma plataforma de trabalho online, aparentemente voltada para a anotação ou avaliação de dados. A interface está em "modo escuro" (fundo preto/cinza escuro com texto branco e detalhes em azul).
Aqui está uma descrição detalhada de cada seção:
1. Cabeçalho (Topo):
 * Título do Projeto: No canto superior esquerdo, lê-se "Code Human Preference Eval - New" (Avaliação de Preferência Humana em Código - Novo).
 * Abas de Navegação: Logo abaixo do título, há abas para diferentes seções: Overview (Visão Geral - atualmente selecionada), Data Rows, Performance, Issues, Notifications e Settings.
 * Botão de Ação: No canto superior direito, há um botão azul escrito "Start" com uma seta para baixo.
2. Barra Lateral Esquerda:
 * Uma faixa vertical fina contendo ícones de navegação rápida: um cubo (ativo), um troféu, um sol (provavelmente para tema claro/escuro), um sino de notificações, um ponto de interrogação (ajuda) e uma letra "S" (perfil do usuário).
3. Área Central (Conteúdo Principal):
 * Banner de Status: Um retângulo azul com um ícone de informação "i" e o texto: "Production - This project is in Production stage. Label data with precision and speed." (Produção - Este projeto está na fase de Produção. Rotule os dados com precisão e velocidade).
 * Seção "Available work" (Trabalho disponível):
   * Uma tabela mostrando a tarefa disponível.
   * Task: Labeling (Rotulagem).
   * Available data rows: 505 (linhas de dados disponíveis).
   * Pay rate: 45 $/task (Taxa de pagamento: 45 dólares por tarefa).
   * Há um botão azul "Start" ao lado dessa linha.
 * Seção "My performance" (Meu desempenho):
   * Mostra métricas vazias no momento: Labels created (Rótulos criados), Total time (Tempo total), Labeling time (Tempo de rotulagem), Rework % (% de retrabalho), Approval % (% de aprovação).
   * No centro, a mensagem: "No performance data available" (Nenhum dado de desempenho disponível).
   * No rodapé desta seção, há um texto pequeno: "To view your exact earnings visit Alignerr. Detailed insights in the performance tab." (Isso identifica a plataforma provável como Alignerr).
4. Barra Lateral Direita:
 * Project info: Exibe novamente a taxa de pagamento (Pay rate) de "45 $/task".
 * Labeling instructions:
   * Um link para "Read labeling instructions" (Ler instruções de rotulagem).
   * Data da última atualização: "Last updated: 2025-10-07".
 * Discord:
   * Um botão azul "Access Discord channel" (Acessar canal do Discord).
   * Um botão secundário "Go to landing channel".
 * Issues:
   * Um link "View issues" (Ver problemas).
   * Texto indicando "No unread issues" (Nenhum problema não lido).

Resumo Geral:
A tela mostra um painel de visão geral para um usuário que tem tarefas de rotulagem de código pendentes (505 tarefas), com um pagamento alto por tarefa ($45), numa plataforma chamada Alignerr. O projeto está ativo e as instruções foram atualizadas recentemente (considerando a data na imagem como outubro de 2025).
'''

### Post Clicking Start and Reading Instruction (code repository):

'''
## Esta imagem mostra uma janela sobreposta (modal) de "Time tracking notice" (Aviso de rastreamento de tempo), que apareceu provavelmente após clicar em "Start" na tela anterior. O fundo mostra a interface de trabalho real, que parece ser a plataforma Labelbox.

### Aqui está a descrição detalhada:

#### 1. Janela Central (Modal de Aviso):
O objetivo principal desta janela é instruir o trabalhador sobre como o tempo e o pagamento são calculados.
 * Título: "Time tracking notice" com um ícone de cronômetro.
 * Instrução Principal: "For this project, we require both a Hubstaff timer and a Labelbox timer to be active." (Para este projeto, exigimos que tanto o temporizador do Hubstaff quanto o do Labelbox estejam ativos).

##### * Caixa 1 - Hubstaff timer:
   * Diz: "This is used to monitor your system-wide activity." (Isso é usado para monitorar a atividade de todo o seu sistema). Ou seja, é para garantir que você está trabalhando, mas não define o valor a receber.

##### * Caixa 2 - Labelbox timer:
   * Diz: "Your payment for this project will be based exclusively on the time reported by the Labelbox timer. Please keep the Labelbox tab open while you are working." (Seu pagamento será baseado exclusivamente no tempo reportado pelo Labelbox. Mantenha a aba aberta).
 * Aviso Importante (Em laranja):
   * "Important: Time reported by the Hubstaff timer will NOT be used for billing purposes. Always refer to the Labelbox timer for accurate time tracking." (O tempo do Hubstaff NÃO será usado para faturamento. Baseie-se sempre no cronômetro do Labelbox).

##### * Botão: Um botão azul escrito "Acknowledge" (Reconhecer/Entendi).

#### 2. Interface de Fundo (O Ambiente de Trabalho):

Embora escurecida, é possível ver a estrutura da tarefa de rotulagem:

##### * Canto Superior Esquerdo: 
Indica "Turn 1" (Turno 1), sugerindo que a tarefa envolve uma conversa ou interação em etapas.

##### * Prompt Instructions (Esquerda):

   * Há um texto instruindo a escrever um prompt para o modelo baseado em um repositório ("repo").
   * Pede para pensar em uma tarefa de engenharia bem definida ("Think of a well-scoped engineering task").
   * Há um campo de entrada: "Send a message".

##### * Labeling Instructions (Barra Lateral Direita):

   * Submission Rules: Regras de envio. Destaca-se a regra: "Do not hit 'Submit' until at least 3 turns are complete." (Não clique em enviar até que pelo menos 3 turnos/interações estejam completos).
   * Menciona que cada interação deve envolver revisão e ciclos de iteração.
   * Git Repo: Há um link azul indicando acesso a um repositório Git.
   * Nota: "One model can take upto 15 mins to output the generated code" (Um modelo pode levar até 15 minutos para gerar o código).

### Resumo para o Usuário:
A plataforma está alertando que você precisa rodar o software Hubstaff (para provar que está no computador) e manter a aba do Labelbox aberta (que é o que realmente vai contar as horas para o seu pagamento de $45/tarefa). A tarefa em si envolve interagir com uma IA para gerar código baseado em um repositório Git, exigindo no mínimo 3 trocas de mensagens (turnos) antes de enviar.
'''

### Prompting Page:

'''
## Esta imagem mostra a interface de trabalho ativa ("workspace") dentro da plataforma Labelbox, onde a tarefa descrita nas imagens anteriores deve ser executada.

### Aqui está a descrição detalhada dos elementos visíveis:

#### 1. Área Principal de Trabalho (Centro e Esquerda):
Esta é a área de interação onde o trabalho criativo acontece.
 * Turn 1 (Turno 1): Indica que esta é a primeira mensagem da conversa.
 * Caixa "Prompt instructions" (Instruções do Prompt):
   * O texto instrui especificamente: "Try writing a prompt for the model based on this repo: beeai-framework." (Tente escrever um prompt para o modelo baseado neste repositório: beeai-framework).
   * Detalha o escopo: "Think of a well-scoped engineering task (new feature, refactor, extension, or tests) that fits naturally within the project." (Pense em uma tarefa de engenharia bem escopada — novo recurso, refatoração, extensão ou testes — que se encaixe naturalmente no projeto).
 * Campo de Entrada:
   * Abaixo das instruções, há um campo de chat padrão com o texto "Send a message" (Enviar uma mensagem), um ícone de clipe de papel (anexo) e uma seta para enviar.

#### 2. Barra de Ferramentas Superior:
 * Esquerda: Ícones de ferramentas. O ícone de "Informação" (i) está azul e selecionado, o que provavelmente exibe os painéis de dados à direita. Ao lado, há ícones para comentários, links, instruções (livro) e atalhos.
 * Direita: Botões de navegação da tarefa.
   * O botão "SUBMIT" (Enviar) está cinza/desativado. Isso confirma a regra vista na imagem anterior de que você não pode enviar o trabalho no primeiro turno (são necessários pelo menos 3).
   * Botão "SKIP" (Pular) está disponível.

#### 3. Barra Lateral Direita (Painéis de Informação):
Esta área exibe os metadados técnicos da tarefa atual (asset).
 * Seção "Data" (Dados):
   * ID: Um código longo alfanumérico (cmg0gz53...).
   * Created: "26 days ago" (Criado há 26 dias).
   * Asset type: "Conversational Text" (Texto Conversacional).
 * Seção "Media attributes" (Atributos de Mídia):
   * Asset type: conversational.
   * File size: 143 B (Arquivo muito pequeno, pois é apenas texto inicial).
   * Draft: true (Indica que é um rascunho).
   * Mime type / Sub type: Formatos internos do Labelbox (application/vnd.labelbox...).
 * Seção "Attachments" (Anexos):
   * Contém um item listado como "Text url".
 * Seção "Metadata": Está recolhida.

### Resumo do Contexto para o Usuário:
Você está agora dentro da tarefa. O objetivo claro é iniciar uma conversa simulando uma tarefa de engenharia de software. Você deve atuar como o usuário solicitando algo ao modelo de IA. O tema obrigatório é o repositório "beeai-framework". Você precisará propor, por exemplo, criar uma nova feature ou um teste unitário para esse framework específico.

'''















