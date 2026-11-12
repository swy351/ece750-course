# Base-R binary-output format checks only; does not read outcomes or grade quality.
# source() this file, then call validate_predictions(predictions, ids, methods).
read_contract <- function(path, columns) {
  d <- read.csv(path, colClasses = "character", check.names = FALSE,
                na.strings = character(), stringsAsFactors = FALSE,
                fileEncoding = "UTF-8-BOM", fill = FALSE, row.names = NULL)
  if (!identical(names(d), columns)) stop(paste(path, "has incorrect columns"))
  if (!nrow(d)) stop(paste(path, "has no records; header-only starters are incomplete"))
  d
}
validate_predictions <- function(predictions, ids_file, methods_file) {
  ids <- read_contract(ids_file, "id")
  methods <- read_contract(methods_file, c("method", "run_id"))
  d <- read_contract(predictions, c("id", "method", "run_id", "prediction", "score"))
  clean <- function(x) all(nzchar(trimws(x)) & x == trimws(x))
  if (!clean(ids$id) || anyDuplicated(ids$id)) stop("IDs must be nonblank and unique")
  if (!clean(methods$method) || !clean(methods$run_id) || anyDuplicated(methods))
    stop("Expected method/run pairs must be nonblank and unique")
  if (anyDuplicated(d[c("id", "method", "run_id")])) stop("Duplicate id/method/run records")
  if (nrow(d) != nrow(ids) * nrow(methods)) stop("Unexpected total row count")
  observed <- unique(d[c("method", "run_id")])
  if (nrow(merge(observed, methods, by = c("method", "run_id"))) != nrow(observed) ||
      nrow(observed) != nrow(methods)) stop("Unexpected or missing method/run pairs")
  for (i in seq_len(nrow(methods))) {
    part <- d[d$method == methods$method[i] & d$run_id == methods$run_id[i], , drop = FALSE]
    if (nrow(part) != nrow(ids) || !setequal(part$id, ids$id)) stop("ID coverage mismatch")
  }
  if (!all(d$prediction %in% c("0", "1", "ABSTAIN"))) stop("Invalid prediction label")
  blank <- d$score == ""
  if (any(blank & d$prediction != "ABSTAIN")) stop("Only abstentions may have blank scores")
  numeric_scores <- suppressWarnings(as.numeric(d$score[!blank]))
  if (any(!is.finite(numeric_scores)) || any(numeric_scores < 0 | numeric_scores > 1))
    stop("Scores must be finite numbers in [0,1]")
  summary <- methods
  summary$n <- nrow(ids)
  summary$answered <- summary$blank_scores <- integer(nrow(methods))
  for (i in seq_len(nrow(methods))) {
    part <- d[d$method == methods$method[i] & d$run_id == methods$run_id[i], , drop = FALSE]
    summary$answered[i] <- sum(part$prediction != "ABSTAIN")
    summary$blank_scores[i] <- sum(part$score == "")
  }
  list(status = "format_and_coverage_passed", performance_evaluated = FALSE,
       note = "Does not verify score orientation, leakage, truth, freeze timing or validity.",
       groups = summary)
}
