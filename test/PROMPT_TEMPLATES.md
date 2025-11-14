# Prompt Templates - Code Human Preference Eval

## 5-Part Prompt Structure (Proven Pattern)

### Template Structure

```markdown
## [TITLE]: Implement [Feature/Refactor/Test] in AI ChatKit

### CONTEXT AND REASONING
Currently, [describe current state]. This causes [problem description]. 
Users need [solution] because [benefit/impact].

### UI/UX REQUIREMENTS
1. When [user action], the system should [expected behavior]
2. [Visual state/feedback] must appear/disappear
3. Must work in [specific cases/scenarios]
4. [Additional requirement if applicable]

### TECHNICAL SUGGESTIONS
- Modify [specific file/component name]
- Use [technology/pattern] for [reason]
- Centralize logic in [suggested location]
- [Additional technical hint without prescribing exact implementation]

### ACCEPTANCE CRITERIA
✓ Works in [normal case]
✓ Handles [edge case 1]
✓ Handles [edge case 2]
✓ Includes [type of test]
✓ [Accessibility requirement if applicable]
```

---

## Ready-to-Use Prompts

### Prompt 1: Typing Indicator (New Feature)

```markdown
## Implement Visual "AI is Responding" Indicator

### CONTEXT AND REASONING
After a user sends a message, the UI remains static without visual 
feedback. Users don't know if the system is processing the response, 
which can lead to confusion and perceived unresponsiveness.

### UI/UX REQUIREMENTS
1. When the AI response begins streaming, display a visual indicator 
   at the bottom of the message list
2. Indicator should be either 3 animated dots or "AI is typing..." text
3. Automatically disappear when the complete response is rendered
4. Must not interfere with automatic scroll behavior of the conversation

### TECHNICAL SUGGESTIONS
- Add `isStreaming: boolean` state to use-chat-store.ts (Zustand)
- Create separate `TypingIndicator.tsx` component for reusability
- Modify chat.tsx to conditionally render the indicator
- Use Tailwind CSS for smooth dot animation

### ACCEPTANCE CRITERIA
✓ Indicator visible only during response streaming
✓ Does not appear for user messages
✓ Smooth, non-intrusive animation
✓ [Bonus] Unit test verifying render when isStreaming=true
```

---

### Prompt 2: Refactor Message Components (Refactoring)

```markdown
## Refactor MessageBubble.tsx into Specialized Components

### CONTEXT AND REASONING
Currently, the MessageBubble.tsx component contains conditional logic 
to render different message types (user messages, AI messages, and 
errors). This violates the Single Responsibility Principle (SRP), 
making the component difficult to maintain and test.

### REQUIREMENTS
1. Create 3 specialized components:
   - UserMessage.tsx - renders user messages
   - AIMessage.tsx - renders AI messages
   - ErrorMessage.tsx - renders error messages
2. MessageBubble becomes a dispatcher that selects which component to 
   render based on message.role
3. Each specialized component must have its own typed props 
   (clear TypeScript interfaces)
4. Maintain current visual styling (no UI breaks)

### TECHNICAL SUGGESTIONS
- Extract type-specific logic into respective components
- Use composition instead of inheritance
- Define specific MessageProps interface for each component
- Avoid code duplication for shared behavior

### ACCEPTANCE CRITERIA
✓ More modular and testable code
✓ Explicit TypeScript types (no 'any' usage)
✓ No code duplication (DRY principle)
✓ Current functionality preserved
✓ [Bonus] Unit test examples for each component
```

---

### Prompt 3: Copy Code Button (New Feature)

```markdown
## Implement "Copy Code" Functionality for Markdown Code Blocks

### CONTEXT AND REASONING
AI responses frequently include code blocks. Currently, users must 
manually select text to copy snippets. Adding a copy button 
significantly improves user experience when working with code, 
without touching backend data.

### UI/UX REQUIREMENTS
1. On hover over a code block, display a "Copy" button in the 
   top-right corner
2. On click, copy entire block content to clipboard
3. Show "Copied!" toast feedback for 1.5 seconds
4. Accessibility: button must be tabbable with proper aria-label
5. Announce via aria-live for screen readers

### TECHNICAL SUGGESTIONS
- Use navigator.clipboard.writeText() API
- Create copyToClipboard.ts utility to centralize clipboard logic 
  and error handling
- Create reusable CopyButton.tsx component
- Integrate with current Markdown renderer

### ACCEPTANCE CRITERIA
✓ Works on long code blocks (>500 lines)
✓ Gracefully handles errors if clipboard API fails
✓ Copied text exactly matches original code (preserves formatting)
✓ Unit test for copyToClipboard utility
✓ Component test for CopyButton
✓ Accessibility (a11y) test
```

---

### Prompt 4: Delete Chat Session (New Feature)

```markdown
## Implement Delete Chat Session Functionality

### CONTEXT AND REASONING
Users can create chat sessions but cannot delete them. This clutters 
the session list and is a basic management functionality expected 
in chat applications.

### UI/UX REQUIREMENTS
1. Add delete button (trash icon) next to each session in the list
2. On click, show confirmation dialog: "Delete this session? This 
   action cannot be undone."
3. On confirm, remove session from list
4. If deleted session was active, switch to most recent remaining session
5. Update localStorage to persist the change

### TECHNICAL SUGGESTIONS
- Add deleteSession action to use-chat-store.ts
- Create confirmation modal component or use existing UI pattern
- Update localStorage after state change
- Handle edge case of deleting the last session

### ACCEPTANCE CRITERIA
✓ Delete button visible for all sessions
✓ Confirmation prevents accidental deletion
✓ State correctly updates after deletion
✓ Active session handling works correctly
✓ [Bonus] Undo functionality with toast notification
```

---

### Prompt 5: Implement Retry for Failed Messages (Feature)

```markdown
## Implement Retry Functionality for Failed Messages

### CONTEXT AND REASONING
Network issues or API errors can cause message sending to fail. 
Currently, users must retype the entire message. A retry mechanism 
improves resilience and user experience.

### UI/UX REQUIREMENTS
1. When a message fails to send, display error state in message bubble
2. Show "Retry" button next to the error message
3. On click, attempt to resend the exact same message
4. Show loading state during retry attempt
5. Replace error with success or new error message based on result

### TECHNICAL SUGGESTIONS
- Add `status` field to Message type: 'sending' | 'sent' | 'failed'
- Store original message content for retry
- Create retryMessage action in use-chat-store.ts
- Handle error state in MessageBubble component

### ACCEPTANCE CRITERIA
✓ Failed messages clearly indicated visually
✓ Retry button functional and obvious
✓ Loading state shown during retry
✓ Successful retry removes error state
✓ Multiple retry attempts allowed
✓ [Bonus] Auto-retry once before showing manual retry button
```

---

### Prompt 6: Add Message Edit Functionality (Feature)

```markdown
## Implement Edit Last User Message Functionality

### CONTEXT AND REASONING
Users sometimes realize they made a typo or want to rephrase their 
question immediately after sending. Allowing edit of the last message 
reduces friction and improves conversation quality.

### UI/UX REQUIREMENTS
1. Add "Edit" button/icon next to the most recent user message
2. On click, convert message bubble to editable textarea
3. Show "Save" and "Cancel" buttons while editing
4. On save, replace message content and regenerate AI response
5. Keyboard shortcut: Ctrl+E (Cmd+E on Mac) to edit last message

### TECHNICAL SUGGESTIONS
- Add `isEditing` state to chat component
- Create EditableMessage component
- Update editLastMessage action in store
- Clear subsequent AI responses when message is edited

### ACCEPTANCE CRITERIA
✓ Edit button only on last user message
✓ Textarea sized appropriately for content
✓ Cancel restores original message
✓ Save triggers new AI response
✓ Keyboard shortcut works
✓ Focus management handled correctly
```

---

### Prompt 7: Export Conversation to Markdown (Feature)

```markdown
## Implement Export Conversation to Markdown File

### CONTEXT AND REASONING
Users want to save conversations for future reference, documentation, 
or sharing. Providing a clean Markdown export enables this without 
requiring screenshots or copy-paste.

### UI/UX REQUIREMENTS
1. Add "Export" button in chat header or menu
2. On click, generate Markdown file with conversation
3. Format: "**User:** [message]\n\n**AI:** [response]\n\n---\n\n"
4. Include timestamp in filename: "chat-export-2024-01-15.md"
5. Automatically download file (no server upload)

### TECHNICAL SUGGESTIONS
- Create exportUtils.ts with formatAsMarkdown() function
- Use Blob and URL.createObjectURL for client-side download
- Extract messages from use-chat-store.ts
- Handle code blocks and formatting correctly in export

### ACCEPTANCE CRITERIA
✓ All messages included in correct order
✓ Code blocks preserved with proper markdown syntax
✓ User and AI messages clearly distinguished
✓ File downloads immediately on click
✓ Filename includes timestamp
✓ [Bonus] Option to exclude system messages
```

---

## Tips for Creating Your Own Prompts

### DO ✅
- Clearly state the problem and why it matters
- Define specific, measurable acceptance criteria
- Suggest WHERE changes should go (files/components)
- Focus on WHAT and WHY, not exact HOW
- Include accessibility requirements if UI-related
- Mention relevant technologies (TypeScript, Tailwind, etc.)

### DON'T ❌
- Use vague terms like "pretty", "better", "good"
- Make scope too large (multiple major features)
- Prescribe exact implementation (line-by-line code)
- Skip context (why this feature matters)
- Forget edge cases in acceptance criteria
- Make problem ambiguous or subjective

### Checklist Before Using a Prompt
- [ ] Title is clear and concise
- [ ] Context explains current state and problem
- [ ] Requirements are specific and verifiable
- [ ] Technical hints guide but don't dictate
- [ ] Acceptance criteria can be objectively checked
- [ ] Scope is completable in one LLM response
- [ ] Edge cases are mentioned
- [ ] Fits naturally within the project

---

## Example Bad Prompts (To Avoid)

### ❌ Too Vague
```
"Make the chat interface better and more user-friendly"
Problem: What does "better" mean? No measurable criteria.
```

### ❌ Too Broad
```
"Add a complete authentication system with login, signup, 
password reset, email verification, OAuth integration, 
and session management"
Problem: Way too large for one turn. Would take days.
```

### ❌ Too Prescriptive
```
"In line 45 of chat.tsx, change const messages = [] to 
const messages = useState([]) and then in line 78 add 
useEffect(() => { ... }) with exactly this code: ..."
Problem: No room for model to think. Just copying code.
```

### ❌ Subjective
```
"Refactor the code to make it cleaner and more elegant 
with better design patterns"
Problem: "cleaner", "elegant", "better" are subjective. 
No way to verify.
```

---

## Adaptation Guide

### For Different Task Types

**New Feature**:
- Focus on: user benefit, UI/UX flow, integration points
- Example: "Add X button that does Y when clicked"

**Refactoring**:
- Focus on: current problem, architecture principle, improvement
- Example: "Split X component to follow SRP"

**Testing**:
- Focus on: what needs testing, coverage goals, test types
- Example: "Add unit tests for X hook covering edge cases Y and Z"

**Bug Fix**:
- Focus on: current incorrect behavior, expected behavior, root cause
- Example: "Fix X issue where Y happens instead of Z"

### For Different Repositories

1. **Research the codebase structure first**
2. **Identify pain points or missing features**
3. **Map to existing components and patterns**
4. **Ensure task fits naturally in project**

Remember: The repository dictates what tasks are realistic. 
A task perfect for AI ChatKit might not make sense for another project.

---

## Quick Reference Card

```
PROMPT STRUCTURE CHEAT SHEET
═════════════════════════════

1. TITLE
   └─> Clear, concise, specific

2. CONTEXT & WHY  
   ├─> Current state
   ├─> Problem
   └─> Impact/benefit

3. REQUIREMENTS
   ├─> User action → System behavior
   ├─> Visual states
   └─> Specific scenarios

4. TECHNICAL HINTS
   ├─> Files to modify
   ├─> Technologies to use
   └─> Architecture suggestions

5. ACCEPTANCE CRITERIA
   ├─> Normal case ✓
   ├─> Edge case 1 ✓
   ├─> Edge case 2 ✓
   ├─> Tests ✓
   └─> A11y (if UI) ✓

REMEMBER:
• Specific > Vague
• Verifiable > Subjective
• Limited > Broad
• Context > Prescription
```

---

**Use these templates as starting points. Adapt them to fit the specific repository and task at hand. The key is clarity, specificity, and verifiability.** 🎯
