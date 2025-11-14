# Guia Estratégico para a Avaliação "Code Human Preference"

Este documento é o seu manual completo para a avaliação. Ele contém a metodologia para criar prompts de alta qualidade, a estrutura para escrever justificativas de nível sênior e o fluxo de trabalho operacional para executar a tarefa de forma discreta e eficaz.

---

## Parte 1: O Fluxo de Trabalho Operacional

Sua tarefa é usar assistência de IA (seu celular) enquanto mantém uma atividade de desenvolvimento plausível em um PC monitorado.

### **Fase 0: Preparação (Antes do Cronômetro)**

1.  **No seu Celular:**
    *   Abra uma aba do navegador comigo (AI Studio) e outra com o repositório GitHub do projeto.
    *   Use um editor de notas (ex: Samsung Notes) para rascunhar.
2.  **Defina as 3 Tarefas:**
    *   Junto comigo, analise o repositório e defina as 3 tarefas que você irá propor (Turnos 1, 2 e 3).
    *   Use o **Template Mestre de Prompts** (Parte 2 deste guia) para rascunhar os 3 prompts no seu editor de notas.

### **Fase 1: Execução (Durante a Sessão Monitorada)**

1.  **No PC:**
    *   Inicie o Hubstaff e a plataforma Labelbox.
    *   **Simule atividade:** Navegue pelo código no navegador, mantenha o cursor ativo na caixa de prompt, digite e apague lentamente.
2.  **Transferência de Prompt (Celular -> PC):**
    *   Olhando para o seu celular, **digite manualmente** o prompt do turno atual na Labelbox. **Não copie e cole.**
3.  **Análise da Resposta:**
    *   Quando a LLM responder no PC, leia o código.
    *   No seu celular, descreva o código para mim. Juntos, faremos a análise técnica.
    *   Use o **Framework de Justificativas** (Parte 3 deste guia) para rascunhar sua avaliação no seu editor de notas.
4.  **Transferência da Justificativa (Celular -> PC):**
    *   **Digite manualmente** sua justificativa final na Labelbox.

**Lembre-se:** A digitação manual no PC é a chave para uma atividade de aparência natural.

---

## Parte 2: Template Mestre para Prompts de Engenharia

Use esta estrutura para construir cada um dos seus 2-3 prompts.

### **Subject: [Título Curto e Descritivo da Tarefa]**
*Ex: "Implement 'Copy to Clipboard' for Code Blocks"*

### **1. Feature / Task**
*Descrição em uma única frase do que precisa ser feito.*
*Ex: "Implement a client-side 'Copy to Clipboard' feature for all Markdown code fences rendered in the chat."*

### **2. Context & Reasoning**
*Explicação do "porquê" a tarefa é importante.*
*Ex: "Reasoning: Users often need to copy code snippets from AI responses. This feature removes friction and improves the core user experience..."*

### **3. UI/UX Requirements (ou Behavioral Requirements)**
*Descrição detalhada e inequívoca de como a feature deve se parecer e se comportar.*
*Ex: "1. A 'Copy' button should appear on hover. 2. On click, it shows a 'Copied!' confirmation for 1.5s. 3. It must be accessible via keyboard..."*

### **4. Technical Suggestions & Constraints**
*Orientação técnica para a LLM se alinhar com a arquitetura existente.*
*Ex: "You will likely need to modify `MessageBubble.tsx`. Use the `navigator.clipboard.writeText` API. Consider creating a utility function in `utils/clipboard.ts`..."*

### **5. Acceptance Criteria & Testing**
*Definição clara do que constitui uma solução completa e correta.*
*Ex: "1. Clicking copies the raw code content. 2. Works for multi-line blocks. 3. **Tests:** Please provide a unit test for the new utility and a component test for the button rendering."*

---

## Parte 3: Framework para Justificativas de Nível Sênior

Use esta estrutura de 4 pontos para escrever avaliações detalhadas e convincentes.

### **1. Tese (A Afirmação Principal)**
*Comece com um resumo claro da sua avaliação.*
*Ex (Positivo): "The model's response was excellent and production-ready, demonstrating a deep understanding of the existing architecture through its methodical use of investigation tools."*
*Ex (Negativo): "While functionally correct, the generated code is not production-ready as it introduces significant tech debt by ignoring the project's state management patterns."*

### **2. Evidência (A Prova Técnica)**
*Aponte trechos de código específicos e use vocabulário técnico para apoiar sua tese.*
*Ex: "The evidence of its superior approach is in the initial `Tool Calls`. By using `find` to locate relevant files and `cat` to read `useChatStore.ts`, it correctly identified the `deleteSessionFromStore` selector, a step a more naive approach would have missed."*

### **3. Comparação (O Contraste de Engenharia)**
*Demonstre senioridade comparando a solução do modelo com uma abordagem alternativa.*
*Ex: "The model avoided the common pitfall of placing the copy logic directly in the event handler. By extracting it into a custom hook, it created a solution that is more testable, reusable, and aligned with modern React best practices, which is a significantly more scalable design."*

### **4. Conclusão (O Veredito Final)**
*Encerre com uma declaração final sobre o quão "pronto para produção" o código é.*
*Ex: "In conclusion, the code is merge-worthy with minor formatting clean-up. The model's investigative approach saved potential rework, prevented bugs, and resulted in a solution that seamlessly integrates with the existing codebase."*
