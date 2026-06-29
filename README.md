# Desktop Notes Application

A lightweight, local desktop notes manager built to master local data persistence, CRUD architecture, and event-driven user interfaces in Python.

## 🛠️ Tech Stack
- **GUI Framework:** Tkinter
- **Database:** SQLite3 (Built-in)
- **Language:** Python 3

## 🚀 Features
- **Create:** Instantly write and save notes with custom titles and content.
- **Read:** Dynamic sidebar synchronization displays saved notes; clicking a note loads its full text.
- **Update:** Smart state tracking detects existing notes and safely modifies them instead of duplicating them.
- **Delete:** Safely remove notes permanently from the local disk with a confirmation pop-up.
- **Search:** Instant, real-time title filtering using SQL `LIKE` wildcard operators bound to keyboard events.

## 🧠 Key Learning Objectives Achieved
- Implemented **Separation of Concerns** by keeping database/SQL logic entirely separated from UI rendering.
- Mitigated **SQL Injection** security vulnerabilities using parameterized queries (`?` placeholders).
- Managed application **state architecture** using global variables to track selected item unique keys (`ids`) across asynchronous UI events.

---

## 👥 Credits & Acknowledgments
- **Developer:** mittalrishabh048 — Responsible for full application implementation, UI layout construction, state management design, and database integration.
- **Project Mentor:** Gemini (AI Collaborator) — Provided structural guidance, code review, architectural design patterns, and technical knowledge checks throughout development.