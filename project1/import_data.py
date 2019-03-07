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
