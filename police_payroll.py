import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import gridspec
import matplotlib.ticker as mtick


def grids():
    """Applies aesthetic gridding to a subplot axis."""

    ax.minorticks_on()
    ax.tick_params('y', length=8, which='major', labelsize='10')
    ax.tick_params('y', length=3, which='minor')
    ax.tick_params('x', which='both', bottom=False, top=False)
    ax.set_axisbelow(True)
    ax.grid(True, which='major', ls='-', lw=.5, alpha=0.75, zorder=0, color='lightgray')
    ax.grid(True, which='minor', ls=':', alpha=.15, zorder=0, color='lightgray')


def spines():
    for spine in ax.spines.values():
        spine.set_visible(False)


def ticks():
    ax.tick_params(which='both', top=False, left=False, right=False, bottom=False)


def set_gridspec(widths, heights, wspace=0, hspace=0):
    fig = plt.figure(figsize=(sum(widths) + wspace * (len(widths) - 1),
                              sum(heights) + hspace * (len(heights) - 1)))
    gs = gridspec.GridSpec(len(heights), len(widths),
                           height_ratios=heights, width_ratios=widths)
    return fig, gs


def getPayrollData(year, job_title):
    df = pd.read_csv(f"payroll data/santa-cruz-{year}.csv")
    df_stats = df.loc[df['Job Title'].str.lower()==job_title.lower()].describe()
    return df_stats

payroll_years = range(2011, 2019)
payroll_data = {year: getPayrollData(year, 'Police Officer') for year in payroll_years}


# Initializing figure.
fig, gs = set_gridspec(widths=[15], heights=[7, 1, 7])

# First figure
ax = fig.add_subplot(gs[0])
grids(); spines()
ax.set_facecolor('ghostwhite')