# 🎯 Plano Estratégico Completo - Code Human Preference Eval

## Análise das Instruções e Guias Existentes

### ✅ O Que Está Correto nos Guias Atuais

Após análise detalhada de todos os planos (plano-1 a plano-6), identifiquei os seguintes pontos corretos e bem elaborados:

1. **Estrutura de Prompts "Padrão de Ouro"** - A estrutura de 5 pontos está alinhada com as melhores práticas
2. **Identificação dos Modelos A vs B** - Distinção clara entre modelo investigativo e codificador direto
3. **Ênfase em Justificativas Técnicas** - Foco em argumentação detalhada (5+ frases) com vocabulário sênior
4. **Compreensão dos Requisitos** - Entendimento correto de 2-3 turnos independentes, tempo de 1h30min
5. **Análise do Repositório** - Necessidade de explorar o AI ChatKit antes de elaborar tarefas

### ⚠️ Ajustes Críticos Necessários

1. **Discrepância de Repositório**
   - As instruções oficiais mencionam `pasonk/ai-chatkit`
   - Alguns screenshots mostram `beeai-framework`
   - **AÇÃO**: Verificar qual repositório aparece na tela da Labelbox no dia do teste

2. **Uso Ético de IA**
   - As instruções **PERMITEM** uso de IA como ferramenta
   - O que **NÃO É PERMITIDO**: uso autônomo/assíncrono de IA para gerar opiniões
   - O que **É PERMITIDO**: Copilots e assistentes de IA se você acompanhar, entender e decidir
   - **AJUSTE**: Não é necessário "esconder" o uso de IA; o importante é que as respostas pareçam escritas por você

3. **Gerenciamento de Tempo**
   - 1h30min com possível espera de 15min por resposta do modelo
   - **CRÍTICO**: Planejar timeline agressiva para completar 3 turnos

---

## 📋 Plano Passo a Passo Definitivo

### FASE PRÉ-TESTE: Preparação Estratégica (Fazer ANTES do teste)

#### 1. Análise do Repositório (30-45 minutos)

**Objetivo**: Familiarizar-se profundamente com o codebase para identificar tarefas realistas

**Passos**:
1. Acessar o repositório no GitHub: https://github.com/pasonk/ai-chatkit
2. Navegar pela estrutura:
   - `/frontend/app/chat` - Páginas principais
   - `/frontend/components` - Componentes React
   - `/frontend/hooks` - Custom hooks (especialmente `use-chat-store.ts`)
   - `/frontend/lib` - Utilitários
3. Identificar tecnologias:
   - React + Next.js
   - TypeScript
   - Zustand (gerenciamento de estado)
   - Tailwind CSS
4. Anotar componentes-chave e suas responsabilidades

**Deliverable**: Lista de 5-7 possíveis tarefas bem escopadas

#### 2. Elaboração de 3 Tarefas Bem Escopadas

**Critérios para Tarefa Bem Escopada**:
- ✅ Específica e inequívoca
- ✅ Verificável (pode confirmar se foi resolvida)
- ✅ Escopo limitado (completável em uma resposta)
- ✅ Realista para o projeto
- ❌ EVITAR: tarefas vagas, subjetivas ou muito amplas

**Tipos de Tarefas Recomendadas**:
1. **Nova Feature Pequena**: Ex: botão "copy code", indicador de digitação, exportar conversa
2. **Refatoração Localizada**: Ex: separar componente grande em componentes especializados
3. **Testes**: Ex: testes unitários para hook ou componente específico

**Exemplos de Tarefas Prontas** (baseadas em análises dos exemplos bem-sucedidos):

##### Tarefa 1: Typing Indicator
```
Título: Implementar indicador visual de "AI está respondendo"

Contexto: Após o usuário enviar uma mensagem, a UI fica estática 
sem feedback visual. Usuários não sabem se o sistema está processando 
a resposta.

Problema: Falta de feedback durante o tempo de processamento prejudica 
a UX e pode fazer o usuário pensar que o sistema travou.

Requisitos de UI/UX:
1. Quando a resposta da IA começar a ser gerada, mostrar indicador 
   visual na parte inferior da lista de mensagens
2. Indicador deve ser 3 pontos animados ou texto "AI is typing..."
3. Desaparecer automaticamente quando a resposta completa for exibida
4. Não deve interferir no scroll automático da conversa

Sugestões Técnicas:
- Adicionar estado `isStreaming: boolean` no use-chat-store.ts (Zustand)
- Criar componente separado `TypingIndicator.tsx` para reutilização
- Modificar chat.tsx para renderizar condicionalmente o indicador
- Usar Tailwind CSS para animação dos pontos

Critérios de Aceitação:
✓ Indicador visível apenas durante streaming de resposta
✓ Não aparece para mensagens do usuário
✓ Animação suave e não intrusiva
✓ [Bônus] Teste unitário verificando render quando isStreaming=true
```

##### Tarefa 2: Refactor Message Components
```
Título: Refatorar MessageBubble.tsx para componentes especializados

Contexto: Atualmente, o componente MessageBubble.tsx contém lógica 
condicional para renderizar diferentes tipos de mensagem (mensagens 
do usuário, da IA, e erros).

Problema: Viola o Princípio da Responsabilidade Única (SRP), tornando 
o componente difícil de manter e testar.

Requisitos:
1. Criar 3 componentes especializados:
   - UserMessage.tsx - renderiza mensagens do usuário
   - AIMessage.tsx - renderiza mensagens da IA
   - ErrorMessage.tsx - renderiza mensagens de erro
2. MessageBubble torna-se um dispatcher que seleciona qual componente 
   renderizar baseado em message.role
3. Cada componente especializado deve ter suas próprias props tipadas 
   (interfaces TypeScript claras)
4. Manter o estilo visual atual (sem quebrar a UI)

Sugestões Técnicas:
- Extrair lógica específica de cada tipo para seu componente
- Usar composição ao invés de herança
- Definir interface MessageProps específica para cada componente
- Evitar duplicação de código compartilhado

Critérios de Aceitação:
✓ Código mais modular e fácil de testar
✓ Tipos TypeScript explícitos (sem uso de 'any')
✓ Sem duplicação de código (princípio DRY)
✓ Funcionalidade atual preservada
✓ [Bônus] Exemplos de teste unitário para cada componente
```

##### Tarefa 3: Copy Code Feature
```
Título: Implementar funcionalidade "Copy Code" em blocos de código Markdown

Contexto: As respostas da IA frequentemente incluem blocos de código. 
Atualmente, usuários precisam selecionar manualmente o texto para 
copiar snippets.

Benefício: Adicionar um botão de cópia melhora significativamente a 
experiência do usuário ao trabalhar com código, sem tocar no backend.

Requisitos de UI/UX:
1. Ao passar o mouse sobre um bloco de código, mostrar botão "Copy" 
   no canto superior direito
2. Ao clicar, copiar todo o conteúdo do bloco para o clipboard
3. Mostrar toast de feedback "Copied!" por 1.5 segundos
4. Acessibilidade: botão deve ser tabbable e ter aria-label adequado
5. Anunciar via aria-live para leitores de tela

Sugestões Técnicas:
- Usar navigator.clipboard.writeText() API
- Criar utilitário copyToClipboard.ts para centralizar lógica de 
  clipboard e tratamento de erros
- Criar componente CopyButton.tsx reutilizável
- Integrar com o renderizador de Markdown atual

Critérios de Aceitação:
✓ Funciona em blocos de código longos (>500 linhas)
✓ Trata erro gracefully se clipboard API falhar
✓ Texto copiado exatamente como no código original (preserva formatação)
✓ Teste unitário para o utilitário copyToClipboard
✓ Teste de componente para CopyButton
✓ Teste de acessibilidade (a11y)
```

#### 3. Memorizar Templates

##### Template de Prompt (Estrutura de 5 Partes)
```
[1. TÍTULO/FEATURE]
Descrição curta e clara da funcionalidade

[2. CONTEXTO + PORQUÊ]
- Situação atual
- Problema identificado
- Impacto/necessidade

[3. REQUISITOS DETALHADOS DE UI/UX]
- Passo 1: Quando [ação], deve [comportamento]
- Passo 2: [Estado visual/feedback]
- Passo 3: [Casos específicos]

[4. SUGESTÕES TÉCNICAS]
- Sugestão de arquivos/componentes a modificar
- Tecnologias ou padrões recomendados
- Onde centralizar lógica
- [Evitar prescrever implementação exata linha por linha]

[5. CRITÉRIOS DE ACEITAÇÃO]
✓ Funciona em [caso normal]
✓ Lida com [edge case 1]
✓ Lida com [edge case 2]
✓ Inclui [tipo de teste]
✓ [Requisito de acessibilidade se aplicável]
```

##### Template de Justificativa (Estrutura de 5+ Sentenças)
```
[TESE - 1 frase forte e clara]
O Modelo [A/B] é superior porque [razão principal concisa].

[PROCESSO - 2-3 frases]
[Se Modelo B]: A abordagem investigativa demonstrou maturidade ao 
primeiro executar [mencione Tool Calls específicas]. Isso garantiu 
que a solução proposta estivesse alinhada com a arquitetura existente 
do projeto. [Detalhes sobre o que ele investigou]

[Se Modelo A]: Apesar de não usar investigação explícita via Tool 
Calls, o modelo demonstrou profundo entendimento da arquitetura ao 
corretamente identificar [mencione decisões técnicas específicas]. 
[Avalie se as suposições estavam corretas]

[QUALIDADE DO CÓDIGO - 2-3 frases]
A implementação seguiu [mencione princípio: SRP/DRY/SOLID/etc] ao 
[exemplo específico do código]. A separação de [X] em [Y] demonstra 
boa modularidade e facilita manutenção futura. O uso de 
[TypeScript/hooks/padrão específico] foi [apropriado/poderia ser 
melhorado porque...].

[PONTOS POSITIVOS E NEGATIVOS - 1-2 frases]
Pontos fortes incluem [listar 2-3]. No entanto, [ponto de melhoria 
específico se houver]. Um desenvolvedor sênior teria [o que faria 
diferente ou o que elogiaria].

[CONCLUSÃO - 1 frase]
Portanto, considerando [critério principal: robustez/manutenibilidade/
aderência ao prompt], o Modelo [X] entrega uma solução [pronta/não 
pronta] para produção porque [razão final específica].
```

---

### FASE TESTE: Execução (1h30min cronometrados)

#### Timeline Recomendada

```
00:00 - 00:10  →  Turno 1: Digitar e enviar prompt
00:10 - 00:25  →  Aguardar resposta do modelo (simular atividade)
00:25 - 00:35  →  Analisar código + Escrever justificativa Turno 1

00:35 - 00:45  →  Turno 2: Digitar e enviar prompt
00:45 - 01:00  →  Aguardar resposta do modelo (simular atividade)
01:00 - 01:10  →  Analisar código + Escrever justificativa Turno 2

01:10 - 01:20  →  Turno 3: Digitar e enviar prompt
01:20 - 01:35  →  Aguardar resposta do modelo (simular atividade)
01:35 - 01:45  →  Analisar código + Escrever justificativa Turno 3

01:45 - 01:50  →  Revisão final e SUBMIT
```

#### Protocolo para Cada Turno (Repetir 3x)

**1. Envio do Prompt (2-3 minutos)**
- Acessar prompt preparado (já deve estar pronto)
- Digitar na plataforma Labelbox
- Enviar e registrar hora de envio

**2. Período de Espera (10-15 minutos)**
- A resposta pode levar até 15 minutos
- **Durante a espera**: Revisar próximo prompt ou navegar pelo repositório
- Manter a aba Labelbox aberta (para tracking do timer)

**3. Análise da Resposta (5-7 minutos)**

**Checklist de Análise Rápida**:
- [ ] O modelo gerou código ou só explicação?
- [ ] Arquivos mencionados existem no repositório?
- [ ] Nomes de componentes/hooks estão corretos?
- [ ] Tipos TypeScript estão presentes? (ou usou 'any'?)
- [ ] Tratamento de erros está incluído?
- [ ] Testes foram mencionados/criados?
- [ ] Atende aos critérios do prompt?

**Para Modelo B (Investigativo)**:
- [ ] Quais Tool Calls foram usadas? (find, cat, ls, etc.)
- [ ] O que ele investigou antes de codar?
- [ ] As investigações foram relevantes?
- [ ] A solução final reflete o que ele descobriu?

**Para Modelo A (Codificador Direto)**:
- [ ] Quais suposições ele fez? (arquivos, imports, APIs)
- [ ] As suposições estão corretas? (verificar no repo se possível)
- [ ] Há "alucinações" (código inventado que não existe)?

**4. Redação da Justificativa (3-5 minutos)**

**Usando o Template Memorizado**:
1. Escrever tese clara (Modelo X é melhor porque Y)
2. Descrever processo (investigativo ou direto)
3. Avaliar qualidade técnica (mencionar 2-3 princípios)
4. Apontar pontos fortes e fracos específicos
5. Concluir com veredicto sobre production-readiness

**Vocabulário Técnico para Incluir**:
- Princípios: SRP, DRY, SOLID, Separation of Concerns, Composição
- React/TS: Type safety, Custom hooks, Props drilling, Memoization
- Práticas: TDD, Accessibility (a11y), Error handling, Edge cases
- Qualidade: Modularidade, Manutenibilidade, Robustez, Testabilidade

**5. Atribuição de Ratings**
- Preencher os sliders/dropdowns da plataforma
- Baseie-se na análise feita
- Seja consistente com a justificativa escrita

---

### FASE PÓS-TURNOS: Revisão Final (5-10 minutos)

#### Checklist Pré-Submissão

**Obrigatório verificar**:
- [ ] Completei EXATAMENTE 3 turnos independentes?
- [ ] Cada justificativa tem pelo menos 5 frases?
- [ ] Usei vocabulário técnico específico (não genérico)?
- [ ] Mencionei princípios de engenharia (SRP, DRY, etc.)?
- [ ] Avaliei o PROCESSO do modelo (não apenas resultado)?
- [ ] Dei exemplos específicos do código em cada justificativa?
- [ ] Incluí pelo menos um ponto de melhoria ou crítica construtiva?
- [ ] Revisei erros de ortografia/gramática?

**Verificação de Qualidade**:
- [ ] Minhas justificativas demonstram pensamento sênior?
- [ ] Usei evidências concretas (não opiniões vagas)?
- [ ] Comparei processo/abordagem entre diferentes modelos se aplicável?
- [ ] Meu tom é profissional e confiante?

**Apenas após todos os checks**: Clicar em SUBMIT

---

## 🎓 Guia de Melhores Práticas

### Como Demonstrar Nível Sênior

#### 1. Na Análise do Código

**❌ Análise Superficial (Júnior)**:
> "O código está bom. Funciona e não tem erros óbvios."

**✅ Análise Profunda (Sênior)**:
> "A implementação demonstra arquitetura sólida ao extrair a lógica 
> de clipboard para um utilitário separado (copyToClipboard.ts), 
> seguindo o princípio DRY. O uso de TypeScript com interfaces 
> explícitas (CopyButtonProps) garante type safety. No entanto, a 
> ausência de tratamento para o caso em que navigator.clipboard 
> não está disponível (browsers antigos) representa uma falha em 
> robustez."

#### 2. Na Avaliação de Testes

**❌ Avaliação Básica**:
> "Tem testes, então está bom."

**✅ Avaliação Técnica**:
> "A suíte de testes cobre o 'happy path', mas não inclui edge cases 
> críticos como: (1) timeout do clipboard, (2) permissões negadas, 
> (3) conteúdo muito grande. Um desenvolvedor sênior implementaria 
> testes usando React Testing Library para simular esses cenários e 
> verificar o comportamento do componente."

#### 3. Na Comparação de Modelos

**❌ Comparação Vaga**:
> "Modelo B é melhor porque pensou mais antes de codar."

**✅ Comparação Específica**:
> "Modelo B demonstrou superioridade ao executar `find . -name 
> "*store*"` e `cat use-chat-store.ts` antes de propor modificações. 
> Isso garantiu que o novo campo `isStreaming` foi adicionado 
> respeitando a interface existente do Zustand, evitando breaking 
> changes. Modelo A, sem essa investigação prévia, arriscaria 
> suposições incorretas sobre a estrutura da store."

### Termos Técnicos Essenciais por Categoria

#### Arquitetura e Design Patterns
- Single Responsibility Principle (SRP)
- Don't Repeat Yourself (DRY)
- SOLID principles
- Separation of Concerns
- Composition over Inheritance
- Dependency Injection
- Factory Pattern
- Observer Pattern

#### React e TypeScript
- Type safety / Type inference
- Generic types
- Interface vs Type
- Custom hooks
- Controlled vs Uncontrolled components
- Props drilling
- React Context
- State management (Zustand, Redux)
- useEffect dependencies
- useMemo / useCallback optimization
- React.memo for performance

#### Testes
- Test-Driven Development (TDD)
- Unit tests vs Integration tests
- Test coverage
- Mocking dependencies
- React Testing Library patterns
- Accessibility testing (a11y)
- Edge case coverage
- Error boundary testing

#### Qualidade de Código
- Cyclomatic complexity
- Code smell
- Refactoring
- Technical debt
- Maintainability
- Scalability
- Performance optimization
- Lazy loading
- Code splitting

#### Acessibilidade
- ARIA labels
- Semantic HTML
- Keyboard navigation
- Screen reader support
- Focus management
- WCAG compliance

---

## 📊 Análise de Exemplos Bons vs Ruins

### Exemplo de Prompt RUIM ❌

```
"refactor the logging and configuration system to make the output 
more human readable and pretty like a json file and show the code 
changes in files and example of the output"

Problemas:
- Muito subjetivo ("pretty", "human readable")
- Escopo mal definido ("system" inteiro?)
- Critérios de aceitação vagos
- Não especifica PORQUÊ
```

### Exemplo de Prompt BOM ✅

```
"Implement a reusable RadioSelectorCard component to replace the 
existing multiple implementations present in the ecomm user journeys. 
They all deliver the same UI/UX experience, but for whatever reason 
were implemented over and over."

Por quê é bom:
✓ Problema específico (duplicação de código)
✓ Escopo claro (um componente)
✓ Contexto fornecido (múltiplas implementações existentes)
✓ Verificável (pode confirmar se duplicações foram eliminadas)
```

### Exemplo de Justificativa RUIM ❌

```
"O modelo fez um bom trabalho. O código funciona e parece correto. 
Não vi problemas graves. Está pronto para produção."

Problemas:
- Vago e genérico
- Sem evidências específicas
- Sem vocabulário técnico
- Sem análise do processo
- Muito curto (<5 frases substantivas)
```

### Exemplo de Justificativa BOA ✅

```
"O Modelo B demonstrou clara superioridade através de sua metodologia 
sistemática. Antes de propor código, ele executou Tool Calls para 
mapear a arquitetura (`find` para localizar stores, `cat` para 
inspecionar use-chat-store.ts), garantindo que sua solução estivesse 
perfeitamente alinhada com o design existente.

Tecnicamente, a implementação é exemplar: (1) adiciona o estado 
`isStreaming` à store Zustand usando a sintaxe idiomática `set()`, 
(2) cria um componente `TypingIndicator` isolado e reutilizável 
seguindo o SRP, e (3) integra condicionalmente no chat.tsx sem 
poluir a lógica existente. O uso de Tailwind com classes de 
animação (`animate-bounce`) demonstra atenção aos detalhes de UX.

Pontos fortes adicionais incluem tipos TypeScript explícitos sem 
uso de 'any' e separação clara de responsabilidades entre state 
management e apresentação. Um ponto de melhoria seria a ausência 
de testes unitários explicitamente mencionados no critério de 
aceitação, embora a arquitetura modular facilite sua adição 
posterior via React Testing Library.

A solução atende 4 de 5 critérios do prompt e está 90% 
production-ready. Com a adição de testes automatizados para 
verificar o render condicional e o comportamento da store, 
seria imediatamente merge-worthy."

Por quê é boa:
✓ Tese clara no início
✓ Análise detalhada do processo
✓ Vocabulário técnico específico (SRP, Zustand, idiomático)
✓ Evidências concretas do código
✓ Balanced (pontos fortes E fracos)
✓ Conclusão com veredicto fundamentado
✓ Muito mais que 5 frases
```

---

## 🚀 Dicas Finais de Execução

### Antes do Teste

1. **Durma Bem**: Clareza mental é crucial para análise técnica
2. **Revise Templates**: Releia estruturas de prompt e justificativa
3. **Familiarize-se com o Repo**: Navegue pelo AI ChatKit antecipadamente
4. **Tenha Água/Café**: 1h30min requer foco contínuo

### Durante o Teste

1. **Mantenha a Calma**: Se um turno sair diferente do esperado, continue
2. **Gerencie o Tempo**: Use timer para não exceder tempo por turno
3. **Confie no Treino**: Você praticou, execute no automático
4. **Não Persiga Perfeição**: 80% muito bom é melhor que 100% não entregue

### Erros Comuns a Evitar

❌ Gastar 40 minutos no primeiro turno (vai faltar tempo)
❌ Não verificar se completou 3 turnos antes de submeter
❌ Copiar/colar justificativas genéricas de IA sem adaptar
❌ Escrever prompts com escopo muito amplo
❌ Justificativas curtas (<5 frases) ou muito vagas
❌ Não mencionar princípios técnicos (SRP, DRY, etc.)
❌ Ignorar o processo do modelo (focar só no resultado final)

### Se Algo Der Errado

- **Modelo demorar >15min**: Continue com próximo turno, volte se der tempo
- **Resposta parcial/quebrada**: Avalie o que foi entregue honestamente
- **Modelo "alucinar" código**: Aponte isso na justificativa como falha crítica
- **Ficar sem tempo**: Submeta o que tem (melhor parcial que nada)

---

## 📝 Sumário Executivo

### O Que Precisa Ser Entregue (Deliverables em Inglês)

1. **3 High-Quality Prompts** seguindo estrutura de 5 partes
2. **3 Detailed Justifications** (5+ sentences each) demonstrando expertise
3. **Rating Scores** consistentes com as justificativas
4. **Evidence of Senior-Level Thinking** através de:
   - Technical vocabulary usage
   - Engineering principles application
   - Process evaluation (not just results)
   - Specific code examples and evidence
   - Balanced analysis (pros and cons)

### Critérios de Sucesso

Você será aprovado se demonstrar:
- ✅ Habilidade de criar prompts claros e bem escopados
- ✅ Capacidade de avaliar código criticamente
- ✅ Comunicação técnica eficaz e convincente
- ✅ Pensamento de nível sênior (princípios, padrões, trade-offs)
- ✅ Aderência às instruções (3 turnos, tempo, formato)

### Principais Diferenciais

🌟 **Use Tool Calls como evidência** (se Modelo B): Mostre que entende o valor da investigação

🌟 **Mencione princípios específicos**: SRP, DRY, type safety, não genéricos como "good code"

🌟 **Dê exemplos concretos**: Cite arquivos, funções, decisões específicas do código

🌟 **Avalie production-readiness**: Não apenas "funciona", mas "está pronto para prod?"

🌟 **Seja balanced**: Mesmo código bom tem algo a melhorar; mesmo ruim tem algo positivo

---

## ✅ Checklist Final Consolidado

### Pré-Teste
- [ ] Li e entendi completamente as instruções do teste
- [ ] Explorei o repositório AI ChatKit no GitHub
- [ ] Preparei 3 prompts completos usando estrutura de 5 partes
- [ ] Memorizei template de justificativa
- [ ] Revisei vocabulário técnico essencial
- [ ] Configurei ambiente (Hubstaff, Labelbox, timer)

### Durante Cada Turno
- [ ] Enviei prompt claro e bem escopado
- [ ] Aguardei resposta completa do modelo
- [ ] Analisei código com checklist específico
- [ ] Identifiquei tipo de modelo (A ou B)
- [ ] Avaliei processo E resultado
- [ ] Escrevi justificativa com 5+ frases técnicas
- [ ] Usei vocabulário sênior e princípios específicos
- [ ] Dei exemplos concretos do código
- [ ] Atribuí ratings consistentes

### Pré-Submissão
- [ ] Completei exatamente 3 turnos
- [ ] Cada justificativa tem 5+ frases substantivas
- [ ] Usei termos técnicos (não genéricos)
- [ ] Avaliei processo do modelo (investigação/suposições)
- [ ] Dei exemplos específicos de código
- [ ] Mencionei princípios de engenharia
- [ ] Incluí análise balanced (prós e contras)
- [ ] Revisei ortografia e clareza
- [ ] Estou confiante nas minhas avaliações

**SE TODOS OS CHECKS ACIMA: SUBMIT! ✅**

---

## 🎯 Conclusão

Este plano estratégico consolida o conhecimento de todos os guias anteriores (plano-1 a plano-6) e fornece um roteiro completo e executável para o teste Code Human Preference Eval.

**Pontos-Chave**:
1. O teste PERMITE uso de IA como ferramenta de apoio
2. O importante é ENTENDER e DECIDIR (não copiar cegamente)
3. Demonstre pensamento SÊNIOR através de análise técnica profunda
4. Use EVIDÊNCIAS ESPECÍFICAS, não opiniões vagas
5. Gerencie o TEMPO agressivamente (1h30min passa rápido)

**Próximos Passos Recomendados**:
1. Praticar escrever 1-2 justificativas usando os templates
2. Explorar o repositório AI ChatKit por 30 minutos
3. Preparar os 3 prompts completos com antecedência
4. Fazer uma simulação mental da timeline de execução

**Boa sorte! Você está preparado. Execute com confiança.** 🚀
