---

description: "Task list for Photo Album Manager feature"

---

# Tasks: Photo Album Manager

**Input**: Design documents from `specs/001-photo-album-manager/`

**Prerequisites**: spec.md (required)

**Tests**: Not requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 [P] Initialize project with dependency management tooling
- [X] T003 [P] Configure linting and formatting tools
- [X] T004 [P] Create shared type definitions and base interfaces in src/types/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Implement local data persistence layer for albums and photos in src/storage/store.py
- [X] T006 [P] Implement image loading and thumbnail generation utilities in src/lib/image.py
- [X] T007 [P] Create base application shell layout with routing in src/app.py
- [X] T008 [P] Create empty-state and error boundary templates in src/templates/

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Browse Albums Grouped by Date (Priority: P1) 🎯 MVP

**Goal**: Users see all albums organized under date headings (newest first) on the main page.

**Independent Test**: Launch the application and verify that all albums appear under their correct date headings in the main view.

- [X] T009 [P] [US1] Create Album data model in src/types/__init__.py
- [X] T010 [US1] Implement album list query grouped by date in src/app.py
- [X] T011 [US1] Build date-grouped album list template in src/templates/index.html
- [X] T012 [P] [US1] Create album card template in src/templates/album_card.html
- [X] T013 [US1] Wire main page routing in src/app.py
- [X] T014 [US1] Add empty-state for album list view in src/templates/index.html

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Photos in Tile Grid (Priority: P1)

**Goal**: Users open an album and see all photos as uniform tiles in a responsive grid.

**Independent Test**: Open any album with photos and verify all photos render as equally-sized tiles in a responsive grid.

- [X] T015 [P] [US2] Create Photo data model in src/types/__init__.py
- [X] T016 [US2] Implement photo query in src/storage/store.py
- [X] T017 [P] [US2] Build photo tile template in src/templates/photo_tile.html
- [X] T018 [US2] Build responsive tile grid in src/templates/album.html
- [X] T019 [US2] Wire album detail page routing in src/app.py
- [X] T020 [US2] Add empty-state for empty album in src/templates/album.html

**Checkpoint**: At this point, User Story 2 should be fully functional and testable independently

---

## Phase 5: User Story 3 - Reorder Albums by Drag-and-Drop (Priority: P2)

**Goal**: Users drag albums within a date group to reorder them; order persists after reload.

**Independent Test**: Drag an album to a new position within its date group and verify the order persists after page reload.

- [X] T021 [US3] Add display-order field to Album model in src/types/__init__.py
- [X] T022 [US3] Implement order update API in src/app.py
- [X] T023 [P] [US3] Implement drag-and-drop in src/static/js/album-list.js
- [X] T024 [US3] Integrate drag-and-drop into album list template
- [X] T025 [US3] Persist new album order on drop in src/static/js/album-list.js
- [X] T026 [US3] Add visual feedback during drag in src/static/css/style.css

**Checkpoint**: At this point, User Story 3 should be fully functional and testable independently

---

## Phase 6: User Story 4 - Create and Populate Albums (Priority: P3)

**Goal**: Users create albums with a title and date, add photos to albums, and remove photos.

**Independent Test**: Create an album, add photos, and verify it appears under the correct date group on the main page.

- [X] T027 [US4] Build album creation form in src/templates/create_album.html
- [X] T028 [US4] Implement album creation API in src/app.py
- [X] T029 [P] [US4] Build photo upload form in src/templates/album.html
- [X] T030 [US4] Implement upload photo API in src/app.py
- [X] T031 [P] [US4] Build photo delete button in src/templates/photo_tile.html
- [X] T032 [US4] Implement delete photo API in src/app.py
- [X] T033 [US4] Wire album creation form on main page in src/templates/index.html

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T034 [P] Add responsive layout refinements across all views in src/static/css/style.css
- [X] T035 Optimize thumbnail generation for large albums in src/lib/image.py
- [X] T036 [P] Add keyboard navigation support in src/static/js/app.js
- [X] T037 Improve error handling in src/templates/error_boundary.html and src/app.py
- [X] T038 [P] Run performance benchmarks against success criteria (manual - verify server starts and pages load)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - US1 (P1) and US2 (P1) can proceed in parallel if staffed
  - US3 (P2) depends on US1 being complete (needs album list view)
  - US4 (P3) depends on US1 (needs album list) and US2 (needs photo grid) being complete
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Depends on US1 for navigation but can be built with stub
- **User Story 3 (P2)**: Requires US1 album list view to be functional
- **User Story 4 (P3)**: Requires US1 album list and US2 photo grid to be functional

### Within Each User Story

- Models before services
- Components before pages
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel
- US1 and US2 can be implemented in parallel (Phase 3 and Phase 4)
- Within each story, tasks marked [P] can run in parallel
- Components within a story marked [P] can run in parallel

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Browse Albums)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (Browse Albums) → Test independently → MVP
3. Add User Story 2 (View Photos) → Test independently → Demo
4. Add User Story 3 (Reorder) → Test independently
5. Add User Story 4 (Create Albums) → Test independently
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Browse Albums)
   - Developer B: User Story 2 (View Photos in Tile Grid)
3. Developer A continues: User Story 3 (Reorder)
4. Developer A or B: User Story 4 (Create Albums)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
