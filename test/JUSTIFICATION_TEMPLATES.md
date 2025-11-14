# Justification Templates - Code Human Preference Eval

## The 5+ Sentence Structure (Proven Pattern)

### Core Template

```markdown
[THESIS - 1 clear, strong sentence]
Model [A/B] is superior because [main concise reason].

[PROCESS - 2-3 sentences]
[If Model B]: The investigative approach demonstrated maturity by first 
executing [mention specific Tool Calls]. This ensured the proposed 
solution was perfectly aligned with the existing architecture. 
[Details about what was investigated]

[If Model A]: Despite not using explicit investigation via Tool Calls, 
the model demonstrated deep understanding of the architecture by 
correctly identifying [mention specific technical decisions]. 
[Assess if assumptions were correct]

[CODE QUALITY - 2-3 sentences]
The implementation follows [mention principle: SRP/DRY/SOLID/etc] by 
[specific example from code]. The separation of [X] into [Y] 
demonstrates good modularity and facilitates future maintenance. 
The use of [TypeScript/hooks/specific pattern] was 
[appropriate/could be improved because...].

[STRENGTHS AND WEAKNESSES - 1-2 sentences]
Strengths include [list 2-3 specific points]. However, [specific 
improvement point if any]. A senior developer would have 
[what they would do differently or praise].

[CONCLUSION - 1 sentence]
Therefore, considering [main criterion: robustness/maintainability/
prompt adherence], Model [X] delivers a solution that is 
[ready/not ready] for production because [specific final reason].
```

---

## Ready-to-Use Justification Examples

### Example 1: Model B (Investigative) - Excellent Response

```markdown
Model B demonstrates clear superiority through its methodical 
investigative approach. Before proposing any code, it executed Tool 
Calls to map the architecture (`find` to locate stores, `cat` to 
inspect use-chat-store.ts and chat.tsx), ensuring its solution was 
perfectly aligned with the existing project structure.

Technically, the implementation is exemplary: (1) it adds the 
`isStreaming` state to the Zustand store using idiomatic `set()` 
syntax, (2) creates an isolated, reusable `TypingIndicator` component 
following the Single Responsibility Principle, and (3) conditionally 
integrates into chat.tsx without polluting existing logic. The use of 
Tailwind with animation classes (`animate-bounce`) demonstrates 
attention to UX details.

Additional strengths include explicit TypeScript types without any 
'any' usage, and clear separation of responsibilities between state 
management and presentation. One improvement point is the absence of 
unit tests explicitly mentioned in acceptance criteria, though the 
modular architecture facilitates their later addition via React 
Testing Library.

The solution meets 4 of 5 criteria and is 90% production-ready. With 
the addition of automated tests to verify conditional rendering and 
store behavior, it would be immediately merge-worthy.
```

**Why this is excellent**:
✓ Clear thesis statement
✓ Specific Tool Calls mentioned
✓ Technical principles cited (SRP)
✓ Concrete code examples (isStreaming, animate-bounce)
✓ Balanced (strengths AND weaknesses)
✓ Quantified readiness (90%, 4 of 5)
✓ Well over 5 sentences

---

### Example 2: Model A (Direct Coder) - Good Response with Caveats

```markdown
Model A delivers a functionally correct solution but with risks 
inherent to its direct approach. Without investigation via Tool Calls, 
it made assumptions about the project structure, including the 
location of use-chat-store.ts and the naming conventions for Zustand 
actions. Fortunately, verification against the actual repository 
confirms these assumptions were accurate, validating the model's 
implicit understanding of common React/Next.js patterns.

The code quality is solid: proper TypeScript interfaces define props, 
the component separation follows DRY principles, and the state 
management integration is clean. The use of semantic HTML and proper 
button elements demonstrates attention to accessibility fundamentals. 
However, the implementation lacks explicit error handling for edge 
cases like rapid state changes or race conditions during streaming.

Strengths include clean code structure, appropriate use of React hooks, 
and adherence to the prompt requirements. A weakness is the assumption-
based approach, which in a more complex or less standard codebase could 
lead to errors requiring significant rework. A senior developer would 
have verified file existence before proposing modifications or at least 
acknowledged the assumptions being made.

Considering the specific prompt requirements and actual codebase, Model 
A delivers a 75% production-ready solution that works correctly but 
would benefit from additional robustness testing before deployment.
```

**Why this is good**:
✓ Acknowledges approach differences
✓ Specific technical details (TypeScript interfaces, DRY)
✓ Balanced analysis (works but has risks)
✓ Mentions what senior dev would do differently
✓ Clear production-readiness assessment

---

### Example 3: Model B - Excellent with Perfect Investigation

```markdown
Model B's response exemplifies engineering best practices through 
systematic investigation and implementation. The sequence of Tool Calls 
(`find . -name "*store*"`, followed by `cat` on relevant files) 
demonstrates a methodical approach to understanding the codebase before 
modification, mirroring how a senior engineer would tackle an unfamiliar 
project.

The implementation excellence is evident in multiple layers: (1) type 
safety through explicit TypeScript interfaces avoiding any 'any' types, 
(2) architectural cleanliness by separating the `copyToClipboard` 
utility from UI components following Separation of Concerns, (3) error 
handling for clipboard API failures with fallback messaging, and (4) 
comprehensive test coverage including unit, component, and accessibility 
tests. The use of `navigator.clipboard.writeText` with proper 
permission checks shows awareness of browser API constraints.

Particularly impressive is the attention to edge cases: the solution 
handles long code blocks (>500 lines), manages focus state for 
accessibility, and includes ARIA labels for screen readers. The only 
minor enhancement would be adding a visual timeout indicator if the 
copy operation takes longer than expected, though this is a rare edge 
case.

This solution exceeds the prompt requirements, meeting all 6 acceptance 
criteria and is production-ready with no additional work needed. It 
represents merge-worthy code that could be deployed immediately with 
confidence.
```

**Why this is excellent**:
✓ Specific process analysis
✓ Multi-layered code quality assessment
✓ Technical depth (clipboard API, permissions, ARIA)
✓ Edge case coverage detailed
✓ Exceeds requirements acknowledged
✓ Clear production readiness verdict

---

### Example 4: Model A - Good But With Concerns

```markdown
Model A provides a working implementation but with concerning gaps that 
impact production-readiness. The direct coding approach without 
investigation led to several assumptions: (1) the message store 
structure, (2) the existence of a toast notification system, and (3) 
the markdown renderer integration points. Cross-referencing with the 
actual repository reveals that assumption #2 was incorrect—there is no 
built-in toast system in the project.

The code structure itself follows good practices: DRY principle through 
utility extraction, proper component composition, and TypeScript usage. 
The `CopyButton` component is well-structured with appropriate state 
management. However, the missing toast system means the feedback 
mechanism specified in the prompt is not implemented, requiring 
additional work to either add a toast library or use an alternative 
feedback method.

Strengths include modular design, clean separation between logic and 
presentation, and appropriate use of React hooks. The critical weakness 
is the incomplete implementation due to unverified assumptions. A senior 
developer would have either: (a) verified the existence of required 
dependencies before proposing the solution, or (b) explicitly noted in 
the response that a toast library would need to be added.

Considering these factors, Model A delivers a 60% production-ready 
solution that demonstrates good coding practices but requires additional 
work to fully meet the prompt requirements.
```

**Why this is effective**:
✓ Identifies specific problems (missing toast)
✓ Cross-references with actual repository
✓ Technical assessment detailed
✓ Clear gap analysis
✓ Specific guidance on what senior would do
✓ Honest production-readiness assessment

---

### Example 5: Comparison Between Two Models

```markdown
Model B significantly outperforms Model A in this refactoring task 
through superior methodology and attention to architectural details. 
Model B's investigative phase included `grep` searches for component 
usage patterns and examination of existing type definitions, while 
Model A proceeded directly to refactoring without verification.

The implementation quality diverges notably: Model B created three 
specialized components (UserMessage, AIMessage, ErrorMessage) with 
fully typed interfaces and no shared state mutation, adhering strictly 
to the Single Responsibility Principle. Model A, while achieving the 
same component separation, introduced a shared utility function that 
maintains mutable state, creating potential race conditions in 
concurrent scenarios. Additionally, Model B's TypeScript types are more 
specific (discriminated unions based on message role) versus Model A's 
generic Message type with optional fields.

Both models successfully reduce code duplication and improve testability. 
Model B includes example tests using React Testing Library that verify 
isolated component behavior, while Model A mentions testing but provides 
no concrete examples. The accessibility considerations are also stronger 
in Model B's implementation, with proper semantic HTML and ARIA 
attributes.

Model A deserves credit for a functional refactoring that improves 
maintainability, but Model B's more thorough approach, type safety, and 
production-ready testing makes it the clear winner. Considering 
architecture, robustness, and completeness, Model B delivers a 95% 
production-ready solution versus Model A's 70%.
```

**Why this comparison works**:
✓ Direct comparison of approaches
✓ Specific technical differences highlighted
✓ Both pros and cons for each model
✓ Quantified assessment (95% vs 70%)
✓ Fair to both models while clear about preference

---

## Vocabulary Bank for Justifications

### Architecture & Design Patterns
- Single Responsibility Principle (SRP)
- Don't Repeat Yourself (DRY)
- Separation of Concerns
- SOLID principles
- Composition over Inheritance
- Dependency Injection
- Modular architecture
- Loose coupling, high cohesion

### React & TypeScript
- Type safety / Type inference
- Discriminated unions
- Generic types with constraints
- Custom hooks for logic reusability
- Controlled vs Uncontrolled components
- Props drilling and context usage
- State management patterns
- Hook dependencies optimization
- Memoization strategies
- Component composition

### Code Quality
- Production-ready / Merge-worthy
- Idiomatic usage
- Defensive programming
- Error boundary implementation
- Edge case coverage
- Robustness / Resilience
- Maintainability / Extensibility
- Technical debt avoidance
- Code smell identification
- Refactoring opportunity

### Testing
- Test-Driven Development (TDD)
- Unit test coverage
- Integration testing
- End-to-end testing
- React Testing Library patterns
- Mock vs Stub vs Spy
- Test isolation
- Accessibility (a11y) testing
- Coverage metrics

### Process & Methodology
- Investigative approach
- Methodical / Systematic
- Assumption verification
- Cross-referencing with codebase
- Tool Call analysis
- Risk mitigation
- Incremental development
- Verification step

---

## Common Mistakes to Avoid

### ❌ Too Vague
```
"The model did a good job. The code looks fine and should work. 
I don't see major issues. It's probably okay for production."

Problems:
- No specific examples
- No technical terminology
- Wishy-washy ("probably", "looks fine")
- Way too short
```

### ❌ Only Positive
```
"Model A is perfect. Everything is implemented correctly. The code 
is clean, follows all principles, has great architecture, and is 
completely production-ready with no issues whatsoever."

Problems:
- Not believable (nothing is perfect)
- No critical analysis
- Misses opportunity to show depth
- No evidence or examples
```

### ❌ Only Negative
```
"Model B's approach is terrible. The Tool Calls waste time. The code 
is overly complex. Everything could be simpler. I wouldn't merge 
this."

Problems:
- Too harsh without justification
- Misses strengths
- No constructive suggestions
- Lacks technical specifics
```

### ❌ Generic Template Speech
```
"The model demonstrates comprehensive understanding of software 
engineering principles. It follows best practices and delivers 
high-quality code that adheres to industry standards. The 
implementation is robust and scalable."

Problems:
- Could apply to anything (no specifics)
- Buzzword soup
- No concrete examples
- Sounds AI-generated
```

---

## Self-Check Questions

Before finalizing your justification, ask yourself:

**Specificity**:
- [ ] Did I mention specific files, functions, or components?
- [ ] Did I cite specific Tool Calls if Model B?
- [ ] Did I give concrete code examples?

**Technical Depth**:
- [ ] Did I use at least 3 technical terms correctly?
- [ ] Did I mention software engineering principles by name?
- [ ] Did I evaluate architecture, not just functionality?

**Balance**:
- [ ] Did I mention both strengths AND weaknesses?
- [ ] Is my assessment fair and justified?
- [ ] Did I avoid extreme language (perfect/terrible)?

**Evidence**:
- [ ] Did I provide evidence for claims?
- [ ] Did I explain WHY something is good or bad?
- [ ] Could another engineer follow my reasoning?

**Senior Thinking**:
- [ ] Did I consider production-readiness?
- [ ] Did I think about maintainability and future changes?
- [ ] Did I mention what a senior dev would do differently?

**Length & Structure**:
- [ ] Is it 5+ substantial sentences?
- [ ] Does it follow the template structure?
- [ ] Is it clear and well-organized?

**Authenticity**:
- [ ] Does it sound like I wrote it (not AI)?
- [ ] Is it specific to THIS code and THIS task?
- [ ] Did I personalize it appropriately?

---

## Quick Reference Card

```
JUSTIFICATION CHECKLIST
═══════════════════════

□ THESIS (1 sentence)
  └─> Model X is better because Y

□ PROCESS (2-3 sentences)
  ├─> Model B: Tool Calls used
  └─> Model A: Assumptions made

□ CODE QUALITY (2-3 sentences)
  ├─> Principles followed (SRP, DRY)
  ├─> Specific examples
  └─> TypeScript usage

□ STRENGTHS/WEAKNESSES (1-2 sentences)
  ├─> 2-3 strong points
  └─> 1-2 improvement areas

□ CONCLUSION (1 sentence)
  └─> Production readiness verdict

MUST INCLUDE:
• Specific examples ✓
• Technical terms (3+) ✓
• Engineering principles ✓
• Balanced analysis ✓
• Evidence-based ✓
• 5+ sentences ✓
• Your authentic voice ✓
```

---

## Practice Exercise Template

Try filling this out for practice:

```markdown
PRACTICE JUSTIFICATION

Task: [Describe the task]
Model Response: [Summarize what model did]

Now write your justification:

[Your thesis sentence]

[Your process analysis 2-3 sentences]

[Your code quality assessment 2-3 sentences]

[Your strengths/weaknesses 1-2 sentences]

[Your conclusion sentence]

Self-check:
□ Specific examples included
□ 3+ technical terms used
□ Engineering principles mentioned
□ Balanced (pros and cons)
□ 5+ substantial sentences
□ Evidence provided
□ Senior-level thinking
```

---

**Remember: Your justification is where you demonstrate expertise. Be specific, be technical, be balanced, be thorough. This is your chance to shine as a senior engineer.** 🌟
