"""Load example data"""
from pathlib import Path

import mokapot
import pandas as pd
from Bio.SeqUtils.ProtParam import ProteinAnalysis

RELPATH = Path(__file__).parent.parent.resolve()


def procal(n_test=15, random_state=42):
    """Load a replicate of the PROCAL retention times.

    Returns
    -------
    train : (numpy.ndarray (n_peptides, 1))
        The PROCAL peptides with their retention times and
        GRAVY score.
    """
    rt_csv = RELPATH / "data/PXD006832/Skyline_output_all_runs.csv"
    df = pd.read_csv(rt_csv)

    # The replicate to select:
    stem = "161207_ProPep_50fmol_4to42_R1"
    has_stem = df["Replicate Name"].str.contains(stem)
    df = df.loc[has_stem, :]
    df["Peptide GRAVY Score"] = (
        df["Peptide Sequence"]
        .apply(lambda x: ProteinAnalysis(x).gravy())
    )

    df = df.sample(frac=1, random_state=random_state)
    n_train = len(df) - n_test
    train_df = df.iloc[:n_train, :]
    test_df = df.iloc[n_test:, :]
    return train_df, test_df


def read_example_pin():
    """Read an example Percolator input file.

    Returns
    -------
    df : pandas.DataFrame
        The PIN file as a DataFrame.
    path : pathlib.Path
        The path to file
    """
    pin_path = RELPATH / "data/pin_files/scope2_FP97AA.pin"
    return mokapot.read_percolator(pin_path), pin_path
