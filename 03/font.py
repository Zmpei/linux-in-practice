import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


fonts = set([fm.FontProperties(fname=font).get_name() for font in fm.findSystemFonts()])

fig = plt.figure(figsize=(8, 100))
ax = fig.add_subplot(1, 1, 1)
ax.set_ylim([-0.5, len(fonts)])

for i, f in enumerate(fonts):
    ax.text(0.2, i, "日本語 {}".format(f), fontdict={"family": f, "fontsize": 16})

plt.show()
