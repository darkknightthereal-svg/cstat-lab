import matplotlib.pyplot as plt

heights = [158, 162, 165, 170, 172, 175, 168, 160, 177, 180, 163, 169, 171, 166, 174, 159, 167, 173, 164, 178]
plt.hist(heights, bins=6, edgecolor="black", color="skyblue")
plt.title("Heights of Classmates")
plt.xlabel("Height (cm)")
plt.ylabel("Number of Students")
plt.show()
