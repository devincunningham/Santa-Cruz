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


df = pd.read_csv(
    '/Users/devincunningham/PycharmProjects/datasci/Santa Cruz/total_operating_expenditures.csv',
    index_col=0)

# Removing the "Total" column.
df = df.loc[:, df.columns != 'Total']
df['City Manager, Information technology, Finance,'
   'Economic Development, City Non-Departmental, Human Resources,'
   'Library, City Attorney, and City Council'] = df[
    ['City Manager',
     'Information technology', 'Finance', 'Economic Development',
     'City Non-Departmental', 'Human Resources', 'Library',
     'City Attorney', 'City Council'
     ]].sum(axis=1)

df = df[
    ['Police', 'Fire', 'Parks and Recreation', 'Public Works', 'Planning and Community Development',
     'City Manager, Information technology, Finance,'
     'Economic Development, City Non-Departmental, Human Resources,'
     'Library, City Attorney, and City Council'
     ]]

colors = [
    '#182940', '#D99B29', '#84B6BD',
    '#EBE8CF', '#F29E6D', '#C6BCC7',
    '#733832', '#BF5B45', '#F29E6D', '#D9B589', '#FFE073',
    '#A0C261', '#4E9950', '#9C6779', '#DAD4DF',
]



# Normalizing dataset
dfn = df.div(df.sum(axis=1), axis=0) * 100

# Initializing figure.
fig, gs = set_gridspec(widths=[15], heights=[7, 1, 7])

# First figure
ax = fig.add_subplot(gs[0])
grids(); spines()
ax.set_facecolor('ghostwhite')
df.plot.bar(ax=ax, color=colors, legend=False)
ax.set_title('City of Santa Cruz Budget History', size=16)
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

# Second figure
ax = fig.add_subplot(gs[2])
grids(); spines(); ticks()
dfn.plot.area(ax=ax, color=colors, legend=False)
ax.set_title('% of total operating expenditures', size=16)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=False)


# fig.suptitle("City of Santa Cruz Budget History")

plt.savefig('sc_budget.png', dpi=600)
plt.show()
