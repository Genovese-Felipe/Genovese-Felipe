# AI ChatKit - LLM Task Prompts

This document contains three well-scoped engineering tasks designed for an LLM to implement on the AI ChatKit repository. Each task includes a detailed justification explaining why the prompt is well-defined, verifiable, and appropriately sized.

---

## Task 1: Refactor Frontend Components

**Prompt:**
> Currently, the chat interface duplicates styling and layout logic across `ChatComponent.tsx`, `MessageBubble.tsx`, and `MessageInput.tsx`. Refactor these files by creating a new reusable component called `ChatWrapper` that encapsulates the common container styles, such as the dark background, rounded corners, and flexbox layout. The `ChatWrapper` component should accept children to render the specific content of each section.

**Justification:**
This refactoring task is well-scoped because it targets a small, specific set of three frontend components (`ChatComponent`, `MessageBubble`, `MessageInput`) that share a clear, identifiable pattern of duplicated styling. The goal is unambiguous: to create a single reusable `ChatWrapper` component that centralizes the common layout code, thereby improving code maintainability and reducing redundancy. The solution's correctness is easily verifiable by visually inspecting the chat interface after the refactoring to ensure that the UI remains identical to the original, with no regressions in layout or styling. Furthermore, the code can be reviewed to confirm that the wrapper component is being used correctly in the parent components and that the duplicated styles have been removed.

---

## Task 2: Implement "Copy to Clipboard" Feature

**Prompt:**
> Implement a "Copy to Clipboard" feature for code blocks within the chat. In `MessageBubble.tsx`, detect when a message contains a markdown code block (e.g., ´´´python...). For each code block, render a "Copy" button in the top-right corner. When clicked, this button should copy the raw code content to the user's clipboard and briefly display a "Copied!" confirmation.

**Justification:**
This feature prompt is well-sized, as it requests a discrete piece of user-facing functionality confined to a single component, `MessageBubble.tsx`. The requirements are unambiguous: detect markdown code blocks, render a "Copy" button for each, and implement clipboard functionality upon click, including a confirmation message. This clarity avoids subjective interpretation of the UI/UX. The correctness of the implementation is highly verifiable through a clear, multi-step testing process: 1) send a message containing a code block to verify the "Copy" button appears, 2) click the button and paste the content into a text editor to ensure the raw code was copied correctly, and 3) confirm that the "Copied!" message appears and then disappears as expected.

---

## Task 3: Add Backend Unit Tests for Chat API

**Prompt:**
> The backend API lacks unit tests for its business logic. Create a new test file at `backend/tests/api/test_chat_routes.py` and write unit tests for the `/api/chat/stream-chat` endpoint defined in `backend/app/api/chat_routes.py`. The tests should use pytest and mock the `stream_chat_s` service dependency to verify that the endpoint correctly handles valid requests by returning a 200 status code and correctly handles requests with missing or invalid parameters by returning an appropriate HTTP error code (e.g., 422 Unprocessable Entity).

**Justification:**
This testing task is well-defined and appropriately scoped, focusing on a single, critical API endpoint (`/api/chat/stream-chat`). The prompt is unambiguous, specifying the exact file path for the new tests (`backend/tests/api/test_chat_routes.py`) and the testing framework to use (pytest). It clearly defines the success and failure criteria: mocking the service dependency to isolate the controller logic, verifying the 200 status code for valid requests, and ensuring a 422 error for invalid ones. The solution is programmatically verifiable by running the new test suite. A successful run will confirm that the tests pass, thereby proving that the endpoint's error handling and success paths are behaving as expected under controlled conditions.
