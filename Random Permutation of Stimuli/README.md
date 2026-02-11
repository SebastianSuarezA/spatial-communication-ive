# README — Participant Randomization Update

**Change Summary**
The randomization script was updated to generate orders for 20 participants instead of 16.

**Reproducibility Assurance:**
• The same random seed (random.seed(2026)) was used when extending the script. Because Python’s random number generator is deterministic when initialized with the same seed, the randomized orders for Participants 1–16 remain exactly the same as in the original version of the experiment.

**Impact on Existing Data**
• The order assigned to the first 16 participants is unchanged.
• Previously conducted experiments are not affected by this modification.
• Participants 17–20 receive newly generated randomized orders that follow the same controlled randomization procedure.

**Methodological Note:**
• Maintaining the same seed ensures reproducibility and preserves the integrity of the experimental counterbalancing while allowing the study to expand to additional participants.
