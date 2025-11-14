# 📋 Quick Reference Guide - Code Human Preference Eval

> **English Version** | Essential templates and checklists for test execution

---

## ⚡ ESSENTIAL TEMPLATES

### 1. PROMPT TEMPLATE (Use for all 3 turns)

```markdown
### [CONCISE FEATURE/TASK TITLE]

**CONTEXT AND REASONING:**
Currently [current situation]. This causes [specific problem].
Users/developers need [solution] because [clear benefit].

**DETAILED REQUIREMENTS:**
1. When [action/condition], it should [expected behavior]
2. [Visual aspect/feedback] should [how it works]
3. Must work in [specific cases: normal, edge cases]
4. [Additional requirement if applicable]

**TECHNICAL SUGGESTIONS:**
- Modify/create [specific file/component]
- Use [technology/pattern] for [technical reason]
- Consider [approach] for [goal]
- Centralize [logic] in [suggested location]

**ACCEPTANCE CRITERIA:**
✓ Works in [normal case]
✓ Handles [edge case 1]
✓ Handles [edge case 2]
✓ Includes [type of test]
✓ Accessible: [a11y requirement if applicable]
✓ [Additional criterion if applicable]
```

---

### 2. JUSTIFICATION TEMPLATE (Memorize structure)

```
[THESIS - 1 sentence]
Model [A/B] demonstrated [adjective] superiority through [concise main reason].

[PROCESS - 2-3 sentences]
[If Model B with Tool Calls:]
Its methodological approach using Tool Calls to [specific action like 'find', 'cat'] 
before proposing code demonstrated robust engineering practices. This ensured the 
solution aligned with the project's existing architecture.

[If Model A direct:]
Despite not using explicit investigation, the model demonstrated deep understanding 
of the architecture by [specific technical decision]. [Verify if assumptions about 
files/functions are correct].

[TECHNICAL QUALITY - 2-3 sentences]
The implementation followed [principle: SRP/DRY/Composition] by [specific code example]. 
[Positive aspect 1: e.g., correct TypeScript types]. [Positive aspect 2: e.g., 
separation of responsibilities]. [Positive aspect 3: e.g., error handling].

[IMPROVEMENT POINTS - 1-2 sentences, if applicable]
However, [specific aspect] could be improved with [concrete suggestion]. A senior 
developer would have [alternative or addition].

[CONCLUSION - 1 sentence]
The solution meets [X of Y] prompt criteria and is [% ready or ready/not ready] 
for production due to [clear final reason].
```

---

## ⏱️ TIMELINE (90 minutes total)

```
00-10:  Turn 1 - Send prompt
10-25:  Turn 1 - Wait for response
25-35:  Turn 1 - Analyze + write justification
35-45:  Turn 2 - Send prompt
45-60:  Turn 2 - Wait for response
60-70:  Turn 2 - Analyze + write justification
70-80:  Turn 3 - Send prompt
80-95:  Turn 3 - Wait for response
95-105: Turn 3 - Analyze + write justification
105-110: Final review
110-120: Safety buffer
```

---

## ✅ PRE-SUBMISSION CHECKLIST

```
☐ Completed EXACTLY 3 independent turns?
☐ Each justification has 5+ complete sentences?
☐ Used technical vocabulary in all (minimum 3 terms)?
☐ Mentioned engineering principles (SRP, DRY, etc.)?
☐ For Model B: evaluated investigation process?
☐ For Model A: verified assumptions about files?
☐ Gave specific code examples in each justification?
☐ Included improvement points (when applicable)?
☐ Checked spelling/grammar errors?
☐ Justifications sound human-written (not copy-paste)?
☐ Tone is professional and technical in all?
```

---

## 🎯 TECHNICAL VOCABULARY TO USE

### Software Design Principles
- **Single Responsibility Principle (SRP)** - One reason to change
- **Don't Repeat Yourself (DRY)** - Avoid code duplication
- **Separation of Concerns** - Separate different logic aspects
- **Composition over Inheritance** - Combine behaviors via composition
- **Interface Segregation** - Specific interfaces over generic ones

### React/TypeScript Concepts
- **Type Safety / Type Inference** - TypeScript type safety
- **Custom Hooks** - Hooks for reusable logic
- **Controlled vs Uncontrolled Components** - Form state control
- **Props Drilling** - Passing props through multiple levels
- **Memoization (useMemo/useCallback)** - Performance optimization
- **State Management (Zustand/Context)** - Global state management

### Best Practices
- **Atomic Design Pattern** - Build UI with atomic components
- **Test-Driven Development (TDD)** - Write tests before code
- **Accessibility (a11y)** - ARIA labels, keyboard navigation
- **Edge Cases / Error Handling** - Extreme cases and error handling
- **Performance Optimization** - Efficient rendering, lazy loading
- **Code Readability / Maintainability** - Readable maintainable code
- **Production-Ready** - Robust code ready for production

---

## 🚀 QUICK ANALYSIS CHECKLIST

### For Model A (Direct Coder):
- [ ] Mentioned files exist in repository?
- [ ] Function/hook/component names are correct?
- [ ] Imports are correct?
- [ ] Logic makes basic sense?
- [ ] TypeScript types present (not using 'any')?

### For Model B (Investigator):
- [ ] Tool Calls showed repo exploration?
- [ ] Read relevant files before coding?
- [ ] Solution based on actual code found?
- [ ] Process demonstrates structured thinking?

### Both Models:
- [ ] Meets main prompt requirements?
- [ ] Includes tests if requested?
- [ ] Considers edge cases?
- [ ] Code is readable and well-structured?
- [ ] Follows best practices (SRP, DRY, etc.)?

---

## 💡 KEY PHRASES FOR SENIOR-LEVEL WRITING

**USE phrases like:**
- "The solution demonstrates deep understanding of..."
- "Following the [X] principle, the code..."
- "A senior developer would have..."
- "Although functional, could be more robust with..."
- "The proposed architecture facilitates..."
- "From a maintainability perspective..."
- "Considering edge cases..."

**AVOID phrases like:**
- "The code is ok"
- "Works well"
- "It's good"
- "I didn't see problems"

---

## ⚠️ COMMON MISTAKES TO AVOID

### Prompt Errors

❌ **Too vague:** "Improve the UI"  
✅ **Specific:** "Add loading indicator during API fetch"

❌ **Too broad:** "Implement authentication system"  
✅ **Well-scoped:** "Add email validation to login form"

❌ **Dictates implementation:** "Use useEffect with empty dependency array to..."  
✅ **Suggests approach:** "Consider effect hook to initialize state"

### Justification Errors

❌ **Too generic:** "The code is good and works well"  
✅ **Specific and technical:** "The code follows SRP by separating presentation logic"

❌ **Too short:** "Model A is better."  
✅ **Detailed:** "Model A demonstrated superiority through... [5+ sentences]"

❌ **No evidence:** "I think it's wrong"  
✅ **With evidence:** "On line X, the model imported from 'lib/utils' but correct file is 'hooks/utils'"

---

## 🎯 SUCCESS FORMULA

```
Good Prompt (well-scoped + specific) 
+ 
Critical Analysis (check files/logic) 
+ 
Technical Justification (5+ sentences + vocabulary) 
= 
High Score
```

---

## 📊 EVALUATION CRITERIA WEIGHTS

1. **Prompt Quality** (33%) - Clear, verifiable, well-scoped
2. **Adherence to Instructions** (33%) - Follow all rules
3. **Justification Quality** (34%) - Technical, detailed, convincing

---

*Document created by: GitHub Copilot Agent*  
*Version: 1.0*  
*Date: November 2024*
