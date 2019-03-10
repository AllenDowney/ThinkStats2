"""Import all data from the selected NSDUH years into pandas dataframes for analysis.

To use this script, a directory named nsduh_data must exist. It should contain
stata files from all selected nsduh survey years. These files can be downloaded
from the SAMHDA website:
https://www.datafiles.samhsa.gov/study-series/national-survey-drug-use-and-health-nsduh-nid13517
Click through the links in the "Studies in this series" column on the right
hand side to navigate to the individual stata files.

The final hdf file will contain a pandas object for each year, identified by a
key 'NSDUH_20XX'.
"""
import pandas as pd
import pathlib

def cat_to_numeric(df):
    """Convert columns with dtype 'category' to a numerical value. This is
    necessary in order to save dataframes to an HDF file.
    """
    cat_columns = df.select_dtypes(include=['category']).columns
    df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)
    return df

if __name__ == "__main__":
    p = pathlib.Path('./nsduh_data')
    dest = 'nsduh.hdf5'

    print("Reading NSDUH files...")
    for f in p.iterdir():
        if f.is_file():
            print("Reading {}".format(f.name))
            df = pd.read_stata(f.resolve())
            df = cat_to_numeric(df)
            print("Succesfully read {}".format(f.name))

            label = f.name.split('.')[0]
            df.to_hdf(dest, label, format='table')
