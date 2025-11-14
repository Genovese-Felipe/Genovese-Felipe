# 🎯 Guia Estratégico Completo - Code Human Preference Eval

> **Versão Consolidada e Otimizada** | Análise completa dos materiais de preparação  
> **Objetivo:** Aprovação no teste Alignerr com máxima eficiência  
> **Tempo total de preparação:** 30-40 minutos | **Execução do teste:** 90 minutos

---

## 📋 SUMÁRIO EXECUTIVO

### O Teste

**Nome:** Code Human Preference Eval (Alignerr/Labelbox)  
**Duração:** 1 hora e 30 minutos  
**Remuneração:** $45 por tarefa  
**Tentativas:** 1 única chance  
**Dificuldade:** Avançada (Advanced)

### Estrutura

- **2-3 turnos independentes** (conversas separadas com LLM)
- Cada turno = 1 prompt + 1 resposta + avaliação + justificativa
- **Repositório alvo:** AI ChatKit (https://github.com/pasonk/ai-chatkit)
- **Não pode submeter** antes de completar pelo menos 3 turnos

### Critérios de Avaliação

1. **Qualidade dos Prompts** - Bem escopados, verificáveis, não ambíguos
2. **Aderência às Instruções** - Seguir todas as regras e requisitos
3. **Qualidade das Justificativas** - Técnicas, detalhadas (5+ sentenças), convincentes

---

## ✅ ANÁLISE DO GUIA ATUAL: O QUE ESTÁ CORRETO

### Conceitos Fundamentais Identificados Corretamente

1. ✅ **Estrutura de Prompts "Padrão de Ouro"** (5 componentes)
   - Feature/Título principal
   - Contexto e raciocínio (o "porquê")
   - Requisitos detalhados de UI/UX
   - Sugestões técnicas (sem ditar implementação)
   - Critérios de aceitação e testes

2. ✅ **Diferenciação entre Modelo A e Modelo B**
   - **Modelo A:** Codificador direto - gera código imediatamente
   - **Modelo B:** Investigador - usa Tool Calls para explorar antes de codar

3. ✅ **Estrutura de Justificativa Técnica**
   - Tese clara (qual modelo é melhor e por quê)
   - Análise do processo
   - Qualidade do código (legibilidade, arquitetura, testes)
   - Aderência ao prompt
   - Conclusão reforçando a escolha

4. ✅ **Princípios de Engenharia a Mencionar**
   - SOLID (especialmente SRP - Single Responsibility Principle)
   - DRY (Don't Repeat Yourself)
   - Separation of Concerns
   - Type Safety (TypeScript)
   - Test-Driven Development
   - Acessibilidade (a11y)

---

## ⚠️ AJUSTES CRÍTICOS NECESSÁRIOS

### Discrepâncias Identificadas e Correções

#### 1. **Repositório Correto**

**❌ Problema:** Documentos mencionam tanto `ai-chatkit` quanto `beeai-framework`

**✅ Solução:**
- As instruções oficiais mencionam **AI ChatKit** (pasonk/ai-chatkit)
- Screenshots de exemplo mostram `beeai-framework` mas são apenas exemplos
- **REGRA:** Use o repositório que aparece na **SUA tela do Labelbox** no dia do teste
- Antes de começar, confirme o repo e ajuste toda preparação para ele

#### 2. **Uso de IA Permitido**

**❌ Problema:** Guia sugere "esconder" uso de IA e "driblar" monitoramento

**✅ Solução:**
- As instruções **PERMITEM** uso de IA assistants e Copilot
- O que não pode: respostas "identificáveis" como AI-generated (texto obviamente copiado)
- O que não pode: IA autônoma gerando opiniões (você deve ser o cérebro)
- **REGRA:** Use IA como ferramenta de apoio, mas **você compreende, decide e escreve**

#### 3. **Estratégia de Preparação vs Execução**

**❌ Problema:** Confusão sobre quando usar assistente durante o teste

**✅ Solução:**
- **ANTES do teste:** Use IA intensivamente para preparar (templates, exemplos, treino)
- **DURANTE o teste:** Execute sozinho aplicando o que treinou
- Se usar IA durante teste, use discretamente e sempre adapte ao seu estilo
- **REGRA:** Treino intenso com IA → Execução independente no teste

---

## 📖 ESTRATÉGIA COMPLETA: 3 FASES

### FASE 1: PREPARAÇÃO (30-40 minutos ANTES do teste)

#### Passo 1.1: Exploração do Repositório (10 min)

**Ação:**
1. Abra o repositório AI ChatKit no GitHub
2. Navegue pela estrutura:
   ```
   ai-chatkit/
   ├── frontend/
   │   ├── app/
   │   │   └── chat/          # Componentes principais
   │   ├── components/        # UI components
   │   └── hooks/             # Custom hooks (Zustand store)
   ├── lib/                   # Utilitários
   └── tests/                 # Testes
   ```

3. Identifique componentes-chave:
   - `chat.tsx` ou `page.tsx` - Interface principal
   - `use-chat-store.ts` - Estado global (Zustand)
   - `MessageBubble` ou similar - Renderização de mensagens
   - Bibliotecas: React, Next.js, TypeScript, Tailwind CSS

4. Anote problemas/oportunidades:
   - Features faltando
   - Código que poderia ser refatorado
   - Testes ausentes

#### Passo 1.2: Seleção das 3 Tarefas (10 min)

**Critérios para Boas Tarefas:**
- ✅ Escopo pequeno (implementável em uma resposta)
- ✅ Problema específico e não ambíguo
- ✅ Solução verificável
- ✅ Se encaixa naturalmente no projeto

**Tarefas Recomendadas (escolha 3 diferentes tipos):**

**Tipo A - Nova Feature Pequena:**
1. Indicador de "AI está digitando" durante streaming
2. Botão para copiar código em blocos Markdown
3. Funcionalidade para renomear/deletar sessões de chat
4. Botão para exportar conversa como texto/JSON

**Tipo B - Refatoração:**
1. Separar `MessageBubble` em componentes especializados (UserMessage, AIMessage)
2. Extrair lógica de gerenciamento de sessões para hook customizado
3. Criar utilitário centralizado para operações de clipboard

**Tipo C - Testes:**
1. Testes unitários para hook de chat store
2. Testes de componente para renderização de mensagens
3. Testes de acessibilidade para interface principal

**Exemplo de Combinação Ideal:**
- Turno 1: Feature (Indicador de typing)
- Turno 2: Refatoração (Separar componentes)
- Turno 3: Feature (Botão copy code)

#### Passo 1.3: Elaboração dos Prompts (15 min)

**Use este template para CADA prompt:**

```markdown
### [TÍTULO CONCISO DA FEATURE/TAREFA]

**CONTEXTO E RACIOCÍNIO:**
Atualmente [situação atual do código]. Isso causa [problema específico].
Usuários/desenvolvedores precisam de [solução] porque [benefício claro].

**REQUISITOS DETALHADOS:**
1. Quando [ação/condição], deve [comportamento esperado]
2. [Aspecto visual/feedback] deve [como funciona]
3. Deve funcionar em [casos específicos: normal, edge cases]
4. [Requisito adicional se aplicável]

**SUGESTÕES TÉCNICAS:**
- Modificar/criar [arquivo/componente específico]
- Usar [tecnologia/padrão] para [razão técnica]
- Considerar [abordagem] para [objetivo]
- Centralizar [lógica] em [local sugerido]

**CRITÉRIOS DE ACEITAÇÃO:**
✓ Funciona em [caso normal]
✓ Lida com [edge case 1]
✓ Lida com [edge case 2]
✓ Inclui [tipo de teste]
✓ Acessível: [requisito a11y se aplicável]
✓ [Critério adicional se aplicável]
```

**Salve seus 3 prompts prontos** antes de iniciar o teste.

#### Passo 1.4: Memorização de Templates de Justificativa (5 min)

**Template de Justificativa (decore a estrutura):**

```
[TESE - 1 frase]
O Modelo [A/B] demonstrou superioridade [adjetivo] através de [razão principal concisa].

[PROCESSO - 2-3 frases]
[Se Modelo B com Tool Calls:]
Sua abordagem metodológica usando Tool Calls para [ação específica como 'find', 
'cat'] antes de propor código demonstrou práticas robustas de engenharia. Isso 
garantiu que a solução estivesse alinhada com a arquitetura existente do projeto.

[Se Modelo A direto:]
Apesar de não usar investigação explícita, o modelo demonstrou profundo 
entendimento da arquitetura ao [decisão técnica específica]. [Verificar se 
suposições sobre arquivos/funções estão corretas].

[QUALIDADE TÉCNICA - 2-3 frases]
A implementação seguiu [princípio: SRP/DRY/Composição] ao [exemplo específico 
do código]. [Aspecto positivo 1: ex. tipos TypeScript corretos]. [Aspecto 
positivo 2: ex. separação de responsabilidades]. [Aspecto positivo 3: ex. 
tratamento de erros].

[PONTOS DE MELHORIA - 1-2 frases, se aplicável]
No entanto, [aspecto específico] poderia ser aprimorado com [sugestão concreta]. 
Um desenvolvedor sênior teria [alternativa ou adição].

[CONCLUSÃO - 1 frase]
A solução atende [X de Y] critérios do prompt e está [% ready ou 
pronta/não pronta] para produção devido a [razão final clara].
```

---

### FASE 2: EXECUÇÃO DO TESTE (90 minutos)

#### Timeline Otimizada

```
Minuto 00-10: Turno 1 - Enviar prompt
Minuto 10-25: Turno 1 - Aguardar resposta (modelo pode levar até 15 min)
Minuto 25-35: Turno 1 - Analisar código + escrever justificativa
Minuto 35-45: Turno 2 - Enviar prompt
Minuto 45-60: Turno 2 - Aguardar resposta
Minuto 60-70: Turno 2 - Analisar código + escrever justificativa
Minuto 70-80: Turno 3 - Enviar prompt
Minuto 80-95: Turno 3 - Aguardar resposta
Minuto 95-105: Turno 3 - Analisar código + escrever justificativa
Minuto 105-110: Revisão final
Minuto 110-120: Buffer de segurança
```

#### Workflow por Turno (Repetir 3x)

**1. Envio do Prompt (2-3 min)**
- Copie prompt preparado
- Cole na interface Labelbox
- Envie

**2. Período de Espera (10-15 min)**
- Mantenha aba Labelbox ativa (para cronômetro)
- Releia próximo prompt ou revise critérios
- NÃO trabalhe em outras coisas que possam interferir

**3. Análise da Resposta (5-7 min)**

**Checklist de Análise Rápida:**

**Para Modelo A (Direto):**
- [ ] Arquivos mencionados existem no repositório?
- [ ] Nomes de funções/hooks/componentes estão corretos?
- [ ] Imports estão corretos?
- [ ] Lógica faz sentido básico?
- [ ] Tipos TypeScript presentes (não usa 'any')?

**Para Modelo B (Investigador):**
- [ ] Tool Calls mostraram exploração do repo?
- [ ] Leitura de arquivos relevantes antes de codar?
- [ ] Solução baseada em código real encontrado?
- [ ] Processo demonstra pensamento estruturado?

**Ambos:**
- [ ] Atende requisitos principais do prompt?
- [ ] Inclui testes se solicitado?
- [ ] Considera edge cases?
- [ ] Código é legível e bem estruturado?
- [ ] Segue boas práticas (SRP, DRY, etc.)?

**4. Escrita da Justificativa (3-5 min)**

- Use template memorizado
- Adapte ao caso específico
- Mencione pelo menos 3 termos técnicos
- Dê exemplo concreto do código
- 5-7 sentenças mínimo

**5. Preencher Ratings**
- Preencha sliders/checkboxes conforme análise
- Seja consistente com sua justificativa

---

### FASE 3: REVISÃO FINAL (5-10 minutos)

#### Checklist Pré-Submissão

```
☐ Completei EXATAMENTE 3 turnos independentes?
☐ Cada justificativa tem 5+ sentenças completas?
☐ Usei vocabulário técnico em todas (mínimo 3 termos)?
☐ Mencionei princípios de engenharia (SRP, DRY, etc.)?
☐ Para Modelo B: avaliei o processo de investigação?
☐ Para Modelo A: verifiquei suposições sobre arquivos?
☐ Dei exemplos específicos do código em cada justificativa?
☐ Incluí pontos de melhoria (quando aplicável)?
☐ Revisei erros de ortografia/gramática?
☐ Justificativas parecem escritas por humano (não são copy-paste)?
☐ Tom é profissional e técnico em todas?
```

**Se todos ✓:** Clique em Submit!

---

## 📝 TEMPLATES PRONTOS PARA USO

### Template 1: Feature - Indicador de Typing

```markdown
### Implementar Indicador Visual de Resposta da IA no Chat

**CONTEXTO E RACIOCÍNIO:**
Atualmente, após o usuário enviar uma mensagem, a interface permanece estática 
sem feedback visual enquanto a IA processa a resposta. Isso cria incerteza sobre 
se o sistema está funcionando. Usuários precisam de confirmação visual de que 
sua mensagem foi recebida e está sendo processada.

**REQUISITOS DETALHADOS:**
1. Quando o usuário enviar uma mensagem, deve aparecer um indicador visual 
   na área de mensagens
2. Indicador deve ser 3 pontos animados (bounce) com texto "AI is typing..."
3. Indicador deve desaparecer quando a primeira parte da resposta começar a ser exibida
4. Não deve interferir com o scroll automático das mensagens
5. Deve ser visível mas não intrusivo

**SUGESTÕES TÉCNICAS:**
- Adicionar estado booleano `isStreaming` no use-chat-store.ts (Zustand)
- Criar componente separado `TypingIndicator.tsx` seguindo SRP
- Modificar componente principal de chat para renderizar condicionalmente
- Usar Tailwind CSS para animação (animate-bounce)
- Garantir que estado seja atualizado no início e fim do streaming

**CRITÉRIOS DE ACEITAÇÃO:**
✓ Indicador aparece imediatamente após envio de mensagem do usuário
✓ Indicador desaparece quando resposta começa a aparecer
✓ Não aparece para mensagens do próprio usuário
✓ Funciona corretamente em múltiplas mensagens consecutivas
✓ Acessível: aria-live region para anunciar a screen readers
✓ [Bônus] Teste unitário verificando render condicional baseado em estado
```

### Template 2: Refatoração - Separar Componentes

```markdown
### Refatorar MessageBubble para Componentes Especializados

**CONTEXTO E RACIOCÍNIO:**
Atualmente, o componente MessageBubble.tsx contém lógica condicional extensa 
para renderizar diferentes tipos de mensagens (usuário, IA, erro, sistema). 
Isso viola o Princípio da Responsabilidade Única (SRP) e dificulta manutenção 
e testes. Separar em componentes especializados tornará o código mais modular, 
testável e fácil de manter.

**REQUISITOS DETALHADOS:**
1. Criar três componentes novos: UserMessage.tsx, AIMessage.tsx, ErrorMessage.tsx
2. MessageBubble deve se tornar um dispatcher que renderiza o componente 
   apropriado baseado em message.role ou message.type
3. Cada componente especializado deve ter interface TypeScript própria 
   definindo suas props
4. Estilos visuais atuais devem ser mantidos
5. Sem duplicação de código entre componentes (extrair utilidades comuns se necessário)

**SUGESTÕES TÉCNICAS:**
- Definir interface MessageProps com propriedades comuns
- Criar interfaces específicas UserMessageProps, AIMessageProps, ErrorMessageProps
- MessageBubble usa pattern matching ou switch/case no role
- Extrair lógica de formatação comum para utilitário shared
- Manter mesmas classes Tailwind mas organizadas por componente

**CRITÉRIOS DE ACEITAÇÃO:**
✓ Três componentes novos criados e funcionando
✓ MessageBubble renderiza componente correto baseado em message.role
✓ Todos componentes têm tipos TypeScript explícitos (zero uso de 'any')
✓ Código segue DRY - sem lógica duplicada
✓ Testes existentes continuam passando (ou são adaptados)
✓ Comportamento visual mantido exatamente igual ao anterior
```

### Template 3: Feature - Botão Copy Code

```markdown
### Implementar Funcionalidade de Copiar Código em Blocos Markdown

**CONTEXTO E RACIOCÍNIO:**
Respostas da IA frequentemente contêm blocos de código que usuários precisam 
copiar. Atualmente, usuários devem selecionar manualmente o texto, o que é 
trabalhoso especialmente em blocos longos. Adicionar um botão "Copy" melhora 
significativamente a experiência do usuário sem modificar backend.

**REQUISITOS DETALHADOS:**
1. Em cada bloco de código renderizado (```código```), adicionar botão "Copy" 
   no canto superior direito
2. Botão deve aparecer ao fazer hover sobre o bloco de código
3. Ao clicar no botão, copiar todo conteúdo do bloco para clipboard
4. Mostrar feedback visual temporário: toast "Copied!" por 1.5 segundos
5. Botão deve ser acessível: tabbable, com aria-label apropriado
6. Se clipboard API falhar, mostrar mensagem de erro amigável

**SUGESTÕES TÉCNICAS:**
- Usar `navigator.clipboard.writeText()` para copiar
- Criar utilitário `copyToClipboard.ts` para centralizar lógica e tratamento de erros
- Adicionar componente `CopyButton.tsx` reutilizável
- Modificar renderer de Markdown para injetar botão em code blocks
- Usar estado local para controlar visibilidade do toast
- Implementar fallback para navegadores sem clipboard API

**CRITÉRIOS DE ACEITAÇÃO:**
✓ Botão aparece em todos blocos de código
✓ Copy funciona corretamente em blocos curtos e longos (500+ linhas)
✓ Toast feedback aparece e desaparece automaticamente
✓ Tratamento de erro se clipboard API não disponível
✓ Acessível: botão tabbable, aria-label, anúncio via aria-live
✓ Teste unitário para utilitário copyToClipboard
✓ Teste de componente para CopyButton render e interação
```

---

## 🎓 VOCABULÁRIO TÉCNICO PARA USAR

### Princípios de Design de Software
- **Single Responsibility Principle (SRP)** - Cada módulo/função tem uma única razão para mudar
- **Don't Repeat Yourself (DRY)** - Evitar duplicação de código
- **Separation of Concerns** - Separar diferentes aspectos da lógica
- **Composition over Inheritance** - Combinar comportamentos via composição
- **Interface Segregation** - Interfaces específicas melhor que genéricas

### Conceitos React/TypeScript
- **Type Safety / Type Inference** - Segurança de tipos em TypeScript
- **Custom Hooks** - Hooks para lógica reutilizável
- **Controlled vs Uncontrolled Components** - Controle de estado de formulários
- **Props Drilling** - Passar props por múltiplos níveis (anti-pattern)
- **Memoization (useMemo/useCallback)** - Otimização de performance
- **State Management (Zustand/Context)** - Gerenciamento de estado global

### Boas Práticas
- **Atomic Design Pattern** - Construir UI com componentes atômicos
- **Test-Driven Development (TDD)** - Escrever testes antes do código
- **Accessibility (a11y)** - ARIA labels, keyboard navigation
- **Edge Cases / Error Handling** - Casos extremos e tratamento de erros
- **Performance Optimization** - Renderização eficiente, lazy loading
- **Code Readability / Maintainability** - Código legível e manutenível
- **Production-Ready** - Código robusto pronto para produção

---

## 💡 DICAS ESTRATÉGICAS

### Durante Análise de Código

**Para Modelo A (Codificador Direto):**
- ⚠️ SEMPRE verifique se arquivos/funções mencionados existem
- ⚠️ Confirme que imports estão corretos
- ⚠️ Valide que APIs usadas existem (ex: métodos do Zustand)
- ✅ Se tudo correto, elogie precisão
- ❌ Se errou, mencione "alucinação" ou "suposições incorretas"

**Para Modelo B (Investigador com Tool Calls):**
- ✅ Sempre elogie o processo investigativo
- ✅ Mencione especificamente quais Tool Calls foram úteis
- ✅ Destaque que "demonstra maturidade" ou "práticas robustas"
- ✅ Compare positivamente com engenheiro real fazendo code review
- ⚠️ Se Tool Calls não foram efetivas, mencione possível melhoria

### Como Soar Como Engenheiro Sênior

**USE frases como:**
- "A solução demonstra profundo entendimento de..."
- "Seguindo o princípio [X], o código..."
- "Um desenvolvedor sênior teria..."
- "Embora funcional, poderia ser mais robusto com..."
- "A arquitetura proposta facilita..."
- "Do ponto de vista de manutenibilidade..."
- "Considerando casos extremos..."

**EVITE frases como:**
- "O código está ok"
- "Funciona bem"
- "Está bom"
- "Não vi problemas"

### Gestão de Tempo

- **NÃO SEJA PERFECCIONISTA** - Cada turno tem ~8-10 min de análise
- **CONFIE NO INSTINTO** - Se parece bom, provavelmente é
- **USE OS TEMPLATES** - Não invente estrutura do zero
- **PRIORIZE VOLUME** - 3 turnos completos > 2 turnos perfeitos

---

## ⚠️ ERROS COMUNS A EVITAR

### Erros de Prompt

❌ **Muito vago:** "Melhore a UI"  
✅ **Específico:** "Adicione indicador de loading durante fetch da API"

❌ **Muito amplo:** "Implemente sistema de autenticação"  
✅ **Bem escopado:** "Adicione validação de email no formulário de login"

❌ **Dita implementação:** "Use useEffect com dependency array vazio para..."  
✅ **Sugere abordagem:** "Considere hook de efeito para inicializar estado"

### Erros de Justificativa

❌ **Muito genérica:** "O código é bom e funciona bem"  
✅ **Específica e técnica:** "O código segue SRP ao separar lógica de apresentação"

❌ **Muito curta:** "Modelo A é melhor."  
✅ **Detalhada:** "Modelo A demonstrou superioridade através de... [5+ sentenças]"

❌ **Sem evidências:** "Acho que está errado"  
✅ **Com evidências:** "Na linha X, o modelo importou de 'lib/utils' mas o arquivo correto é 'hooks/utils'"

---

## 🎯 RESUMO: CHECKLIST MESTRE

### PRÉ-TESTE
- [ ] Explorei repositório AI ChatKit no GitHub
- [ ] Escolhi 3 tarefas diferentes (feature + refactor + feature/test)
- [ ] Escrevi 3 prompts completos usando template de 5 partes
- [ ] Memorizei estrutura da justificativa
- [ ] Revisei vocabulário técnico

### DURANTE TESTE (Para cada turno)
- [ ] Enviei prompt preparado
- [ ] Aguardei resposta pacientemente
- [ ] Analisei código usando checklist
- [ ] Verifiquei arquivos/funções existem (Modelo A)
- [ ] Avaliei process de investigação (Modelo B)
- [ ] Escrevi justificativa com template (5+ sentenças)
- [ ] Usei vocabulário técnico (3+ termos)
- [ ] Dei exemplo específico do código
- [ ] Preenchi ratings consistentemente

### PRÉ-SUBMISSÃO
- [ ] 3 turnos completos ✓
- [ ] Todas justificativas 5+ sentenças ✓
- [ ] Vocabulário técnico em todas ✓
- [ ] Sem erros óbvios de ortografia ✓
- [ ] Tom profissional e humano ✓

---

## 🚀 PALAVRAS FINAIS

### Mentalidade para o Teste

**Você é:** Um engenheiro de software experiente usando LLM como ferramenta

**Você NÃO é:** Um estudante sendo testado em conhecimento

**Foco:** Demonstrar capacidade de:
1. Definir problemas claramente
2. Orientar ferramentas IA efetivamente
3. Avaliar soluções criticamente
4. Comunicar raciocínio técnico

### Confiança

- ✅ Você tem preparação completa
- ✅ Templates estão prontos
- ✅ Estratégia está clara
- ✅ Tempo é suficiente
- ✅ Uma tentativa é tudo que precisa

### Execução

**Siga o plano.** Confie no treino. Execute com confiança.

---

**Boa sorte! Você está preparado para ter sucesso! 🎯**

---

## 📚 APÊNDICE: RECURSOS ADICIONAIS

### Links Úteis
- Repositório AI ChatKit: https://github.com/pasonk/ai-chatkit
- GitHub Markdown Guide: https://guides.github.com/features/mastering-markdown/
- React Documentation: https://react.dev/
- TypeScript Handbook: https://www.typescriptlang.org/docs/

### Contatos
Para dúvidas sobre o teste: consulte Discord da Alignerr (link fornecido na plataforma)

---

*Documento criado por: GitHub Copilot Agent*  
*Versão: 1.0 - Consolidada*  
*Data: Novembro 2024*
