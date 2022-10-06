import matplotlib.pyplot as plt
import numpy as np

import ITViec
import topcv
import topdev
import vietnamworks
import careerbuilder

print("Thành phố: ")
province = input()
print("Từ khóa: ")
jobInput = input()

# Get result
itviecResult = ITViec.itviecTotal(province,jobInput)
topcvResult = topcv.topcvTotal(province,jobInput)
topdevResult = topdev.topdevTotal(province,jobInput)
vietnamworksResult = vietnamworks.vietnamworksTotal(province,jobInput)
careerbuilderResult = careerbuilder.careerbuilderTotal(province,jobInput)

# print total
totalITViec = [int(s) for s in itviecResult.split() if s.isdigit()][0]
totalTopcv = [int(s) for s in topcvResult.split() if s.isdigit()][0]
totalTopdev = [int(s) for s in topdevResult.split() if s.isdigit()][0]
totalVietnamworks = [int(s) for s in vietnamworksResult.split() if s.isdigit()][0]
totalCareerbuilderResult = [int(s) for s in careerbuilderResult.split() if s.isdigit()][0]
print("Total ITViec: ", totalITViec)
print("Total Topcv: ", totalTopcv)
print("Total Topdev: ", totalTopdev)
print("Total Vietnamworks: ", totalVietnamworks)
print("Total Careerbuilder: ", totalCareerbuilderResult)

# Grap
x = np.array(["IT Viec", "Top CV", "Top Dev", "Vietnamworks", "Careerbuilder"])
y = np.array([totalITViec, totalTopcv, totalTopdev, totalVietnamworks, totalCareerbuilderResult])

fig, ax = plt.subplots(figsize = (10,5))
ax.bar(x,y,width=0.4)
for index,data in enumerate(y):
    plt.text(x=(index-0.06) , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=16))
plt.tight_layout()

plt.title('Thành phố: ' + province + ", Từ khóa:" + jobInput)
plt.xlabel('Trang tuyển dụng')
plt.ylabel('Tổng')
plt.bar(x,y)
plt.show()