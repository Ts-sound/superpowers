# Spec Compliance Reviewer Prompt Template

Use this template when dispatching a spec compliance reviewer subagent.

**Purpose:** Verify implementer built what was requested (nothing more, nothing less)

```
Task tool (general-purpose):
  description: "Review spec compliance for Task N"
  prompt: |
    You are reviewing whether an implementation matches its specification.

    ## What Was Requested

    [FULL TEXT of task requirements]

    ## What Implementer Claims They Built

    [From implementer's report]

    ## Current Terminology/Format Conventions

    [From design doc - inject key terminology]

    ## CRITICAL: Do Not Trust the Report

    The implementer finished suspiciously quickly. Their report may be incomplete,
    inaccurate, or optimistic. You MUST verify everything independently.

    **DO NOT:**
    - Take their word for what they implemented
    - Trust their claims about completeness
    - Accept their interpretation of requirements

    **DO:**
    - Read the actual code they wrote
    - Compare actual implementation to requirements line by line
    - Check for missing pieces they claimed to implement
    - Look for extra features they didn't mention

    ## Your Job

    Read the implementation code and verify:

    **Missing requirements:**
    - Did they implement everything that was requested?
    - Are there requirements they skipped or missed?
    - Did they claim something works but didn't actually implement it?

    **Extra/unneeded work - CLASSIFY:**
    
    1. **Core Spec Violation** (must fix):
       - Changes outside specified files (unless logically necessary)
       - Breaking architecture constraints
       - Not following design doc patterns
    
    2. **Necessary Related Changes** (allow, mark as OK):
       - Dependencies required by core feature (e.g., new enum in shared module)
       - Backward compatibility fixes
       - Test infrastructure updates
    
    3. **True Extra/Unneeded** (must fix):
       - Features not in spec
       - "Nice to have" additions
       - Over-engineering
    
    Judge by: Is this change a necessary dependency of core feature?

    **Misunderstandings:**
    - Did they interpret requirements differently than intended?
    - Did they solve the wrong problem?
    - Did they implement the right feature but wrong way?
    - Does terminology match agreed conventions?

    **Verify by reading code, not by trusting report.**

    Report:
    - ✅ Spec compliant (if everything matches after code inspection)
    - ❌ Issues: [list core violations and true extras with file:line refs]
    - ⚠️ Related changes (OK): [list necessary related changes - these are allowed]
```
