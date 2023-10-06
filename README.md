# GamesDAU

## Summary of .py files - 

1. *dataloading*: Loading CSV, viewing it via DataFrames, and extracting iOS and Android sub-datasets.
2. *initialplotting*: Methods for visualising the trends of multiple cohorts on a graph, and consequently visualising a full year of cohorts.
3. *timeseriesanalysis*: Methods (fine-tuned personally) for accurately identifying all significant junctures of change in DAU across cohorts
4. *exceptionregionanalysis*: Methods for understanding regions of ambiguity better using summary statistics.
5. *exceptionregioninference*: Assuming a linear curve fit (which can be switched to other approaches such as case-wise vayesian perturbation, or other forms of regression, etc.), inferring a model to explain the exception region.
6. *generalinference*: Time-series based curve-fitting (exponential smoothing, to start with) on general trend of alert of regions per 60-day-runs across cohorts. This may also be used to extrapolate preliminary baseline for future data (predictive mode).
7. *correlationDAU*: Methods for assessing correlation between truncated previous summative DAU population and current cohort's Day 1 DAU.
