from pyrama import calc_ramachandran, plot_ramachandran

def covid_rama_plot():
    protein = ['6lu7.pdb']
    normals, outliers = calc_ramachandran(protein)
    plot_ramachandran(normals, outliers)

def sars_rama_plot():
    protein = ['6w4b.pdb']
    normals, outliers = calc_ramachandran(protein)
    plot_ramachandran(normals, outliers)


def ncov_rama_plot():
    protein = ['6yb7.pdb']
    normals, outliers = calc_ramachandran(protein)
    plot_ramachandran(normals, outliers)