# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

x = np.arange(-3, 3, 0.1)
y = np.arange(-2,2,0.1)
y = np.cos(x)
plt.plot(x, y)
plt.show()

# !jupytext --to py --output ./jupytexts/Version_control.py ./Version_control.ipynb


