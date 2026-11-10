import pandas, numpy, duckdb, pyomo.environ, highspy, lightgbm
import gridstatus

print("pandas", pandas.__version__)
print("duckdb", duckdb.__version__)

ercot = gridstatus.Ercot()
load = ercot.get_load("today")
print(load.tail())