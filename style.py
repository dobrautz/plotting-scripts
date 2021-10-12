#!/home/dobrautz/anaconda2/bin/python
'''
set my default plot parameter
'''

import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns

# def set_defaults():
sns.set_color_codes('dark')
sns.set_style('ticks')

# general independent rc params
# if available us computer moden (latex default)
rc('font', family = 'serif')
rc('font', serif = ['CMU Serif'])

# use tex to create the labels
rc('text', usetex = True)

# make the legend look nicer:
rc('legend', frameon = True)
rc('legend', edgecolor = 'black')
rc('legend', framealpha = 1.0)
rc('legend', shadow = True)
# maker markers a bit smaller
rc('legend', markerscale = 0.8)
rc('legend', handlelength = 1.8)
rc('legend', handletextpad = 0.6)
rc('legend', borderpad = 0.3)
rc('legend', columnspacing = 1.6)

# remove spines
rc('axes.spines', top = False)
rc('axes.spines', right = False)

rc('savefig', bbox = 'tight')
rc('savefig', transparent = True)

# use standard font-size of 10
rc('font', size = 12)

def set_fontsize_and_get_fig_width(paper_type, **kwargs):
    '''
    depending on the papertype (A4, A5, A0, presentation, usletter)
    change the font. also returns the width of the chosen paper format, for further use

    Arguments:
    ----------
    paper_type      string of: {A4, A5, usletter} (for now)

    optional argumets:
    two_column      bool, if it is for a paper with two-columned A4
    num_figures     int,  giving the number of subplots in the figure, then the fontsize will be reduced

    output:
    -------
    width   depending on the paper type and number of columns
    '''

    if paper_type == 'A4':
        if 'two_column' in kwargs:
            if kwargs.get('two_column'):
                # double column A4 paper format

                if 'num_figures' in kwargs:
                    if kwargs.get('num_figures') > 1:
                        rc('axes', labelsize = 'smaller')
                        rc('xtick', labelsize = 'smaller')
                        rc('ytick', labelsize = 'smaller')
                        rc('legend', fontsize = 'smaller')

                # return size in inches
                return 3 + 3/8.

        else:

            if 'num_figures' in kwargs:
                if kwargs.get('num_figures') > 1:
                    rc('axes', labelsize = 'smaller')
                    rc('xtick', labelsize = 'smaller')
                    rc('ytick', labelsize = 'smaller')
                    rc('legend', fontsize = 'smaller')

            # give the width with some padding
            return 0.8 * 8.3

    elif paper_type == 'A5':
        # for A5 make fontsize generally smaller
        rc('font', size = 9)

        # and even smaller for mutiple plots:
        if 'num_figures' in kwargs:
            if kwargs.get('num_figures') > 1:
                rc('axes', labelsize = 'smaller')
                rc('xtick', labelsize = 'smaller')
                rc('ytick', labelsize = 'smaller')
                rc('legend', fontsize = 'smaller')


        # return a5 widht with some margins
        return 0.85 * 5.8

    elif paper_type == 'usletter':
        if 'two_column' in kwargs:
            if kwargs.get('two_column'):

                if 'num_figures' in kwargs:
                    if kwargs.get('num_figures') > 1:
                        rc('axes', labelsize = 'smaller')
                        rc('xtick', labelsize = 'smaller')
                        rc('ytick', labelsize = 'smaller')
                        rc('legend', fontsize = 'smaller')

                return 3.25

        else:
            if 'num_figures' in kwargs:
                if kwargs.get('num_figures') > 1:
                    rc('axes', labelsize = 'smaller')
                    rc('xtick', labelsize = 'smaller')
                    rc('ytick', labelsize = 'smaller')
                    rc('legend', fontsize = 'smaller')

            return 7.

    elif paper_type == 'A0':
        line_width = 4
        leg_lw = 2
        shadow = True
        sns.set_context('poster', font_scale = 1.7, \
                        rc={'lines.linewidth': line_width, \
                            'lines.markersize': 15, \
                            'axes.linewidth': 4})
        rc('axes', linewidth = 2)
        rc('patch', linewidth = 2)

        a0_width = 33.1

        return a0_width



