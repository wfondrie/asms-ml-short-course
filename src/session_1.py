"""Function for Session 1."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor

from . import data

sns.set_context("notebook")
sns.set_style("ticks")
pal = sns.color_palette()
PROCAL_STATE = ([[], [], []], data.procal())


def make_first_plot(parameter):
    """Create a simple plot."""
    if not isinstance(parameter, int) and not isinstance(parameter, float):
        raise ValueError("'parameter' must be a number.")

    x = np.linspace(0, 10, 1000)
    y = x * np.sin(x * parameter)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("$X$")
    plt.ylabel("$f(X)$")
    plt.show()


def fit_model_to_ret_times(k=None):
    """Fit the PROCAL data."""
    (train_err, test_err, kvals), (train_df, test_df) = PROCAL_STATE
    max_rt = 1.10 * max(
        train_df["Peptide Retention Time"].max(),
        test_df["Peptide Retention Time"].max(),
    )

    min_x = 1.10 * min(
        train_df["Peptide GRAVY Score"].min(),
        test_df["Peptide GRAVY Score"].min(),
    )
    max_x = 1.10 * max(
        train_df["Peptide GRAVY Score"].max(),
        test_df["Peptide GRAVY Score"].max(),
    )

    x_space = np.linspace(min_x, max_x, 1000)[:, None]

    labs = ["Training Set", "Validation Set"]
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    err_ax = axs[2]
    for ax, df, lab in zip(axs[:2], [train_df, test_df], labs):
        sns.scatterplot(
            data=df,
            x="Peptide GRAVY Score",
            y="Peptide Retention Time",
            ax=ax,
        )
        ax.set_title(lab)
        ax.set_xlim(min_x, max_x)
        ax.set_ylim(0, max_rt)

    err_ax.set_xlabel("Flexibility")
    err_ax.set_ylabel("Mean Squared Error")

    if k is not None:
        if k < 1 or k > len(train_df):
            raise ValueError(f"Choose a k between 1 and {len(train_df)}")

        model = KNeighborsRegressor(k).fit(
            train_df.loc[:, ["Peptide GRAVY Score"]].to_numpy(),
            train_df["Peptide Retention Time"].to_numpy(),
        )

        updates = []
        for ax, df in zip(axs[:2], [train_df, test_df]):
            X = df.loc[:, ["Peptide GRAVY Score"]].to_numpy()  # noqa: N806
            y = df["Peptide Retention Time"].to_numpy()
            pred = model.predict(X)
            mse = mean_squared_error(pred, y)
            all_rt = model.predict(x_space)
            ax.plot(x_space, all_rt, color=pal[1])
            updates.append(mse)

        PROCAL_STATE[0][0].append(updates[0])
        PROCAL_STATE[0][1].append(updates[1])
        PROCAL_STATE[0][2].append(k)
        kvals = np.array(kvals)
        order = np.argsort(kvals)
        kvals = len(train_df) - kvals[order]
        train_err = np.array(PROCAL_STATE[0][0])[order]
        test_err = np.array(PROCAL_STATE[0][1])[order]

        err_df = pd.DataFrame(
            {
                "kvals": np.concatenate([kvals, kvals]),
                "mse": np.concatenate([train_err, test_err]),
                "dataset": (
                    ["Training MSE"] * len(kvals)
                    + ["Validation MSE"] * len(kvals)
                ),
            }
        )

        sns.lineplot(
            data=err_df,
            x="kvals",
            y="mse",
            hue="dataset",
            marker="o",
            ax=err_ax,
        )
        err_ax.legend(
            title="",
            frameon=False,
            loc="lower left",
        )
        err_ax.set_title("Bias-Variance Trade-off")

    plt.tight_layout()
    plt.show()
