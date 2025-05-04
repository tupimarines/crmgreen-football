````markdown
# AI Copilot Strategy – Rework-Proof Workflow

> **Project Context**
> CRM clone UI with WhatsApp, football data, and Excel integrations.
> Stack: **Django + Redis + HTML/CSS copied from CRM**

---

## **Daily Workflow**

### **1. Setup (Before Coding)**

- [ ] Create/update `CONTEXT.md`:
  ```md
  Project: CRM clone with WhatsApp, football data, Excel integration.
  Stack: Django backend, Redis queueing, copied HTML/CSS.
  Current goal: <insert today's task>
  Working parts: <describe what's working — must NOT be broken>
  Files allowed to change: <list them>
````

* [ ] Commit current working state:

  ```bash
  git init            # if not already initialized
  git add .
  git commit -m "Snapshot before edits on YYYY-MM-DD"
  ```

---

### **2. Start of Each AI Session**

Paste this prompt:

```prompt
You are my coding assistant. I'm a beginner, so I need clarity and precision.

**Project**: CRM clone UI (WhatsApp, football data, Excel export). Stack: Django + Redis.

**Rules:**
1. NEVER change working or unrelated code.
2. ALWAYS explain what you’re about to do.
3. ONLY edit files I list.
4. RETURN only patch-style code (diff format) if possible.

**Today's task**: <set priority to show a demo for client: Which is better: Test copied CSS and compare with the template (CRMgreesinais) or work on whatsapp API integration for working status. I need something that is fast to deliver and cause the client a good impression>
**Working parts**: <not specific>
**Edit only**: <all files>
```

---

### **3. Task Execution Checklist**


```
You are my coding assistant. I'm a beginner, so I need clarity and precision.

**Project**: CRM clone UI (WhatsApp, football data, Excel export). Stack: Django + Redis.

**Rules:**
1. NEVER change working or unrelated code.
2. ALWAYS explain what you're about to do.
3. ONLY edit files I list.
4. RETURN only patch-style code (diff format) if possible.

**Today's task**: Test CSS implementation and verify theme switching functionality to ensure a polished UI for client demo
**Working parts**: CSS files (navbar.css, main.css, custom.css, light/dark.css), theme switching in base.html and navbar.html
**Edit only**: css_test.html, football/painel/central/static/css/*.css, football/painel/central/templates/central/includes/base.html
```

## Getting Started Checklist:

1. [ ] **Verify CSS Files Load Correctly**
   - Use css_test.html to check all CSS files load without 404 errors
   - Confirm all styles render properly across different screen sizes

2. [ ] **Test Theme Switching**
   - Verify desktop theme toggle in navbar works
   - Test mobile theme toggle functionality
   - Confirm theme preference is saved and persists between page refreshes

3. [ ] **Fix Any Visual Inconsistencies**
   - Check for alignment issues or broken layouts
   - Ensure consistent styling between light and dark themes

4. [ ] **Cross-Browser Testing**
   - Test in Chrome, Firefox, and Edge (as available)
   - Document any browser-specific issues

5. [ ] **Update Changelog**
   - Document testing results and any fixes in changelog.yaml
   - Include screenshots of before/after if making visual improvements

6. [ ] **Prepare Demo Notes**
   - Create a short list of UI features to highlight during client demo
   - Note any particularly impressive visual elements to showcase


  > "Give only the changed lines in diff format. Add inline comments."
* [ ] Manually test the changes.
* [ ] Log changes in `CHANGELOG.md`:

  ```md
  ## YYYY-MM-DD
  - Added Redis queue using django-rq.
  - Changed views.py and settings.py.
  ```

---

### **4. End of Session**

* [ ] Test everything again.
* [ ] Final commit:

  ```bash
  git add .
  git commit -m "Feature: integrated Redis queue for WhatsApp messages"
  ```
* [ ] Optional zip backup:

  ```bash
  git archive -o backup-YYYY-MM-DD.zip HEAD
  ```

---

## **Best Coding Strategy (AI vs Manual)**

### **Manual + AI Hybrid = Best Approach**

| You Do                  | AI Helps                              |
| ----------------------- | ------------------------------------- |
| Define architecture     | Generate scaffolding                  |
| Research best libraries | Create isolated working examples      |
| Set task scope          | Apply targeted changes                |
| Interpret and test      | Handle repetitive or boilerplate code |

---

## **Summary: CONTEXT TEMPLATE**

```markdown
## CONTEXT

Project: CRM clone (WhatsApp, football data, Excel export)
Stack: Django + Redis + Copied HTML/CSS

Working modules:
- WhatsApp chat trigger UI (working)
- Redis installed & tested
- CSS styles copied from original CRM

Today’s goal:
<Insert description>

Files allowed to change:
- views.py
- styles.css
- templates/*.html

Rules for you (the AI):
1. Explain your plan first.
2. Change only listed files.
3. Use diff/patch format.
4. Do NOT break working code.
```

```

Would you like a downloadable copy of this file as well?

```
