# Reference: sdui-and-mob Kanban Structure

6-stage **direct-output process** with PascalCase element folders. Deliverables accumulate as items progress.

```
.kanban/sdui-and-mob/
├── 01_noticed/                         # Stage 1: Recognize element
│   └── AndroidBacklog/                 #   Example item with extensive research
│       ├── trello.md                   #     Trello card sync (standard)
│       ├── discussion.md              #     Per-item discussion (not cross-topic)
│       ├── research.md                #     Research deliverable
│       ├── repositories.md            #     Codebase analysis files...
│       ├── managers.md
│       ├── viewmodels.md
│       ├── dagger-modules.md
│       ├── adr-001-kmp-vs-native.md   #     Architecture decision records
│       ├── adr-002-local-persistence.md
│       └── brainstorm.md
│
├── 02_framing/                         # Stage 2: Research behavior
│   └── OperationalRecordsAndExpressionResolution/
│       ├── trello.md                   #   Standard deliverables at this stage:
│       └── framing.md                  #   trello.md (synced) + framing.md (produced)
│
├── 03_specifying/                      # Stage 3: Write EARS requirements
│   ├── AcuantButton/                   #   26 elements currently in this stage.
│   │   ├── trello.md                   #   Each element folder carries forward
│   │   └── framing.md                  #   deliverables from prior stages.
│   ├── AuthProvider/
│   ├── BarcodeScanTextbox/
│   ├── BlankScreen/
│   ├── Checkbox/
│   ├── CommentLog/
│   ├── ConfigProvider/
│   ├── ConnectivityProvider/
│   ├── DateSelector/
│   ├── DecisivCase/
│   ├── HomeScreen/
│   ├── HTMLLabel/
│   ├── Label/
│   ├── MultiScreenOperation/
│   ├── MultiSelect/
│   ├── NavigationTile/
│   ├── PassFail/
│   ├── PermissionsProvider/
│   ├── Radio/
│   ├── RecallCheckButton/
│   ├── RecallColorLabelList/
│   ├── SessionProvider/
│   ├── SingleDropDown/
│   ├── TermsProvider/
│   ├── Textbox/
│   │   ├── trello.md
│   │   └── framing.md
│   └── UploadProvider/
│
├── 04_prototyping/                     # Stage 4: Build interface + component
│                                       #   (empty -- no items at this stage yet)
│
├── 05_nativifying/                     # Stage 5: Native implementations
│                                       #   (empty)
│
└── 06_distilling/                      # Stage 6: Final review
                                        #   (empty)
```

## Key Patterns

**PascalCase item folders:** Element names use PascalCase (`Textbox`, `BlankScreen`, `AuthProvider`) matching the SDUI naming convention. This contrasts with kebab-case in android-inspectpro-review.

**Deliverable accumulation:** Items carry forward deliverables from previous stages. A `Textbox/` folder in `03_specifying/` contains both `trello.md` (from notice) and `framing.md` (from framing). New deliverables are added at each stage without removing old ones.

**Bulk specifying stage:** 26 elements currently sit in `03_specifying/`. This is normal for direct-output processes where many items can be recognized and framed quickly, then queue up for the more intensive specification work.

**No cross-topic discussion.md:** Unlike android-inspectpro-review, this board has no root-level `discussion.md`. Per-item discussion lives inside individual element folders when needed (e.g., `AndroidBacklog/discussion.md`).

**Stage naming:** No gerund/past-participle convention here -- stages use a mix (`noticed`, `framing`, `specifying`, `prototyping`, `nativifying`, `distilling`). The naming was chosen for clarity of intent rather than grammatical consistency.

**Mixed element types:** Components (`Textbox`, `Checkbox`), Screens (`BlankScreen`, `HomeScreen`), Providers (`AuthProvider`, `SessionProvider`), and Operations (`MultiScreenOperation`) all coexist on the same board with the same stage progression.
