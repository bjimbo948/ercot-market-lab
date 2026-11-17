"""Pull one day of Houston Hub DA and RT prices and save them to data/raw/."""
from pathlib import Path   # handles file paths cleanly on any OS
import gridstatus          
from gridstatus import Markets

DATE = "today"
LOCATION = "HB_HOUSTON"
OUT_DIR = Path("data/raw")
OUT_DIR.mkdir(parents=True, exist_ok=True)

ercot = gridstatus.Ercot()

def pull(market):
    return ercot.get_spp(
        date = DATE,
        market = market,
        locations = [LOCATION],
        location_type = "Trading Hub",
    )
da = pull(Markets.DAY_AHEAD_HOURLY)
rt = pull(Markets.REAL_TIME_15_MIN)

# Name files by the actual date in the data, not the word "today"
day = da["Interval Start"].iloc[0].strftime("%Y-%m-%d")
da.to_csv(OUT_DIR / f"da_{LOCATION}_{day}.csv", index = False)
rt.to_csv(OUT_DIR / f"rt_{LOCATION}_{day}.csv", index = False)

print(f"Saved {day}: DA rows = {len(da)}, RT rows = {len(rt)}")
