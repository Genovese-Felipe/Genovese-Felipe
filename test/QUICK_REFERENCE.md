# Quick Reference Guide - Code Human Preference Eval

## 🎯 Test Overview

**What**: Evaluate LLM-generated code for 2-3 coding tasks
**Time**: 1 hour 30 minutes
**Repository**: AI ChatKit (https://github.com/pasonk/ai-chatkit)
**Platform**: Labelbox/Alignerr
**Payment**: $45/task
**Attempts**: Single attempt only

---

## ⏱️ Time Management

```
RECOMMENDED TIMELINE
════════════════════════════════════════════

00:00-00:10  │ Turn 1: Send prompt
00:10-00:25  │ Wait for model response
00:25-00:35  │ Analyze + Write justification

00:35-00:45  │ Turn 2: Send prompt
00:45-01:00  │ Wait for model response
01:00-01:10  │ Analyze + Write justification

01:10-01:20  │ Turn 3: Send prompt
01:20-01:35  │ Wait for model response
01:35-01:45  │ Analyze + Write justification

01:45-01:50  │ Final review + SUBMIT
════════════════════════════════════════════
```

---

## 📝 Prompt Structure (5 Parts)

```
1. TITLE
   └─> Clear, specific feature/refactor/test

2. CONTEXT & WHY
   ├─> Current state
   ├─> Problem
   └─> Impact/benefit

3. REQUIREMENTS
   ├─> User action → Expected behavior
   ├─> Visual states
   └─> Specific scenarios

4. TECHNICAL HINTS
   ├─> Files to modify
   ├─> Technologies/patterns
   └─> Architecture suggestions
   [Don't prescribe exact implementation]

5. ACCEPTANCE CRITERIA
   ├─> Normal case ✓
   ├─> Edge cases ✓
   ├─> Tests ✓
   └─> Accessibility (if UI) ✓
```

---

## ✍️ Justification Structure (5+ Sentences)

```
1. THESIS (1 sentence)
   Model [A/B] is superior because [reason]

2. PROCESS (2-3 sentences)
   • Model B: Tool Calls analysis
   • Model A: Assumptions assessment

3. CODE QUALITY (2-3 sentences)
   • Principles (SRP, DRY, SOLID)
   • Specific examples
   • TypeScript/architecture notes

4. STRENGTHS/WEAKNESSES (1-2 sentences)
   • List 2-3 strong points
   • Note 1-2 improvements

5. CONCLUSION (1 sentence)
   Production readiness verdict with reason
```

---

## 🔍 Analysis Checklist (Per Turn)

**Quick Code Review**:
- [ ] Files/components mentioned exist in repo?
- [ ] Imports and names are correct?
- [ ] TypeScript types present (no 'any')?
- [ ] Error handling included?
- [ ] Edge cases addressed?
- [ ] Tests mentioned/included?
- [ ] Meets prompt requirements?

**Model B (Investigative)**:
- [ ] What Tool Calls were used?
- [ ] What did it investigate?
- [ ] Investigation relevant?
- [ ] Solution reflects findings?

**Model A (Direct Coder)**:
- [ ] What assumptions were made?
- [ ] Are assumptions correct?
- [ ] Any hallucinations (invented code)?
- [ ] Would work in actual codebase?

---

## 💡 Technical Vocabulary Bank

### Use These Terms

**Architecture**:
- Single Responsibility Principle (SRP)
- Don't Repeat Yourself (DRY)
- Separation of Concerns
- SOLID principles
- Composition over Inheritance
- Modular architecture

**React/TypeScript**:
- Type safety
- Custom hooks
- Props drilling
- State management
- Discriminated unions
- Component composition
- Memoization

**Quality**:
- Production-ready
- Merge-worthy
- Idiomatic
- Robust/Resilient
- Maintainable
- Extensible
- Edge case coverage

**Testing**:
- Unit tests
- Integration tests
- React Testing Library
- Test coverage
- Accessibility (a11y) testing

---

## 🎯 Task Ideas (Ready to Use)

### Feature Tasks
1. Typing indicator ("AI is responding")
2. Copy code button in code blocks
3. Delete chat session
4. Edit last message
5. Retry failed messages
6. Export conversation to Markdown

### Refactoring Tasks
1. Split MessageBubble into specialized components
2. Extract reusable form components
3. Centralize error handling
4. Improve TypeScript types (remove 'any')

### Testing Tasks
1. Unit tests for chat store hook
2. Component tests for message rendering
3. Accessibility tests for interactive elements

---

## ✅ Pre-Submission Checklist

**MANDATORY**:
- [ ] Completed exactly 3 turns
- [ ] Each justification 5+ sentences
- [ ] Used technical vocabulary (3+ terms per justification)
- [ ] Mentioned engineering principles (SRP, DRY, etc.)
- [ ] Evaluated process (not just results)
- [ ] Gave specific code examples
- [ ] Included both strengths and weaknesses
- [ ] No spelling/grammar errors

**QUALITY CHECK**:
- [ ] Justifications sound authentic (not AI-generated)
- [ ] Demonstrated senior-level thinking
- [ ] Used evidence-based reasoning
- [ ] Ratings consistent with written justifications

---

## 🚫 Common Mistakes to Avoid

### In Prompts
❌ Vague requirements ("make it better")
❌ Too broad scope (entire features)
❌ Subjective criteria ("pretty", "clean")
❌ Prescribing exact implementation
❌ No acceptance criteria

### In Justifications
❌ Too short (<5 sentences)
❌ Too generic (could apply to anything)
❌ No specific examples
❌ No technical terms
❌ Only positive OR only negative
❌ No evidence/reasoning
❌ Sounds AI-generated

### In Time Management
❌ Spending 40+ min on one turn
❌ Submitting before 3 turns complete
❌ No time for final review
❌ Rushing justifications

---

## 💬 Model A vs Model B

### Model A (Direct Coder)
**Behavior**:
- Immediately generates code
- Makes assumptions about structure
- Fast but potentially risky

**Evaluate**:
- ✓ Are file/component names correct?
- ✓ Do imports match real code?
- ✓ Are assumptions valid?
- ✓ Any hallucinations?

**In Justification**:
- Acknowledge direct approach
- Verify assumptions against repo
- Praise if assumptions correct
- Criticize if invented non-existent code

### Model B (Investigative)
**Behavior**:
- Uses Tool Calls first (find, cat, grep)
- Investigates before coding
- Methodical and thorough

**Evaluate**:
- ✓ Which Tool Calls used?
- ✓ What did it discover?
- ✓ Is investigation relevant?
- ✓ Does solution reflect findings?

**In Justification**:
- Praise methodical approach
- Mention specific Tool Calls
- Compare to senior engineer workflow
- Note alignment with architecture

---

## 📊 Production Readiness Scale

Use this to assess:

**90-100% Ready**:
- Meets all criteria
- No critical issues
- Tests included
- Edge cases handled
- Can merge immediately

**70-89% Ready**:
- Meets most criteria
- Minor issues present
- Would need small fixes
- Tests partial/missing

**50-69% Ready**:
- Basic functionality works
- Significant gaps
- Major refactoring needed
- Tests missing

**<50% Ready**:
- Fundamental issues
- Wrong assumptions
- Doesn't meet requirements
- Not functional

---

## 🎓 Demonstrate Senior Thinking

### Ask Yourself

**Architecture**:
- Does it follow SOLID principles?
- Is code modular and maintainable?
- How will it handle future changes?

**Robustness**:
- What edge cases exist?
- How does it handle errors?
- What about race conditions?

**Testing**:
- Is it testable?
- What tests would you write?
- Coverage adequate?

**User Impact**:
- Does it solve the real problem?
- Is UX smooth?
- Accessibility considered?

**Code Quality**:
- TypeScript types explicit?
- No code duplication?
- Clear naming?
- Proper separation of concerns?

---

## 🔥 Last-Minute Tips

**30 Minutes Before Test**:
- [ ] Review this guide
- [ ] Check repository structure
- [ ] Read 3 prepared prompts
- [ ] Remember justification template

**During Test**:
- [ ] Stay calm
- [ ] Trust your training
- [ ] Use checklist for each turn
- [ ] Don't chase perfection

**If Running Out of Time**:
- [ ] Complete all 3 turns (required)
- [ ] Shorter but complete justifications
- [ ] Quick final review
- [ ] Submit (partial better than nothing)

**If Model Response is Poor**:
- [ ] Don't panic
- [ ] Evaluate honestly
- [ ] Point out specific issues
- [ ] Still give thorough justification

---

## 📋 Quick Copy-Paste Templates

### Thesis Options
```
Model B is superior because its investigative approach ensures 
architectural alignment.

Model A delivers a functional solution but with risks from 
unverified assumptions.

Model B significantly outperforms through methodical investigation 
and robust implementation.
```

### Process (Model B)
```
The methodical approach is evident in the Tool Call sequence: 
[list calls]. This investigation ensured [benefit].
```

### Process (Model A)
```
The direct coding approach made assumptions about [list items]. 
Cross-referencing with the repository reveals [verdict].
```

### Code Quality
```
The implementation follows [principle] by [example]. The use of 
[technology/pattern] demonstrates [quality].
```

### Conclusion
```
Considering [criterion], Model [X] delivers a [%] production-ready 
solution that [verdict].
```

---

## 🎯 Success Criteria Summary

**You'll Pass If You**:
✅ Complete 3 well-scoped turns
✅ Write detailed technical justifications
✅ Demonstrate senior-level analysis
✅ Use specific examples and evidence
✅ Follow time guidelines
✅ Show understanding of architecture
✅ Balance strengths and weaknesses
✅ Use professional technical vocabulary

**You'll Likely Fail If You**:
❌ Submit less than 3 turns
❌ Write vague, generic justifications
❌ Use no technical terminology
❌ Make only superficial observations
❌ Copy-paste AI responses without adaptation
❌ Prompts too broad or subjective
❌ Miss critical code issues in analysis

---

## 📞 Emergency Protocols

**If Model Takes >15 Minutes**:
- Continue with next turn
- Come back if time permits
- Better to complete 3 turns partially than 2 fully

**If You Don't Understand Response**:
- Focus on what you can evaluate
- Mention in justification: "unclear sections limit assessment"
- Still provide thorough analysis of understandable parts

**If Repository Changed**:
- Adapt to whatever repo shown in Labelbox
- Use same principles and structure
- Tasks should fit that specific codebase

**If Technical Issue on Platform**:
- Screenshot error
- Note exact time
- Contact support immediately
- Document everything

---

## 🏁 Final Wisdom

**Remember**:
1. Quality > Speed (but complete all 3 turns)
2. Specific > Generic (always give examples)
3. Balanced > Extreme (find pros AND cons)
4. Evidence > Opinion (back up claims)
5. Senior thinking > Junior observation

**You've prepared. You know the structure. Execute with confidence.** 🚀

---

## 📱 Print This Page

Key sections to have handy:
- Timeline
- Prompt structure
- Justification structure
- Analysis checklist
- Vocabulary bank
- Pre-submission checklist

**Good luck! You're ready.** 💪
