import numpy as np
import pandas as pd

asc_file = r'/home/ds1/AnalysisH/REM/77532_1356756_M-34-64-B-d-3-2.asc'
csv_file = r'/home/ds1/AnalysisH/REM/CSV_data.csv'  


def convert_asc_to_csv(asc_file, csv_file):
    with open(asc_file, "r") as f:
        lines = f.readlines()

    header = {}
    data_start = 0
    for i, line in enumerate(lines):
        parts = line.strip().split()
        if parts[0].isalpha():
            key = parts[0].lower()
            try:
                header[key] = float(parts[1])
            except ValueError:
                continue
        else:
            data_start = i
            break

    ncols = int(header.get("ncols", 0))
    nrows = int(header.get("nrows", 0))
    cellsize = header.get("cellsize", None)
    nodata = header.get("nodata_value", header.get("nodata", -9999))

    if "xllcorner" in header and "yllcorner" in header:
        xll = header["xllcorner"]
        yll = header["yllcorner"]
    elif "xllcenter" in header and "yllcenter" in header:
        xll = header["xllcenter"] - (cellsize / 2)
        yll = header["yllcenter"] - (cellsize / 2)
    else:
        raise ValueError("Missing xllcorner/xllcenter or yllcorner/yllcenter!")

    data_lines = [line.strip() for line in lines[data_start:] if not any(c.isalpha() for c in line)]
    data = np.loadtxt(data_lines, dtype=np.float32)

    x_coords = np.array([xll + cellsize * i for i in range(ncols)])
    y_coords = np.array([yll + cellsize * (nrows - i - 1) for i in range(nrows)])

    rows = []
    for i in range(nrows):
        for j in range(ncols):
            z = data[i, j]
            if z != nodata:
                rows.append([x_coords[j], y_coords[i], z])

    df = pd.DataFrame(rows, columns=["X", "Y", "Z"])
    df.to_csv(csv_file, index=False)
    print(f"CSV file saved as: {csv_file}")

if __name__ == "__main__":
    convert_asc_to_csv(asc_file, csv_file)
