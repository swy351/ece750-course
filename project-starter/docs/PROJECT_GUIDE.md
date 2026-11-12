# ECE 750 Project guide

**Updated 12 November 2026 — Python and R submissions.**

Investigate one focused software-analytics question with a defensible traditional baseline and a motivated LLM/agent component. Choose among source code, comments/review records, class/component metrics, logs, performance telemetry/traces, or commits. State the unit of analysis, target, intended decision and information available at decision time. Explain how your project extends or tests a research idea beyond simply rerunning a supplied lab.

Use the current LEARN instructions for group arrangements, deadlines, report length, presentation requirements and the project's contribution to the course grade. The rubric below allocates 100 points **within the project**; it does not change the course weighting. Resolve any offering-specific requirements with the instructor before collecting results.

## Choose Python or R

**Python and R are equally acceptable** for traditional analysis, LLM/agent experiments, visualization and evaluation. Submit one complete implementation in your chosen language; implementing both is not required and earns no extra credit by itself. External tools or languages are appropriate when the research task needs them, but include their source, dependencies and execution instructions. For example, Java/JDT may supply source-code findings that you analyze in Python or R. The Assignment 2 detector requirement is not a blanket restriction on all project topics.

| Language | Required analysis source and readable output | Required environment record |
|---|---|---|
| Python | Executed `analysis.ipynb`, `analysis.html`, and all imported `.py` helpers | Python version, pinned dependencies such as `requirements.txt`, and exact setup/run/export commands |
| R | Completed `analysis.Rmd`, knitted `analysis.html`, and all sourced `.R` helpers | R version, `sessionInfo()`, package versions via `renv.lock` or a versioned list with setup instructions, and exact render commands |

Multiple notebooks are acceptable: identify the entry point and run order in `README`. A standalone script or rendered report alone does not replace the notebook source, reasoning and executable evidence. If both languages are used, document both environments and their execution order.

Restart the Python kernel and run all cells in order, or render R Markdown in a fresh R session. For example: `Rscript -e 'rmarkdown::render("analysis.Rmd", output_format="html_document")'`. Record the working directory, system dependencies and relative data paths. Include assets needed by the HTML. Complete the TODOs and retain outputs; do not submit an unchanged starter notebook.

## Milestones and evidence

These are preparation stages, not additional deadlines or separate grade weights.

| Stage | Evidence to prepare |
|---|---|
| Weeks 1–3 | Focused research question; unit and target; motivating paper(s); candidate data and access constraints |
| Weeks 5–6 | Small data-quality audit; sample baseline run; feasible LLM/agent task; initial risks and resource estimate |
| Week 8 proposal | Question and contribution; paper connection; data/label provenance; baseline and model conditions; split, metrics, uncertainty method, tool boundaries and budget |
| Weeks 9–11 | Implemented methods, preserved run records, development error analysis and documented protocol changes |
| Week 12 clinic | Preliminary evidence, leakage checks, uncertainty, limitations and an artifact reproduction check |
| Final submission | Report, runnable artifact, frozen results and contribution/assistance statement on the published schedule |

## Research and evaluation requirements

1. **Define the claim.** Frame a question that the available data can answer. Explain what you borrow from the motivating papers and what you change. Distinguish replication, extension, comparison and exploratory analysis. A new model or larger dataset is not required for a strong project.
2. **Audit the data.** Record source/version, permitted use, sampling, unit, stable IDs, fields, missingness, duplicates, class prevalence and exclusions. Explain how labels were obtained. If you annotate, supply a labeling protocol and assess disagreements; model or detector predictions are not independent ground truth.
3. **Implement a defensible traditional baseline.** Choose a relevant rule, statistical model or conventional learning method. Explain its assumptions and fit preprocessing only within the permitted training/development data. A deliberately weak comparator does not establish a useful gain.
4. **Specify the LLM/agent treatment.** Define inputs, prompts, output schema, model identity/settings, allowed tools and a finite decision/token/cost budget before the final evaluation. Explain the mechanism you are testing. Separate coding assistance from the model being evaluated. If the agent retrieves extra context, include an information-matched fixed-context control when feasible; otherwise identify the confounding and narrow the claim.
5. **Freeze an evaluation contract.** Define development and evaluation partitions before optimization. Prevent related records, duplicates, later information and outcome-derived features from leaking across splits. Use time/project/group separation when the intended use requires it. Keep supplied final holdouts unchanged. For purely explanatory studies, define the estimand, sample and specification instead of manufacturing a prediction task.
6. **Compare on matched evidence.** Use the same evaluation IDs, target and metric definitions. Match information and computational budgets, or explicitly treat their differences as part of the experiment. Report effect magnitudes, uncertainty and error categories, plus coverage/abstention and resource use where relevant. For stochastic pipelines, predeclare repeat counts and seeds; report all planned runs, not only the best. Justify a single-run study as a limitation when resources prevent replication.
7. **Interpret conservatively.** Investigate representative disagreements, verify quoted evidence and numerical claims, and report failures and negative results. Distinguish association, prediction and causation. State how sampling, labels, dependence and model access limit generalization. Do not claim superiority from authored example responses.

For instructor-held evaluation labels, submit frozen predictions and mark test metrics **pending instructor evaluation**. For a project-managed test set, document how it stayed separate during development and when it was first scored. Do not tune after seeing test results and reuse that same test as an untouched final evaluation. Record any necessary protocol change and its consequences.

## Final deliverables

Submit one project archive through the designated LEARN submission area. Keep the paths below or provide an explicit mapping in `README`.

| File or folder | Required contents |
|---|---|
| `README` | Project title, authors, research question, file map, exact setup and run order, expected outputs, runtime/resource needs and known limitations |
| `report.pdf` or `report.html` | Self-contained question and paper motivation, data, methods, evaluation design, results, uncertainty, error analysis, threats to validity and references; follow LEARN's length/format requirements |
| `analysis.ipynb` **or** `analysis.Rmd`, plus `analysis.html` | Executed traditional analysis and genuine LLM/agent results, figures, tables and narrative reasoning; clearly marked unexecuted portions |
| `src/` and environment files | All helper code and any detector/tool implementations; runtime/package versions, dependency installation instructions and external-tool configuration |
| `data_manifest` and `data_dictionary` | Provenance, licenses/access instructions, source hashes, unit/fields/target, labeling protocol, exclusions, and actual split/fold IDs; include data only when redistribution is permitted |
| `protocol` and `decision_log` | Predeclared comparisons, metrics, budgets, repetitions, selection rules, freeze record, configurations and justified changes |
| `results/` | Machine-readable predictions or task outputs, aggregate metrics, uncertainty calculations and evidence linking tables/figures to their source runs; preserve full precision |
| `runs/` | Prompts, responses, model settings, input IDs, tool arguments/observations, failures, timing, token/cost records when available and human interventions |
| `claim_audit.csv` | Claim, supporting data/run/evidence, independent verification, verdict, and correction or confirmation for consequential model claims |
| `contributions_and_assistance` | Each member's contribution; human help; reused code; AI tools used, affected files, accepted/changed output and verification |

If a presentation or demonstration is required on LEARN, submit its requested materials and be ready to explain the implementation and reproduce a representative result. A narrated screenshot is not a replacement for executable source.

### Machine-readable outputs

For binary classification, use UTF-8 CSV with `id,method,prediction,score`. Include a separate file per run or a documented `run_id` column for repeated trials. Each completed method/run must have exactly one row per evaluation ID. Define the positive class; use `0`, `1` or literal `ABSTAIN`, with finite scores in [0,1] oriented toward the positive class. Blank scores are allowed only for abstentions. Report coverage and explain when whole-sample ranking metrics cannot be computed. Do not silently re-threshold submitted predictions.

For parsing, localization, ranking, regression or explanatory studies, declare a task-appropriate schema in the proposal: stable ID where applicable, method/run, output or estimate, uncertainty/status and evidence reference. Do not force these tasks into binary labels. Include the evaluation code and metric definitions. Instructor-scored tasks must use the supplied schema and evaluation scope.

Python CSV exports should use `index=False`; R exports should use `row.names=FALSE`. Preserve IDs as character strings from import, exact column names, full-precision values and explicit abstentions. `NA`, `NaN`, blanks and `TRUE/FALSE` are not binary prediction labels. Read the exported file back and check coverage, duplicates, missing values and schema before submission. Avoid including private labels, credentials or restricted data in shared artifacts or model inputs.

## Grading rubric — 100 project points

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Research question and paper-based motivation | 10 | Focused, answerable question; accurate use of prior work; clearly scoped contribution and decision context |
| Data quality and experimental design | 20 | Traceable data/labels; correct unit and target; appropriate sampling/splits; leakage prevention; predeclared metrics and information boundaries |
| Traditional analysis | 20 | Correct, reproducible baseline or statistical analysis; justified assumptions and preprocessing; meaningful diagnostics and relevant uncertainty |
| LLM/agent method and audit | 20 | Motivated treatment; explicit tools/budgets; authentic preserved runs; validated outputs; independent verification of consequential claims and fair information controls |
| Comparative results and interpretation | 20 | Matched comparisons; suitable metrics/effect sizes; uncertainty and coverage; evidence-based failure analysis; cost/repeatability where relevant; conclusions bounded by validity limits |
| Reproducibility and communication | 10 | Complete runnable artifact and environment; consistent report/notebook/CSV outputs; clear limitations, citations, contributions and assistance disclosure |
| **Total** | **100** | |

A correct, well-supported negative result can earn full credit. Model accuracy, novelty of a model name, language choice or an agent beating the baseline is not a direct grade multiplier. Partial credit reflects the evidence actually completed. Unsupported claims, broken data boundaries and missing source/run records reduce credit in the relevant criterion. One root error should not receive repeated deductions merely because it propagates through later calculations; explain valid downstream reasoning and the limits of the original result.

### Acceptable Python/R differences

Both languages use this same rubric. Identical records and frozen predictions with identical metric definitions should give matching counts and confusion matrices and numerically consistent scores. Different documented solvers, regularization, training-selected thresholds, quantile conventions or uncertainty methods can legitimately produce different results. A common seed does not generate identical cross-language folds or bootstrap samples: preserve the actual IDs and record the resampling method.

State the model formula, transformations, preprocessing fit scope, interval method and convergence information. Justify meaningful differences rather than trying to match a reference score. Changed targets, silent exclusions, test-set tuning, reversed class coding and different metric definitions are methodological errors, not language effects.

## LLM/agent use and access

Coding and writing assistance is allowed with disclosure; you remain responsible for submitted code, calculations, citations and claims. Preserve the distinction between assistance used to build the artifact and the independent model treatment being measured. Treat dataset contents as data, not tool instructions. Restrict tools to the declared data and operations, validate plans before trusted code executes them, and keep hidden labels and instructor solutions out of prompts and tool access.

Do not invent responses, citations, runtimes, costs or tool traces. Record unavailable service metadata as unavailable. Retain failed and corrected attempts, not just successful ones. If live model access is unavailable, follow the course alternative-access instructions and document the issue early. An accepted protocol-only alternative must include prompts, input IDs, schemas, tool contracts, budgets, validation checks and intended comparisons, with all empirical model results marked **not run**. Its design and auditability replace execution evidence only under that accepted alternative; it does not waive the traditional analysis or justify performance claims.

## Dataset-specific cautions

SATD sampling imposes class prevalence. Ant lacks the logging/exception variables of the motivating papers. Loghub samples do not constitute full operational timelines. OpenRCA traces are sampled and boundary-clipped; component anomalies alone do not establish causality. The JIT sample has functional-defect labels and cannot reproduce PerfJIT performance labels. Authored LLM fixtures cannot substantiate model superiority.

## Final checklist

- [ ] Question, paper connection, contribution, unit, target and data provenance are clear.
- [ ] Traditional and LLM/agent methods have explicit inputs, budgets and evaluation rules.
- [ ] Development decisions and final evaluation are separated and documented.
- [ ] Notebook source, executed HTML, helper code and environment records reproduce the report.
- [ ] Predictions/task outputs pass schema and ID checks; withheld metrics are marked pending.
- [ ] Run records, claim audit, uncertainty, failures and limitations support the conclusions.
- [ ] Contributions, assistance and external sources are disclosed; restricted information is excluded.
- [ ] Archive and any required presentation follow current LEARN policies.
